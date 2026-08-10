---
name: youtube-transcript
description: Ingest YouTube transcripts from a single video or an entire playlist and produce a detailed, structured summary of what was said. Use when the user shares a YouTube URL (video or playlist) and wants a transcript, notes, key takeaways, or a summary. Triggers include 'summarize this YouTube video', 'transcribe this playlist', 'what does this video say', or any youtube.com / youtu.be link.
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: "<youtube-video-or-playlist-url>"
---

# YouTube Transcript Ingestion & Summary

## Mission

Turn a YouTube **video or playlist** into (1) clean, physically-downloaded transcripts and
(2) a detailed, well-structured summary of everything that was said. Transcript retrieval is
**fully deterministic** — it runs a bundled script that drives `yt-dlp`, never guesswork or
fabricated content. Summarization is your job, performed strictly from the downloaded text.

**Never invent or infer content that is not in the transcript.** If captions are unavailable,
say so plainly rather than guessing what the video contains.

## Scope & Preconditions

- Works on anything `yt-dlp` accepts: single video, playlist, or channel URL.
- Requires `yt-dlp` and Python 3. If `yt-dlp` is missing, install it first:
  - `pip install -U yt-dlp` (cross-platform), or
  - `winget install yt-dlp.yt-dlp` (Windows) / `brew install yt-dlp` (macOS).
- Prefers human-written ("manual") captions; falls back to auto-generated captions.
- Some videos (age-restricted, members-only) need browser cookies — pass
  `--cookies-from-browser <chrome|edge|firefox|...>` to the script.
- This skill downloads **subtitles only**, never the audio/video itself.

## Workflow

1. **Ensure `yt-dlp` is installed (do this first).** The download step depends on it. Check
   for it and install it if missing:

   ```bash
   # Check (either of these should print a version):
   yt-dlp --version || python -m yt_dlp --version
   ```

   If neither prints a version, install it before continuing:

   ```bash
   pip install -U yt-dlp                 # cross-platform (recommended)
   # or:
   winget install yt-dlp.yt-dlp         # Windows
   brew install yt-dlp                  # macOS
   ```

   The bundled script also auto-falls back to `python -m yt_dlp`, so a `pip install -U yt-dlp`
   is enough even when there's no standalone `yt-dlp` binary on PATH. Do not proceed to the
   download step until a version prints successfully.

2. **Identify the URL.** Take the video or playlist URL from the user's request (the skill
   argument). Ask only if no URL is present.

3. **Download transcripts deterministically.** Run the bundled script from the skill directory:

   ```bash
   python scripts/fetch_transcript.py "<URL>" --out transcripts
   ```

   Useful options:
   - `--langs "en,en-US,en-GB,en.*"` — subtitle language priority (default shown).
   - `--cookies-from-browser edge` — for restricted videos.
   - `--keep-raw` — keep the raw `.vtt` / `.info.json` files for debugging.

   The script writes, under the output directory:
   - `manifest.json` — index of every video (id, title, uploader, duration, url, caption
     source: `manual` / `auto` / `none`, and output file names).
   - `<NNN>-<id>.txt` — clean, de-duplicated plain-text transcript per video.
   - `<NNN>-<id>.md` — the same transcript with `[mm:ss]` timestamps per caption cue.
   - `all.md` — every transcript concatenated with per-video headers (handy for playlists).

4. **Read the results.** Open `manifest.json` first to learn what was captured, then read the
   `.txt` (or `.md` if you need timestamps) for each video. For playlists, `all.md` gives you
   everything in one pass.

5. **Handle gaps honestly.** For any video whose `transcript_source` is `none` or `empty`,
   report that no captions were available and exclude it from the content summary (don't
   fabricate). Suggest `--cookies-from-browser` if access seems to be the cause.

6. **Summarize.** Produce a detailed summary grounded only in the transcript text (see below).

## Output Expectations

Deliver a summary tailored to the input:

**Single video**
- **Title & link**, channel, and duration.
- **TL;DR** — 2–4 sentences capturing the core message.
- **Detailed summary** — the main points in the order presented, with enough depth that a
  reader gets the substance without watching. Cite timestamps `[mm:ss]` for key moments
  (available in the `.md` transcript).
- **Key takeaways / action items** — bulleted.
- **Notable quotes** — only if genuinely present, quoted verbatim.

**Playlist**
- **Overview** — playlist title/source, number of videos, and how many had captions.
- **Per-video sections** — for each video: title, link, and a focused summary of its content.
- **Cross-cutting themes** — threads, progressions, or recurring ideas spanning the playlist.
- Clearly flag any videos that had no captions.

Keep it information-dense and skimmable: headings, bullets, and timestamps over prose walls.

## Quality Assurance

- Every claim in the summary must be traceable to the downloaded transcript text.
- Verify `transcript_source` per video; never present an `auto` caption summary as if it were
  an authoritative manual transcript without noting captions may contain recognition errors.
- The transcript download is deterministic: the same URL and `--langs` yield the same files.
  Re-run the script rather than hand-editing transcripts.
- If `yt-dlp` errors (private video, removed content, region lock, rate limiting), surface the
  actual error to the user instead of guessing the content.
