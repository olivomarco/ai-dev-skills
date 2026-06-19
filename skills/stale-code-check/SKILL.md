---
name: stale-code-check
description: Detect stale, dead, deprecated, or obsolete code, dependencies, config, and assets that can be safely removed. Use when asked to "find dead code", "check for stale code", "find unused dependencies", "detect obsolete code", or "clean up the codebase". Technology-agnostic.
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <path-or-area-to-scan>
---

# Stale Code & Dead Weight Detection

## Mission

Scan the codebase for stale, unused, deprecated, or obsolete code, dependencies, configuration, and assets that can be safely removed to reduce maintenance burden and bundle/build size. Be conservative — flag for review, prefer evidence over guesses, and report; do not delete unless explicitly asked.

## Scope & Preconditions

- If the user names an area, scope there; otherwise cover source, manifests, config, and static assets.
- Infer the stack. If a dead-code/unused-export tool exists for it (e.g. `knip`, `ts-prune`, `depcheck`, `vulture`, `deadcode`, `unused`), run it as a starting point — but verify results, don't trust them blindly.
- Beware of dynamic references: reflection, string-based lookups, dynamic imports, config-driven wiring, and DI containers can use code that looks unreferenced.

## Workflow

1. **Unused exports & files** — Find exported symbols and whole files with no importers/usages.
2. **Dead routes/handlers/operations** — Cross-reference declared routes/handlers against actual usage; flag declared-but-unreferenced ones.
3. **Orphaned components/modules** — Find components/modules not imported anywhere.
4. **Deprecated patterns/APIs** — Identify code using deprecated language/library APIs or outdated patterns.
5. **Stale data models** — Check schema/models against actual read/write usage; flag models or fields with no usage.
6. **Outdated dependencies** — Check manifests for packages with major updates available, known deprecations, or duplicate purpose.
7. **Debt markers** — Search for `TODO`, `FIXME`, `HACK`, `XXX`, `DEPRECATED`, and stale feature flags/toggles.
8. **Unused static assets** — Check images/fonts/data files against references in code and styles.
9. **Stale migrations/build artifacts** — Identify superseded migrations or committed build output that shouldn't be tracked.
10. **Unused configuration** — Check config files for unused plugins, rules, paths, or env keys.

## Output Expectations

Produce a Markdown report with:

### Summary
Total stale items found, broken down by category.

### Findings by Category
For each item:
- **Item**: file path, dependency name, or code reference
- **Evidence**: why it's considered stale (e.g. "no importers found", "deprecated upstream")
- **Risk**: Safe to remove / Needs verification / Keep but update
- **Confidence**: High / Medium / Low
- **Action**: remove / update / investigate

### Dependency Audit
| Package | Current | Latest | Breaking changes | Action |
| --- | --- | --- | --- | --- |

### Cleanup Plan
Prioritized list of actions ordered safest → riskiest, with estimated effort.

## Quality Assurance

- Do NOT flag generated/vendored directories (e.g. build output, `node_modules`, framework-generated folders) as stale.
- Verify "unused" items are not referenced dynamically (dynamic import, reflection, string lookup, config) before recommending removal.
- Assign a confidence level to every finding; prefer "needs verification" when unsure.
- Do not delete anything unless explicitly asked. This skill reports by default.
