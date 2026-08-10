#!/usr/bin/env python3
"""Deterministically download YouTube transcripts for a video or playlist.

This script is the *deterministic* half of the `youtube-transcript` skill. It shells
out to `yt-dlp` to physically download subtitle tracks (manual first, then
auto-generated as a fallback), cleans them into readable text, and writes a stable set
of output files plus a `manifest.json` describing every video processed.

It performs NO summarization. Summarizing is the job of the calling agent, which reads
the files this script produces.

Usage:
    python fetch_transcript.py <URL> [--out DIR] [--langs LANGS] [--cookies-from-browser B]

Arguments:
    URL                 A YouTube video or playlist URL (anything yt-dlp accepts).
    --out DIR           Output directory (default: ./transcripts).
    --langs LANGS       Comma-separated subtitle language preference, in priority order.
                        Each entry is a yt-dlp sub-lang pattern. Default: "en,en-US,en-GB,en.*".
    --cookies-from-browser B
                        Optional browser name (e.g. chrome, edge, firefox) to load cookies
                        from, for age-restricted / members-only videos.
    --keep-raw          Keep the raw downloaded .vtt/.info.json files (default: removed).

Outputs (under DIR):
    <NNN>-<id>.txt      Clean, de-duplicated plain-text transcript per video.
    <NNN>-<id>.md       Timestamped transcript per video ([mm:ss] line per caption cue).
    all.md              All transcripts concatenated with per-video headers.
    manifest.json       Machine-readable index of every video and its outputs.

Exit codes:
    0  success (at least one transcript captured, or playlist had no captions but ran cleanly)
    2  yt-dlp not found
    3  yt-dlp failed to run
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def resolve_ytdlp() -> list[str] | None:
    """Return the command prefix used to invoke yt-dlp, or None if unavailable."""
    exe = shutil.which("yt-dlp")
    if exe:
        return [exe]
    # Fall back to the pip-installed module so the skill works without the standalone binary.
    try:
        subprocess.run(
            [sys.executable, "-m", "yt_dlp", "--version"],
            check=True,
            capture_output=True,
        )
        return [sys.executable, "-m", "yt_dlp"]
    except Exception:
        return None


def run_ytdlp(base_cmd: list[str], args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(base_cmd + args, capture_output=True, text=True)


TS_RE = re.compile(
    r"(\d{2}):(\d{2}):(\d{2})[.,](\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})[.,](\d{3})"
)
TAG_RE = re.compile(r"<[^>]+>")


def _hms_to_seconds(h: str, m: str, s: str) -> int:
    return int(h) * 3600 + int(m) * 60 + int(s)


def parse_vtt(path: Path) -> list[tuple[int, str]]:
    """Parse a .vtt/.srt file into a list of (start_seconds, text) cues, cleaned."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    cues: list[tuple[int, str]] = []
    current_start: int | None = None
    current_lines: list[str] = []

    def flush():
        nonlocal current_start, current_lines
        if current_start is not None and current_lines:
            # Keep lines separate so the auto-caption rolling-duplicate collapse
            # in dedup_cues() can operate at line granularity.
            text = "\n".join(current_lines)
            if text.strip():
                cues.append((current_start, text))
        current_start = None
        current_lines = []

    for line in raw.splitlines():
        stripped = line.strip()
        m = TS_RE.search(line)
        if m:
            flush()
            current_start = _hms_to_seconds(m.group(1), m.group(2), m.group(3))
            continue
        if current_start is None:
            # Outside a cue: skip headers (WEBVTT), NOTE/STYLE blocks, indices, blanks.
            continue
        if not stripped:
            flush()
            continue
        # Inside a cue body: strip inline tags (auto-captions embed <00:00:00.000><c> tags).
        cleaned = TAG_RE.sub("", line)
        cleaned = cleaned.replace("&nbsp;", " ")
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        if cleaned:
            current_lines.append(cleaned)
    flush()
    return cues


def dedup_cues(cues: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Collapse the rolling duplication typical of YouTube auto-captions.

    Auto-captions repeat the previous cue's tail at the head of the next cue. We walk
    every cue, split it into lines, and keep only lines that differ from the last line
    already emitted. Each retained cue keeps its earliest start time.
    """
    result: list[tuple[int, str]] = []
    last_line: str | None = None
    for start, text in cues:
        new_lines: list[str] = []
        for ln in text.split("\n"):
            ln = ln.strip()
            if not ln:
                continue
            if ln == last_line:
                continue
            new_lines.append(ln)
            last_line = ln
        if new_lines:
            result.append((start, " ".join(new_lines)))
    return result


def fmt_ts(seconds: int) -> str:
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h:d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def find_subtitle(work: Path, video_id: str, langs: list[str]) -> Path | None:
    """Find the best subtitle file for a video id, honoring the language priority order."""
    candidates = list(work.glob(f"*{video_id}*.vtt")) + list(work.glob(f"*{video_id}*.srt"))
    if not candidates:
        return None

    def lang_rank(p: Path) -> int:
        name = p.name.lower()
        for i, lang in enumerate(langs):
            base = lang.lower().rstrip("*").rstrip(".")
            if base and f".{base}" in name:
                return i
        return len(langs)

    candidates.sort(key=lambda p: (lang_rank(p), p.name))
    return candidates[0]


def download_subs(base_cmd: list[str], url: str, work: Path, langs: str,
                  auto: bool, cookies_browser: str | None) -> subprocess.CompletedProcess:
    work.mkdir(parents=True, exist_ok=True)
    out_tmpl = str(work / "%(playlist_index|0)03d-%(id)s.%(ext)s")
    args = [
        "--ignore-config",
        "--skip-download",
        "--no-warnings",
        "--sub-langs", langs,
        "--sub-format", "vtt/srt/best",
        "--write-info-json",
        "-o", out_tmpl,
    ]
    args += ["--write-auto-subs"] if auto else ["--write-subs"]
    if cookies_browser:
        args += ["--cookies-from-browser", cookies_browser]
    args.append(url)
    return run_ytdlp(base_cmd, args)


def main() -> int:
    parser = argparse.ArgumentParser(description="Download YouTube transcripts deterministically.")
    parser.add_argument("url", help="YouTube video or playlist URL")
    parser.add_argument("--out", default="transcripts", help="Output directory")
    parser.add_argument("--langs", default="en,en-US,en-GB,en.*",
                        help="Comma-separated subtitle language priority list")
    parser.add_argument("--cookies-from-browser", default=None,
                        help="Browser to read cookies from (chrome, edge, firefox, ...)")
    parser.add_argument("--keep-raw", action="store_true", help="Keep raw downloaded files")
    args = parser.parse_args()

    base_cmd = resolve_ytdlp()
    if base_cmd is None:
        sys.stderr.write(
            "ERROR: yt-dlp not found. Install it with one of:\n"
            "  pip install -U yt-dlp\n"
            "  winget install yt-dlp.yt-dlp   (Windows)\n"
            "  brew install yt-dlp            (macOS)\n"
        )
        return 2

    out_dir = Path(args.out).resolve()
    manual_dir = out_dir / "_raw_manual"
    auto_dir = out_dir / "_raw_auto"
    out_dir.mkdir(parents=True, exist_ok=True)

    langs = args.langs
    lang_list = [l.strip() for l in langs.split(",") if l.strip()]

    # Pass 1: manual subtitles (also writes the info JSON we use for metadata).
    r1 = download_subs(base_cmd, args.url, manual_dir, langs, auto=False,
                       cookies_browser=args.cookies_from_browser)
    if r1.returncode != 0 and not list(manual_dir.glob("*.info.json")):
        sys.stderr.write("yt-dlp failed:\n" + (r1.stderr or r1.stdout) + "\n")
        return 3

    # Pass 2: auto-generated subtitles (fallback when no manual track exists).
    download_subs(base_cmd, args.url, auto_dir, langs, auto=True,
                  cookies_browser=args.cookies_from_browser)

    info_files = sorted(manual_dir.glob("*.info.json"))
    if not info_files:
        # Single-video info JSON may have landed only in the auto pass.
        info_files = sorted(auto_dir.glob("*.info.json"))

    manifest: list[dict] = []
    all_md_parts: list[str] = []

    for info_path in info_files:
        try:
            info = json.loads(info_path.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        if info.get("_type") == "playlist":
            continue
        video_id = info.get("id") or info_path.stem
        title = info.get("title") or video_id
        duration = info.get("duration")
        url = info.get("webpage_url") or f"https://www.youtube.com/watch?v={video_id}"
        index = info.get("playlist_index") or 0
        uploader = info.get("uploader") or info.get("channel")

        sub_path = find_subtitle(manual_dir, video_id, lang_list)
        source = "manual"
        if sub_path is None:
            sub_path = find_subtitle(auto_dir, video_id, lang_list)
            source = "auto" if sub_path else "none"

        prefix = f"{int(index):03d}-{video_id}" if index else video_id
        txt_path = out_dir / f"{prefix}.txt"
        md_path = out_dir / f"{prefix}.md"

        entry = {
            "index": int(index) if index else None,
            "id": video_id,
            "title": title,
            "uploader": uploader,
            "duration_seconds": duration,
            "duration": fmt_ts(int(duration)) if isinstance(duration, (int, float)) else None,
            "url": url,
            "transcript_source": source,
            "language_file": sub_path.name if sub_path else None,
            "txt": None,
            "md": None,
        }

        if sub_path is not None:
            cues = dedup_cues(parse_vtt(sub_path))
            if cues:
                plain = "\n".join(text for _, text in cues)
                txt_path.write_text(plain + "\n", encoding="utf-8")
                md_lines = [f"# {title}", "", f"<{url}>", ""]
                md_lines += [f"`[{fmt_ts(start)}]` {text}" for start, text in cues]
                md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")
                entry["txt"] = str(txt_path.name)
                entry["md"] = str(md_path.name)
                header = f"## {int(index):03d}. {title}" if index else f"## {title}"
                all_md_parts.append(
                    f"{header}\n\nSource: {source} captions — <{url}>\n\n{plain}\n"
                )
            else:
                entry["transcript_source"] = "empty"

        manifest.append(entry)

    manifest.sort(key=lambda e: (e["index"] if e["index"] is not None else 0, e["id"]))

    (out_dir / "manifest.json").write_text(
        json.dumps(
            {
                "source_url": args.url,
                "language_priority": lang_list,
                "video_count": len(manifest),
                "videos": manifest,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    if all_md_parts:
        (out_dir / "all.md").write_text(
            f"# Transcripts for {args.url}\n\n" + "\n\n".join(all_md_parts),
            encoding="utf-8",
        )

    if not args.keep_raw:
        shutil.rmtree(manual_dir, ignore_errors=True)
        shutil.rmtree(auto_dir, ignore_errors=True)

    captured = sum(1 for e in manifest if e["txt"])
    print(f"Processed {len(manifest)} video(s); captured {captured} transcript(s).")
    print(f"Output directory: {out_dir}")
    print(f"Manifest: {out_dir / 'manifest.json'}")
    if captured == 0:
        print(
            "WARNING: no transcripts were captured. The video(s) may have no captions, "
            "or may require --cookies-from-browser.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
