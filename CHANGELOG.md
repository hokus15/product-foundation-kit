# Changelog

This file records kit changes for release consumers. Versions follow [the versioning policy](VERSIONING.md). Entries are newest first. Each release uses `## [MAJOR.MINOR.PATCH] - YYYY-MM-DD`, with an optional prerelease suffix in the version, and includes `### Compatibility` and `### Migration` sections.

`Unreleased` is pending work, not a published version. Before tagging, move the relevant changes into a dated version entry and retain an `Unreleased` section for subsequent work. No release history has been reconstructed here.

## [Unreleased]

### Added

- MIT License for the kit, with author and source attribution, and guidance for reuse in generated projects.
- Kit compatibility policy, project revision pinning, and deliberate upgrade procedure.
- Existing-project assessment and authorized-update prompts, with migration records, interruption recovery, and adoption completion rules.
- GitHub tag-triggered draft releases with a complete source ZIP, SHA-256 checksum, and commit provenance in release notes.
- Local release preparation tooling and tests for packaging and release metadata.

### Changed

- Start and resume instructions use one adopted revision for all method resources and preserve missing-revision uncertainty.
- GitHub distribution links and source URL examples use `hokus15/product-foundation-kit`.

### Compatibility

Existing project-state metadata keys, artifact destinations, workflow IDs, and status tokens are preserved. Legacy tag-only or unknown revisions require evidence-based recovery or an explicit adoption decision to establish repeatable retrieval.

### Migration

Existing projects keep their adopted kit until an upgrade is authorized. On adoption, retain project content and record the source and full commit SHA in the existing `method_source` and `method_revision` fields when supported; use the procedure in `VERSIONING.md` for legacy provenance and affected reviews.
