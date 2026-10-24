---
name: ai-slop-detector
description: Audit AI-assisted code for logic defects, unsupported claims, overengineering, and hallucinated dependencies (slopsquatting). Use for AI-slop reviews, suspicious generated imports, or prevention guidance for recurring generated-code defects.
---

# AI Slop Detector

Find quality defects in AI-assisted code and recommend concrete fixes. Judge behavior and evidence, not presumed authorship: generic names, polished prose, or boilerplate can guide inspection but do not prove a defect or AI origin.

Report by default. Apply fixes only when explicitly requested; architectural or public-API changes require human approval.

## Workflow

1. **Scope.** Review the requested diff, paths, or repository. Read local instructions, stack configuration, representative code, tests, and existing shared implementations. For supplied snippets, limit conclusions to the available context and identify missing callers or contracts. Finish with the review boundary, expected behavior, and applicable project standards identified.
2. **Inspect.** Apply every relevant review category below. Use searches to locate candidates, then read surrounding code and callers. Finish when each category is examined or marked not applicable; identify any uninspected areas.
3. **Verify.** Trace each candidate to a failing behavior, violated contract, unsupported claim, or concrete maintenance cost. Check edge cases and integration context. Use focused tests, existing analysis tools, or measurements where they resolve uncertainty. Finish when each candidate is supported, rejected, or explicitly unresolved with the missing evidence.
4. **Recommend.** Rank supported findings by the severity guide. Give the smallest fix that respects existing architecture, plus a regression check. Finish when every finding has a location, evidence, impact, remedy, and verification path. Flag Critical/High findings for experienced developer review before merge.
5. **Close.** Deliver the report below. If fixes were requested, apply the approved changes and run affected tests and existing lint, type, and security checks as relevant. Finish with outcomes recorded and any remaining failure or unverified claim stated plainly.

For requests about **preventing recurrence, generation guardrails, or CI checks**, read [Prevention](references/prevention.md). For prevention-only requests, use that workflow directly and inspect code only as needed to substantiate the advice. Keep one-off reviews focused on the code rather than introducing a process rollout.

## Review categories

### Logic and contracts

Trace inputs through conditions, state transitions, outputs, and error propagation. Check empty/null/zero/boundary cases, race conditions, resource ownership, and API compatibility. Verify that tests assert behavior and exercise the real implementation.

### Efficiency

Look for redundant work, unsuitable data structures, N+1 queries, blocking operations, leaks, and unnecessary optimization. Explain the affected path and workload. Use profiling or benchmarks for quantitative performance claims; distinguish measured results from suspected bottlenecks.

### Readability and architecture

Compare naming, abstraction levels, module boundaries, error handling, and logging with repository conventions. Look for copy-paste families, unused abstractions, and reinvention of existing helpers. Report generic naming only when it obscures meaning; recommend the smallest change that removes the ambiguity or maintenance cost.

### Comments and documentation

Use these signals to find claims worth checking:

| Signal | Verify | Recommendation |
| --- | --- | --- |
| "Optimized", "efficient", or percentage improvements | A supporting benchmark and its conditions | Cite the measurement, describe the actual change, or remove the claim |
| "Robust", "seamless", "production-ready" | The mechanism or guarantee being claimed | State the concrete behavior and limits |
| Comments translating function names | Whether they add rationale, constraints, or a non-obvious contract | Keep useful context; remove redundant narration |
| Conversational artifacts or placeholder TODOs | Whether they belong in the committed artifact and identify actionable work | Replace with technical content or a specific tracked gap |
| Aesthetic language | Whether the document calls for it and whether it makes a technical claim | Preserve intentional voice; verify factual claims separately |

Search matches are leads, not severity ratings. A misleading claim can matter more than redundant prose; assess its actual consequence. When proposing wording, use verified facts rather than invented metrics or technical detail.

### Security

Inspect input handling, query construction, authorization, secret handling, and sensitive-data flows. Establish the reachable path and impact before reporting a vulnerability. Use existing security tooling where relevant and available; state when a concern needs specialist verification.

### Dependencies and slopsquatting

**Slopsquatting** is abuse of a plausible package name hallucinated by an AI system: an attacker can register that name to distribute malicious code.

For suspicious or newly introduced dependencies, verify the exact name, version, source, and intended API against the authoritative registry or upstream project. Compare manifests and lockfiles; inspect provenance and known advisories where available. `npm view` can query registry metadata; `pip show` describes a local installation and does not establish registry existence or trust.

Verify before installing or executing a suspicious package. A registered name alone is not proof of legitimacy. If registry or provenance evidence is unavailable, report that limit rather than declaring the dependency safe or malicious.

## Severity

| Severity | Impact |
| --- | --- |
| Critical | Supported exploitable security issue, malicious dependency, data corruption, or severe outage |
| High | Incorrect core behavior, major performance degradation, resource leak, or breaking contract |
| Medium | Meaningful maintenance burden, localized inefficiency, or misleading technical guidance |
| Low | Limited-impact naming, redundant comments, or minor style inconsistencies |

Use impact and reachability to choose severity. Style signals, missing measurements, and suspicious package names do not independently justify High or Critical ratings.

## Report

Lead with the most important supported result and review scope. If no defects are supported, say so without implying proof of correctness.

| Severity | Location | Finding | Evidence and impact | Recommended fix |
| --- | --- | --- | --- | --- |

Use `file:line-range` and the relevant symbol for each location. Under each finding, give a focused regression check and any prevention measure specific to its cause. Separate unresolved concerns from verified defects and state checks that could not be run.

For requested fixes, summarize changes, validation outcomes, remaining issues, and human approvals still needed.
