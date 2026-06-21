---
name: functional-review
description: Review the existing functionality of an application for correctness, broken flows, missing states, and bugs. Use when asked to "do a functional review", "check the app works correctly", "find broken flows", "review functionality", or "audit user flows". Technology-agnostic.
disable-model-invocation: true
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <feature-or-flow-to-review>
---

# Functional Review

## Mission

Review the application's **current** functionality and behavior for correctness and completeness. Identify broken or incomplete user flows, missing feedback states, edge-case mishandling, and likely bugs. This is a quality review of what already exists — not a request for new features. Report findings only; do not modify code unless the user explicitly asks.

## Scope & Preconditions

- If the user names a feature or flow, scope the review there; otherwise review the primary user-facing flows.
- Infer the stack and architecture: read manifests, entry points, routing/operation declarations, and any `docs/`, `README`, or architecture notes.
- Map the actual feature set from routes, handlers/operations, and the directory structure before judging completeness.

## Workflow

1. **Inventory flows** — Enumerate the main user flows end to end (e.g. sign-up, core actions, settings, payments). For each, trace the path from entry point through business logic to output.
2. **Correctness check** — For each flow, verify the logic does what it claims: inputs map to expected outputs, state transitions are valid, and calculations/conditions are correct. Flag logic that looks wrong or contradictory.
3. **State coverage** — Verify each flow handles all states: loading, empty, error, success, partial/permission-restricted, and offline/timeout where relevant. Flag missing or misleading feedback states.
4. **Edge cases & validation** — Check boundary inputs (empty, zero, very large, malformed, duplicate, concurrent), and confirm the app degrades gracefully rather than crashing or corrupting data.
5. **Error handling** — Verify failures are caught and surfaced meaningfully to the user; flag swallowed errors, generic messages hiding real problems, and unhandled rejections/exceptions.
6. **Consistency of behavior** — Check that equivalent actions behave the same way across the app (e.g. confirmation before destructive actions, consistent permission gating, consistent navigation results).
7. **Accessibility & UX gaps** — Note obvious accessibility issues (keyboard, labels, focus, contrast) and confusing or dead-end interactions, where applicable to the platform.

## Output Expectations

Produce a Markdown report with:

### Functional Health Overview
A brief assessment of how complete and correct the reviewed functionality is.

### Findings
A numbered list, each with:
- **Flow / Area**: which feature or flow it affects
- **Issue**: what is broken, incomplete, or incorrect
- **Location**: file path(s) and line range(s)
- **Impact on user**: what the user experiences
- **Severity**: Critical (broken/data loss) / High / Medium / Low
- **Suggested fix**: concise description of how to address it
- **Confidence**: Confirmed / Likely / Potential

### Missing States Matrix
| Flow | Loading | Empty | Error | Success | Notes |
| --- | --- | --- | --- | --- | --- |

### Prioritized Fix Plan
| Priority | Finding # | Severity | Effort (S/M/L) | Description |
| --- | --- | --- | --- | --- |

### Quick Wins
Low-effort fixes that immediately improve correctness or UX.

## Quality Assurance

- Every finding must reference a specific file and location and be grounded in actual code, not assumptions.
- Distinguish confirmed bugs from suspected ones via the confidence level.
- Keep this review about existing behavior; defer brand-new feature ideas to the next-feature-opportunities skill.
- Do not modify code unless explicitly asked. This skill reports by default.
