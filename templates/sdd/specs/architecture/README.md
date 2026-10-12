# Architecture

Architecture profiles define how different implementations satisfy one shared product definition. Product behavior, reusable UI, interaction contracts, and quality requirements remain decoupled from architectural approaches and programming stacks.

- [Principles](principles.md): shared constraints chosen for this initiative.
- [Current selection](current.md): authoritative profile and implementation selection.
- [Profiles](profiles/README.md): different architectural approaches and programming stacks, each mapped to the shared specifications.
- [Templates](templates/README.md): decisions, capabilities, delivery plans and validation evidence.

## One definition, multiple implementations

Each profile references the shared specifications and acceptance criteria and owns its technical decisions, capabilities, Feature integration plans, operating guides, and conformance evidence. Profiles can cover different subsets or revisions; their coverage records identify what each implementation satisfies.

Adding or changing a profile preserves the product definition. Product requirements evolve through product decisions; architecture or stack changes update profile documentation and implementation. Resolve the task's explicitly named profile or use the active selection.

## Decision boundaries

Technology-specific decisions belong to the relevant profile. An ADR records one significant decision; an enabler defines a bounded technical capability and its verification. Feature-specific integration belongs to the profile's implementation plans.

Keep setup, development, validation and deployment instructions in the relevant profile, using language choices in [project conventions](../../../project/conventions.md) or a separate authoritative documentation policy when present. Maintain coverage and evidence separately for each implementation.
