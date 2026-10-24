---
name: stale-code-check
description: Audit dead code, unused dependencies, obsolete configuration, and orphaned assets. Use for stale-code checks or cleanup requests; report evidence and removal risks before deleting anything.
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <path-or-area-to-scan>
---

# Stale Code Audit

Identify removable or outdated code, dependencies, configuration, and assets. Report by default; delete only when the user explicitly asks. A missing static reference is a candidate, not proof of disuse.

## Workflow

1. **Scope.** Use the named area, or cover source, manifests, configuration, and static assets. Locate entry points, framework conventions, generated/vendor boundaries, and any configured dead-code tools. Finish with the scan boundary and known external consumers or runtime wiring identified.
2. **Collect candidates.** Run existing stack-appropriate unused-code tooling when available, then inspect each applicable category below. Treat tool output as leads. Exclude generated and vendored internals; assess tracked build output only through its configuration and consumers. Finish when every category is examined or marked not applicable; disclose unavailable tools and uninspected areas.
3. **Verify reachability.** Trace each candidate through imports, entry points, tests, scripts, configuration, and dynamic wiring. Check reflection, string lookups, dynamic imports, dependency injection, framework discovery, and external callers. Finish when each candidate is supported, rejected, or marked Needs verification with the missing evidence.
4. **Assess action.** Separate removal from upgrade work. Confirm upstream deprecations and version claims through official sources or the package registry; identify the installed version from the lockfile when available. Finish with an action, confidence, removal risk, and validation needed for every retained finding.
5. **Plan cleanup.** Order supported actions from safest to riskiest, with effort estimates. Finish when each finding is accounted for and uncertain removals have an explicit verification step.

## Scan categories

| Category | Candidate evidence and required checks |
| --- | --- |
| Exports, files, components, modules | No discovered consumers; check package exports, side effects, and runtime loading |
| Routes, handlers, operations | Disconnected registration or obsolete callers; public endpoints can be used outside the repository |
| Deprecated APIs and patterns | Verify deprecation and replacement for the project's version |
| Models and fields | Check reads, writes, serialized contracts, external queries, and retention requirements |
| Dependencies | Find unused, deprecated, overlapping-purpose, or outdated packages; check application imports plus test, build, script, and CI consumers before recommending removal |
| Debt markers and feature flags | Inspect `TODO`, `FIXME`, `HACK`, `XXX`, `DEPRECATED`, flag consumers, and rollout state |
| Static assets | Check code, styles, templates, manifests, and constructed paths |
| Migrations and tracked build output | Check migration history, fresh installs, deployment, and distribution requirements; supersession alone is not removal evidence |
| Configuration | Trace plugins, rules, paths, and environment keys through build, runtime, and deployment consumers |

## Report

**Summary:** Counts by category, separating supported findings from candidates needing verification. State scope and evidence limits.

**Findings by category:** For each item, include its path and symbol or line range, evidence and reachability checks, risk (Safe to remove / Needs verification / Keep but update), confidence (High / Medium / Low), and action (remove / update / investigate). Reserve Safe to remove for items whose relevant consumers and retention requirements have been checked.

**Dependency audit**, when applicable:

| Package | Installed / declared | Latest verified | Breaking changes | Action |
| --- | --- | --- | --- | --- |

Mark unavailable version or compatibility information as unverified.

**Cleanup plan:** Reference findings in safest-to-riskiest order, with effort, prerequisites, and checks that would validate each change.
