# AGENTS.md

## Scope and writing

- These instructions govern Product Foundation Kit and its use as an external source. Preserve existing authoritative instructions in a generated destination.
- Keep all kit documentation and templates in English. Each project chooses conversation and documentation languages at W01.
- Write directly about behavior, decisions, and work. Preserve identifiers and actual evidence; keep specific uncertainty in its responsible source.
- Keep the kit independent of hosts, AI providers, SDD tools, architectures, and programming stacks.

## Repository responsibilities

- `method/workflow.md` owns the complete route, selectable endpoints, and workflow modes. W00–W05 establish the product foundation.
- `method/sdd/` owns W06–W12 specification and planning guides and I01–I04 implementation and follow-up guides, with their roles, catalog, and content rules.
- `method/technical-discovery.md` supports conditional feasibility work and early profile decisions during PM.
- `templates/` contains canonical authoring schemas. Catalogs define project destinations separately from source paths.
- `reference/` contains supplementary coordination resources.
- Root documents describe use and maintenance of the kit.
- `VERSIONING.md` owns release compatibility, adopted source revisions, and project upgrades; `CHANGELOG.md` records changes for release consumers.

Keep workflow, roles, catalogs, navigation, start prompts, state, and templates consistent during maintenance. Preserve canonical metadata and main sections; update incoming links when moving a resource.

## Execute the requested route

1. Read the source README, conversation guide, complete workflow, roles, generation protocol, and PM catalog.
2. Inspect existing destination instructions, conventions, policy, state, definitions, and profile records. Reuse supported answers and work.
   Resolve the adopted source revision at W00 and record the full commit SHA when available. Read all method resources from that revision. On resumption, preserve the recorded selection; resolve missing source access before dependent work and follow `VERSIONING.md` for authorized upgrades.
3. At W01, record the endpoint and `workflow_mode`. Use `kit` unless an external workflow is selected. Clarify an ambiguous request for further work; a foundation-only request covers PM.
4. Run the applicable W00–W05 work. Keep source checkouts and all method resources outside the project.
5. With ready W05 and a broader kit endpoint, read `method/sdd/workflow.md`, `roles.md`, `artifacts.md`, and `authoring-guide.md`; continue through W06–W12 up to the endpoint. Reuse early technical records and supported reviews.
6. With an implementation endpoint and supported W12 readiness, follow I01–I02 through bounded code and actual verification. Follow I03 or I04 when included in the project's requested scope.
7. For an external mode, use `method/handoff.md` and the receiving workflow's own phases and native templates.
8. Register each concrete output, use its canonical source, save substantive definitions in their responsible documents, and update project state after meaningful work.

Recorded scope and delegation authorize subsequent routine work without repeated permission at each phase. Missing inputs or unsupported prerequisite reviews require their specific resolution. Adding a method capability does not authorize implementation or release in an unrelated initiative.

Ask one to three related questions per turn. Explain human and AI hats at transitions, match input to the participant's knowledge, and preserve decision ownership. Silence does not accept a proposal.

## Product ownership and profiles

Shared product documents own behavior, scope, quality, and acceptance. Reusable UI remains framework-independent; interaction contracts remain transport-independent. PM records own evidence, hypotheses, objectives, risks, priorities, and investment decisions.

Profiles own architecture, programming stack, ADRs, technical capabilities, delivery plans, operating guides, and conformance evidence. Multiple profiles reuse the same shared product definition. Keep technical limitations in their profile until a supported product decision changes behavior.

Resolve an explicitly requested profile first; otherwise read the active selection from the project's `specs/architecture/current.md`. A new evaluation profile does not activate itself. Reuse supported PM and specification reviews for another profile; record its own technical readiness and execution evidence.

Use canonical profile and ADR schemas for early technical decisions when needed. New ADRs start as `proposed` unless acceptance is supported. Preserve accepted decisions when clarifying them; significant changes follow supersession.

## Authoring, progress, and validation

Generate project root documents from `templates/project/`. Keep kit guides and source template directories external. Recalculate generated links using cataloged destinations and existing project outputs.

Preserve canonical metadata keys, main sections, IDs, filenames, and status tokens. Assign the next unused number. Features and UI pages start as `draft`, ADRs as `proposed`, and enablers as `draft` unless instructions or evidence establish another status.

Use project state for the selected endpoint, mode, increment, intended profile, active W or I step, hats, artifacts, reviews, questions, and next action. Keep PM reviews per increment and baseline, and technical handoffs and verification per increment, profile, and revision.

Distinguish observations, hypotheses, proposals, decisions, authoring readiness, implementation, release, and observed outcomes. Leave unperformed checks and unsupported acceptance items unchecked.

Read the relevant product context, Feature, domain rules, UI, contracts, architecture principles, intended profile, ADRs, enablers, and plans before implementation. Plan concrete source and generated paths; implement only requested behavior and run applicable behavior, contract, implementation, and tooling checks. Record actual evidence.

Review documentation manually. Run automated documentation checks only when explicitly requested. Release follows its recorded target, procedure, access, and authorization. Outcome review uses actual observations.

New artifact types follow the applicable catalog extension rule. Requests to change the reusable kit are maintenance and do not start a project wizard.
