# Prevention

Use this reference for generation guardrails, recurring defects, or CI recommendations. Build on the project's existing workflow and scale controls to the observed risk.

## Generation guardrails

1. **Supply context.** Give the generating agent the relevant contracts, repository conventions, representative implementations, and test commands. Reuse existing prompt templates when they help; version templates only when repeated use warrants it.
2. **Bound the change.** Define the intended behavior, allowed surfaces, and human review points. Reserve approval for security-sensitive decisions, complex domain rules, architecture changes, and public contracts.
3. **Require evidence.** Ask for behavior-focused tests and verification of unfamiliar dependencies before use. Performance claims need measurements; documentation claims need a source.

The guardrails are ready when a reviewer can identify what may change, how correctness will be checked, and which decisions require approval.

## Human review

| Point | Reviewer and purpose |
| --- | --- |
| After generation | Developer checks behavior, scope, and obvious defects |
| Critical/High finding | Experienced developer or security specialist validates impact and remedy before merge |
| Architecture or public API change | Tech lead or architect approves the contract and migration approach |
| Before merge | Code reviewer checks the complete change and validation evidence |

Escalate security questions to a specialist, architectural tradeoffs to the tech lead, and measured performance regressions to the responsible engineering team. For repeated defects, address their shared cause in prompts, context, or checks.

## CI checks

Inspect existing scripts and CI configuration first. Recommend only checks that address a demonstrated gap:

| Risk | Check |
| --- | --- |
| Incorrect behavior | Relevant tests, including regression cases for verified defects |
| Type or convention drift | Existing compiler, type checker, linter, and formatter |
| Unsafe dependency changes | Manifest/lockfile consistency, registry and provenance checks, advisory scanning |
| Security defects | Existing secret scanning, static analysis, and specialist review |
| Complexity or duplication | Project-configured analysis, followed by contextual review |
| Unsupported performance claims | Reproducible benchmarks on the affected workload |

Use repository targets for coverage, complexity, duplication, and vulnerability gates. Where none exist, propose thresholds with a rationale for human review. Identifier counts, comment density, package age, and keyword matches are not standalone quality gates.

Finish a prevention proposal with the observed failure mode, the smallest control that would catch it, where that control belongs, and how its effectiveness will be checked. After a fix, rerun affected checks and update shared guidance only when the lesson applies beyond that incident.
