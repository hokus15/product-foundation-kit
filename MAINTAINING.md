# Maintaining Product Foundation Kit

The kit distributes a complete project conversation method and canonical authoring schemas, starting with PM and supporting SDD, implementation, verification, release, and outcome review.

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

The GitHub distribution targets [hokus15/product-foundation-kit](https://github.com/hokus15/product-foundation-kit), with drafts and published versions under [Releases](https://github.com/hokus15/product-foundation-kit/releases). It uses [.github/workflows/release.yml](.github/workflows/release.yml). Pushing one `v*` tag triggers preparation of a draft release. It does not publish automatically. The workflow packages the tagged commit and uses its dated [changelog](CHANGELOG.md) entry for notes. GitHub's default `GITHUB_TOKEN` needs `contents: write`; no additional secret is required. The workflow derives the repository from the GitHub execution context, so no owner or repository name needs to be hardcoded in its configuration.

Before the first publication, enable Actions and [release immutability](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes) in repository settings. Immutability applies to future published releases. Confirm the license and source access for the intended audience. These settings and a license are not created by the workflow.

For each release:

1. Review documentation and source-relative references manually. Assess compatibility using `VERSIONING.md`; choose a stable version or an explicit prerelease such as `1.0.0-rc.1`. No first version is assigned by these files.
2. Move the relevant `Unreleased` changes into `## [<version>] - <actual-date>` in `CHANGELOG.md`. Include substantive `### Compatibility` and `### Migration` sections, even when the conclusion is that no conversion is required. Keep `Unreleased` for future changes.
3. Run `python -B -m unittest discover -s tests -v` when release tooling changes. These tests exercise packaging and release metadata; automated documentation checks remain opt-in.
4. Commit the reviewed files and push the commit to the selected release branch. Create and push an annotated tag at that exact commit. Replace the example version below with the selected version; it is not an existing release.

   ```text
   git tag -a v1.0.0 -m "Product Foundation Kit v1.0.0"
   git push origin v1.0.0
   ```

5. Open the workflow run and resulting draft. Verify the version, recorded full commit SHA, release notes, complete ZIP, and checksum. The ZIP contains the tracked kit tree at the commit, including source-only maintenance files, without Git history or uncommitted working files. Extract outside any generated project and review the method entry points. Treat a failed or partial upload as an incomplete draft.
6. Publish the reviewed draft through GitHub Releases. Prerelease tags are marked as prereleases. With immutability enabled, attach and verify all assets before publication; the published assets and tag are locked. Share the version-specific tree URL or archive, and have consumers record its resolved commit.

The release tag and its matching changelog entry are the version authorities. There is no package manifest or separate `VERSION` file. The workflow checks tag syntax, matching dated notes, and the checked-out commit; it does not certify authoring readiness or project review outcomes.

For a local packaging preview in a Git checkout, after creating the tag:

```text
python scripts/prepare_release.py --tag v1.0.0 --output-dir dist
```

Python 3.10+ and Git are required only for maintainer tooling. This writes `product-foundation-kit-v1.0.0.zip`, its `.sha256` file, and `release-notes.md` under the ignored output directory. The checksum covers the attached ZIP bytes, rather than GitHub's separately generated source archives. The GitHub workflow uses the runner's Python and GitHub CLI; generated projects require neither.

If a run fails before a draft exists, resolve the external failure and rerun the same job for the same unchanged tag. If a draft already exists, the workflow refuses to overwrite it; inspect it and complete missing assets manually or delete only the unpublished draft before rerunning. Never move or reuse the tag to fix source content. Corrections to the tagged source require a new version and changelog entry. Published releases are never replaced.

The automation is an optional distribution adapter. Other hosts can use the same policy and packaging script, then publish the resulting assets through their own release mechanism.

## Layout and state migration

PM and route guides are under `method/`; SDD execution guides are under `method/sdd/`; canonical schemas are under `templates/`, including `templates/sdd/`. Supplementary coordination resources remain under `reference/`.

Older projects retain their own files. When adopting this layout, update source references and recorded revision; preserve W and I history. Record the selected endpoint, workflow mode, and intended profile in state, and expand only the steps and reviews needed by the adopted scope.

Existing PM-only progress remains valid. A project can extend its scope and resume at the earliest unresolved prerequisite. Source layout changes do not require moving project documents.
