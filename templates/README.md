# Canonical authoring templates

The assistant reads these schemas while executing the [project workflow](../method/workflow.md). The [PM catalog](../method/artifacts.md) and [SDD catalog](../method/sdd/artifacts.md) define their project destinations and creation conditions.

| Area | Input schemas |
| --- | --- |
| Project | [Purpose](project/readme.md), [agent rules](project/agents.md), [conventions](project/conventions.md), [language policy](project/documentation-policy.md), and [state](project/state.md). |
| PM | [Discovery and decision records](pm/README.md). |
| Product foundation | [Vision](product/vision.md), [actors](product/actors.md), [glossary](product/glossary.md), [scope](product/scope.md), [capabilities](product/capabilities.md), and [quality needs](product/quality-requirements.md). |
| SDD and technical planning | Shared behavior, UI, contracts, architecture, and operating schemas cataloged under [templates/sdd/](../method/sdd/artifacts.md). |
| Project navigation | PM index schemas under `pm/indexes/`; product indexes under `product/`. |

Each template is an input to authoring. Generate actual project facts, choices, hypotheses, and questions in the selected language. Preserve metadata and section meanings; remove producer instructions and recalculate links for the generated destinations.

Templates stay in the external source. The [SDD and execution catalog](../method/sdd/artifacts.md) defines additional specification and technical schemas under `templates/sdd/`, used as the selected kit route reaches them.
