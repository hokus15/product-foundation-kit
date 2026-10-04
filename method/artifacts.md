# PM artifact catalog

This catalog defines the PM wizard's input schemas and generated outputs. All source paths are relative to Product Foundation Kit; all destinations are relative to the separate `<project-root>`.

Read templates externally. Register concrete project paths before authoring, preserve existing IDs and content, and generate each output when its condition applies. Source guides and catalogs remain external.

## Step outputs

| Step | Required content | Conditional content |
| --- | --- | --- |
| W00 | `project-state.md` with actual source, resolved revision when available, destination, and next action; unknown provenance includes its recovery action. | External retrieval at the adopted revision when needed; its checkout is outside the project. |
| W01 | Root README, AGENTS, conventions, documentation policy, and updated state. | Supported additional working rules. |
| W02 | Initiative, vision, actors, and glossary content supported by known answers. | Research or technical records when an identifiable question needs them. |
| W03 | Scope, capabilities, quality requirements, and opportunities; objective updates. | Further research and technical records when constraints or feasibility affect scope. |
| W04 | Risks, priorities, roadmap, and selected INC record. | Research, validation, investment decisions, and scoped technical profile records under their triggers. |
| W05 | PM handoff, increment's retained review, reconciled navigation, and state. | Discovery records to resolve failed readiness; mappings when downstream transfer is requested. |

Required content can be satisfied by an applicable reviewed update to an existing document. Unknown facts remain specific pending questions. Conditional absence needs a reason; unperformed investigation provides no findings.

## Project configuration and progress

| Canonical source template | Generated project destination | Trigger or owning step | Responsibility |
| --- | --- | --- | --- |
| [templates/project/readme.md](../templates/project/readme.md) | `README.md` | W01 | Project purpose and navigation to existing outputs. |
| [templates/project/agents.md](../templates/project/agents.md) | `AGENTS.md` | W01 | Project-specific agent rules and method resumption. |
| [templates/project/conventions.md](../templates/project/conventions.md) | `project-conventions.md` | W01 | Identity, working rules, participants, and authority. |
| [templates/project/documentation-policy.md](../templates/project/documentation-policy.md) | `documentation-policy.md` | W01 | Documentation languages and naming conventions. |
| [templates/project/state.md](../templates/project/state.md) | `project-state.md` | W00 onward | Actual provenance, progress, hats, reviews, and next action. |

## PM records

| Canonical source template | Generated project destination | Trigger or owning step | Responsibility |
| --- | --- | --- | --- |
| [templates/pm/initiative.md](../templates/pm/initiative.md) | `pm/initiative.md` | W02–W04 | Problem, objectives, sponsorship, and constraints. |
| [templates/pm/opportunities.md](../templates/pm/opportunities.md) | `pm/opportunities.md` | W03 | Candidate needs and desired outcomes. |
| [templates/pm/risks.md](../templates/pm/risks.md) | `pm/risks.md` | W04 | Known uncertainty and actions. |
| [templates/pm/priorities.md](../templates/pm/priorities.md) | `pm/priorities.md` | W04 | Priority rationale. |
| [templates/pm/roadmap.md](../templates/pm/roadmap.md) | `pm/roadmap.md` | W04 | Outcome-oriented increment sequence. |
| [templates/pm/sdd-handoff.md](../templates/pm/sdd-handoff.md) | `pm/sdd-handoff.md` | W05 | Reviewed baseline, PM-SDD results, questions, and transfer. |
| [templates/pm/decisions.md](../templates/pm/decisions.md) | `pm/decisions.md` | Conditional | Index when a DEC record exists. |
| [templates/pm/research.md](../templates/pm/research.md) | `pm/research/RES-NNN-short-description.md` | Conditional, W02 or W04 | Identifiable evidence source or research activity; keep planned work distinct from findings. |
| [templates/pm/validation.md](../templates/pm/validation.md) | `pm/validation/VAL-NNN-short-description.md` | Conditional, W04 | Defined hypothesis and proportionate agreed or delegated check. |
| [templates/pm/decision.md](../templates/pm/decision.md) | `pm/DEC-NNN-short-description.md` | Conditional, any PM step | Consequential product or investment choice needs a rationale or supersession record. |
| [templates/pm/increment.md](../templates/pm/increment.md) | `pm/INC-NNN-short-description.md` | W04 | Selected bounded outcome with evaluation approach and retained review. |

## Shared product foundation

| Canonical source template | Generated project destination | Trigger or owning step | Responsibility |
| --- | --- | --- | --- |
| [templates/product/vision.md](../templates/product/vision.md) | `specs/product/vision.md` | W02 | Shared product context and vocabulary. |
| [templates/product/actors.md](../templates/product/actors.md) | `specs/product/actors.md` | W02 | Shared product context and vocabulary. |
| [templates/product/glossary.md](../templates/product/glossary.md) | `specs/product/glossary.md` | W02 | Shared product context and vocabulary. |
| [templates/product/scope.md](../templates/product/scope.md) | `specs/product/scope.md` | W03 | Bounded shared product definition and observable needs. |
| [templates/product/capabilities.md](../templates/product/capabilities.md) | `specs/product/capabilities.md` | W03 | Bounded shared product definition and observable needs. |
| [templates/product/quality-requirements.md](../templates/product/quality-requirements.md) | `specs/product/quality-requirements.md` | W03 | Bounded shared product definition and observable needs. |

## Conditional technical records

Use the [technical discovery branch](technical-discovery.md) when early technical input affects feasibility, scope, cost, priority, or investment. These outputs can be authored within W02–W04; they require no W09 specification review or full W10 planning cycle.

| Canonical source | Generated project destination | Creation condition |
| --- | --- | --- |
| [Research](../templates/pm/research.md) or [validation](../templates/pm/validation.md) | Existing RES or VAL patterns above. | A bounded technical question needs investigation or a defined hypothesis needs an agreed or delegated check. |
| [Profile overview](../templates/sdd/specs/architecture/templates/profile.md) | `specs/architecture/profiles/<profile>/README.md` | A consequential early technical choice needs an identified architectural context; record only known decisions and specific pending work. |
| [ADR](../templates/sdd/specs/architecture/templates/adr.md) | `specs/architecture/profiles/<profile>/adr/ADR-NNNN-short-description.md` | A significant technical decision needs a recorded basis, scope, alternatives, and consequences. |

Keep ADR numbering local to the stable profile name. New ADRs are `proposed` unless explicit instructions or evidence establish acceptance. A new evaluation profile does not activate itself or require plans, enablers, code, or operating guides.

Register prototype or executable-check paths and scope through the extension rule before creating them. Record executed evidence in the investigation; an accepted ADR proves a decision, not a successful experiment or implementation.

## Navigation outputs

| Canonical source template | Generated project destination | Trigger or owning step | Responsibility |
| --- | --- | --- | --- |
| [templates/pm/indexes/pm.md](../templates/pm/indexes/pm.md) | `pm/README.md` | When PM content exists | Navigation to existing PM records. |
| [templates/pm/indexes/research.md](../templates/pm/indexes/research.md) | `pm/research/README.md` | When RES records exist | Research navigation. |
| [templates/pm/indexes/validation.md](../templates/pm/indexes/validation.md) | `pm/validation/README.md` | When VAL records exist | Validation navigation. |
| [templates/product/index.md](../templates/product/index.md) | `specs/product/README.md` | When product content exists | Product navigation. |
| [templates/product/specifications-index.md](../templates/product/specifications-index.md) | `specs/README.md` | When specification content exists | Navigation to existing shared definitions. |

Generate indexes around existing documents. Empty future directories and template navigation add no project output.

## Source-only resources

- Root kit README, AGENTS, Getting Started, maintainer guide, versioning policy, changelog, and source housekeeping and release-tooling files.
- All `method/` guides, including this catalog and the handoff rules.
- Template catalogs and canonical schemas under `templates/`.
- Optional resources under `reference/`.

The source `.gitignore` is kit housekeeping. Project-specific ignore rules require a selected tool and supported scope through the extension rule.

## Status and completion

Use these artifact-register statuses independently of a document's metadata:

| Status | Meaning |
| --- | --- |
| `retained` | Existing content preserved; no new readiness claimed. |
| `planned` | Concrete applicable output registered. |
| `draft` | Content being defined or containing open questions. |
| `authored` | Main sections contain project facts or specific pending items; producer instructions removed. |
| `reviewed` | Manual authoring checks supported by sources. |
| `not-applicable` | Conditional output unnecessary, with a reason. |
| `deferred` | Supported later work, with reason and next action; not a substitute for required PM content. |

Working document statuses remain `draft`, `reviewed`, and `archived`. Keep research, validation, decision, and increment statuses from their canonical templates.

Manual completion checks cover metadata, main sections, identifier uniqueness, relative links, and consistency with authoritative definitions. PM-SDD-01–07 establish handoff readiness. Automated documentation checks run only when explicitly requested.

## Identifiers and naming

Preserve existing IDs and filenames. Use the next unused number per series: OBJ, OPP, RES, VAL, RISK, DEC, and INC. Metadata keys and defined status tokens remain stable.

Use the project's chosen filename conventions with kebab-case descriptions. The catalog's destination patterns retain their established prefixes and numbering. Define new type naming explicitly in the extension register.

## Extending the catalog

Before creating a new type or destination, record purpose, owning area, trigger, concrete path or pattern, canonical source, and authorization basis in project state. Reuse an existing type when it fits.

Proceed when explicit instructions or delegated scope support the extension; clarify absent authority. The project extension register supplements this catalog without copying method instructions locally.

After PM transfer, the receiving workflow defines its native outputs. Record actual paths and shared-source ownership in the handoff. Broader kit endpoints use the [SDD and execution catalog](sdd/artifacts.md). External modes use native output definitions and recorded mappings.
