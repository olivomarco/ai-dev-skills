---
name: unit-test-coverage
description: Audit unit-test coverage gaps and generate new tests to improve confidence on critical paths. Use when asked to "improve test coverage", "find untested code", "write missing unit tests", "audit test coverage", or "increase coverage". Technology-agnostic.
disable-model-invocation: true
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <path-or-area-to-cover>
---

# Unit Test Coverage Audit & Enhancement

## Mission

Analyze the existing unit-test suite, identify coverage gaps (prioritizing business-critical and security-sensitive code), and generate new tests that meaningfully improve confidence. This skill **writes tests** — but never weakens or alters production code to make tests pass.

## Scope & Preconditions

- If the user names an area, scope there; otherwise cover the primary source.
- **Detect the test setup first**: find the test runner and coverage tool from manifests/config (e.g. Jest/Vitest/Mocha, pytest, go test, JUnit, RSpec, PHPUnit) and the command used to run them. If you cannot determine the commands, ask the user before proceeding.
- **Read existing tests first** — they are the canonical style guide for structure, naming, mocking, and fixtures. Match them.
- Read any testing docs/instructions in the repo before writing tests.

## Workflow

### Phase 1 — Coverage Baseline
1. Run the project's coverage command and capture the output. If no coverage tool exists, derive coverage manually by mapping source units to existing tests.
2. Build a **coverage matrix**: for each major area, record current line/branch/function coverage and mark it 🟢 Good (≥80%), 🟡 Needs work (40–79%), or 🔴 Missing/Critical (<40% or none).

### Phase 2 — Gap Analysis
For each 🔴 and 🟡 area, identify:
1. **Untested units** — public functions/handlers/operations with no test.
2. **Untested branches** — conditionals, error paths, permission checks, edge cases.
3. **Untested security paths** — auth, authorization, input validation, rate limiting.
4. **Untested business logic** — calculations, state machines, scoring, money/units.

Prioritize gaps by risk:
- **P0 — Security**: auth, authorization, payments, input validation
- **P1 — Data integrity**: create/update/delete of user data
- **P2 — Business logic**: domain rules, calculations
- **P3 — Presentation**: rendering, display logic, formatting

### Phase 3 — Test Generation
For each gap, write tests that:
- Mirror the existing test layout, naming, and mocking conventions.
- Use one group/`describe` per unit and one case per behavior, with descriptive names (e.g. "rejects request when user is not authenticated").
- Cover happy path, error paths, edge cases, and auth/permission checks.
- Mock external services (network, DB, payment, storage, clock) — never make real calls or touch real infrastructure.
- Assert something meaningful — avoid tests that only check "does not throw".

### Phase 4 — Validation
1. Run the test suite and ensure all new tests pass.
2. Re-run coverage and confirm it improved.
3. Fix failing tests you wrote. If a test reveals a production bug, **do not silently change production code to hide it** — flag the bug separately. Never use skip/todo to mask failures.

## Output Expectations

### Coverage Report
Coverage matrix with before/after columns and delta.

### New Tests Summary
| Test File | Tests Added | Area | Priority |
| --- | --- | --- | --- |

### Remaining Gaps
Areas that couldn't be covered with unit tests (e.g. needs integration test) and recommended next steps.

## Quality Assurance

- All tests must pass; the suite must exit cleanly.
- No test may depend on execution order or shared mutable state.
- No test may make network requests or touch real filesystems/databases — mock them.
- Do NOT modify production code to make tests pass; test the code as-is and flag bugs separately.
- Do NOT add skipped/todo tests to inflate counts — every test must run and assert.
- Verify new tests actually exercise the code under test (not passing vacuously).
