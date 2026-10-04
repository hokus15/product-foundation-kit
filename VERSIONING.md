# Versioning Product Foundation Kit

Each release identifies one complete kit: root instructions, method guides, catalogs, canonical templates, and reference resources. A project adopts one revision and uses it across sessions and workflow steps. Publishing a newer kit does not update existing projects.

## Versions and compatibility

Use [Semantic Versioning](https://semver.org/) with tags in the form `vMAJOR.MINOR.PATCH`, optionally followed by a prerelease identifier such as `-rc.1`. Release tags do not use build metadata. Tags identify releases; there is no separate version file to keep synchronized.

The public contract consists of:

- Canonical metadata keys, required sections, identifiers, status meanings, and filename patterns.
- Cataloged project destinations and ownership boundaries.
- Workflow steps, endpoints, modes, required reviews, and continuation rules.
- Documented source entry points and links needed to retrieve the complete method.

Compatibility means an existing project can adopt the revision and continue within its recorded scope without mandatory conversion of existing artifacts, reinterpretation of decisions, or invalidation of supported reviews solely because the kit changed.

| Version change | Rule | Examples |
| --- | --- | --- |
| PATCH | Correct behavior or documentation while preserving the public contract. | Fix a broken link or clarify an instruction without adding a requirement. |
| MINOR | Add compatible capabilities. | Add an optional artifact or endpoint that existing projects need not adopt. |
| MAJOR | Change the public contract incompatibly. | Rename a required metadata key, change a status meaning or destination, or introduce a prerequisite that invalidates existing readiness. |

Judge the effect on projects, even when only Markdown changes. A new required section can be incompatible; a large explanation can be compatible. For `0.y.z`, the contract is experimental and each release must explain compatibility explicitly. Choose `1.0.0` when committing to this contract. Prereleases are for evaluation and are adopted only when explicitly selected.

Never move, reuse, or replace a released tag or its assets. Publish corrections under a new version. Keep previous revisions accessible. Release notes identify changes, compatibility impact, and migration instructions; they do not substitute for the method at the recorded commit.

## Adopt a revision at W00

Prefer a version-specific source URL. Resolve it to the full commit SHA when the source is a Git repository, and record the existing canonical fields in `project-state.md`:

```yaml
method_source: https://github.com/hokus15/product-foundation-kit/tree/v1.2.0
method_revision: <full-commit-sha>
```

The repository is the selected GitHub distribution location; the version and SHA placeholder are illustrative, not a published kit revision. `method_source` records the actual source location and selected tag when applicable. `method_revision` records the resolved commit, rather than only the tag or a branch name. Record an archive's verified revision when available; do not infer it from its filename. Keep temporary checkout paths in session context.

If starting from a moving reference such as a branch or a latest-release URL, resolve it once and use that commit for all subsequent reads. A release page identifies the version; retrieve its complete source tree or archive to read the method. GitHub supports [source archives by commit](https://docs.github.com/en/enterprise-cloud@latest/repositories/working-with-files/using-files/downloading-source-code-archives), and the attached kit ZIP provides a downloadable snapshot.

Read every guide, catalog, template, and reference from the same adopted revision, including resources first needed in later phases. Resolve source-relative links against that revision. Retrieve checkouts and archives outside the generated project. Do not follow a source link to a moving branch and silently mix versions.

Unknown revisions stay `null`, with the limitation and recovery action recorded in state. Work supported by accessible source material can continue, but repeatable retrieval remains unresolved until a revision is established. A local edited checkout must not claim that its files match a commit; identify the modified source and preserve a recoverable snapshot or select a clean revision.

## Resume an existing project

1. Read the project's instructions, policies, state, and relevant definitions before consulting the kit.
2. Retrieve the recorded commit and verify that it is the source of all resources used in the session. If a recorded tag now points elsewhere, use the recorded commit and report the discrepancy.
3. Reconcile actual project content with saved progress and continue at the earliest unresolved prerequisite within recorded scope.

Do not replace the adopted revision with the newest release, including a PATCH release. If the recorded revision is inaccessible, identify the missing source and resolve access or an authorized migration before dependent work. Independent work supported by project sources can continue.

For legacy state containing only a tag, resolve and record its commit with the available evidence; do not claim that the current tag proves which files an earlier session used. For an unknown revision, recover it from supported records or make an explicit adoption decision. Keep the earlier uncertainty in the scope revision record.

## Upgrade a project deliberately

An update requires explicit instructions or recorded delegation covering kit upgrades. A new release alone supplies no authorization, including a PATCH release. Each project chooses its target independently and can remain on an older revision. A request to assess an upgrade authorizes assessment; a request to apply it authorizes routine migration within the stated bounds without repeated permission for each file.

The Project Owner selects the target and owns consequential product or technical decisions. The assistant compares the revisions, applies authorized document changes, and records evidence and unresolved inputs. Upgrading the method does not by itself authorize implementation or release of the project.

### Select the target and recover the baseline

1. Select a specific release tag or verified revision. For GitHub, use `https://github.com/hokus15/product-foundation-kit/tree/<release-tag>`. Resolve the full target commit SHA. Prereleases require explicit selection, and their migration impact must be evaluated even within the same future stable version. Never treat a moving `latest` URL as the final revision record.
2. Read the project's existing instructions, conventions, documentation policy, `project-state.md`, and relevant product and profile definitions. Recover its adopted source and revision, endpoint, workflow mode, increment, intended profile, active step, and supported reviews. Identify concurrent or unsaved changes and preserve them. Establish a recoverable baseline using the project's existing persistence mechanism, such as a commit or saved document history.
3. Retrieve both kit revisions outside the project. If the old revision is unknown, use supported records to recover it; do not guess it from current artifact shape. If recovery is impossible, record the uncertainty and the basis for an explicit adoption of the target. If a known old revision is inaccessible, identify the access issue; any migration with incomplete comparison evidence needs authority covering that limitation.

### Assess and record the migration

Read the target's `VERSIONING.md`, changelog, and relevant changed guides, catalogs, and schemas. Compare directly with the adopted source; when skipping versions, include intervening migration instructions. Follow migration prerequisites in their required order without inventing intermediate project adoptions. If an older source has no versioning guide, use its available instructions and retain the comparison limitation.

Map each applicable change to concrete project paths, affected W or I steps, reviews, increments, and profiles. Distinguish changes needed to continue under the target from optional new capabilities. Scope, endpoint, workflow mode, selected increment, and profile selection remain as recorded unless changing them is also authorized. Preserve authoritative project instructions; do not replace a customized rule merely because the target template differs.

Save the proposal or authorized migration in the existing state sections:

| State section | Content to record |
| --- | --- |
| `Scope revisions` | Old and target source locations and revisions, authority or assessment-only scope, affected paths and steps, reviews to revisit, and migration progress. |
| `Open questions and proposals` | Missing source evidence, ambiguous mappings, conflicting instructions, or product decisions with impact and responsible input. |
| `Latest saved updates` | Actual changes saved, retained content, and checks performed or still pending. |
| `Next conversation step` | The next migration action while adoption is incomplete, or the next applicable workflow prerequisite after adoption. |

Keep `method_source` and `method_revision` at the adopted baseline during assessment and incomplete migration. Record the target separately in the migration entry. An assessment alone changes no product definition or adopted source selection; any assessment notes saved in state must be identified as proposals.

### Apply the authorized changes

Read the target's canonical source before changing each affected artifact. Update only applicable content and links. Preserve project decisions, languages, identifiers, accepted ADRs, progress, and actual evidence. Do not regenerate the entire project or copy kit guides into it. Optional capabilities create outputs only when their own applicability and authorization conditions are met.

Reopen reviews whose criteria or underlying definitions are affected; a version bump alone does not erase existing evidence. Preserve prior results with their reviewed baselines. Missing product knowledge, unsupported prerequisites, or a migration not explained by the release need their specific resolution. Do not invent accepted decisions or mark unperformed checks complete.

If migration is interrupted, retain the old adopted source fields, the target revision, and the concrete partial changes and next action in state. On resumption, reconcile and continue the unfinished migration before ordinary wizard work that depends on affected artifacts. Do not restart the project or silently treat partially migrated documents as a completed adoption.

### Complete adoption and resume

Review changed documents, metadata, identifiers, references, and consistency manually. Follow the project's existing policy for automated documentation checks; run them only when explicitly requested. Record which affected reviews were actually repeated and which remain unresolved.

When applicable conversion is complete, record the result in `Scope revisions`, then update `method_source` and `method_revision` to the target URL and verified revision. Use the target for all subsequent method reads. Adoption does not establish specification, implementation, or release readiness: unresolved reviews still block their dependent workflow steps. Resume at the earliest affected or previously unresolved prerequisite within recorded scope.

If no project artifacts need conversion, still record the comparison result and provenance change. If adoption is deferred, retain the existing source selection and state the next action. Returning to an earlier kit requires reconciling any migrated artifacts against the recoverable baseline; changing only the URL and SHA is insufficient.

[Getting started](GETTING_STARTED.md#update-an-existing-project) provides separate assessment and authorized-update prompts. This is an assistant-guided document procedure; the release workflow publishes kit versions and does not migrate consumer projects automatically.

## Distribution and publication

The policy is independent of repository hosts. A distributor must provide an identifiable revision and access to the complete kit. Pinning stabilizes method resources; it does not guarantee identical assistant responses across sessions.

This repository includes a GitHub publication workflow as a distribution option. [Maintaining the kit](MAINTAINING.md#prepare-and-publish-a-release) describes its draft, review, and publication procedure. Enable [immutable releases](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes) before publishing; GitHub then locks the associated tags and attached assets for future published releases. Repository settings are configured separately from these source files.
