# Product templates

- [Feature](feature.md): bounded behavior; save in `features/FEAT-NNN-short-description.md`.
- [Process](process.md): business flow; save in `processes/short-description.md`.
- [Rules](business-rule.md): shared definitions; save in `domain/rules/short-description.md`.
- [Acceptance scenario](acceptance-scenario.md): a journey spanning several Features; save in `acceptance/scenarios/SCN-NNN-short-description.md`.
- [Acceptance example](acceptance-example.md): reusable synthetic inputs and rule-derived outcomes; save in `acceptance/examples/EX-NNN-short-description.md`.
- [Regulatory catalog](regulatory-catalog.yaml): optional resource for rules dependent on legislation, official guidance, or other changing external criteria.

Copy the regulatory catalog to `domain/regulatory-decisions.yaml` when applicable to the product; its entries reference existing rules. Adapt its scope to relevant regulation and retain effective dates, sources, owners, and review evidence. Keep internal decisions without regulatory dependencies in their rules and decision records.

Preserve template metadata and section meanings. Follow language choices in [project conventions](../../../../project/conventions.md) or a separate authoritative documentation policy when present, assign stable IDs, and remove instructions from the resulting document.

Use the [artifact catalog](../../../../../method/sdd/artifacts.md) for creation conditions and the [workflow](../../../../../method/sdd/workflow.md) for step ownership.
