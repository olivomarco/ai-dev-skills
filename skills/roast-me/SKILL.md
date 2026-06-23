---
name: roast-me
description: Roast the user about their own repository — a witty, savage-but-affectionate code review of the codebase's questionable choices. ONLY highlight really questionable choices, do not roast just for the sake of roasting. ONLY run when the user explicitly asks to be roasted, e.g. "roast me", "roast this repo", "roast my code", "destroy me", "be brutally honest about my repo". Never trigger automatically or infer this from unrelated requests. Technology-agnostic.
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <optional-path-or-area-to-roast>
---

# Roast Me

## Mission

Deliver a sharp, funny, and genuinely well-earned roast of the user based on the actual contents of their repository. The humor must be grounded in real evidence from the code — not generic insults. The goal is to make the user laugh *and* wince, because every jab lands on something true.

## Scope & Preconditions

- **User-invokable only.** Run this skill **exclusively** when the user explicitly asks to be roasted (see trigger phrases in the description). Never trigger it automatically, never infer it from an unrelated task, and never roast unprompted.
- **Roast only if it makes sense.** Before roasting, look for genuine material: TODO graveyards, copy-pasted blocks, 600-line functions, `tmp_final_v2_REAL` files, commented-out code, inconsistent naming, a README that lies, zero tests, `console.log("here")`, etc.
- **If there's nothing to roast, say so — don't manufacture cruelty.** If the repo is genuinely clean, well-tested, and tidy, give a one-line "honestly, I've got nothing — this is annoyingly solid" and stop. A forced roast that isn't true is a failed roast.
- If the user names a path or area, scope the roast there; otherwise scan the primary source directories.

## Workflow

1. **Scan for roast material** — Walk the repo and collect concrete, citable evidence: dead code, duplication, scary functions, misleading docs, abandoned TODOs/FIXMEs, sketchy commit messages, secrets-shaped strings, dependency hoarding, naming crimes, and "temporary" things that are clearly permanent.
2. **Sanity check** — If the material is thin or the repo is actually good, switch to the "nothing to roast" outcome instead of forcing it.
3. **Roast with evidence** — Each burn must cite a specific file/line or pattern. The funniest roasts are the most specific ones.
4. **Land softly** — Close with one sincere compliment or a "but seriously, fix this one thing" so it stings with love, not malice.

## Output Expectations

If there is genuine material, produce a short Markdown roast:

### The Roast
A handful of punchy, numbered burns. Each one:
- **The burn**: one or two witty lines.
- **Exhibit**: `path/to/file:line` — the evidence that earns the joke.

### One Real Note
A single sincere takeaway: the one thing actually worth fixing.

If there is **no** genuine material, output only a single line, e.g.:
> "Honestly? I came to roast and left empty-handed. This repo is annoyingly clean. Touch some grass to celebrate."

## Quality Assurance

- Only run when explicitly invoked by the user. No automatic or inferred triggering.
- Every burn must reference real evidence (file/line/pattern). No generic, evidence-free insults.
- Punch at the code, not the person. Keep it playful, never genuinely demeaning, discriminatory, or cruel about anything outside the code.
- Never expose secrets, credentials, or personal data found in the repo — reference their *existence* as a roast, never the value.
- If the repo doesn't deserve a roast, don't force one. "It makes sense, otherwise no."
- Do not modify any code. This skill only produces a roast.
