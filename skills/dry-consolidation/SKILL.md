---
name: dry-consolidation
description: Audit duplication and inconsistent patterns, then propose shared building blocks and a prioritized consolidation plan.
disable-model-invocation: true
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <path-or-area-to-audit>
---

# DRY Consolidation Audit

Find repeated knowledge and inconsistent implementations of the same concept. Report consolidation opportunities; refactor only when the user explicitly asks.

## Workflow

1. **Scope.** Audit the named area, or the repository if none is named. Identify the stack, module boundaries, conventions, and existing shared components, hooks, utilities, and constants. Finish with the audit boundary and reusable building blocks located.
2. **Discover.** Inspect every applicable category below in maintained source. Trace generated duplication to its generator and leave third-party internals outside the audit. Group related occurrences and record each location as `file:line-range`. Finish when each category is examined or marked not applicable; disclose any uninspected area.
3. **Validate.** Read each candidate occurrence in context. Establish whether the variants encode the same rule or behavior and should change together. Retain intentional differences; identical syntax or equal literals alone do not justify consolidation. Finish with supported clusters and a reason for treating each divergence as a problem.
4. **Design.** For each supported cluster, prefer an existing shared implementation. Otherwise, propose the smallest abstraction serving at least two occurrences. Preserve module boundaries, contracts, and meaningful variations. Finish when each recommendation names its consumers, API, migration risks, and behavior-preserving checks.
5. **Prioritize.** Rank by user impact and maintenance savings relative to effort and coupling. Identify low-risk reuse of existing helpers as quick wins. Finish when every supported cluster has a proposed action or a reason to leave it separate.

## Audit categories

| Category | Look for |
| --- | --- |
| Logic | Repeated validation, parsing, mapping, formatting, and guards |
| Copy-paste families | Components, functions, or classes differing only in parameters or small variants |
| Constants and configuration | Repeated domain values, endpoints, and settings with one intended source of truth |
| Behavior | Divergent fetching, retries, pagination, error handling, and permission checks |
| UI and styling | Reimplemented controls, dialogs, tables, feedback states, and visual variants of the same concept |
| Formatting | Inconsistent dates, times, numbers, and currencies |
| Structure | Outlier operation flows, such as authorization occurring at a different stage |

## Report

Lead with the most valuable consolidations and the scope inspected. If none are justified, say so.

**Duplication map**

| Pattern | Occurrences | Locations | Existing shared version |
| --- | --- | --- | --- |

**Consistency issues:** For each, give its category, differing behaviors, all variant locations, and severity (High / Medium / Low) based on user impact and maintenance cost.

**Shared building blocks:** For each proposal, give its name and type, existing implementation to reuse or reason for a new one, API sketch, replaced locations, call-site count, effort (S / M / L), and migration risks or checks.

**Consolidation plan**

| Priority | Item | Type | Effort | Files affected | Impact |
| --- | --- | --- | --- | --- | --- |

Mark quick wins in the plan rather than repeating them in a separate list.
