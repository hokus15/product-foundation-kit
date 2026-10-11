# Working on Product Foundation Kit

Follow this procedure for each repository change, from starting the work to checking its release. Use your preferred editor and Git client. Each step describes the work and when it is complete. A short command reference appears at the end.

[MAINTAINING.md](MAINTAINING.md) owns maintenance and publication procedures. [VERSIONING.md](VERSIONING.md) owns compatibility and migration policy. Changes to the reusable kit are maintenance; they do not start the product workflow in a generated project.

## Contributing with an AI assistant

Use these instructions when the user asks an assistant to change Product Foundation Kit itself. They govern contribution work in this repository. When the kit is used as an external method for another project, its execution follows the kit's project workflow.

1. Read the repository README, this procedure, maintenance and versioning policies, current changelog, and PR template. Respect the authoring and source-ownership rules in [AGENTS.md](AGENTS.md). Read the affected method resources or canonical schemas before changing them.
2. Identify the concrete change and the requested endpoint from the user's instructions and existing delegation. A request to contribute without a specified change needs a focused question about the intended work.
3. Inspect existing edits, the current branch, and any relevant PR. Preserve work outside the contribution and reuse an existing branch when continuing its open PR.
4. Execute the authorized steps, including related documentation, changelog notes, and applicable validation. Routine work within recorded scope does not require repeated permission.
5. Finish with a reviewable result and a report of changed files, performed checks, compatibility, migration, and the next action. If the endpoint is unspecified, prepare the local changes and proposed commit and PR text; do not infer authorization to merge and publish.

The requested endpoint determines where the assistant finishes:

| Requested endpoint | Expected result |
| --- | --- |
| Prepare the change | Reviewed local files, changelog notes, validation evidence, and proposed commit and PR text. |
| Commit the change | The intended files committed with the documented message format. |
| Submit a PR | The committed branch pushed and the PR opened or updated with the required description. |
| Merge and publish | The authorized PR merged and the resulting release checked. |

Existing authorization can cover several endpoints. Preserve it across the work. Repository access and completed checks do not by themselves authorize publication; merging starts release automation.

If the assistant cannot use interactive Commitizen, it can prepare the answers for the user. When committing is authorized, an equivalent noninteractive commit must preserve the same allowed types, message format, and breaking declaration. Missing tools or access must be reported with the affected step; complete independent authorized work that remains possible.

## 1. Start or resume the task

1. Identify the intended change and the resources it affects.
2. Check the current branch and any pending local edits. Finish or preserve existing work before switching tasks.
3. Select the branch according to the task's state:

| Situation | Action |
| --- | --- |
| New task | Update your local `main` from GitHub, then create a new branch with a descriptive name. |
| Continuing an open PR | Use that PR's existing branch. |
| Previous PR already merged | Update `main` and create a new branch for the follow-up. |

**Complete when:** the task has a clear scope and you are on the branch that will contain its changes.

## 2. Make and review the change

1. Read [AGENTS.md](AGENTS.md) and the relevant maintenance instructions.
2. Edit the authoritative resources and update related links, guides, catalogs, or templates that must remain consistent. Keep kit documentation in English.
3. Save the files and review the differences, including newly created files and deletions.
4. Review documentation manually. Run automated documentation checks only when explicitly requested. For maintenance tooling changes, perform the applicable checks and record the actual results.

**Complete when:** the change achieves its intended result, related resources are consistent, and performed checks have recorded evidence.

## 3. Prepare the changelog

1. Add the change to `Unreleased` in [CHANGELOG.md](CHANGELOG.md), in the same branch as the work.
2. Explain what was added, changed, or fixed.
3. Update `Compatibility` to describe the effect on existing projects and the public contract.
4. Update `Migration` with the required conversion steps, or explicitly state that no migration is needed.
5. Review all pending notes together and preserve unrelated entries.

For incompatible changes, describe the affected contract elements, concrete conversions, conversion order, and reviews to repeat, following [VERSIONING.md](VERSIONING.md).

Semantic Release supplies the version and date after merge. Published entries remain historical records; subsequent corrections belong in `Unreleased`. The prepared initial release has a specific exception described in [MAINTAINING.md](MAINTAINING.md#prepare-and-publish-a-release).

**Complete when:** the PR will include the change description, compatibility assessment, and migration instructions before it is merged.

## 4. Record the work in a commit

1. Select the files or changes that belong in this commit. This selection is called staging.
2. Review the selected content and include the changelog notes in this commit or another commit on the same branch.
3. Create the commit using Commitizen (`cz commit`). Choose a type that reflects the change, an optional scope, and a short English subject.
4. Mark incompatible public-contract changes as breaking and explain them in a `BREAKING CHANGE:` paragraph, even when only Markdown changes.

Use the [commit type reference](#commit-type-reference) below. A subject follows `<type>(<scope>): <summary>`, with the scope omitted when it is not useful.

A commit records the selected content locally. If you edit a file after staging it, select its updated content again before committing. Several commits can belong to the same task and PR.

**Complete when:** the intended snapshot is saved in local history with an accurate commit message.

## 5. Upload the branch to GitHub

1. Push the branch's commits. For its first push, publish the branch and establish its remote tracking branch.
2. Confirm that GitHub shows the expected branch and latest commit.

A push uploads committed work. Unsaved, unstaged, or uncommitted edits are not uploaded. Pushing a task branch updates any open PR for that branch; release automation runs on `main`.

**Complete when:** the commits intended for review are available on GitHub.

## 6. Open the pull request

1. Open [the repository](https://github.com/hokus15/product-foundation-kit) on GitHub and create a pull request (PR) with `main` as the destination and your task branch as the source.
2. Write a Conventional Commit title that describes the complete change.
3. Fill in the [PR template](.github/pull_request_template.md):

| Section | Content |
| --- | --- |
| Change | Resulting behavior and affected resources. |
| Release impact | Compatibility, migration, and any breaking declaration, consistent with the changelog. |
| Validation | Manual review and checks actually performed, with pending checks identified as pending. |

4. Review the PR's changed files to confirm that all intended work is included.

**Complete when:** the PR contains the change and its changelog notes, and its title and description reflect the submitted work.

## 7. Complete the review and make corrections

1. Review the complete change, release impact, and available validation evidence.
2. Make any corrections on the same branch, including missing changelog notes.
3. Commit and push those corrections. They update the existing PR; keep it open.
4. Update the PR title and description if the scope has changed, then review the resulting changes again.

Opening a PR or making its first commit does not freeze its contents. If the PR has already merged, a correction follows this procedure in a new branch and PR.

**Complete when:** the change, changelog, and applicable checks are ready for merge, with review issues resolved.

## 8. Merge the PR

1. Select **Squash and merge** on GitHub.
2. Review the final commit title and body. Keep a valid Conventional Commit title and any required `BREAKING CHANGE:` paragraph.
3. Confirm the merge.

Squashing combines the branch's commits into one commit on `main`. Semantic Release evaluates that final commit; individual branch commits embedded in its body are not parsed separately. Several commits in one PR do not create several releases.

Merging authorizes publication. The current [release configuration](releaserc.toml) maps compatible `feat` changes to MINOR and the other supported types to PATCH. Breaking changes increment MINOR during `0.y.z` and MAJOR after `1.0.0`. Selecting `1.0.0` remains a deliberate maintenance decision.

**Complete when:** GitHub marks the PR as merged and its changes are on `main`.

## 9. Verify publication

1. Open [Actions](https://github.com/hokus15/product-foundation-kit/actions) and find the **Release kit** run for the merge.
2. Check that the run finishes successfully.
3. Open [Releases](https://github.com/hokus15/product-foundation-kit/releases) and verify the resulting version, tagged changelog, and source archives.

Semantic Release calculates the version, dates the changelog entry, creates the release commit and annotated tag, and publishes the GitHub release. The normal procedure does not require manually creating a tag or running `cz bump`.

If publication fails, inspect the action log and follow [the maintenance troubleshooting procedure](MAINTAINING.md#prepare-and-publish-a-release). A successful merge does not establish successful publication. A workflow rerun does not guarantee recovery of a partially completed release. Corrections to released source require a new version; published tags and assets remain immutable.

**Complete when:** the release is available and its contents match the merged change.

## 10. Prepare for the next task

1. Return to `main` and update the local copy from GitHub after release automation has finished. Include both the merged change and the generated release commit.
2. Create a new branch when starting the next task.
3. Remove completed branches when you choose to clean them up.

**Complete when:** the next task can start from the current published source.

## Apply the procedure to Dependabot PRs

[Dependabot](.github/dependabot.yml) checks GitHub Actions weekly and opens update PRs with `ci(deps)` messages. Updates still require review and merging.

1. Review the dependency's release notes, diff, and required configuration changes.
2. Continue on the PR's existing branch. Add the changelog notes and any necessary adjustments using steps 2–5.
3. Complete review, merge, and verify publication using steps 7–9.

This repository currently has a release workflow on `main`; an update PR has no automatic validation workflow that proves the updated action works. Perform the applicable maintenance tooling checks and record their evidence. A compatible `ci` update produces a PATCH release under the current configuration.

## Commit type reference

| Type | Purpose |
| --- | --- |
| `feat` | Add a compatible kit capability. |
| `fix` | Correct a defect. |
| `docs` | Change documentation. |
| `style` | Change formatting without changing meaning. |
| `refactor` | Restructure while preserving behavior. |
| `perf` | Improve performance. |
| `test` | Add or correct tests. |
| `build` | Change build tooling or external dependencies. |
| `ci` | Change GitHub Actions or dependency-update automation. |

Use the configured Commitizen choices; `chore` is not offered. Leave optional answers empty when they do not apply. Commit types and breaking declarations must reflect the reviewed public-contract impact.

## Optional command reference

You can perform Git operations through your preferred client. For terminal use, replace values between angle brackets with your own values before running a command.

| Operation | Command |
| --- | --- |
| Update local main | `git switch main`, then `git pull --ff-only` |
| Create a task branch | `git switch -c "<branch-name>"` |
| Select a file for the next commit | `git add -- "<path-to-file>"` |
| Create a Commitizen commit | `cz commit` |
| Publish a branch for the first time | `git push -u origin "<branch-name>"` |
| Upload further commits | `git push` |

Preserve pending edits before switching tasks and resolve a command failure before continuing. [Git documentation](https://git-scm.com/docs) provides details for individual operations.
