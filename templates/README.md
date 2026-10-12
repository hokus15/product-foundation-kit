# Canonical authoring templates

Read these schemas as their [workflow](../method/workflow.md) work becomes applicable. The [PM catalog](../method/artifacts.md) and [SDD catalog](../method/sdd/artifacts.md) define project destinations and creation conditions.

| Area | Input schemas |
| --- | --- |
| Project core | [README](project/readme.md), [agent rules](project/agents.md), [conventions](project/conventions.md), and [state](project/state.md). A separate [language policy](project/documentation-policy.md) is conditional. |
| PM | [Initiative, increment, and conditional records](pm/README.md). |
| Product foundation | [Consolidated foundation](product/foundation.md). Split [vision](product/vision.md), [actors](product/actors.md), [glossary](product/glossary.md), [scope](product/scope.md), [capabilities](product/capabilities.md), and [quality](product/quality-requirements.md) remain available for retained or independently maintained definitions. |
| SDD and technical planning | Shared behavior, UI, contracts, architecture, and operating schemas under [templates/sdd/](../method/sdd/artifacts.md). |
| Conditional navigation | PM schemas under `pm/indexes/` and product indexes under `product/`; root README serves the initial PM core. |

Preserve metadata keys, IDs, status meanings, and core section meanings. Add conditional sections only when their triggers apply and later-phase sections when reached. Generate supported facts, choices, attributed hypotheses, and specific questions; remove producer instructions and unused prompts. Recalculate links to actual project owners.

Templates stay external. Reuse already read schemas within a session when unchanged and from the adopted revision. Generate content according to the catalog's creation conditions and the current phase's minimum.
