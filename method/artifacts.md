# PM artifact catalog

This catalog defines canonical schemas and destinations for W00–W05. Source paths are relative to the external kit; destinations are relative to the separate project root. Generate content progressively using the [conversation guide](guide.md), [workflow](workflow.md), and [generation protocol](generation.md).

## Default PM core

A new PM foundation uses seven files by W05: README, AGENTS, conventions, state, initiative, product foundation, and one selected increment. Create them as their content becomes applicable. Existing project sources satisfy the corresponding content requirements.

| Step | Minimum required content | Conditional work |
| --- | --- | --- |
| W00 | State with source, adopted revision or recovery action, destination, and next action. | External retrieval at the adopted revision, outside the project. |
| W01 | README, AGENTS, conventions, and state with languages, authority, endpoint, and workflow mode needed for discovery. | Separate language policy when it needs independent maintenance. |
| W02 | Initiative problem and its basis; foundation value, actors, and usage context. | Current practice if it affects a decision; vocabulary, evidence records, or technical discovery when needed. |
| W03 | Foundation scope, exclusions, capabilities, applicable quality conditions and planned checks; initiative objectives. | Candidate opportunity comparisons, future options, or additional investigation that informs a current decision. |
| W04 | A selected INC with outcome, boundaries, selection rationale, and evaluation approach; identified decision-relevant risks and dependencies. | Separate opportunity, risk, priority, or roadmap documents when they need independent maintenance; RES, VAL, DEC, and early profile records under their triggers. |
| W05 | One authoritative PM-SDD review for the increment and baseline, referenced from state; reconciled navigation and next action. | Separate transfer document and mapping when a receiving workflow or participant needs them; discovery to resolve failed readiness. |

Minimum content can be satisfied by supported existing sources. Unknowns have a specific impact and next action; they block a phase when its exit condition depends on them. Include fields and questions that support current decisions or phase minima.

## Project configuration and progress

| Canonical source | Project destination | Creation condition | Responsibility |
| --- | --- | --- | --- |
| [README](../templates/project/readme.md) | `README.md` | W01 | Brief purpose and navigation to existing sources. |
| [Agent instructions](../templates/project/agents.md) | `AGENTS.md` | W01 | Operational rules and method resumption; reference conventions. |
| [Conventions](../templates/project/conventions.md) | `project-conventions.md` | W01 | Identity, languages, rules, participants, and authority. |
| [State](../templates/project/state.md) | `project-state.md` | W00 onward | Provenance, active step, actual progress, blockers, and next action. |
| [Documentation policy](../templates/project/documentation-policy.md) | `documentation-policy.md` | Conditional | Existing policy retained, or language and translation rules need independent maintenance. Otherwise conventions own these choices. |

## PM records

| Canonical source | Project destination | Creation condition | Responsibility |
| --- | --- | --- | --- |
| [Initiative](../templates/pm/initiative.md) | `pm/initiative.md` | W02, expanded at W03–W04 | Problem, objectives, evidence, constraints, and applicable hypotheses, opportunities, priorities, and risks. |
| [Increment](../templates/pm/increment.md) | `pm/INC-NNN-short-description.md` | W04 | Selected bounded outcome, rationale, evaluation, and authoritative W05 review. |
| [Transfer](../templates/pm/sdd-handoff.md) | `pm/sdd-handoff.md` | A receiving workflow or participant needs a separate transfer or mapping record. | References the authoritative review and sources; owns transfer progress. |
| [Opportunities](../templates/pm/opportunities.md) | `pm/opportunities.md` | Candidate needs require an independently maintained map. | Extracted opportunities and their evidence. |
| [Risks](../templates/pm/risks.md) | `pm/risks.md` | Risks require a separate maintained register. | Extracted uncertainty, impact, ownership, and actions. |
| [Priorities](../templates/pm/priorities.md) | `pm/priorities.md` | Several candidates require a maintained ordering and comparison. | Extracted priority rationale; INC owns its selection. |
| [Roadmap](../templates/pm/roadmap.md) | `pm/roadmap.md` | Multiple increments need a maintained sequence. | Outcome-oriented sequence. |
| [Research](../templates/pm/research.md) | `pm/research/RES-NNN-short-description.md` | An identifiable source or research activity informs a decision. | Attributed sources, planned activity, and actual findings when available. |
| [Validation](../templates/pm/validation.md) | `pm/validation/VAL-NNN-short-description.md` | A defined hypothesis needs a proportionate agreed or delegated check. | Planned check and actual findings when executed. |
| [Decision](../templates/pm/decision.md) | `pm/DEC-NNN-short-description.md` | A consequential product or investment choice needs a separate rationale or supersession record. | Decision basis and history. |
| [Decision index](../templates/pm/decisions.md) | `pm/decisions.md` | DEC navigation needs a separate index. | Links to existing decisions. |

## Shared product foundation

| Canonical source | Project destination | Creation condition | Responsibility |
| --- | --- | --- | --- |
| [Foundation](../templates/product/foundation.md) | `specs/product/foundation.md` | W02, bounded at W03 | Shared value, actors, scope, capabilities, quality, and needed vocabulary. |
| [Vision](../templates/product/vision.md) | `specs/product/vision.md` | Existing definition retained, or product direction needs independent maintenance. | Extracted purpose and direction; reference the initiative's problem. |
| [Actors](../templates/product/actors.md) | `specs/product/actors.md` | Existing definition retained, or actors and responsibilities need independent maintenance. | Extracted actors and applicable access. |
| [Scope](../templates/product/scope.md) | `specs/product/scope.md` | Existing definition retained, or scope needs independent maintenance. | Extracted boundaries and exclusions. |
| [Capabilities](../templates/product/capabilities.md) | `specs/product/capabilities.md` | Existing definition retained, or capability navigation needs independent maintenance. | Extracted functional map and Feature links. |
| [Quality](../templates/product/quality-requirements.md) | `specs/product/quality-requirements.md` | Existing definition retained, or quality needs independent maintenance. | Extracted observable conditions and planned checks. |
| [Glossary](../templates/product/glossary.md) | `specs/product/glossary.md` | Existing definition retained, or vocabulary needs independent maintenance. | Extracted business terms and distinctions. |

When extracting content, preserve identifiers and replace its former definition with a link. One source owns each definition. Use the project's authoritative consolidated or split definitions throughout PM and SDD.

## Conditional technical records

Use [technical discovery](technical-discovery.md) when feasibility or a consequential technical choice affects scope, cost, priority, or investment. Reuse RES and VAL records above.

| Canonical source | Project destination | Creation condition |
| --- | --- | --- |
| [Profile](../templates/sdd/specs/architecture/templates/profile.md) | `specs/architecture/profiles/<profile>/README.md` | A consequential early choice needs an identified technical context. |
| [ADR](../templates/sdd/specs/architecture/templates/adr.md) | `specs/architecture/profiles/<profile>/adr/ADR-NNNN-short-description.md` | A significant technical choice needs basis, alternatives, consequences, and decision status. |

Preserve profile-local numbering. New ADRs are `proposed` unless acceptance is supported. Profile activation follows a supported selection decision; early records contain the known technical context. Register executable-check paths and scope through the extension rule; record actual evidence in the investigation. Keep decision acceptance and executed feasibility or implementation evidence distinct.

## Navigation outputs

The root README is sufficient navigation for the default PM core. Create the following indexes only when the number or grouping of existing records makes separate navigation useful; retain existing indexes and update affected links at phase closure.

| Canonical source | Conditional project destination |
| --- | --- |
| [PM index](../templates/pm/indexes/pm.md) | `pm/README.md` |
| [Research index](../templates/pm/indexes/research.md) | `pm/research/README.md` |
| [Validation index](../templates/pm/indexes/validation.md) | `pm/validation/README.md` |
| [Product index](../templates/product/index.md) | `specs/product/README.md` |
| [Specifications index](../templates/product/specifications-index.md) | `specs/README.md` |

## Tracking and completion

Register concrete outputs and their canonical sources before authoring. Keep factual status and meaningful changes current. In PM, record conditional no-file decisions when omission affects phase readiness, a request, or downstream work.

| Tracking status | Meaning |
| --- | --- |
| `retained` | Existing content preserved with its current status. |
| `planned` | Applicable concrete output registered. |
| `draft` | Content being defined or containing open questions. |
| `authored` | Applicable sections contain facts or specific pending items; producer instructions removed. |
| `reviewed` | Manual authoring review supported by sources. |
| `not-applicable` | A relevant conditional output is unnecessary, with its reason. |
| `deferred` | Supported later work with reason and next action; phase completion requires its minimum content. |

Working document statuses remain `draft`, `reviewed`, and `archived`. RES, VAL, DEC, and INC retain their canonical status meanings. Manual phase review checks applicable metadata, IDs, links, and consistency. W05 uses PM-SDD-01–07 from the [increment template](../templates/pm/increment.md). State and transfer records link the authoritative review; preserve reviews per increment and baseline. Automated documentation checks run only when explicitly requested.

## Source-only resources

Root kit documents, housekeeping and release files, all method guides, canonical schemas, and supplementary reference resources stay external. Tool-specific project configuration needs a selected tool and supported scope.

## Identifiers and naming

Preserve IDs, filenames, metadata keys, and status meanings. Assign the next unused OBJ, OPP, RES, VAL, RISK, DEC, or INC number when creating its record. Use the project's language and kebab-case conventions with cataloged prefixes and patterns. Stable QR references apply whether quality is inline or extracted.

## Extending the catalog

Before creating a new type or destination, record purpose, owning area, trigger, concrete path or pattern, canonical source, and authorization basis in state's extension register. Reuse an existing type when it fits. Explicit instructions or delegated scope support routine extension; clarify absent authority.

After PM, broader kit endpoints use the [SDD catalog](sdd/artifacts.md). External workflows use their native schemas and the [transfer procedure](handoff.md), preserving actual paths and shared-source ownership.
