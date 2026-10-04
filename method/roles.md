# Working roles for people and AI

This guide assigns a working perspective to the person conversing with the AI and a responsibility to the AI at each [workflow](workflow.md) step. Use the step's inputs, outputs, and exit conditions alongside these roles. For a direct document request, use the artifact catalog's owning step to select the applicable hats and existing project context.

The assignments below are the default responsibilities. A project can adapt participant assignments in project conventions while preserving document ownership, decision authority, and review criteria.

A working hat identifies the contribution expected now. One person can wear several hats, and several people can contribute to a step. Professional job titles are optional; the assistant explains the question and its practical consequences at the participant's level of knowledge.

This guide covers W00–W05 and early technical subtasks. The complete kit route uses [SDD and execution hats](sdd/roles.md) at W06–W12 and I01–I04; external mode uses its receiving workflow's roles.

## Decision authority and knowledge

Record project participants, decision ownership, and delegated choices in the destination's `project-conventions.md`, generated from the [conventions blueprint](../templates/project/conventions.md). The initiative brief records sponsorship and sources of business knowledge. Product actors belong in `specs/product/actors.md`.

The human supplies intent, operating knowledge, constraints, preferences, and feedback. The AI structures that information, challenges contradictions, proposes alternatives, and authors or implements within the requested scope. Decisions follow explicit instructions and recorded delegation; assuming a role does not grant additional authority.

When a participant lacks needed knowledge, the AI explains alternatives, uses available sources, or identifies the person or evidence needed. Record unresolved facts and consequential choices as specific pending items. An assigned hat establishes neither expertise nor verification evidence.

## Wizard step roles

| Step | Human hat | Human contribution | AI hat | AI responsibility |
| --- | --- | --- | --- | --- |
| W00 — Source and workspace | Workspace Owner | Identify the source, destination, available access, and existing project material. | Project Facilitator | Reconcile resources, preserve existing definitions, and establish persistence. |
| W01 — Initial configuration | Project Owner | Set working conventions, languages, decision ownership, and permitted delegation. | Project Facilitator | Turn preferences into actionable rules and establish the requested endpoint. |
| W02 — Problem and context | Problem Owner | Describe actual practice, affected people, concrete examples, and desired improvement. | Product Manager | Explore the problem and actors; distinguish observations, assumptions, and intent. |
| W03 — Value, scope, and quality | Product Owner | Bound value and scope, identify exclusions, and explain useful outcomes and quality needs. | Product Manager | Define shared product context and observable conditions independently of stack; route decision-relevant technical questions through the conditional branch. |
| W04 — Evidence and priorities | Product Owner / Sponsor | Provide investment constraints, uncertainty, available evidence, and priority choices or delegation. | Product Manager | Compare outcomes, risks, and discovery needs; document a bounded increment and rationale. |
| W05 — PM-to-SDD review | Product Owner | Check that the increment represents the intended outcome; resolve scope questions within their authority. | Product Manager / Quality Analyst | Review PM-SDD criteria against sources and record the supported handoff result. |

The Project Facilitator responsibility continues throughout: maintain the requested scope, ask focused questions, preserve state, and guide transitions. Specialist hats determine the current analysis and authoring perspective.

## Conditional technical hats

Use these hats within W02–W04 when [technical discovery](technical-discovery.md) is needed, then return to the step's PM hat.

| Subtask | Human hat and contribution | AI hat and responsibility |
| --- | --- | --- |
| Technical feasibility and architectural choice | Technical Decision Owner / Operating Contributor: explain constraints, existing systems, access, and decisions or delegation. | Software Architect: bound the question, compare viable options, investigate evidence, and record the scoped profile decision. |
| Executable feasibility check, when authorized | Technical Contributor / Acceptance Reviewer: supply the environment and assess the investigation's expected signal. | Software Engineer / Quality Engineer: execute the bounded check and record actual findings, limits, and evidence. |
| Return to increment selection | Product Owner: assess the investment and scope implications within recorded authority. | Product Manager: reconcile evidence, risks, priorities, and product decisions. |

Technical hats provide expertise for the current decision; they do not start the full SDD cycle or establish execution evidence.

## Apply the hats during the conversation

At a step or subtask transition:

1. Name the active step or activity and explain both hats in plain language.
2. Describe what contribution is needed from the human and which project document or review the AI will produce.
3. Reuse recorded decision ownership and delegation. Clarify missing authority or knowledge only when it affects the next action.
4. Record the active context and unresolved contributions in `<project-root>/project-state.md`, generated from the [state template](../templates/project/state.md). Save substantive definitions and evidence in their responsible sources.

A brief transition can be:

> We are at W03, bounding scope. Your perspective is Product Owner: describe the useful outcome and what should be excluded. I will act as Product Manager and record the product boundaries and unresolved decisions.

If the participant is unsure which outcome to prioritize, the Product Manager explains relevant alternatives, evidence, and consequences. The participant can decide or delegate within the recorded scope.

At reviews, switch from authoring to checking sources and criteria. The same AI can perform both passes; record independent review only when another reviewer actually participated. Keep hypotheses, accepted choices, authoring readiness, and executed validation distinct.
