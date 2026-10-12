# AI project onboarding

Read this guide from the external adopted revision. The [workflow](workflow.md) owns phase minima and endpoints, [roles](roles.md) own contributions, [generation protocol](generation.md) owns source and destination handling, and [PM catalog](artifacts.md) owns schemas and project paths.

## Starting and resuming

A request to define an initiative starts onboarding. A request to change this kit is maintenance.

At the start of a session, read the source README, AGENTS, workflow, roles, generation protocol, and catalog. Inspect the destination's existing instructions, policies, state, and relevant definitions. Source policies are blueprints; retain authoritative project instructions.

At W00, resolve the destination and adopted source revision, establish persistence, and create project state. Record the actual location and full commit SHA when available, with specific recovery work for unknown provenance. Keep checkouts and method resources outside the project. All resources use that revision, including templates first needed later.

At W01, establish only the configuration needed for discovery. New projects use conventions for documentation languages; retain a separate policy when one already exists or needs independent maintenance. Create the remaining PM core progressively.

On resumption, reconcile state with actual definitions and recorded delegation. Retrieve the adopted revision and reuse supported answers, reviews, IDs, and W/I history. Follow [versioning](../VERSIONING.md) for source recovery or authorized upgrades. Use the project's authoritative consolidated or split definitions.

Missing access or persistence blocks dependent work. Continue independent work supported by available sources and identify unsaved drafts explicitly.

## Conversation rules

1. Use the user's language initially; record conversation and documentation languages independently at W01.
2. Ask one to three related questions per turn, for input that affects a current decision or phase minimum.
3. Request a concrete example when needed to understand observable behavior.
4. Explain concise alternatives and their consequences; challenge contradictions.
5. Attribute user knowledge, observations, intent, hypotheses, proposals, and AI inferences to their actual sources.
6. Respect explicit instructions and delegation. Clarify consequential ambiguity; silence does not accept a proposal.
7. Keep actual unknowns with their impact and next action in the responsible source. Resolve them when they affect the current exit condition.
8. Preserve decisions and progress when the user pauses or changes context; reopen only affected reviews.
9. Keep discovery proportional to uncertainty and the cost of a wrong decision.

## Human and AI working hats

Use the [role assignment](roles.md) for the current phase or subtask. At transitions, briefly explain the human's needed contribution and the AI's responsibility.

Conventions own participants and delegation; product actors belong to the shared foundation. Identify missing expertise only when a specific decision requires it. The same AI can author and review, but an independent review requires an actual separate reviewer.

During decision-relevant technical work, use [technical discovery](technical-discovery.md), its conditional roles, and existing profile records; return to the interrupted PM phase. W05 can continue into [SDD](sdd/roles.md) or an external workflow within recorded scope.

## Initial questions

After W00 establishes persistence, ask only unresolved configuration: working name, conversation and documentation language, required working rules, and decision ownership. Reuse choices supplied in instructions. A single default documentation language is sufficient unless actual area exceptions are needed.

Record endpoint and workflow mode. A foundation-only request covers PM; broader scope uses the kit unless an external workflow is selected. Leave future tooling and technology choices until they affect work.

## Each conversation turn

For PM, use this bounded cycle:

1. Read the active phase's minimum, relevant project sources, and delegation. Reuse method resources and templates already read in this session from the adopted revision. Read new resources when needed; reread affected material if it changed or the context is uncertain.
2. Identify the new information and the definition or decision it affects. Check direct contradictions with affected sources.
3. Update the responsible document with the supported addition. Register a new output and read its canonical schema before authoring. Change another source only when a concrete dependency or contradiction requires it.
4. Update changed state fields: actual artifact status, active phase or hats, blocker reference, or next action.
5. Ask the next unresolved decision-relevant question or advance when the phase minimum is supported.

Save substantive answers during the conversation, including supported information relevant to later phases. Reuse that information when its phase is reached.

## Review cadence

| Moment | Review |
| --- | --- |
| After an answer | Supported addition, direct contradictions, and changed references. |
| At W02–W04 closure | Phase minimum and consistency of affected sources; reconcile changed navigation and state. |
| At W05 | Full PM-SDD-01–07 review of the selected increment and baseline. |

Each PM review has one authoritative source, normally the INC. State and transfer documents link that source. Reopen reviews when changes to underlying definitions affect their validity.

Broader kit endpoints retain the SDD module's W09, W12, and execution review requirements.

## Content boundaries

Conventions own project rules and language choices. The initiative owns problem context, objectives, evidence, applicable risks and priority comparisons. The foundation owns shared product value, actors, scope, capabilities, quality, and necessary vocabulary. The INC owns selected scope, selection rationale, outcome evaluation, and W05 review. Profiles own technical choices and evidence.

Extract a section only when it needs independent maintenance; replace its original definition with a reference. Keep one owner for each fact, question, and review. State records progress and blocker links.

Apply the [document description rules](generation.md#document-descriptions) when creating or updating project definitions. Remove producer comments and generic prompts from generated outputs. Keep unresolved decisions specific and include applicable conditional sections. Quantities, rules, procedures, and execution claims require supporting sources; record missing definitions as pending. Implementation, release, and observed outcomes need their own evidence.
