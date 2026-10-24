---
name: unit-test-coverage
description: Audit unit-test gaps and add focused tests for critical behaviors using the project's existing test setup.
disable-model-invocation: true
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <path-or-area-to-cover>
---

# Unit Test Coverage

Add tests that increase confidence in critical behavior. Keep production code unchanged; report any production bug a test exposes.

## Workflow

1. **Discover.** Scope to the named area, or primary source if none is named. Read repository testing instructions, runner and coverage configuration, and representative existing tests. Finish with the commands, test layout, fixture style, and mocking conventions identified. If the test command cannot be determined, ask before proceeding.
2. **Baseline.** Run the existing test command for the scope, with coverage when configured, and record results and failures. If coverage tooling is absent, map source units and behaviors to tests manually and label numeric coverage unavailable; adding tooling requires agreement. Finish with each major area accounted for and pre-existing failures distinguished from missing coverage.
3. **Select gaps.** Inspect untested public units, branches, error paths, boundary cases, permission checks, and domain rules. Include critical behavior even in high-coverage files. Rank using the priorities below. Finish with a bounded set of behaviors to test and a reason each matters; record remaining gaps.
4. **Write tests.** Apply the test rules below to each selected behavior. Finish when every selected gap has an executable test exercising the real unit or a documented blocker requiring integration tests or production changes.
5. **Validate.** Run the smallest existing suite covering the added tests and affected units, plus existing lint/type checks for edited test files. Repeat the same coverage command when available for comparable before/after results. Broaden checks if failures or shared fixtures warrant it. Fix test defects and rerun affected checks. Finish when added tests pass, suite results are accounted for, and coverage changes are explained. If a test reveals a production bug, preserve a faithful reproducer and report the blocker; leave the run explicitly incomplete rather than masking the failure.

## Gap priorities

| Priority | Behavior |
| --- | --- |
| P0 | Authentication, authorization, payments, input validation, and rate limiting |
| P1 | Data integrity during create, update, and delete operations |
| P2 | Domain rules, calculations, state transitions, scoring, money, and units |
| P3 | Rendering, display logic, and formatting |

Use repository coverage targets when defined. Otherwise, use 80% or more, 40-79%, and below 40% as triage bands, not proof of behavioral coverage or completion.

## Test rules

- Follow existing layout, grouping, naming, mocking, and fixture conventions. Name cases by observable behavior.
- Exercise the real unit and assert its output, state change, or interaction contract. Mock external boundaries rather than the behavior under test.
- Cover relevant success, failure, edge, and permission cases for each selected gap.
- Isolate network, filesystem, database, payment, storage, and clock effects with mocks or existing in-memory fakes. Keep cases independent of execution order and shared mutable state.
- Keep every added case runnable with meaningful assertions. Skips, todos, weakened expectations, and production edits are not ways to obtain a passing result.

## Report

**Coverage:** Give before/after line, branch, and function coverage with deltas for each inspected area, where measured. For a manual map, report tested and untested behaviors instead of invented percentages. Note unchanged metrics when new tests strengthen assertions on already-covered code.

**New tests**

| Test file | Tests added | Behaviors covered | Priority |
| --- | --- | --- | --- |

**Validation and remaining gaps:** State commands and outcomes, distinguish baseline failures from new failures, and identify production bugs, integration-test needs, or other blockers.
