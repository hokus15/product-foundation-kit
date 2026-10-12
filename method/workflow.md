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
| `pm-foundation` | W05 | Selected increment with an authoritative PM review and next action. |
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

The branch creates investigations or profile decisions needed for the current PM choice, then returns to the interrupted step.

## Completion and conversation rules

Apply the hats in the role guide and explain their contributions at transitions. Ask for missing knowledge or decision authority only when it affects the next action; apply recorded delegation and reuse answers.

For PM, follow the [bounded per-answer cycle](guide.md#each-conversation-turn): persist the new contribution, check direct contradictions, and update changed state fields. Reuse resources already read from the adopted revision within a session.

Before completing a step:

- Check its minimum content, using consolidated or existing split sources. Account for actual outputs in state; record conditional omissions when they affect readiness, a request, or downstream work.
- Replace resolved prompts with factual content; retain specific open questions with impact, owner where known, and next action.
- Reference sources or decisions supporting consequential definitions and identify hypotheses and proposals.
- Review applicable metadata, IDs, core sections, changed links, and consistency of affected sources. Reconcile navigation at phase closure; W05 reviews the whole selected increment.
- Record the exit result and actual saved artifacts. File presence alone establishes no readiness or execution evidence.

Include applicable conditional sections. Phase completion requires its minimum content. A question blocks the phase only when its exit condition depends on the answer. Keep the step active or blocked while that condition is unmet. Automated documentation checks run only when explicitly requested.

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

**Outputs:** generate or update `project-conventions.md`, README, and AGENTS from their canonical schemas. Conventions own one default documentation language and actual exceptions; retain a separate `documentation-policy.md` when existing or needed for independent maintenance. Record endpoint, mode, bounds, and changed working context in state. Root documents reference authoritative project sources.

**Checks:** distinguish conversation language from document languages, preferences from constraints, and routine drafting from consequential choices. Resolve language, participant, and tooling choices when they affect current work.

**Exit:** a provisional identity, destination, languages, working rules, and authority sufficient for discovery are known. Relevant unresolved configuration has a next action; future configuration does not block discovery.

## W02 — Problem, people, and context

**Working hats:** Human — Problem Owner; AI — Product Manager.

**Inputs:** the user's idea, known practice, and available observations or sources.

**Questions:** What need or problem justifies the product, who is affected, and what improvement would be useful? Ask about current practice only when it affects understanding the problem, scope, or improvement. Request an example or distinguish users from recipients when needed.

**Outputs:** start `pm/initiative.md` with the problem and its basis, and `specs/product/foundation.md` with value, actors, and usage context. Existing vision and actor definitions can satisfy this content directly. Add vocabulary or research only when needed. Save supported later-phase facts in their responsible source and reuse them at W03–W04.

**Checks:** attribute user knowledge and distinguish observations from assumptions. Distinguish users from people represented in data. Resolve access only when it affects current boundaries. Initiative owns problem evidence; the foundation references it and owns shared product value and actors.

**Exit:** the problem, intended users, and desired improvement are understandable and supported by an attributed statement or source.

## W03 — Value, scope, and quality

**Working hats:** Human — Product Owner; AI — Product Manager.

**Inputs:** problem, actors, proposed value, and operating constraints.

**Questions:** What belongs in the initial product and what is excluded? Which capabilities support it? What would show success? Which quality conditions matter, and under what circumstances? Which imposed technical constraints or feasibility questions affect these boundaries?

**Outputs:** expand the foundation with scope, exclusions, capabilities, and applicable quality conditions; define initiative objectives and success signals. Use existing split definitions when present. Compare opportunities only when the decision requires it; separate documents follow catalog triggers.

**Checks:** keep scope independent of implementation and future possibilities distinct from commitments. Known quality requirements need observable conditions and planned checks; unknown thresholds remain pending. Use a qualitative or quantitative success signal supported by the available information.

**Exit:** included capabilities and exclusions are understandable, objectives have observable success signals, and applicable quality conditions and consequential unknowns are recorded. If no additional quality concerns are identified, record that assessment briefly.

## W04 — Evidence, risks, and priorities

**Working hats:** Human — Product Owner / Sponsor; AI — Product Manager.

**Inputs:** candidate capabilities, objectives, available evidence, constraints, and uncertainty.

**Questions:** Which assumption could change the decision to build? What needs investigation? Which outcome should come first, and why? Which dependencies or costs affect that choice? Does a technical assumption need evidence or a scoped decision before selecting the increment?

**Outputs:** create the selected `INC-NNN` with outcome, boundaries, selection rationale, and evaluation approach. Record applicable risk and candidate comparisons in the initiative; reference them from the increment. A separate risk register, priority list, or roadmap is conditional on independent maintenance needs. RES, VAL, DEC, and technical discovery retain their catalog triggers; indexes are conditional on useful navigation.

**Checks:** identify actual dependencies and decision-relevant uncertainty. Use qualitative rationale and outcome assessment when sufficient; add quantitative estimates when supported and needed for the decision. Keep experiments separate from execution and proposals from selection.

**Exit:** a bounded increment is selected by an explicit instruction, decision, or delegated choice, with its rationale, observation method, and review condition or timing recorded. Questions blocking selection or definition are resolved; remaining uncertainties have their impact and next action in the responsible source.

## W05 — PM-to-SDD review

**Working hats:** Human — Product Owner; AI — Product Manager / Quality Analyst.

**Inputs:** the selected increment and its product and PM sources.

**Questions:** Are its outcome and boundaries consistent with the user's intent? Which open question prevents specification? Resolve specific disagreements within recorded authority.

**Outputs:** record the authoritative review in the selected INC, with baseline, criterion evidence, result, and next action. Preserve earlier baselines and reference the authoritative review source. State links this review; reconcile root navigation. Generate a separate `pm/sdd-handoff.md` only when a receiving workflow or participant needs transfer records or mappings, using the [integration procedure](handoff.md#transfer-procedure).

**Checks:** apply PM-SDD-01–07 from the [increment template](../templates/pm/increment.md) to the full selected scope. Record supporting sources and unsupported criteria once. Keep product authority independent of tool-native artifacts and include relevant early technical context. Record the consequence and resolution of feasibility uncertainty relevant to the review.

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
