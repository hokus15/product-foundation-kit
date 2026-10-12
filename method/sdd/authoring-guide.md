# SDD authoring guide

This guide supports W06–W12 in the kit's SDD module. Read it from the external source when the endpoint includes that work and the increment has a ready PM-to-SDD review. An external SDD tool uses its own sequence and native templates through the [integration procedure](../handoff.md). Specification links below identify source blueprints or templates; generated definitions belong to the target project. The [wizard workflow](workflow.md) owns execution order and completion conditions; [working roles](roles.md) define the human and AI perspectives; the [artifact catalog](artifacts.md) owns output paths and templates.

Define product behavior once, independently of implementation architecture and programming stack. Multiple architecture profiles reuse the same product, UI, contracts, and acceptance criteria, with their own technical plans and evidence.

Read project conventions and any separate authoritative documentation policy, then the actual product foundation or retained/extracted vision, scope, actors, capabilities, quality, and vocabulary sources. Resolve contradictions in the source owning the behavior. Reference PM evidence and the selected increment's authoritative W05 review. Use each definition's authoritative consolidated or split source.

Apply the [document description rules](../generation.md#document-descriptions) to shared specifications and profile guides. Update them to describe current behavior, decisions, and procedures; keep rationale and history in their responsible records.

## Domain, processes, and rules — W06

For applicable processes, describe the trigger, participants, steps, decisions, exceptions, and outcomes using the [process template](../../templates/sdd/specs/product/templates/process.md). When shared concepts, relationships, or states need a model, define them in the project's domain model using the [blueprint](../../templates/sdd/specs/product/domain/model.md). Record shared constraints and calculations with the [business rule template](../../templates/sdd/specs/product/templates/business-rule.md).

Business concepts belong in the domain; storage representation belongs to the technical profile. When a rule depends on changing external criteria, use the [regulatory catalog](../../templates/sdd/specs/product/templates/regulatory-catalog.yaml) to record applicability, dates, sources, and reviews. Verify official sources before marking a source review complete.

## Features — W07

Use the [canonical template](../../templates/sdd/specs/product/templates/feature.md) and cataloged Feature path. Preserve its fields and section meanings, follow the product documentation language choice, and remove resolved prompts.

Define verifiable requirements, use cases, criteria, and boundaries. Reference shared rules and existing sources. Keep `ui_refs` and `contract_refs` empty when those documents are unavailable. Specification status is separate from fulfillment of its Definition of Done.

Feature and page statuses: `draft` (being defined), `ready` (definition reviewed for the increment), and `deprecated` (retired). A documented review or explicit instruction supports the transition to `ready`.

## Interactions — W08

Complete applicable shared UI patterns and write pages using the [page template](../../templates/sdd/specs/ui/templates/page.md). Describe hierarchy, actions, loading, empty, error, and success states, adaptation, and accessibility. Use the [flow template](../../templates/sdd/specs/ui/templates/flow.md) when a cross-page journey needs a shared definition.

Create applicable contracts using the [operation template](../../templates/sdd/specs/contracts/templates/operation.md), independently of transport. Link the Features and rules that support inputs, results, failures, and guarantees.

For a product without a graphical interface, record UI non-applicability and define the corresponding channel's experience. Do not create contracts for an interaction boundary that does not exist.

## Acceptance and specification readiness — W09

Keep each Feature's own criteria in its specification. Use shared [acceptance scenarios](../../templates/sdd/specs/product/templates/acceptance-scenario.md) when verification spans Features and [synthetic examples](../../templates/sdd/specs/product/templates/acceptance-example.md) when reusable data clarifies defined behavior.

Review these criteria for the selected increment:

- [ ] SDD-READY-01 — The increment's scope and actors are bounded.
- [ ] SDD-READY-02 — Required rules and domain concepts are defined.
- [ ] SDD-READY-03 — Features have verifiable outcomes and criteria.
- [ ] SDD-READY-04 — UI and contracts cover applicable interactions.
- [ ] SDD-READY-05 — Relevant edge cases and quality conditions have planned verification.
- [ ] SDD-READY-06 — Behavior blockers are resolved and remaining questions are located.

Record criterion outcomes and project references in target `project-state.md`, generated from the [state template](../../templates/project/state.md), before technical planning. Reference this review from the increment's technical plans when they are created at W11. These criteria review specification content; implementation readiness also requires the W12 review.

## Architecture and technical planning — W10–W11

Review the [principles](../../templates/sdd/specs/architecture/principles.md), define the intended profile's architectural approach and programming stack, and record significant choices with [ADRs](../../templates/sdd/specs/architecture/templates/adr.md). Use the explicitly requested profile or resolve the default through [current.md](../../templates/sdd/specs/architecture/current.md). Update that selection only when a supported instruction or decision activates the profile. Identify frontend and backend implementation selections separately where applicable.

Use the [profile templates](../../templates/sdd/specs/architecture/templates/README.md) for the overview, Feature integration plans, reusable [enablers](../../templates/sdd/specs/architecture/templates/enabler.md), operating guides, and initial conformance record. CI and deployment guides are conditional and have their own templates.

For another profile of an already specified increment, reuse supported PM and W09 reviews and repeat W10–W12. Refer to existing shared specifications and record the profile's coverage separately. A technical limitation remains a profile gap; changing shared behavior requires an explicit product decision.

Each Feature plan identifies concrete source and generated files, integration work, dependencies, and validation mappings. Record proposed procedures as unexecuted and unknown commands as pending.

Early technical research can resolve a feasibility risk. If its result changes behavior or scope, resolve that decision in product specifications and reopen affected reviews.

## Implementation handoff — W12

Apply BUILD-READY-01 through BUILD-READY-05 from the workflow. Resolve implementation blockers, reconcile the artifact register, and preserve the review in project state and profile plans. A readiness result records supported definitions and planning.

## Implementation, verification, and subsequent increments

With an authorized implementation request, use the workflow's I01–I04 activities and [implementation roles](roles.md#authorized-implementation-roles). Build the specified scope under `implementation/`. Run proportionate behavior, contract, and quality checks and record actual revision, coverage, and results in the profile.

Evaluate technical compliance and product outcomes separately: the profile demonstrates conformance; PM reviews whether the increment produced its intended effect.

For another increment, update risks and priorities and return to the applicable workflow step. Preserve identifiers and authoritative sources. Changed accepted technical decisions require superseding ADRs; changed behavior requires updating its product source and reviewing affected dependencies.
