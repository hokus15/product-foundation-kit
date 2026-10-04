# Project execution workflow

This is the authoritative route for PM, SDD, implementation, and follow-up. The detailed PM steps are below; the [SDD module](sdd/README.md) defines W06–W12 and I01–I04. Use the [conversation guide](guide.md), [working roles](roles.md), [generation protocol](generation.md), and [artifact catalog](artifacts.md). Source templates and project destinations are separate.

## Order and endpoint

| Step | Responsibility | Prerequisite |
| --- | --- | --- |
| W00 | Source and destination | A request to define an initiative. |
| W01 | Configuration, languages, and authority | Persistence is established or drafts are explicitly identified. |
| W02 | Problem, people, and context | Conventions needed to record answers are known. |
| W03 | Value, scope, capabilities, and quality | Problem and intended users are understandable. |
| W04 | Evidence, risks, priorities, and increment | Candidate outcomes and boundaries are identified. |
| W05 | PM-to-SDD review and handoff | A bounded increment has been selected. |

## Selected endpoint and workflow mode

At W01, record the endpoint from instructions. A foundation-only request covers `pm-foundation`; clarify ambiguous broader scope. Use `workflow_mode: kit` unless the project chooses an external SDD tool or process.

| Target stage | Last kit step | Required result |
| --- | --- | --- |
| `pm-foundation` | W05 | Reviewed selected increment and PM handoff. |
| `product-specifications` | W09 | Specification review supported by SDD-READY-01–06. |
| `implementation-plan` | W12 | Intended profile's BUILD-READY-01–05 review. |
| `implementation` | I02 | Requested code and applicable executed verification against specifications. |
| `release` | I03 | Recorded delivery to the identified target and operating verification. |
| `outcome-review` | I04 | Actual outcome evidence and subsequent product decision. |

A broader endpoint includes its necessary earlier steps. Scope can be extended later without repeating supported work. Recorded authorization governs execution within that scope; readiness reviews check prerequisites and do not create a separate permission request for routine phase transitions.

In `external` mode, record the receiving workflow and use its own gates after the PM handoff. Kit W and I IDs apply to the kit route; external phases retain their actual labels and mappings.

Technical discovery and consequential architecture or stack choices can occur during PM when needed. PM readiness requires no selected external tool.

Work can iterate within these steps. New evidence changes its responsible definition and reopens affected reviews. For another increment, revisit W04 and W05 and update W02–W03 when shared context changes.

## Conditional technical discovery

During W02–W04, follow [technical discovery](technical-discovery.md) when a constraint, feasibility question, or consequential technical choice affects scope, cost, priority, or investment. Use its technical hats and [cataloged records](artifacts.md#conditional-technical-records), then return to the interrupted PM step. W05 carries the evidence and decisions into the handoff.

The branch creates only needed investigations or profile decisions. It adds no mandatory architecture phase or full SDD planning sequence.

## Completion and conversation rules

Apply the hats in the role guide and explain their contributions at transitions. Ask for missing knowledge or decision authority only when it affects the next action; apply recorded delegation and reuse answers.

Before completing a step:

- Account for required outputs and applicable conditional outputs in project state.
- Replace resolved prompts with factual content; retain specific open questions with impact, owner where known, and next action.
- Reference sources or decisions supporting consequential definitions and identify hypotheses and proposals.
- Review metadata, IDs, main sections, project links, and consistency with upstream sources.
- Record the exit result and actual saved artifacts. File presence alone establishes no readiness or execution evidence.

A conditional absence needs a reason. Deferral does not satisfy a required output. Keep the step active or blocked while its exit condition is unmet. Automated documentation checks run only when explicitly requested.

## W00 — Source and workspace

**Working hats:** Human — Workspace Owner; AI — Project Facilitator.

**Inputs:** method location, available revision, intended destination, and existing project material.

**Questions:** Where should the project be maintained? Is this a new initiative or an existing product? Ask only for information not already designated.

**Outputs:** generate or reconcile `<project-root>/project-state.md`; record the actual method source, resolved full commit SHA when available, target context, and next action. Keep unknown provenance explicit with a recovery action. Retrieve required method resources externally from the same adopted revision. Later project documents are generated when their content becomes applicable.

**Checks:** keep the method source and any checkout outside the destination; preserve existing project content. Do not copy the source repository into the target. Verify access to the needed guides and templates at the adopted revision, and identify any missing capability. On resumption, do not silently replace the recorded revision. Follow the [versioning policy](../VERSIONING.md) for source recovery and authorized upgrades. Record unsaved drafts explicitly.

**Exit:** the external source and separate target are identified, project state can persist the next answers, and missing source resources are addressed before dependent work.

## W01 — Initial configuration

**Working hats:** Human — Project Owner; AI — Project Facilitator.

**Inputs:** destination, existing user instructions, conventions, language policy, and requested scope.

**Questions:** What working name should we use? Which conversation and document languages apply? What general rules should guide the assistant? Who can supply business knowledge and decide product or technical questions, and which choices can the AI make when delegated? Establish the endpoint and workflow mode from instructions; clarify ambiguous broader scope and use the kit route unless an external workflow is selected. Follow up only on unresolved conventions and authority.

**Outputs:** generate or update `project-conventions.md`, `documentation-policy.md`, the project's README using its canonical source template, and `AGENTS.md` using the project agent template. Record the target stage, workflow mode, scope bounds, and decision context in `project-state.md`. Root documents contain initiative-specific rules and navigation.

**Checks:** distinguish conversation language from document languages, preferences from mandatory constraints, and routine drafting from consequential choices. Keep unrelated platform and technology choices pending.

**Exit:** identity may be provisional, but destination and conventions required for the next documents are known. Every relevant unresolved configuration choice has a next action.

## W02 — Problem, people, and context

**Working hats:** Human — Problem Owner; AI — Product Manager.

**Inputs:** the user's idea, known practice, and available observations or sources.

**Questions:** What outcome would be useful? Who experiences the problem and how is it handled today? Can you describe a concrete case? Who uses the product, receives outputs, or decides scope?

**Outputs:** generate `pm/initiative.md`, `specs/product/vision.md`, `specs/product/actors.md`, and relevant glossary content from source blueprints and answers. Reference recorded method provenance in the brief when relevant. Create a research record only for an identifiable source or activity; generate indexes when their project content exists.

**Checks:** separate observations from assumptions; distinguish product users from people represented in data. Keep detailed access rules pending if unknown. Maintain product purpose in vision and initiative objectives in the brief.

**Exit:** the problem, intended users, and desired improvement are understandable and supported by an attributed statement or source.

## W03 — Value, scope, and quality

**Working hats:** Human — Product Owner; AI — Product Manager.

**Inputs:** problem, actors, proposed value, and operating constraints.

**Questions:** What belongs in the initial product and what is excluded? Which capabilities support it? What would show success? Which quality conditions matter, and under what circumstances? Which imposed technical constraints or feasibility questions affect these boundaries?

**Outputs:** `specs/product/scope.md`, `specs/product/capabilities.md`, `specs/product/quality-requirements.md`, and `pm/opportunities.md`; update the brief's objectives and vision where needed.

**Checks:** keep scope independent of implementation; distinguish future possibilities from commitments. Give each known quality requirement an observable condition and planned check. Unknown thresholds remain pending. Catalog order does not establish priority.

**Exit:** candidate outcomes have boundaries; applicable quality concerns and consequential unknowns are recorded.

## W04 — Evidence, risks, and priorities

**Working hats:** Human — Product Owner / Sponsor; AI — Product Manager.

**Inputs:** candidate capabilities, objectives, available evidence, constraints, and uncertainty.

**Questions:** Which assumption could change the decision to build? What needs investigation? Which outcome should come first, and why? Which dependencies or costs affect that choice? Does a technical assumption need evidence or a scoped decision before selecting the increment?

**Outputs:** `pm/risks.md`, `pm/priorities.md`, `pm/roadmap.md`, and an `INC-NNN` record for the selected increment. Create `RES-NNN`, `VAL-NNN`, and `DEC-NNN` records only under their catalog conditions; update their indexes. When needed, use the technical branch's investigation and profile records without producing a complete delivery plan.

**Checks:** record the selected increment's outcome, bounds, rationale, dependencies, and evaluation approach. Keep a proposed experiment distinct from execution and a proposal distinct from an accepted choice.

**Exit:** a bounded increment is selected by an explicit instruction, decision, or delegated choice. Discovery actions address questions blocking its definition.

## W05 — PM-to-SDD review

**Working hats:** Human — Product Owner; AI — Product Manager / Quality Analyst.

**Inputs:** the selected increment and its product and PM sources.

**Questions:** Are its outcome and boundaries consistent with the user's intent? Which open question prevents specification? Resolve specific disagreements rather than requesting approval for each document.

**Outputs:** `pm/sdd-handoff.md` with reviewed source references and baseline, PM readiness, open questions, and downstream selection or pending next action; preserve the increment's review in its `INC-NNN` record; update state. Record concrete mappings and transfer progress only when downstream work is requested, using the [integration procedure](handoff.md#transfer-procedure).

**Checks:** review PM-SDD-01 through PM-SDD-07 from the handoff document, recording sources and unanswered criteria. Keep product authority independent of tool-native technical artifacts. Include existing technical evidence, constraints, and profile decisions. Record the impact of unresolved feasibility questions; architecture, stack, and receiving-tool selection are conditional rather than universal readiness requirements.

**Exit:** record `ready`, `needs-discovery`, or `cancelled` with its basis. With `needs-discovery`, return to the relevant unresolved step; with `cancelled`, retain the rationale and stop that increment. At a PM endpoint, report the result and next action. With `ready` and broader kit scope, continue at W06 without an extra routine approval. With external mode, transfer to its recorded receiving workflow.


## Continue through SDD and execution

With ready W05 and a broader kit endpoint, continue through the [SDD execution guide](sdd/workflow.md):

| Step | Responsibility | Prerequisite |
| --- | --- | --- |
| W06 | Domain, processes, and shared rules | Ready PM handoff and specification scope. |
| W07 | Feature behavior and acceptance criteria | Required business concepts and rules defined. |
| W08 | Applicable UI and interaction contracts | Related Feature behavior defined. |
| W09 | Acceptance and specification review | Included behavior and applicable interactions can be checked together. |
| W10 | Architecture and intended profile | Supported specification review; existing early decisions available. |
| W11 | Bounded delivery and operating plans | Relevant technical decisions recorded. |
| W12 | Implementation handoff | Applicable profile plans and dependencies defined. |
| I01 | Implement the bounded scope | Supported W12 review and implementation in recorded scope. |
| I02 | Verify behavior and profile conformance | Applicable implementation available for its checks. |
| I03 | Release to the requested target | Supported verification and applicable operating prerequisites. |
| I04 | Evaluate observed outcomes | Evaluation in scope and actual evidence available. |

Read the module's [roles](sdd/roles.md), [catalog](sdd/artifacts.md), and [content guide](sdd/authoring-guide.md) as the selected route reaches them. Reuse supported early decisions, definitions, and reviews; preserve existing profile records.

For another increment, revisit W04/W05 and affected specification steps. For another implementation profile of the same defined scope, reuse supported W00–W09 work and repeat W10–W12 and applicable I activities for that profile.

For an external workflow, apply the [handoff protocol](handoff.md) and record its own next action instead of imposing kit steps.

## Additional artifact types

Use the catalog for the current stage: [PM](artifacts.md) or [SDD and execution](sdd/artifacts.md). For a type or path outside those definitions, follow the applicable catalog extension rule. Record purpose, owner, trigger, canonical source, and authorization basis. Proceed when instructions or delegated scope support it; clarify absent authority.
