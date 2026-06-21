---
name: next-feature-opportunities
description: Review an application as a product and recommend the most impactful next features and functional improvements to build. Use when asked "what should I build next", "suggest new features", "next feature opportunities", "product improvement ideas", or "what's missing". Technology-agnostic.
disable-model-invocation: true
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <product-area-to-focus-on>
---

# Next Feature Opportunities

## Mission

Analyze the application as a product — its current features, user flows, and gaps — and recommend the most impactful next features and functional improvements to build. Think like a product manager with deep technical understanding. Output ideas and a plan; do not implement anything.

## Scope & Preconditions

- If the user names a focus area or target audience, center recommendations there.
- Infer the product from the codebase: map the feature set from routes, handlers/operations, and the directory structure, plus any `docs/`, `README`, product, or requirements files.
- Ground every recommendation in what actually exists — no invented features or assumptions about code that isn't there.

## Workflow

1. **Audit current features** — Build a complete map of what the product does today from routes/handlers and docs.
2. **Identify UX gaps** — Incomplete flows, missing feedback states, friction points, and accessibility gaps that block value.
3. **Spot missing capabilities & integrations** — Adjacent capabilities or integrations that would extend existing value (e.g. import/export, sync, sharing, notifications, search, automation).
4. **Evaluate engagement & retention** — Assess onboarding, habit loops, and any gamification/notifications; suggest improvements that drive repeat use.
5. **Evaluate monetization** (if applicable) — Examine how value is gated and recommend features likely to improve conversion or expansion.
6. **Differentiate** — Suggest features that would set the product apart from typical competitors in its category.

## Output Expectations

Produce a Markdown report with:

### Feature Health Overview
Brief assessment of current feature completeness and polish.

### Improvement Suggestions
For each suggestion:
- **Area**: which part of the product it affects
- **Suggestion**: what to improve or add
- **User value**: why it matters to end users
- **Effort estimate**: Small / Medium / Large
- **Priority**: P0 (critical) / P1 (high) / P2 (medium) / P3 (nice-to-have)

### Top 5 Next Features to Build
A ranked list, each with:
- Description
- User story ("As a … I want to … so that …")
- Key implementation considerations (data models, operations, UI/components needed) grounded in the existing architecture
- Estimated complexity

### Quick UX Wins
Low-effort improvements that immediately boost the experience.

## Quality Assurance

- Every suggestion must be grounded in what actually exists in the codebase (no assumptions).
- Implementation considerations must respect the project's actual framework and patterns.
- Recommendations must be actionable and specific (not "improve performance" but what and how).
- This skill recommends only; it does not implement features.
