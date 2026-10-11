# Maintaining Product Foundation Kit

The kit distributes a complete project conversation method and canonical authoring schemas, starting with PM and supporting SDD, implementation, verification, release, and outcome review.

For the procedure from starting a change through PR review and release verification, follow [Working on Product Foundation Kit](CONTRIBUTING.md). This document defines the maintenance and publication procedures used by that guide.

## Maintain the route and resources

Keep documentation in English and project choices unselected in source templates. Initiative facts, credentials, implementation configuration, and execution evidence belong to generated projects.

When changing the kit:

- Keep README, instructions, prompts, complete workflow, PM and SDD guides, roles, catalogs, and state consistent.
- Preserve W00–W05, W06–W12, I01–I04, and established review IDs. Define endpoints and supporting evidence clearly.
- Give each generated type a canonical schema, destination or pattern, trigger, owner, and completion rule.
- Preserve metadata, main sections, identifiers, and statuses. Explain necessary migrations.
- Keep method resources separate from project destinations and update incoming links and heading fragments after moves.
- Keep early technical discovery available during PM; retain shared product independence and per-profile technical evidence.
- Review prose, references, and ownership manually. Run automated documentation checks only when explicitly requested.

A selected endpoint determines applicable outputs. Source schemas and future-phase resources create no mandatory project placeholders.

## Distribute and evolve

Publish an accessible source URL or archive through the selected service. Include the [MIT License](LICENSE) and preserve its copyright and permission notices in distributed copies or substantial portions of the kit. Publish the complete kit under one version and follow the [versioning and compatibility policy](VERSIONING.md).

Each project stays on its adopted revision until an update is authorized. Evaluate changes against its recorded revision, rules, definitions, and profiles. Preserve decisions, languages, IDs, progress, and evidence, and record migrations in project state. Consumer projects follow the [upgrade procedure](VERSIONING.md#upgrade-a-project-deliberately) and can use the [assessment or update prompts](GETTING_STARTED.md#update-an-existing-project).

Release migration notes must identify applicable source versions, changed contract elements, concrete old-to-new mappings, conversion order when relevant, and affected review criteria. State explicitly when no conversion is needed. For incompatible changes, provide enough detail to reconcile existing project content without inventing facts; the general upgrade procedure does not replace release-specific migration instructions. Describe prerelease migration impact as well as stable-release changes. Keep previous sources available so projects can compare and continue using their adopted revisions.

## Prepare and publish a release

The GitHub distribution targets [hokus15/product-foundation-kit](https://github.com/hokus15/product-foundation-kit). [.github/workflows/release.yml](.github/workflows/release.yml) uses the official [Python Semantic Release action](https://python-semantic-release.readthedocs.io/en/latest/configuration/automatic-releases/github-actions.html) after pushes to `main`. The action calculates the version, updates the changelog, creates and pushes the release commit and annotated tag, and publishes the GitHub release. There is no build, package publication, or separate release PR.

Before the first release, enable Actions and allow the pinned checkout and Semantic Release actions. Enable [release immutability](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes). If `main` requires PRs or checks for direct writes, configure `RELEASE_AUTOMATION_TOKEN` for an actor allowed to bypass those rules for the generated release commit. A fine-grained token needs repository **Contents: read and write**; the actor must also be allowed to create release tags. Without that secret, the workflow uses `GITHUB_TOKEN`, subject to repository rules. Remove any required `tooling-tests` check from the previous distribution workflow; the simplified workflow has no PR check.

For each change:

1. Add or update notes under `CHANGELOG.md` → `Unreleased`. Review `### Compatibility` and `### Migration` against the complete pending change set, including concrete conversions or an explicit statement that no conversion is required. This is a human PR review requirement; the workflow does not validate these assessments automatically.
2. Use Conventional Commit messages. [releaserc.toml](releaserc.toml) maps `feat` to MINOR and the other supported Commitizen types (`fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`) to PATCH. Mark incompatible changes with `!` and explain them in a `BREAKING CHANGE:` paragraph. Breaking changes increment MINOR during `0.y.z` and MAJOR after `1.0.0`. A `docs` change can be incompatible. For squash merges, the final commit title and breaking-change paragraph determine the version; branch commits embedded in the squash body are not parsed individually.
3. Review and merge the normal PR. Merge authorizes publication. Actions generates the version and UTC date, moves the reviewed pending notes into the release entry, adds a commit summary, clears `Unreleased`, and publishes. The prepared initial `0.1.0` entry is preserved when it matches the calculated version and `Unreleased` is empty. Subsequent releases use pending notes rather than manually dated entries.
4. Check the workflow result and share the version-specific source URL or GitHub source archive. The release description links to its tagged changelog, including compatibility and migration. Consumer projects resolve and record the full commit SHA; publication does not upgrade them automatically.

The small templates in [.github/release-templates](.github/release-templates) preserve the kit's changelog format and link release notes to the matching source revision. They are separate from canonical kit schemas under `templates/`. GitHub supplies ZIP and tar archives for release tags; this repository does not build additional archives or checksums. There is no package manifest or separate `VERSION` file, and nothing is published to PyPI.

Selecting `1.0.0` remains deliberate: change `major_on_zero` to `true` with a breaking commit or use an explicitly authorized Semantic Release CLI override. The supplied configuration publishes stable versions from `main`; prereleases require an explicit configuration decision. The generated commit uses `docs(release): publish <version> [skip ci]` to avoid another workflow run with an additional token.

When changing this adapter, verify the configuration and template behavior in a temporary repository without remote writes, and review documentation manually. Generated projects require none of this maintainer tooling. If publication fails, inspect the action log and use the documented [Semantic Release troubleshooting](https://python-semantic-release.readthedocs.io/en/latest/misc/troubleshooting.html). **Actions → Release kit → Run workflow** on `main` reruns the standard action; it does not guarantee recovery of a partially completed release. Never move a published tag or overwrite its assets. Corrections to released source require a new version.

Other hosts can apply the same versioning policy through their own publication mechanism.

## Layout and state migration

PM and route guides are under `method/`; SDD execution guides are under `method/sdd/`; canonical schemas are under `templates/`, including `templates/sdd/`. Supplementary coordination resources remain under `reference/`.

Older projects retain their own files. When adopting this layout, update source references and recorded revision; preserve W and I history. Record the selected endpoint, workflow mode, and intended profile in state, and expand only the steps and reviews needed by the adopted scope.

Existing PM-only progress remains valid. A project can extend its scope and resume at the earliest unresolved prerequisite. Source layout changes do not require moving project documents.
