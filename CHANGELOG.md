# Changelog

This file records kit changes for release consumers. Versions follow [the versioning policy](VERSIONING.md). Entries are newest first. Each release uses `## [MAJOR.MINOR.PATCH] - YYYY-MM-DD`, with an optional prerelease suffix in the version, and includes `### Compatibility` and `### Migration` sections.

`Unreleased` is pending work, not a published version. Review pending compatibility and migration notes in the change PR. Release automation moves them into a dated version entry before tagging and retains an empty `Unreleased` section for subsequent work. A dated entry prepares release notes; it does not by itself establish that the release has been published.

## [Unreleased]

### Changed

- PM now uses a progressive seven-file core: README, AGENTS, conventions, state, initiative, shared product foundation, and selected increment. Existing split definitions remain supported; separate language policies, opportunity maps, risk registers, priorities, roadmaps, transfer records, and indexes are conditional.
- W00–W05 have explicit phase minima. Each PM answer is persisted with direct contradiction checks and updates to changed sources and state fields; affected content is reconciled at phase closure and the complete PM review runs at W05. Already read adopted-revision resources are reused within a session unless changed or uncertain.
- Current alternatives are explored only when current practice affects the problem, scope, or improvement. Qualitative objectives, selection rationale, and outcome assessment are sufficient when supported; unused sections and future-phase placeholders are omitted.
- The increment owns the authoritative PM-SDD-01–07 review by default, with baseline and criterion evidence. State and conditional transfer documents reference it. SDD reads the consolidated foundation or existing split definitions without requiring additional PM files.
- Kit guides and authoring schemas use direct conditions and source ownership. Descriptive project documents specify the current definition when created or updated; obsolete explanations, defensive narration, and comparisons with superseded designs are removed. Decision rationale, change history, migration details, and review evidence remain in their responsible records.

### Compatibility

This changes the default PM authoring contract from the layout and schemas distributed in 0.1.0–0.1.2: required destinations, conditional section rules, language-policy ownership, state population, and the default location of PM review evidence. Treat the default contract change as breaking. W and I IDs, endpoint and mode values, metadata keys, identifier series, status meanings, and all seven PM readiness criteria remain stable. W06–W12 and execution requirements remain in force.

Existing projects stay on their adopted revision until an upgrade is authorized. On adoption, existing split files, authoritative language policies, and supported reviews can remain in place; the new core is not a mandatory restructuring of existing projects. No consumer project is changed by updating the kit.

### Migration

For authorized adoption from 0.1.0–0.1.2, follow VERSIONING.md and apply these steps in order:

1. Preserve a recoverable baseline and map actual definitions, policies, IDs, reviews, and their authoritative sources. Retain source provenance while the upgrade is incomplete.
2. Update project AGENTS and continuation rules to use phase minima, bounded per-answer work, conditional sections, review references, and current descriptive documentation. When revising descriptive documents, integrate the supported definition and remove obsolete explanations, defensive narration, and comparisons with superseded versions; retain rationale and history in their responsible records. Existing documentation-policy.md remains authoritative; new projects keep default language choices in conventions. Do not create two policy owners.
3. Retain existing initiative, opportunities, risks, priorities, and roadmap content where it is independently maintained. New PM work can use inline initiative sections. If consolidation is requested, move actual content with its IDs and evidence and replace the old definitions with references; do not maintain competing copies.
4. Retain vision, actors, scope, capabilities, quality, and glossary files as valid product inputs. New projects use specs/product/foundation.md. Optional consolidation maps those definitions into its value/users, scope/capabilities, quality, and vocabulary sections, preserves QR references, and repairs all incoming links. Do not require consolidation to enter SDD.
5. Keep an existing PM review in pm/sdd-handoff.md or another authoritative source and reference it from the INC and state. New increment reviews use the INC's PM-to-SDD review section. If relocation is requested, preserve all baseline, date, owner, result, criterion evidence, and history, then replace the old review with a link. A transfer document owns mappings and consumption evidence, not a second review.
6. Preserve state metadata and W/I history. Remove empty future rows or duplicate summaries only when appropriate; retain actual artifact, review, scope revision, and upgrade records. Point PM review entries and blockers to their authoritative sources; navigation indexes can remain.
7. Review affected content and links manually. Reopen a PM or downstream review only when its sources, scope, or evidence changed; relocation alone does not invalidate supported criteria. Record actual migration and unresolved reviews, then adopt the target source and revision when conversion is complete. Never delete existing files merely to reach seven files.

## [0.1.2] - 2026-10-11

### Added

- A repository contribution procedure for people and AI assistants, with actions and completion criteria for branches, changes, commits, changelog review, PR updates, release verification, and Dependabot updates, independent of the editor or Git client.

### Compatibility

This change adds repository maintenance guidance. The kit's method, canonical schemas, artifact destinations, and public contract remain compatible with existing projects.

### Migration

Existing projects require no migration or conversion of generated artifacts.

### Commit summary

#### Documentation

- docs(contributing): add repository contribution procedure (#3) ([b65afc4](https://github.com/hokus15/product-foundation-kit/commit/b65afc4304b009e319e74e50bd114f3d8596a333)).


## [0.1.1] - 2026-10-11

### Added

- Weekly Dependabot checks for GitHub Actions, including checkout and Python Semantic Release, with update PRs using `ci(deps)` commit messages.

### Compatibility

This change affects repository maintenance only. The kit's method, canonical schemas, artifact destinations, and public contract remain compatible with existing projects.

### Migration

Existing projects require no migration or conversion of generated artifacts.

### Commit summary

#### Continuous integration

- ci(deps): configure Dependabot for GitHub Actions (#2) ([0508f4b](https://github.com/hokus15/product-foundation-kit/commit/0508f4b302994fce3cb8985ef1d062711bad15d1)).


## [0.1.0] - 2026-10-04

### Added

- Initial Product Foundation Kit method, with an AI-guided route through product foundation, specifications, technical planning, implementation, verification, release, and outcome review, and selectable endpoints.
- Canonical Markdown schemas and artifact catalogs for project instructions and state, PM records, shared product definitions, UI, contracts, architecture profiles, and delivery plans.
- Shared product ownership independent of implementation stack, with profile-specific architecture decisions, plans, operating guides, and conformance evidence.
- Conditional technical discovery during PM, external-workflow handoff rules, and supplementary collaboration resources.
- MIT License for the kit, with author and source attribution, and guidance for reuse in generated projects.
- Kit compatibility policy, project revision pinning, and deliberate upgrade procedure.
- Existing-project assessment and authorized-update prompts, with migration records, interruption recovery, and adoption completion rules.
- GitHub release automation using the official Python Semantic Release action, Conventional Commit-based versions, reviewed compatibility and migration notes, annotated tags, and automatic publication after merge.

### Changed

- Start and resume instructions use one adopted revision for all method resources and preserve missing-revision uncertainty.
- GitHub distribution links and source URL examples use `hokus15/product-foundation-kit`.
- Release preparation generates versions and dated changelog entries after the normal change PR is merged; compatibility and migration are reviewed in that PR.

### Compatibility

This initial `0.y.z` release defines an experimental public contract under `VERSIONING.md`. Future releases must describe compatibility and migration explicitly; publishing a new kit version does not update consumer projects automatically.

Existing project-state metadata keys, artifact destinations, workflow IDs, and status tokens are preserved. Legacy tag-only or unknown revisions require evidence-based recovery or an explicit adoption decision to establish repeatable retrieval.

### Migration

New projects require no migration. Select the published version's source URL, resolve its full commit SHA, and record both at W00. Keep the kit source outside the generated project.

Existing projects keep their adopted kit until an upgrade is authorized. This release introduces no conversion of the existing canonical metadata, destinations, IDs, or status tokens. On adoption, retain project content and record the source and full commit SHA in the existing `method_source` and `method_revision` fields when supported; use the procedure in `VERSIONING.md` for legacy provenance and affected reviews.
