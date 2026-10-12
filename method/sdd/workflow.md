# SDD and execution workflow

Use this workflow with `workflow_mode: kit` and an endpoint beyond PM. The [complete route](../workflow.md) defines scope and owns W00–W05; this module continues from a ready W05 handoff. External mode uses its receiving workflow's own sequence.

Read the [authoring guide](authoring-guide.md), [working roles](roles.md), and [artifact catalog](artifacts.md), then the project's existing definitions. Keep all source resources external through the [generation protocol](../generation.md).

W06–W09 define shared behavior and acceptance. W10–W12 create the intended profile's technical plan and handoff. I01–I04 implement, verify, release, and review outcomes within the recorded endpoint and scope. Reuse supported reviews and early decisions; update project state with the active W or I step, hats, increment, profile, artifacts, evidence, and next action.

Read the actual PM sources: a consolidated product foundation or retained/extracted definitions, and the selected INC's authoritative PM review or its retained source. Conventions own language choices unless a separate existing policy owns them. W06–W12 and I01–I04 retain their own output and review requirements.

## Shared definition and implementation profiles

Define product behavior independently of implementation architecture and programming stack. W02–W09 build the shared product foundation, reusable UI, and transport-independent contracts. W10–W12 map that definition to a specific architecture profile.

Each profile owns its architectural approach, stack, ADRs, enablers, delivery plans, operating guides, and conformance evidence. Profiles reference the same product sources and acceptance criteria. Architecture and stack changes update the relevant profile; product changes update the shared sources and reopen affected reviews.

In the kit route, plan another profile for an already specified increment as follows. External workflows preserve the same source ownership through the integration procedure:

1. Read its existing PM and specification reviews and verify that they still apply to the requested scope and source revision.
2. Reuse supported W00–W09 work and continue at W10 for the intended profile. Resolve a missing or changed product definition at its responsible step.
3. Register W10–W12 artifacts and handoff reviews for that profile, preserving earlier profiles and their evidence.
4. Record implementation coverage against the shared criteria separately for each profile. A technical limitation remains a profile gap until addressed or an explicit product decision changes the requirement.

Use an explicitly requested profile for the task; otherwise resolve the active combination from `specs/architecture/current.md`. Creating or evaluating another profile does not activate it. Update the active selection only when a supported instruction or decision selects it.


## W06 — Domain, processes, and shared rules

**Working hats:** Human — Domain Contributor; AI — Business Analyst.

**Inputs:** selected increment, product context, glossary, quality conditions, and known business practice.

**Questions:** What triggers the process? Which concepts, relationships, states, decisions, exceptions, and calculations determine its outcome? Which rules are shared? Which external criteria constrain them?

**Outputs:** update vocabulary in its actual owning foundation or glossary source; create an applicable domain model, PROC processes, and shared BR rules. Record omitted conditional domain outputs and their reasons in project state. Create `domain/regulatory-decisions.yaml` when a changing external criterion constrains a rule. Update the process and rule indexes.

**Checks:** use the cataloged process and rule templates. Attribute rules to product decisions or sources; do not infer business behavior from a technical preference. Keep unreviewed external sources pending. Explain when entities, persistent state, or shared rules do not apply.

**Exit:** the concepts, process, and rules needed to specify the increment are defined; business questions blocking observable behavior are resolved.

## W07 — Feature specifications

**Working hats:** Human — Functional Reviewer; AI — Functional Analyst.

**Inputs:** the increment's bounds and applicable context, domain, processes, and rules.

**Questions:** Which bounded behaviors realize the outcome? What are their actors, preconditions, success results, failure paths, and edge cases? What examples would distinguish correct behavior?

**Outputs:** one or more `specs/product/features/FEAT-NNN-short-description.md` documents using the canonical Feature template; update the Feature index and capability navigation in its owning foundation or capability document.

**Checks:** preserve template fields and section meanings; use stable RF, CU, and AC identifiers within each Feature. Reference existing shared rules. Keep optional UI and contract references empty until those documents exist. Explain non-applicable sections and retain unsupported Definition of Done items unchecked.

**Exit:** every behavior included in the increment is represented by a Feature with verifiable requirements and acceptance criteria, or is explicitly excluded.

## W08 — UI and interaction contracts

**Working hats:** For UI: Human — Experience Reviewer; AI — UX/UI Designer. For contracts: Human — Interaction Consumer; AI — Functional Analyst.

**Inputs:** Features, actors, product rules, and quality conditions.

**Questions:** How does the user or caller perform the task? What information and feedback are needed? Which operations, results, and business failures are observable? Does this increment need graphical UI, reusable patterns, or a separate flow?

**Outputs:** applicable `specs/ui/principles.md`, `navigation.md`, `layouts.md`, `components.md`, page and flow specifications, and `CON-NNN` contracts. Generate UI and contract indexes when records exist; record non-applicability in project state. Add optional Feature traceability only to existing documents.

**Checks:** use page, flow, and operation templates. Keep UI framework-independent and contracts transport-independent. Do not invent metrics, permissions, formulas, consistency guarantees, or error behavior. Resolve missing behavior in product sources. Record non-applicability when there is no graphical UI or no relevant interaction boundary.

**Exit:** the increment's applicable interactions are specified and traceable to its Features; each omitted conditional artifact has a recorded reason.

## W09 — Acceptance and specification review

**Working hats:** Human — Acceptance Reviewer; AI — Quality Analyst.

**Inputs:** Features, domain rules, applicable interactions, and quality requirements.

**Questions:** Which examples or cross-Feature journeys require shared acceptance records? Do the specified outcomes cover important boundaries and failures? Which unanswered criterion blocks technical planning?

**Outputs:** conditional `SCN-NNN` scenarios, `EX-NNN` synthetic examples, and their acceptance index; the specification review in project state. Retain each Feature's own criteria in that Feature.

**Checks:** use cataloged scenario and example templates. Derive expected outcomes from defined rules; label synthetic data. Review SDD-READY-01 through SDD-READY-06 from the SDD guide. Check that the artifact register covers every applicable Feature, interaction, and acceptance record.

**Exit:** the specification readiness criteria are supported by references and behavior blockers are resolved. A specifications-only request can stop here. Preserve this review in state; link it from delivery plans when they are created at W11.

## W10 — Architecture and profile selection

**Working hats:** Human — Technical Decision Owner; AI — Software Architect.

**Inputs:** reviewed shared specifications, quality conditions, operating constraints, explicit technical preferences, and existing profiles.

**Questions:** Are we reusing an existing profile or defining another implementation of the same product? What architectural approaches, programming stacks, constraints, and trade-offs matter? Which significant decisions need a record? Resolve the intended task profile and any requested activation separately.

**Outputs:** `specs/architecture/principles.md`, a profile README, applicable ADRs, and the profile catalog. Update `current.md` only for a supported selection, recording the applicable implementation directories.

**Checks:** use profile and ADR templates. Keep architectural patterns and stack choices in the profile, with shared principles applied where relevant. Reference existing product, UI, and contract sources without copying their behavior into profile-specific variants. Attribute constraints and decisions to their sources; keep proposed ADRs proposed unless acceptance is explicit or supported by a recorded decision. Do not activate architecture from a folder's presence. Keep unknown implementation selections pending.

**Exit:** significant choices needed by the delivery plan have an explicit basis and the intended profile is identified. Proposed choices that block planning keep this step open.

## W11 — Delivery and operating plans

**Working hats:** For delivery planning: Human — Delivery Owner; AI — Technical Lead. For operating guides: Human — Operating Owner; AI — DevOps Engineer.

**Inputs:** shared specifications, the applicable W09 review, intended profile decisions, and reusable technical needs.

**Questions:** Which reusable capabilities are needed? How will each Feature integrate with them? Which concrete files and checks belong to delivery? Which local, CI, and deployment procedures are actually needed and known?

**Outputs:** Feature implementation plans, conditional enablers, an initial profile conformance record, and applicable development, CI, and deployment guides. Update profile navigation. Record Feature-specific code and tooling files in Feature plans and shared capability files in enablers; preserve their exact source and generated-path boundaries.

**Checks:** use the cataloged templates for each record. Separate reusable capability work from Feature integration. Copy or link the supported W09 review into plans. Map each profile's coverage to the shared acceptance criteria. Mark initial coverage as `not-started` unless actual evidence for that profile supports another status; another profile's completion does not establish this one's. Commands require a selected tool and a known basis; record tentative procedures as proposed and unexecuted.

**Exit:** each included Feature has a bounded integration plan and proportionate validation mapping. Required enablers and operating procedures are defined or their blockers are identified. Optional CI and deployment remain non-applicable or deferred with a reason.

## W12 — Documentation and implementation handoff

**Working hats:** Human — Product Owner / Technical Decision Owner; AI — Quality Analyst / Software Architect.

**Inputs:** the selected increment and intended profile, their artifact register, the applicable shared specification review, and that profile's architecture decisions and delivery plans.

**Questions:** Which remaining gap blocks implementation? Which recorded assumption or operating limitation must the implementation work respect? Ask about the next requested action when it is not established.

**Outputs:** the final authoring review in state and necessary updates to the increment and profile plans. Update the project README's navigation to existing project documents.

**Checks:** apply the generation protocol's final authoring review: all target files belong to the initiative, local navigation refers to existing project outputs, and source-only guides and templates remain external. Record these criteria with supporting sources for the selected increment and intended profile:

- [ ] BUILD-READY-01 — The selected increment's PM and specification reviews support the planned behavior.
- [ ] BUILD-READY-02 — Applicable technical decisions and implementation selections have a recorded basis.
- [ ] BUILD-READY-03 — Included Features and required enablers have bounded plans and validation mappings.
- [ ] BUILD-READY-04 — The artifact register accounts for required and conditional outputs, and remaining implementation blockers are resolved.
- [ ] BUILD-READY-05 — Source, generated files, and planned code/tooling boundaries are recorded where applicable.

**Exit:** record `ready-for-implementation` for the selected increment and intended profile only when all five criteria are supported. Otherwise retain the open review and name the specific next action. Documentation readiness does not mark implementation, tests, deployment, or product outcomes verified.

## Authorized implementation and follow-up

These activities follow supported W12 readiness when implementation or follow-up is included in the recorded scope. Keep actual progress in project state and profile delivery and conformance records. W00–W12 define the documentation sequence; I01–I04 execute applicable engineering and product follow-up. External mode retains the receiving workflow's own execution process. Use the [implementation roles](roles.md#authorized-implementation-roles) and record the active activity in state.

### I01 — Implement the bounded task

**Working hats:** Human — Technical Decision Owner; AI — Software Engineer.

Read the relevant shared specifications, intended profile, accepted decisions, enablers, and delivery plans. Confirm the requested bounds from existing instructions. Implement through the planned source and generated-file boundaries; resolve missing behavior in its product source and technical gaps in the profile. A significant new architectural choice returns to W10 with its working hats before updating the decision and plan. Update the relevant delivery records.

### I02 — Verify behavior and technical conformance

**Working hats:** Human — Acceptance Reviewer; AI — Quality Engineer.

Run the applicable authorized behavior, contract, quality, and tooling checks. Record actual criteria, source and implementation revisions, results, and gaps in the profile conformance and delivery records. Return to I01 for failures; reopen the responsible specification step when expected behavior is unclear. Automated documentation checks retain the project's explicit-request policy.

### I03 — Release when requested

**Working hats:** Human — Operating Owner; AI — DevOps Engineer.

Proceed when release is explicitly requested or included in the authorized task. Follow the intended profile's documented prerequisites and procedure for the selected target, using I02 results to assess its release conditions. Record actual release and verification evidence in its deployment guide and conformance record. Resolve missing access or procedures before dependent actions.

### I04 — Evaluate outcomes when requested

**Working hats:** Human — Product Owner; AI — Product Manager.

Use the increment's evaluation plan and actual observations. Record the observed outcome and subsequent decision in its increment record; update relevant risk and priority content in the initiative or extracted records, and an existing roadmap when applicable. Another increment returns to W04; another architecture profile of the same specified scope returns to W10 with supported reviews.

## Completion of execution activities

- I01 records bounded source changes and mapped requirements in delivery records; writing code does not establish verification.
- I02 records applicable executed checks, results, source and implementation revisions, and unresolved failures in conformance. The implementation endpoint requires actual checks supporting the requested criteria; failures return to I01 or the responsible specification step.
- I03 records the actual target, delivered revision, operating checks, and material gaps. Planned procedures or missing access do not establish a release.
- I04 records actual observations, comparison with the increment's evaluation plan, and a subsequent product decision. Missing observations remain a named dependency.

Stop at the selected endpoint when its result is supported. A readiness review or completed phase does not complete later phases. Extend scope when requested and resume from its earliest unresolved prerequisite.

## Scope changes and additional files

Use the artifact catalog before creating a document. Register concrete paths and applicability as answers establish them. A cataloged type can be instantiated within the requested scope without an extra approval for every file.

For a new type or path outside the catalog, first record its purpose, owner, trigger, proposed template, and authorization basis in the extension register. Reuse an existing type when it fits. Proceed when explicit instructions or delegated scope support the extension; otherwise clarify the new scope. Record supported extensions in project state with their concrete destinations and source templates. The external catalog remains in the method source.

Maintenance of this module follows [the maintainer guide](../../MAINTAINING.md). It does not start or complete an initiative's wizard steps.
