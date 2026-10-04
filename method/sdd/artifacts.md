# SDD and execution artifact catalog

This catalog defines schemas and project destinations for the kit's selected W06–W12 and I01–I04 scope. The [PM catalog](../artifacts.md) owns W00–W05 and the foundation. Core entries summarize prerequisites; the endpoint determines applicable outputs.

This catalog separates resources in the method source from files generated for the initiative. Source paths refer to the supplied repository or external checkout; project destinations refer to `<project-root>`. Follow the [generation protocol](../generation.md) alongside the [workflow](workflow.md).

## Creation and recording rules

Read method guides, blueprints, and canonical templates externally. Generate project outputs when their step and creation condition apply. Preserve existing project artifacts and identifiers; update supported content in place.

Source-only resources have no default target destination. In particular, project generation keeps `method/`, `templates/`, and `reference/` resources external.

Before authoring, register the concrete project path, type, owning step, applicability, source, and status in `<project-root>/project-state.md`, using the [state template](../../templates/project/state.md). Record conditional no-file decisions. Source resources are retrieved as needed and recorded through method provenance, rather than listed as project outputs.

Use these artifact statuses:

| Status | Meaning |
| --- | --- |
| `retained` | An existing project artifact is preserved; no new completion is implied. |
| `planned` | Applicable output and concrete project path are identified, but authoring has not started. |
| `draft` | Project content is being defined or contains unresolved questions. |
| `authored` | Required sections contain actual content or specific pending decisions; template instructions and dummy placeholders are removed. |
| `reviewed` | Authoring checks passed with references; implementation verification remains separate. |
| `not-applicable` | A conditional project output is unnecessary for the selected scope, with a reason. |
| `deferred` | Applicable project work belongs to a later stage, with a reason and next action. |

These tracking statuses supplement document statuses; they do not replace ADR status, validation execution status, or Feature Definition of Done.

## Required and conditional project content

The PM core uses W00–W05. W06–W12 apply as the selected kit endpoint reaches them. An external SDD workflow follows its own artifact definitions; record actual paths and source ownership through the catalog extension rule and handoff mapping.

This matrix applies through the requested endpoint. Outputs are generated progressively in the target; method resources are read from the external source. Indexes are updated as their records exist. A conditional output becomes required when its creation condition applies.

| Step | Required content | Conditional content |
| --- | --- | --- |
| W00 | `project-state.md`; method source, revision when known, and destination context. | An external source checkout when retrieval needs it. No checkout files are project outputs. |
| W01 | `project-conventions.md`, including participants and decision authority; `documentation-policy.md`, `AGENTS.md`, `README.md`; requested endpoint and working context in state. | Additional project rules through the catalog extension procedure. |
| W02 | `pm/initiative.md`, `specs/product/vision.md`, `specs/product/actors.md`, `specs/product/glossary.md`. | Research records for identifiable sources or activities. |
| W03 | `specs/product/scope.md`, `capabilities.md`, `quality-requirements.md`, and `pm/opportunities.md`; objective updates in the initiative. | Additional research. |
| W04 | `pm/risks.md`, `priorities.md`, `roadmap.md`, and a selected `INC-NNN` record. | Research, validation, and decision records under their conditions. |
| W05 | `pm/sdd-handoff.md`, including source baseline, readiness and downstream next action; the increment's retained review; state. | Discovery records needed to resolve a failed handoff; downstream mappings when requested. |
| W06 | Relevant business vocabulary and domain applicability in project state. | A domain model, processes, shared rules, and regulatory catalog entries needed to define the increment. |
| W07 | At least one Feature and its index; capability navigation to existing Features. | Further Features as the bounded increment requires. |
| W08 | Interaction applicability and conditional-output decisions in project state. | Applicable shared UI specifications, pages, flows, operation contracts, and indexes. |
| W09 | The specification review and project state. | Cross-Feature scenarios, reusable synthetic examples, and their acceptance index. |
| W10 | `specs/architecture/principles.md`, selected profile overview, `current.md`, and profile catalog. | Significant decisions recorded as ADRs. |
| W11 | An implementation plan for each included Feature in its intended profile; profile conformance and navigation. | Required enablers; development, CI, and deployment guides under their conditions. |
| W12 | Implementation handoff review, reconciled state, increment/profile plan updates, root navigation, and generation-boundary review. | Supported catalog extensions needed by the selected scope. |

Unqualified filenames in a row share the directory of the preceding qualified filename. Repeatable destinations and templates are specified below. Requirements for an existing document are satisfied by a reviewed update or retained content with an applicable source reference.

## Root and method source inventory

| Source path | Project destination | Generation condition or source role |
| --- | --- | --- |
| `README.md` | — | Source only: Method purpose and navigation. |
| `AGENTS.md` | — | Source only: Method maintenance and generation instructions. |
| `GETTING_STARTED.md` | — | Source only: Human usage guide. |
| `MAINTAINING.md` | — | Source only: Template maintenance guide. |
| `templates/project/conventions.md` | `project-conventions.md` | W01. |
| `templates/project/documentation-policy.md` | `documentation-policy.md` | W01. |
| `method/guide.md` | — | Source only: Conversation rules. |
| `method/workflow.md` | — | Source only: Step order and gates. |
| `method/roles.md` | — | Source only: Human and AI working hats, contributions, and authority boundaries. |
| `method/generation.md` | — | Source only: External source and progressive project generation protocol. |
| `templates/project/agents.md` | `AGENTS.md` | Generate project-specific agent instructions; W01. Retain the canonical template externally. |
| `templates/project/readme.md` | `README.md` | Generate the initiative's purpose and actual navigation; W01. Retain the canonical template externally. |
| `method/artifacts.md` | — | Source only: File catalog and creation conditions. |
| `templates/project/state.md` | `project-state.md` | Generate project progress and method provenance; W00 onward. Keep template guidance in the source. |
| `method/handoff.md` | — | Source only: Portable SDD handoff, transfer procedure, and source ownership. |
| `.gitignore` | — | Source housekeeping. Use a supported project extension for tool-specific ignore rules. |

## PM source inventory

| Source path | Project destination | Generation condition or source role |
| --- | --- | --- |
| `templates/pm/indexes/pm.md` | `pm/README.md` | Generate navigation when the corresponding project documents exist. PM navigation and source ownership. |
| `templates/pm/initiative.md` | `pm/initiative.md` | Generate the initiative brief; W02–W04. Reference recorded method provenance when relevant. |
| `templates/pm/opportunities.md` | `pm/opportunities.md` | W03–W04. |
| `templates/pm/priorities.md` | `pm/priorities.md` | W04. |
| `templates/pm/roadmap.md` | `pm/roadmap.md` | W04; revise as outcomes change. |
| `templates/pm/risks.md` | `pm/risks.md` | W03–W05; revise when evidence changes. |
| `templates/pm/decisions.md` | `pm/decisions.md` | Update when a decision record exists. |
| `templates/pm/sdd-handoff.md` | `pm/sdd-handoff.md` | W05. |
| `templates/pm/indexes/research.md` | `pm/research/README.md` | Generate navigation when the corresponding project documents exist. Research index. |
| `templates/pm/indexes/validation.md` | `pm/validation/README.md` | Generate navigation when the corresponding project documents exist. Validation index. |
| `templates/pm/README.md` | — | Source only: PM template navigation. |
| `templates/pm/research.md` | — | Source only: Research template. |
| `templates/pm/validation.md` | — | Source only: Validation template. |
| `templates/pm/decision.md` | — | Source only: Product/planning decision template. |
| `templates/pm/increment.md` | — | Source only: Increment template. |

## Product source inventory

| Source path | Project destination | Generation condition or source role |
| --- | --- | --- |
| `templates/product/specifications-index.md` | `specs/README.md` | Generate navigation when the corresponding project documents exist. Specification map. |
| `method/sdd/authoring-guide.md` | — | Source only: SDD content rules and readiness criteria. |
| `templates/product/index.md` | `specs/product/README.md` | Generate navigation when the corresponding project documents exist. Product navigation. |
| `templates/product/vision.md` | `specs/product/vision.md` | W02–W03. |
| `templates/product/actors.md` | `specs/product/actors.md` | W02; refine access when behavior is defined. |
| `templates/product/scope.md` | `specs/product/scope.md` | W03. |
| `templates/product/capabilities.md` | `specs/product/capabilities.md` | W03; add navigation at W07. |
| `templates/product/quality-requirements.md` | `specs/product/quality-requirements.md` | W03; refine for the increment. |
| `templates/product/glossary.md` | `specs/product/glossary.md` | W02 onward. |
| `templates/sdd/specs/product/domain/model.md` | `specs/product/domain/model.md` | W06 when shared concepts, relationships, or states need a model. |
| `templates/sdd/specs/product/domain/rules/README.md` | `specs/product/domain/rules/README.md` | Generate navigation when the corresponding project documents exist. Shared rule index. |
| `templates/sdd/specs/product/processes/README.md` | `specs/product/processes/README.md` | Generate navigation when the corresponding project documents exist. Process index. |
| `templates/sdd/specs/product/features/README.md` | `specs/product/features/README.md` | Generate navigation when the corresponding project documents exist. Feature index. |
| `templates/sdd/specs/product/acceptance/README.md` | `specs/product/acceptance/README.md` | Generate navigation when the corresponding project documents exist. Shared scenario and example index. |
| `templates/sdd/specs/product/templates/README.md` | — | Source only: Product template navigation. |
| `templates/sdd/specs/product/templates/feature.md` | — | Source only: Feature template. |
| `templates/sdd/specs/product/templates/process.md` | — | Source only: Process template. |
| `templates/sdd/specs/product/templates/business-rule.md` | — | Source only: Shared rule template. |
| `templates/sdd/specs/product/templates/acceptance-scenario.md` | — | Source only: Scenario template. |
| `templates/sdd/specs/product/templates/acceptance-example.md` | — | Source only: Synthetic example template. |
| `templates/sdd/specs/product/templates/regulatory-catalog.yaml` | — | Source only: Optional regulatory catalog template. |

## UI and contract source inventory

| Source path | Project destination | Generation condition or source role |
| --- | --- | --- |
| `templates/sdd/specs/ui/README.md` | `specs/ui/README.md` | Generate navigation when the corresponding project documents exist. UI navigation and applicability. |
| `templates/sdd/specs/ui/principles.md` | `specs/ui/principles.md` | W08 when graphical UI applies. |
| `templates/sdd/specs/ui/navigation.md` | `specs/ui/navigation.md` | W08 when graphical UI applies. |
| `templates/sdd/specs/ui/layouts.md` | `specs/ui/layouts.md` | W08 when applicable. |
| `templates/sdd/specs/ui/components.md` | `specs/ui/components.md` | W08 when applicable. |
| `templates/sdd/specs/ui/pages/README.md` | `specs/ui/pages/README.md` | Generate navigation when the corresponding project documents exist. Page index. |
| `templates/sdd/specs/ui/templates/page.md` | — | Source only: Page template. |
| `templates/sdd/specs/ui/templates/flow.md` | — | Source only: Cross-page flow template. |
| `templates/sdd/specs/contracts/README.md` | `specs/contracts/README.md` | Generate navigation when the corresponding project documents exist. Contract catalog and applicability. |
| `templates/sdd/specs/contracts/templates/operation.md` | — | Source only: Operation template. |

For a nonvisual increment, record UI non-applicability in project state and omit graphical UI outputs. Record absent interaction boundaries similarly. Source scaffolds remain authoring resources; they do not establish a need for target files.

## Architecture, collaboration, and implementation source inventory

| Source path | Project destination | Generation condition or source role |
| --- | --- | --- |
| `templates/sdd/specs/architecture/README.md` | `specs/architecture/README.md` | Generate navigation when the corresponding project documents exist. Architecture navigation and boundaries. |
| `templates/sdd/specs/architecture/principles.md` | `specs/architecture/principles.md` | W10. |
| `templates/sdd/specs/architecture/current.md` | `specs/architecture/current.md` | W10 when selection is supported. |
| `templates/sdd/specs/architecture/profiles/README.md` | `specs/architecture/profiles/README.md` | Generate navigation when the corresponding project documents exist. Profile catalog. |
| `templates/sdd/specs/architecture/templates/README.md` | — | Source only: Architecture template navigation. |
| `templates/sdd/specs/architecture/templates/profile.md` | — | Source only: Profile overview template. |
| `templates/sdd/specs/architecture/templates/adr.md` | — | Source only: Decision record template. |
| `templates/sdd/specs/architecture/templates/enabler.md` | — | Source only: Reusable capability template. |
| `templates/sdd/specs/architecture/templates/feature-implementation.md` | — | Source only: Feature delivery plan template. |
| `templates/sdd/specs/architecture/templates/development.md` | — | Source only: Local development guide template. |
| `templates/sdd/specs/architecture/templates/conformance.md` | — | Source only: Coverage and validation template. |
| `templates/sdd/specs/architecture/templates/ci.md` | — | Source only: Optional automation guide template. |
| `templates/sdd/specs/architecture/templates/deployment.md` | — | Source only: Optional deployment guide template. |
| `reference/collaboration/README.md` | `collaboration/README.md` | Generate local coordination conventions and navigation only when those records are used. |
| `reference/collaboration/templates/opportunity.md` | — | Source only: Coordination template. |
| `reference/collaboration/templates/work-item.md` | — | Source only: Coordination template. |
| `reference/collaboration/templates/change-review.md` | — | Source only: Coordination template. |
| `templates/sdd/areas/implementation.md` | `implementation/README.md` | Generate known source boundaries and existing navigation when implementation planning or code needs them. |
| `templates/sdd/areas/dev.md` | `dev/README.md` | Generate known tooling boundaries and existing navigation when project tools are needed. |

## Repeatable PM outputs

| Type and destination | Canonical source template | Creation condition and first step |
| --- | --- | --- |
| `pm/research/RES-NNN-short-description.md` | [Research](../../templates/pm/research.md) | Identifiable research source or activity informs a decision; W02 or W04. No findings are invented for planned work. |
| `pm/validation/VAL-NNN-short-description.md` | [Validation](../../templates/pm/validation.md) | A defined hypothesis and a proportionate agreed or delegated check can affect a decision; W04. Execution remains planned until performed. |
| `pm/DEC-NNN-short-description.md` | [Decision](../../templates/pm/decision.md) | A consequential product/planning choice needs rationale or supersession; any applicable step. Proposals remain proposed. |
| `pm/INC-NNN-short-description.md` | [Increment](../../templates/pm/increment.md) | A candidate outcome is bounded; W04. Selection requires a recorded choice. |

## Repeatable product and interaction outputs

| Type and destination | Canonical template | Creation condition and first step |
| --- | --- | --- |
| `specs/product/processes/short-description.md`, ID `PROC-NNN` | [Process](../../templates/sdd/specs/product/templates/process.md) | A flow is needed to define the selected increment; W06. |
| `specs/product/domain/rules/short-description.md`, rule IDs `BR-NNN` | [Business rules](../../templates/sdd/specs/product/templates/business-rule.md) | A shared constraint or calculation needs one authoritative definition; W06. Group related rules with distinct IDs. |
| `specs/product/domain/regulatory-decisions.yaml` | [Regulatory catalog](../../templates/sdd/specs/product/templates/regulatory-catalog.yaml) | A rule depends on changing regulation or official criteria; W06 or revision of that rule. |
| `specs/product/features/FEAT-NNN-short-description.md` | [Feature](../../templates/sdd/specs/product/templates/feature.md) | A bounded behavior is included in the selected increment; W07. At least one Feature is required for an increment entering specification. |
| `specs/ui/pages/short-description.md` | [Page](../../templates/sdd/specs/ui/templates/page.md) | Graphical UI performs a specified task; W08. |
| `specs/ui/flows/FLOW-NNN-short-description.md` | [Flow](../../templates/sdd/specs/ui/templates/flow.md) | A cross-page journey needs a shared definition beyond its page specifications; W08. |
| `specs/contracts/operations/CON-NNN-short-description.md` | [Operation](../../templates/sdd/specs/contracts/templates/operation.md) | An observable interaction boundary requires an operation contract; W08. |
| `specs/product/acceptance/scenarios/SCN-NNN-short-description.md` | [Scenario](../../templates/sdd/specs/product/templates/acceptance-scenario.md) | Acceptance spans multiple Features; W09. |
| `specs/product/acceptance/examples/EX-NNN-short-description.md` | [Example](../../templates/sdd/specs/product/templates/acceptance-example.md) | Synthetic business data and expected results are reused or clarify a significant boundary; W09. |

Own Feature criteria remain in Features. Single-page interaction stays in its page unless a separate flow is useful. Empty reference lists are valid when no applicable existing source is available; record the gap instead of linking an invented document.

## Repeatable architecture outputs

All profile paths below start with `specs/architecture/profiles/<profile>/`. Instantiate them for each intended profile while reusing the shared product, UI, contract, and acceptance sources. Another profile of the same specified increment repeats W10–W12 with its own artifacts and evidence.

| Destination inside the profile | Canonical template | Creation condition and first step |
| --- | --- | --- |
| `README.md` | [Profile](../../templates/sdd/specs/architecture/templates/profile.md) | An early technical decision needs a profile, or W10 evaluates an implementation. |
| `adr/ADR-NNNN-short-description.md` | [ADR](../../templates/sdd/specs/architecture/templates/adr.md) | A significant choice needs a record during early technical discovery or W10. Acceptance and supersession require a supported decision. |
| `enablers/ENAB-NNN-short-description.md` | [Enabler](../../templates/sdd/specs/architecture/templates/enabler.md) | A bounded reusable technical capability is required; W11. |
| `implementation/FEAT-NNN-short-description.md` | [Feature plan](../../templates/sdd/specs/architecture/templates/feature-implementation.md) | An included Feature needs delivery planning for this profile; W11. Reuse the Feature ID. |
| `conformance.md` | [Conformance](../../templates/sdd/specs/architecture/templates/conformance.md) | A profile delivery plan needs a coverage record; W11. Start without claimed implementation evidence. |
| `development.md` | [Development](../../templates/sdd/specs/architecture/templates/development.md) | A planned implementation needs local setup and validation procedures; W11. |
| `ci.md` | [CI](../../templates/sdd/specs/architecture/templates/ci.md) | Automation is selected and needs documented execution; W11. |
| `deployment.md` | [Deployment](../../templates/sdd/specs/architecture/templates/deployment.md) | Release or distribution to an operating environment is in scope; W11. |

Technical plans reference shared product, UI, contracts, and their profile's accepted decisions without changing product behavior. Each profile records its own conformance against the shared criteria. A guide with unresolved required commands is draft and may block implementation readiness; do not write plausible commands as though they were verified.

## Coordination, code, and external configuration

Collaboration records are conditional: create them when local coordination is needed within the requested scope. They can also be used in a selected external tracker without creating local files.

| Local destination | Canonical template | Creation condition |
| --- | --- | --- |
| `collaboration/records/opportunities/short-description.md` | [Opportunity](../../reference/collaboration/templates/opportunity.md) | A product question needs a coordination record. |
| `collaboration/records/work-items/short-description.md` | [Work item](../../reference/collaboration/templates/work-item.md) | A bounded activity needs assignment or tracking. |
| `collaboration/records/change-reviews/short-description.md` | [Change review](../../reference/collaboration/templates/change-review.md) | A proposed change needs a recorded review. |

Register the concrete location and purpose before creating a local record. Reference applicable existing sources and specification IDs; unresolved discovery can reference its PM context. Coordination records do not become alternative sources of business behavior.

Apply the workflow's I01–I04 activities and [implementation roles](roles.md#authorized-implementation-roles) when their scope is authorized. Code, tests, generated assets, and executable tooling are planned in profile delivery records with concrete paths, purposes, and validation. Feature plans own Feature-specific files; enablers own shared capability files. Their creation requires implementation scope. Provider-specific configuration additionally requires a selected integration. The documentation wizard does not create a runtime or CI configuration because an example or template mentions one.

## Identifiers and paths

Assign the next unused identifier in each established series and preserve existing IDs. Use the selected filename language with kebab-case descriptions. ADR and enabler numbering is local to each profile; other document IDs are unique within the project.

Scope criterion references by their document, such as `FEAT-NNN / AC-01`. Keep the Feature template's RF and CU IDs stable, UI page criteria as `UI-AC-NN`, and quality criteria as `QR-NN-AC-NN`.

Translate headings and descriptive content through the documentation policy. Preserve metadata keys and defined status tokens. Create conditional directories when their first applicable file is registered.

## Extending the catalog

Before adding a new type or location, record purpose, owning area, trigger, source template, and authorization basis in project state's extension register. Explicit user instructions or delegated scope can establish that basis; otherwise clarify the need before expanding scope.

Record the supported type, concrete destination or path pattern, and source template in the project's extension register. It supplements this external catalog without copying it into the project. Update project navigation when outputs exist. Method maintainers reconcile the source inventory and generation rules when distributing a changed method.
