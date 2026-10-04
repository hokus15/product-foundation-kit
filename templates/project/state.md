---
status: not-started
current_phase: W00
target_stage: null
workflow_mode: null
selected_increment: null
target_profile: null
method_source: null
method_revision: null
sdd_workflow: null
updated_on: null
---

# Project state

<!-- Canonical source template; generate at <project-root>/project-state.md.
Keep the template external. Populate factual context, remove producer comments,
and omit unselected stage rows and empty optional sections. W00 can start with
metadata, source/destination context, and next action; expand as work progresses.
Never invent a revision, review, saved change, or executed check. -->

## Requested scope and context

- Requested endpoint and bounds: pending.
- Workflow mode and receiving workflow: pending.
- Target project and persistence method: pending.
- Adopted method source and revision evidence or recovery action: pending.
- Current increment record: none selected.
- Intended profile and applicable implementation selections: not selected.
- Handoff or transition status: not started.

<!-- target_stage: pm-foundation, product-specifications, implementation-plan,
implementation, release, or outcome-review. workflow_mode: kit or external.
Use kit unless an external workflow is selected. sdd_workflow records the actual
kit or external workflow identity; it can stay null for pending continuation.
target_profile is the task's intended stable profile, not inferred from folders.
method_source is the actual URL/location, including the selected release tag when
applicable; method_revision is the full resolved Git commit SHA when available,
another verified revision for a non-Git source, or null when unknown. Record
revision evidence and any recovery action above. All method resources use that
revision; never infer it from an archive filename or silently adopt the latest.
Keep temporary checkout paths in session context.
current_phase is W00-W12 or I01-I04 for kit mode; external mode records its actual
phase label after transfer. Preserve all existing PM and subsequent history. -->

## Current working context

- Active step or activity: not started.
- Human working hat and contribution needed: pending.
- AI working hat and responsibility: pending.
- Participant or source needed for unresolved input: pending.
- Decision ownership and delegation: pending.

## Step progress

| Step | Increment and profile context when applicable | Status | Exit result and project sources |
| --- | --- | --- | --- |
| W00 | Project | `pending` | Pending |
| W01 | Project | `pending` | Pending |
| W02 | Shared foundation | `pending` | Pending |
| W03 | Shared foundation | `pending` | Pending |
| W04 | Increment selection | `pending` | Pending |
| W05 | Selected increment | `pending` | Pending |

<!-- Include applicable rows below as the kit endpoint reaches them. Omit unused
rows from generated PM-only state. External mode uses native rows and gates.
Repeat increment/profile rows as contexts change and preserve earlier results. -->

| Step | Increment and profile context when applicable | Status | Exit result and project sources |
| --- | --- | --- | --- |
| W06 | Selected increment | `pending` | Pending |
| W07 | Selected increment | `pending` | Pending |
| W08 | Selected increment | `pending` | Pending |
| W09 | Selected increment and shared baseline | `pending` | Pending |
| W10 | Selected increment and intended profile | `pending` | Pending |
| W11 | Selected increment and intended profile | `pending` | Pending |
| W12 | Selected increment, profile, and baseline | `pending` | Pending |
| I01 | Requested scope and profile | `pending` | Pending |
| I02 | Requested scope, profile, and revisions | `pending` | Pending |
| I03 | Requested release target and profile | `pending` | Pending |
| I04 | Increment and measured context | `pending` | Pending |

<!-- Overall statuses: not-started, in-progress, paused, blocked, ready-for-sdd,
ready-for-architecture, ready-for-implementation, implemented, verified, released,
outcome-reviewed. Use milestones only with supporting evidence; a milestone does
not imply the broader endpoint is complete. Paused follows a user request.
Step statuses: pending, active, blocked, complete, not-applicable, deferred.
Completed I01 means bounded changes exist; verified requires applicable I02
evidence, released actual I03 delivery, and outcome-reviewed actual I04 findings. -->

## Artifact register

| Concrete project path or no-file decision | Catalog type | Owning step | Applicability and reason | Status | Supporting source or decision | Review or next action |
| --- | --- | --- | --- | --- | --- | --- |

<!-- Register outputs before authoring. Schemas and guides stay external.
Use catalog tracking statuses independently of document metadata and execution. -->

## Review register

| Review | Increment or scope, profile when applicable, and baseline | Result | Criteria and project sources | Remaining blockers |
| --- | --- | --- | --- | --- |
| PM-to-SDD, W05 | Not selected | `pending` | PM-SDD-01–07; not reviewed | Pending |

<!-- Include only applicable kit review rows below. External mode records its
actual gates. Preserve prior reviews per increment and reviewed baseline; keep
technical readiness and execution evidence per profile and revision. -->

| Review | Increment or scope, profile when applicable, and baseline | Result | Criteria and project sources | Remaining blockers |
| --- | --- | --- | --- | --- |
| Specification readiness, W09 | Not selected | `pending` | SDD-READY-01–06; not reviewed | Pending |
| Implementation handoff, W12 | Not selected | `pending` | BUILD-READY-01–05; not reviewed | Pending |
| Verification, I02 | Not selected | `pending` | Applicable source criteria and checks; not executed | Pending |
| Release, I03 | Not selected | `pending` | Profile procedure and operating evidence; not executed | Pending |
| Outcome review, I04 | Not selected | `pending` | Increment evaluation plan and actual findings; not reviewed | Pending |

## Answered topics

| Topic | Project source | Remaining clarification |
| --- | --- | --- |

## Open questions and proposals

| Question or proposal | Impact | Blocking step or decision | Project source | Next action |
| --- | --- | --- | --- | --- |

## Extension register

| Proposed type and concrete path or pattern | Purpose and owning area | Trigger | Canonical source or project-owned template | Authorization basis | Status and next action |
| --- | --- | --- | --- | --- | --- |

## Scope revisions

<!-- For an authorized kit upgrade, record old/new source locations and revisions,
authority, reconciled artifacts, affected reviews, and next action here. Preserve
earlier uncertainty; update adopted source fields only when migration is complete.
For interrupted migrations, retain the target revision, actual partial changes,
remaining inputs, and next action in the existing state sections so resumption
continues the migration before dependent wizard work. Adoption alone establishes
no readiness; keep affected unresolved reviews in the review register. -->

| Changed project source, endpoint, or mode | Affected artifacts and steps | Reviews reopened | Next action |
| --- | --- | --- | --- |

## Latest saved updates

Pending.

<!-- List actual saved changes; identify unsaved drafts and unexecuted checks. -->

## Next conversation step

- Next step: W00.
- Next question or action: establish unresolved source and target context.
- Reason this is next: determine where answers can be persisted.
