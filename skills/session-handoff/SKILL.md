---
name: session-handoff
description: Capture the current session's state into a clean, copy-pasteable handoff block so work can continue in a fresh session. Use when the user wants to hand off, continue elsewhere, start a new session, or uses any 'handoff' / 'continue session' trigger phrases.
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: "[optional focus or note for the next session]"
---

# Session Handoff

## Mission

Produce a single, self-contained **handoff block** that summarizes everything a fresh
session needs to continue this work without losing context. The block is designed to be
copied (e.g. via a `/copy` command) and pasted as the first message of a new session.

The handoff must be accurate and grounded in what actually happened in this session — never
invent decisions, files, or progress that did not occur.

## Scope & Preconditions

- Summarize **only** the current session's work, decisions, and context.
- Inspect real evidence before writing: the conversation so far, files that were read or
  edited, commands that were run, and any plan or notes created during the session.
- If the user passed an argument, treat it as the **focus or steering note** for the next
  session and reflect it in the "Next Steps" section.
- Do not make code changes. This skill only generates the handoff text.

## Workflow

1. **Gather context.** Review the session to identify:
   - The overall goal and what was accomplished.
   - Decisions that were made and the reasoning behind them.
   - Files that matter (created, edited, or central to the work) with their paths.
   - Questions that are still open or blocked.
   - The concrete next steps to pick up.
2. **Verify file references.** Only list files that genuinely exist and are relevant. Prefer
   absolute or repo-relative paths so the next session can open them directly.
3. **Write the handoff block** using the exact template below.
4. **Keep it tight.** Favor specific, actionable detail over narration. A reader with no prior
   context should be able to resume in minutes.

## Output Expectations

Output **only** the handoff block, wrapped in a single fenced code block so it copies cleanly.
Use this exact structure (omit a section only if it is genuinely empty, and say "None" rather
than padding):

```
# Session Handoff

## Summary
<2-5 sentences: the goal, what was done, and current state.>

## Key Decisions
- <decision> — <why>
- ...

## Important Files
- `<path>` — <why it matters / what changed>
- ...

## Open Questions
- <unresolved question or blocker>
- ...

## Next Steps
1. <the first concrete action the new session should take>
2. ...

## Context to Carry Over
<branch, environment, commands to re-run, links, or constraints the next session must know.>
```

## Quality Assurance

- Every file path, decision, and "done" claim must be traceable to something that actually
  happened in this session.
- Open Questions must reflect real unknowns — do not leave it blank by fabricating certainty.
- Next Steps must be ordered and concrete enough to act on without re-deriving context.
- The entire handoff lives in one fenced block with no commentary before or after, so a single
  copy captures the whole thing.
