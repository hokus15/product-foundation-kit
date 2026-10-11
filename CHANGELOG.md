# Changelog

This file records kit changes for release consumers. Versions follow [the versioning policy](VERSIONING.md). Entries are newest first. Each release uses `## [MAJOR.MINOR.PATCH] - YYYY-MM-DD`, with an optional prerelease suffix in the version, and includes `### Compatibility` and `### Migration` sections.

`Unreleased` is pending work, not a published version. Review pending compatibility and migration notes in the change PR. Release automation moves them into a dated version entry before tagging and retains an empty `Unreleased` section for subsequent work. A dated entry prepares release notes; it does not by itself establish that the release has been published.

## [Unreleased]

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
