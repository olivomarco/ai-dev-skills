---
name: align-documentation
description: Audit and update existing documentation so it matches the current codebase — in-place updates only, no new files. Use when asked to "align the docs", "update documentation", "fix stale docs", "sync docs with code", or "check docs accuracy". Technology-agnostic.
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <docs-path-or-glob>
---

# Align Documentation with the Codebase

## Mission

Audit existing documentation and update any content that is stale, incorrect, or missing relative to the actual codebase. **Do NOT create new files** — only edit existing ones, in place. **Do NOT change source code** — docs only.

## Scope & Preconditions

- Discover the docs to audit: by default `README*`, files under `docs/`, and other Markdown/docs the user points to. If the user provides a path or glob, use exactly that. These are the only files you may touch.
- Infer the stack so you can read the right source files when verifying claims.
- If a doc references an external framework/library and you're unsure what's current, consult authoritative up-to-date sources (official docs / a docs MCP tool) before judging correctness.

## Workflow

1. **Discover all docs** — List every doc file in scope. These are the only files you may edit.
2. **Read the codebase** — For each doc, identify the features, APIs, commands, or patterns it describes, then read the relevant source to learn the current state.
3. **Diff doc vs. code** — For each doc, note every discrepancy:
   - Outdated API signatures, import paths, or commands
   - Removed or renamed files/functions/modules/entities
   - Missing coverage of features that already exist in the code
   - Wrong instructions (wrong command, wrong config, wrong convention)
4. **Update in place** — Edit each doc to fix the discrepancies. Keep the existing structure and tone. Remove only what is factually wrong; preserve still-valid context and rationale.
5. **Report** — After all edits, output a summary table.

## Output Expectations

After making edits, output:

### Summary Table
| File | Changes made |
| --- | --- |
| docs/FOO.md | Updated X, removed Y, added note about Z |

If a doc was already accurate, record "No changes needed".

## Constraints

- Do NOT create any new file anywhere.
- Do NOT delete any existing doc file.
- Do NOT change source code — documentation only.
- Do NOT reformat for style alone; only change content that is factually wrong or missing.
- Preserve each doc's existing voice, structure, and conventions.
- Verify every change against the actual code before writing it; do not guess.
