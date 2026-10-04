# Generate and evolve a project

The assistant reads the external kit and generates initiative-specific documentation and authorized implementation in a separate destination, through the selected endpoint and workflow mode. Use the [workflow](workflow.md), [roles](roles.md), and [artifact catalog](artifacts.md).

## Source and project

| Location | Responsibility |
| --- | --- |
| Source URL or `<kit-root>` | Read method guides, canonical templates, and requested reference resources. |
| `<project-root>` | Save actual project rules, progress, PM records, and product definitions. |

```text
workspace/
├── method-sources/
│   └── product-foundation-kit/   # optional external retrieval
└── my-product/                  # generated initiative
    ├── README.md
    ├── AGENTS.md
    ├── project-conventions.md
    ├── documentation-policy.md
    ├── project-state.md
    ├── pm/                      # actual records from the conversation
    └── specs/
        └── product/             # shared product foundation
```

Resolve both roots before writing and keep neither nested inside the other. Keep downloads and caches outside the destination. Generate directories and files as their registered content becomes applicable.

## W00 bootstrap

1. Read the source README and AGENTS, then the method guides.
2. Identify the destination and inspect existing content, instructions, policies, identifiers, and progress.
3. Resolve the selected source once and record the actual source URL or external location and identifiable revision; use the full commit SHA for a Git source when available. Read all method resources from that revision. Leave unknown revisions unknown, with the limitation and recovery action recorded. Follow the [versioning policy](../VERSIONING.md) for source recovery and upgrades.
4. Establish writable persistence and generate target `project-state.md` from [its template](../templates/project/state.md), initially recording factual context and next action.
5. Retrieve other canonical templates as their steps require them.

If access or writing is unavailable, identify the missing capability and provide clearly marked unsaved drafts or request an accessible source. Missing resources block dependent authoring; continue independent supported work. Report only files actually saved.

## Generate each output

1. Register its concrete destination, type, owning step, applicability, and supporting source in project state.
2. Read the cataloged template. Preserve metadata keys, IDs, main sections, and defined status meanings.
3. Write facts, confirmed choices, attributed hypotheses, proposals, or specific pending questions in the project's chosen language. Remove producer comments, generic prompts, and the kit's identity.
4. Recalculate relative references using the catalog's **project destinations**. A link between two source templates becomes a link between their generated project documents when both exist. Remove navigation to method guides, template catalogs, and optional reference resources.
5. Review content and references manually. Save actual artifact status, active hats, consequential sources, and next action.

Root README and agent instructions use [project templates](../templates/README.md). Retain existing authoritative destination instructions. Index templates create navigation only when the corresponding project content exists.

## Save and resume

Project state preserves the endpoint, workflow mode, active W or I step, selected increment and intended profile, source provenance, artifacts, reviews, evidence, questions, and next action. Keep shared reviews per increment and baseline and technical handoffs and verification per profile. Business decisions and evidence remain in responsible sources.

Keep temporary checkout paths in session context. On resumption, retrieve the recorded kit revision and reconcile state against actual project content before proceeding. Use the same revision for all guides, catalogs, templates, and reference resources, even when first retrieved in a later phase. Do not substitute the latest release. Unknown or inaccessible revisions need their specific resolution before dependent work; independent work supported by project sources can continue.

Kit upgrades follow the [versioning policy](../VERSIONING.md#upgrade-a-project-deliberately). Preserve existing project instructions and evidence, record old and new provenance and affected reviews in `Scope revisions`, and update the adopted source fields when migration is complete. For an interrupted migration, reconcile its saved partial changes and continue it before ordinary wizard work that depends on affected artifacts. Completed adoption does not satisfy unresolved workflow reviews.

For a legacy destination with copied kit resources, preserve project facts and customized rules, repair navigation, and classify generic resources. Removing existing files follows explicitly requested cleanup scope.

## Checkpoints and continuation

At W05, apply PM-SDD-01–07 from the handoff template, retain the increment's review, and reconcile root navigation and state. Confirm that every target file belongs to the initiative and all local references resolve to existing project sources.

With ready W05 and a broader kit endpoint, continue through [SDD and execution](sdd/workflow.md), using its catalog and schemas as outputs become applicable. Record W09 specification review, W12 profile readiness, and actual I activity evidence in state and responsible project records. Stop at the selected endpoint when its result is supported.

Use the [generic transfer procedure](handoff.md) for external mode. Reuse supported early technical investigations and profile decisions in either route. Source `method/`, `templates/`, and `reference/` stay external throughout.
