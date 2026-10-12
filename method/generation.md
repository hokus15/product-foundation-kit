# Generate and evolve a project

Read the external kit at the adopted revision and generate only initiative-specific content through its recorded endpoint. Use the [workflow](workflow.md), [roles](roles.md), and [PM catalog](artifacts.md); broader endpoints add the [SDD catalog](sdd/artifacts.md).

## Source and project

| Location | Responsibility |
| --- | --- |
| Source URL or external kit root | Method guides, canonical schemas, and requested reference resources. |
| Project root | Actual instructions, state, definitions, and authorized implementation. |

A new PM foundation reaches this core progressively:

```text
my-product/
├── README.md
├── AGENTS.md
├── project-conventions.md
├── project-state.md
├── pm/
│   ├── initiative.md
│   └── INC-NNN-short-description.md
└── specs/product/
    └── foundation.md
```

Resolve separate, non-nested source and target locations before writing. Downloads and caches stay external. Use actual project definitions. Separate policies, investigations, decisions, transfer records, and indexes follow their catalog conditions.

## W00 bootstrap

1. Read the source README and AGENTS, then required method guides.
2. Identify the destination and inspect existing instructions, policies, definitions, identifiers, and progress.
3. Resolve the selected source once. Record the actual location and full commit SHA when available in project state. All later resources use that revision. Record unknown provenance with its limitation and recovery action; follow [versioning](../VERSIONING.md).
4. Establish persistence and create state from its canonical schema, initially with factual source/destination context and next action.
5. Read other schemas as their outputs become applicable. Reuse resources already read from the adopted revision within a session; reconcile changed or uncertain sources before using them.

Resolve missing access or persistence before dependent work. Continue independent supported analysis, identify unsaved drafts explicitly, and report files actually saved.

## Generate each output

1. Register its concrete destination, type, phase, canonical source, and current status before first authoring.
2. Read the cataloged schema. Preserve metadata keys, IDs, status meanings, and core section meanings. Include conditional sections only when their trigger applies; later-phase sections are added when that phase is reached.
3. Write supported facts, attributed knowledge or hypotheses, proposals, confirmed choices, and specific pending questions in the selected language. Remove producer instructions and unused prompts.
4. Recalculate links from cataloged project destinations and actual owning sources. An extracted or retained source can replace a consolidated source. Remove source-only navigation and links to absent outputs.
5. Check the new or affected content manually. Update changed state fields.

The [conversation guide](guide.md#each-conversation-turn) bounds per-answer work. Phase closure reconciles affected definitions and navigation; W05 performs the complete PM readiness review.

Root README and AGENTS use project schemas and retain authoritative existing instructions. README provides navigation for the initial PM core. Separate indexes follow their catalog triggers.

## Document descriptions

Describe current behavior, responsibilities, scope, constraints, and procedures directly in project READMEs, policies, specifications, and operating guides. When a definition changes, integrate the supported change and remove obsolete explanations, defensive narration, and comparisons with superseded versions.

Record rationale, alternatives, change history, and migration details in the responsible DEC, INC, ADR, changelog, migration, or review record. Descriptive documents reference these records when readers need their basis. Express exclusions, failures, and limitations as concrete rules tied to the applicable scope. Preserve recorded evidence and review history in their responsible sources.

## Save and resume

State retains provenance, endpoint, mode, increment, intended profile, active step, actual progress, blocker references, and next action. Register meaningful saved changes and review references. Definitions, full questions, and evidence remain in their responsible sources.

Keep each PM review per increment and baseline in one authoritative source, normally the INC. State and transfers link it. W09, W12, and execution evidence retain the SDD module's required increment/profile/revision contexts.

On resumption, retrieve the recorded revision and reconcile state with actual project sources. Use that revision for all method resources. Resolve missing source access before dependent work; independent work grounded in project sources can continue.

Authorized upgrades follow [VERSIONING.md](../VERSIONING.md#upgrade-a-project-deliberately). Record old and target provenance, preserved or changed sources, affected reviews, and actual partial progress in state. Change adopted fields only when migration is complete. An interrupted migration resumes before dependent ordinary work.

Authorized extraction or consolidation preserves facts, IDs, accepted decisions, history, and authority. Replace former definitions with links to their current owner and repair incoming references. Cleanup of existing files follows requested scope.

## Checkpoints and continuation

At W05, apply PM-SDD-01–07 from the [increment schema](../templates/pm/increment.md) to the selected scope and baseline. Retain its criterion evidence once, link the review from state, and reconcile root navigation. Confirm project ownership and actual local references.

With ready W05 and a broader kit endpoint, continue through [SDD and execution](sdd/workflow.md). Read the actual consolidated or split product sources and retain the module's schemas, W09 specification review, W12 profile readiness, and actual I evidence. Stop when the selected endpoint's result is supported.

External mode uses the [transfer procedure](handoff.md). A separate transfer document is conditional on a receiving workflow or participant needing a mapping or transfer record; it references the authoritative PM review. Reuse early technical evidence and profile decisions in either route. The kit's method, templates, and reference resources remain external.
