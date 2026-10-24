---
name: next-feature-opportunities
description: Recommend the next product features and UX improvements, ranked by user value and grounded in the existing application.
disable-model-invocation: true
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <product-area-to-focus-on>
---

# Next Feature Opportunities

Recommend what to build next, using the product's current capabilities and user flows as evidence. This is a recommendation task; leave implementation unchanged.

## Workflow

1. **Map the product.** Honor any named focus area and audience; otherwise inspect the application. Trace routes, screens, handlers, models, and integrations alongside product docs and requirements. If an unknown audience or goal would materially change the ranking, ask a focused question; otherwise state the working assumption. Finish with a map of each major capability in scope, its user flow, and source locations. Distinguish implemented behavior from documented plans, label UX behavior inferred from source rather than observed, and identify unexplored areas.
2. **Find opportunities.** Apply each relevant lens below to the map. Check plausible gaps against existing implementations, including less visible routes or settings, before calling a capability missing. Finish with candidates tied to an observed limitation or an extension of an existing capability.
3. **Rank.** Compare user value, flow blockers, reach, implementation effort, dependencies, and uncertainty. Use P0 for critical blockers, P1 for high-value work, P2 for medium-value work, and P3 for optional polish. Finish with an ordered shortlist and an explicit reason for each ranking. Treat demand, retention, and revenue effects as hypotheses unless supported by supplied research or analytics.
4. **Make actionable.** For the top five supported opportunities, or fewer if evidence warrants, identify the user outcome and the smallest useful scope. Ground implementation considerations in the actual framework, models, operations, and UI patterns. Label proposed additions as new work. Finish when each top recommendation has evidence, a user story, an effort estimate, and a way to assess its value.

## Opportunity lenses

| Lens | Examine |
| --- | --- |
| UX completeness | Interrupted flows, missing loading/error/empty states, friction, and accessibility barriers |
| Adjacent capabilities | Import/export, search, sharing, sync, notifications, automation, or integrations that extend current value |
| Engagement | Onboarding and reasons to return that serve the user's goals |
| Monetization | Existing value gates and conversion or expansion opportunities, when relevant to the product |
| Differentiation | Distinctive value built on current strengths; verify competitor claims or label them as hypotheses |

## Report

**Feature health:** Briefly describe what works today, incomplete flows, and the scope or evidence limits.

**Ranked opportunities**

| Priority | Area | Suggested change | Evidence | User value | Effort |
| --- | --- | --- | --- | --- | --- |

Use source paths and relevant symbols or line ranges for evidence. Estimate effort as Small / Medium / Large and state material dependencies.

**Top features:** Expand the top five, or the supported subset, without repeating the table. For each, give a user story ("As a ... I want to ... so that ..."), minimum useful scope, architecture-specific implementation considerations, complexity drivers, and a success signal.

Mark low-effort UX wins in the table. State open product questions that could change the ranking rather than filling gaps with invented user needs.
