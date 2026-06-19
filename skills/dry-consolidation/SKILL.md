---
name: dry-consolidation
description: Audit a codebase for duplication and inconsistency (DRY violations) and propose concrete consolidation into shared components, helpers, and utilities. Use when asked to "find duplication", "DRY this up", "check consistency", "deduplicate code", or "find repeated patterns". Technology-agnostic.
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <path-or-area-to-audit>
---

# DRY & Consolidation Audit

## Mission

Audit the codebase for repeated logic, copy-pasted code, and inconsistent patterns (UI, behavior, styling, structure), then propose concrete opportunities to consolidate duplication into shared, reusable building blocks. Report findings and a consolidation plan; do not refactor unless explicitly asked.

## Scope & Preconditions

- If the user names an area, scope there; otherwise cover the whole repository.
- Infer the stack and inspect existing shared code first (e.g. `shared/`, `common/`, `utils/`, `lib/`, `hooks/`, `components/`) so you don't propose recreating something that already exists.
- Respect the project's existing conventions and module boundaries.

## Workflow

### Phase 1 — Duplication Discovery
1. **Repeated logic** — Find blocks of near-identical logic across files (validation, formatting, parsing, mapping, guards). Group them.
2. **Copy-paste families** — Identify families of components/functions/classes that differ only slightly and could share a base or be parameterized.
3. **Constants & config** — Find duplicated literals, magic numbers, strings, endpoints, and config values that should be centralized.

### Phase 2 — Consistency Audit
1. **Behavioral patterns** — Compare how the same concept is implemented across the app (data fetching, error handling, retries, pagination, auth/permission checks). Flag divergent approaches.
2. **UI patterns** (if applicable) — Compare buttons, forms, modals/dialogs, cards, tables, empty/loading/error states, toasts. Flag inconsistent variants and ad-hoc reimplementations of the same concept.
3. **Formatting** — Flag inconsistent date/time, number, and currency formatting done multiple different ways.
4. **Structural patterns** — Verify handlers/operations/modules follow a uniform shape (e.g. validate → authorize → act → respond). Flag outliers.

### Phase 3 — Consolidation Opportunities
For each duplication cluster, propose a single shared component, hook, helper, or constant. Verify the proposed abstraction does not already exist before suggesting creating it.

## Output Expectations

Produce a Markdown report with:

### Executive Summary
Overview of the consistency/duplication state and the most impactful opportunities.

### Duplication Map
| Pattern | Occurrences | Files | Shared version exists? |
| --- | --- | --- | --- |

### Consistency Issues
A numbered list, each with:
- **Category**: UI / Behavior / Formatting / Structure
- **Issue**: what is inconsistent or duplicated
- **Locations**: file paths and line ranges of each variant
- **Severity**: Low / Medium / High (by user impact and maintenance cost)

### Proposed Shared Building Blocks
For each proposed component/hook/utility/constant:
- **Name**: proposed name
- **Type**: Component / Hook / Utility / Constant
- **Replaces**: files and line ranges it would replace
- **API sketch**: brief interface
- **Effort**: S / M / L
- **Impact**: number of call sites consolidated

### Prioritized Consolidation Plan
| Priority | Item | Type | Effort | Files affected | Impact |
| --- | --- | --- | --- | --- |

### Quick Wins
Low-effort, low-risk consolidations (e.g. replacing inline duplicates with an existing helper).

## Quality Assurance

- Every finding must reference specific file paths and line ranges.
- Do NOT propose extracting an abstraction used in only one place.
- Verify a shared version doesn't already exist before suggesting creation.
- Prefer the smallest abstraction that removes the duplication; avoid over-engineering.
- Do not refactor unless explicitly asked. This skill reports by default.
