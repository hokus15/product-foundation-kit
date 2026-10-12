# Collaboration

[Work items](templates/work-item.md) coordinate work; specifications retain the behavior definition. Use the [opportunity template](templates/opportunity.md) for product questions and the [change review template](templates/change-review.md) to review proposed changes.

These Markdown templates can be used as local documents, in a task tracker, or in a repository review system. Reference existing documents and identifiers from coordination records. Record the outcome and verifiable status in the responsible source when a discussion produces a decision.

For local records, use these destinations only when coordination work is needed:

| Record | Template | Destination |
| --- | --- | --- |
| Opportunity | [Opportunity](templates/opportunity.md) | `records/opportunities/short-description.md` |
| Work item | [Work item](templates/work-item.md) | `records/work-items/short-description.md` |
| Change review | [Change review](templates/change-review.md) | `records/change-reviews/short-description.md` |

Register each concrete local path through the [artifact catalog](../../method/sdd/artifacts.md). Create the directory when the first record is needed. External tracker entries follow the selected tool's conventions.

Adapt collaboration templates to language choices in [project conventions](../../templates/project/conventions.md) or a separate authoritative documentation policy when present.

## Optional platform integration

Each initiative can choose repository hosting, task tracking, review, and automation tools independently. When a platform is selected, adapt the relevant templates to its format and add its configuration in the location that platform requires.

Keep shared executable checks in `dev/ci/`. Define any automated orchestration, dependencies, permissions, and commands in the technical profile. Local validation can be used without a hosted CI service.
