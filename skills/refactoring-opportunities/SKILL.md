---
name: refactoring-opportunities
description: Analyze a codebase for refactoring opportunities that improve maintainability, readability, and reduce technical debt, then produce a prioritized plan. Use when asked to "find refactoring opportunities", "identify code smells", "reduce tech debt", or "suggest refactors". Technology-agnostic.
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <path-or-area-to-analyze>
---

# Refactoring Opportunities Analysis

## Mission

Analyze the codebase and identify concrete refactoring opportunities that improve maintainability, readability, performance, and reduce technical debt. Produce a prioritized plan. Report findings; do not refactor unless explicitly asked.

## Scope & Preconditions

- If the user names an area, scope there; otherwise analyze the primary source directories.
- Infer the stack and respect the project's existing architecture and conventions.
- Do not propose changes that break documented invariants or public APIs without flagging the breakage.

## Workflow

1. **Scan for code smells** — Duplicated logic, overly long files/functions, deep nesting, large "god" modules/components, long parameter lists, and high cyclomatic complexity.
2. **Detect abstraction gaps** — Repeated patterns across modules that could become a shared utility, helper, or base abstraction.
3. **Evaluate structure** — Modules mixing concerns (I/O + business logic + presentation), missing separation of layers, and tight coupling that could be decoupled.
4. **Assess naming & readability** — Misleading or inconsistent names, dead branches, commented-out code, and unclear control flow.
5. **Assess type/contract safety** — Loose or missing types, unchecked casts, untyped boundaries, and missing return/error contracts (adapt to the language).
6. **Performance smells** — Obvious inefficiencies: N+1 queries, repeated expensive work without memoization/caching, unnecessary re-computation or re-rendering, blocking I/O on hot paths.
7. **Review dependency usage** — Overlapping libraries serving the same purpose, or heavy dependencies used trivially.

## Output Expectations

Produce a Markdown report with:

### Summary
One-paragraph overview of codebase health and top findings.

### Findings
A numbered list, each with:
- **Location**: file path and line range
- **Smell/Issue**: concise description
- **Why it matters**: maintainability/performance/readability impact
- **Impact**: Low / Medium / High
- **Suggested refactor**: brief description of the change
- **Risk**: Low / Medium / High (chance of regression)

### Prioritized Plan
| Priority | Finding # | Effort (S/M/L) | Impact | Risk | Description |
| --- | --- | --- | --- | --- | --- |

### Quick Wins
Low-effort, low-risk, high-value refactors that can be done immediately.

## Quality Assurance

- Every finding must reference a specific file and location.
- Suggestions must be compatible with the project's actual framework and conventions.
- Do not propose new abstractions for one-time use.
- Call out any refactor that would change public behavior or APIs.
- Do not modify code unless explicitly asked. This skill reports by default.
