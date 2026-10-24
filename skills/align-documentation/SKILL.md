---
name: align-documentation
description: Align existing documentation with the codebase through in-place edits. Use when asked to sync docs with code, fix stale instructions, document existing behavior, or check documentation accuracy.
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <docs-path-or-glob>
---

# Align Documentation

Update existing docs to match verified behavior. Edit documentation only; preserve existing files, structure, voice, and valid rationale. Create no files and leave source code unchanged.

## Workflow

1. **Scope.** Use the user's paths or glob exactly. Otherwise, inventory `README*` and documentation under `docs/`. Finish with an explicit list of every document to audit; only those files may be edited. If nothing matches, report that and stop.
2. **Verify.** For each document, trace its claims about features, APIs, paths, commands, configuration, and conventions to source, manifests, or tests. Check for existing functionality missing from the document's subject. For uncertain framework or library claims, consult official documentation for the version the project uses. Surface conflicting sources instead of silently choosing one. Finish when every relevant claim is checked or marked unresolved with the missing evidence.
3. **Align.** Correct verified discrepancies in place: outdated signatures or paths, removed entities, incorrect instructions, and missing descriptions of existing behavior. Limit edits to factual alignment; preserve unrelated wording and formatting. Leave unresolved claims unchanged and identify them in the report.
4. **Check.** Recheck each changed claim against its evidence and verify affected links, paths, and examples. Validate commands through configuration, help output, or non-destructive checks; examples that deploy, delete, or change external services remain reference unless separately authorized. Use existing documentation checks when available. Finish when every edit is supported and the diff contains only scoped documentation changes.

## Report

Account for every document in the scope:

| File | Changes made |
| --- | --- |
| docs/usage.md | Corrected the CLI command and renamed configuration key |
| README.md | No changes needed |

List any unresolved claims and the evidence needed to settle them. If existing behavior needs a new document, note the gap rather than creating one.
