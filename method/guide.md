# AI project onboarding

Read this conversation guide from the method source. Use the [generation protocol](generation.md) to keep source resources external, the [workflow](workflow.md) for execution order, [working roles](roles.md) for contributions, and the [artifact catalog](artifacts.md) for project destinations.

## Starting and resuming

Start onboarding when the user asks to define an initiative from the supplied method URL. Requests to change Product Foundation Kit itself are method maintenance.

Read the source README, source agent instructions, generation protocol, workflow, roles, and catalog. Then inspect the destination's existing project instructions, conventions, documentation policy, progress, and definitions. Source policies are blueprints; they do not establish choices for the initiative.

At W00, identify the destination, resolve the selected source revision, and establish persistence capability. Generate project state at `<project-root>/project-state.md` from the [state template](../templates/project/state.md). Record the actual source and full commit SHA when available; keep unknown provenance explicit. Read further source blueprints and templates from that same revision as their steps need them. Follow the [versioning policy](../VERSIONING.md) for recovery and upgrades.

At W01, establish missing conventions and generate the project's own README, rules, and agent instructions. Create later files when their content becomes applicable. Keep source guides, canonical templates, downloads, and caches outside the target.

If source access or writing is unavailable, state the missing capability and request an accessible external source or provide identified unsaved drafts. Report only files actually saved.

On resumption, read the target's `project-state.md` and retrieve the recorded method resources and revision. Reconcile current documents and instructions with saved progress. Map earlier phase names to W01–W05 when needed, preserving answers, IDs, and supported reviews. Preserve W06–W12 and I01–I04 history for kit mode; external workflows retain their actual phase records.

Use the adopted revision for every method resource. A newer release does not change it. Resolve unknown or inaccessible revisions before dependent work; keep independent work grounded in available project sources. An upgrade follows explicit instructions or recorded upgrade delegation and records its impact in project state.

## Conversation rules

1. Use the user's language initially and record the conversation language at W01. Apply document language choices independently.
2. Ask one to three related questions per turn. Use the workflow questions as topic prompts and reuse existing answers.
3. Request concrete examples when an abstract explanation is insufficient.
4. Offer concise alternatives, explain material trade-offs, and challenge contradictions.
5. Accept provisional names and uncertainty. Record specific unknowns, impact, and next action.
6. Distinguish intent, observations, hypotheses, proposals, and assistant inferences. User statements do not establish research findings or implementation evidence.
7. Apply explicit instructions and delegated scope. Clarify consequential ambiguity; silence does not accept a proposal.
8. Save routine authoring within the requested scope. Register output paths and follow the extension rule before adding a new type.
9. Keep question depth proportional to uncertainty. A source blueprint does not make every section or output applicable.
10. Preserve progress when the user pauses; changed definitions reopen affected reviews.

## Human and AI working hats

Use the [role assignment](roles.md#wizard-step-roles) for the current step and subtask. At transitions, explain the person's perspective and needed contribution and name the AI's active role.

One person may cover several responsibilities, request explanation, or delegate a bounded choice. Record actual participants and authority in the project's conventions. Keep missing domain input with its responsible source and next action in project state.

For example, W02 invites concrete problem context from a Problem Owner while the AI acts as Product Manager. W05 reviews the selected increment with a Product Owner and Product Manager / Quality Analyst. Later SDD roles apply only within the selected downstream scope.

For decision-relevant technical questions during PM, use the [technical discovery branch](technical-discovery.md) and its conditional hats, then return to the PM step.

At W05, use the [handoff rules](handoff.md). For a broader kit endpoint, continue with [SDD roles](sdd/roles.md) and its execution guide; external mode uses the receiving workflow's roles.

## Initial questions

After W00 identifies where answers can be persisted, a first batch can be:

> What name should we use for the project, even provisionally?
>
> Which language should we use in our conversation?
>
> Should documentation use one language or different languages by area?

Ask only for unresolved configuration. Follow up on working rules and authority before product discovery. Record the endpoint and workflow mode. A foundation-only request covers PM; broader scope follows the kit route unless an external workflow is selected. Technology, hosting, and SDD tool selection remain pending until needed.

## Each conversation turn

Read the active step's inputs, hats, existing project artifacts, and recorded delegation. Select the smallest unresolved question that advances the step.

After an answer, read the canonical source structure and generate or update its responsible project document. Remove method instructions and source-only links; maintain navigation only to existing project outputs.

Update project state with actual saved files, consequential sources, active hats, artifact statuses, reviews, open questions, and next action. Advance when the step's exit condition is supported.

## Content boundaries

Keep project rules in root policies, product definitions in project specifications, evidence and priorities in PM, and technical choices in profiles. Progress references those sources.

Replace prompts with facts or specific pending decisions. Do not invent thresholds, permissions, formulas, research, selected technologies, commands, or verification evidence to complete a structure.

Clearly synthetic examples can introduce sample data; expected outcomes derive from established behavior. Authoring readiness, implementation, tests, release, and product outcomes require their own supporting evidence.
