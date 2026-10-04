# Project agent instructions

<!-- Canonical template for <project-root>/AGENTS.md.
Write in the project's selected agent-instruction language.
Preserve existing authoritative instructions. Replace prompts with agreed rules,
remove this comment and source-only links, and include only applicable areas.
Use project-state.md for the actual method source and revision.
Do not copy the method repository's AGENTS.md. -->

## Project conventions

<Reference the existing project-conventions.md and documentation-policy.md.
State agreed communication, delegated decisions, authoring, and validation rules.
Describe the specific project's purpose and boundaries where useful.>

## Project definitions and source ownership

<Identify existing product, UI, contract, and PM sources and their responsibilities.
Keep product behavior independent of architectural patterns and programming stacks.
Reference only existing project files.>

## PM-to-SDD handoff

<Read the selected endpoint and workflow mode from project-state.md. Run applicable
W00-W05 work and reference pm/sdd-handoff.md once authored. With kit mode and
broader scope, continue through its W06-W12 and applicable I01-I04 guides and
canonical schemas. External mode uses the receiving workflow's sequence and templates. Preserve
source ownership, stable IDs, the reviewed baseline, and actual downstream paths.
Keep technical choices associated with their intended architecture profile.>

## Technical profiles

<Use an explicitly requested profile or the active selection in
specs/architecture/current.md when that file exists.
Keep profile decisions, plans, implementation, and conformance evidence separate.
Preserve shared specifications when adding or changing a technical profile.>

## Authoring and project continuation

<Read project-state.md when resuming. Retrieve required workflow, role, catalog,
and canonical template resources from its recorded method source and revision;
use that same revision for all resources and keep any checkout outside the project.
Do not silently switch to a newer release. Resolve unknown or inaccessible source
revisions before dependent work. Kit upgrades require explicit instructions or
recorded upgrade delegation; preserve project content and record the migration
and affected reviews in project-state.md. Use the applicable human and AI hats.
Save project definitions in their responsible sources, preserve existing IDs,
and keep specific unknowns and the next action current.>

## Implementation and validation

<Implement only the requested scope using its shared specifications and intended
profile plans. Identify source and generated paths, known commands, and required
checks when defined. Keep unexecuted criteria unchecked and record actual evidence.
State the project's agreed automated documentation-check policy.>
