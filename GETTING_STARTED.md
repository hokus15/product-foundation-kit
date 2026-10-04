# Getting started

Give an AI assistant the Product Foundation Kit URL, project destination, and desired endpoint. The kit can guide PM, SDD, implementation, verification, release, and outcome review.

## Start prompt

Replace the placeholders:

For the GitHub distribution, use `https://github.com/hokus15/product-foundation-kit/tree/<release-tag>` as `<method-url>`, replacing `<release-tag>` with a published tag selected from [Releases](https://github.com/hokus15/product-foundation-kit/releases). Keep the project destination and desired endpoint specific to your initiative.

> Let's build the project foundation using Product Foundation Kit from `<method-url>` in `<project-location>`. Guide me through `<desired-endpoint>` using the kit's workflow. Resolve the selected source to an identifiable revision and use that same revision for every method resource. Read README.md and AGENTS.md, then method/guide.md, method/workflow.md, method/roles.md, method/generation.md, and method/artifacts.md. Start with configuration, languages, and working rules. Keep the kit and any downloaded checkout outside the project. Explain my working hat and yours at transitions. Read canonical templates as their outputs become applicable. If the scope includes SDD or implementation, continue with method/sdd/ after the required reviews. Record the actual method source, full commit SHA when available, endpoint, workflow mode, increment, intended profile, answers, and progress in project-state.md.

Use one of these endpoints:

| Endpoint | Work covered |
| --- | --- |
| `pm-foundation` | W00–W05 and the PM-to-SDD review. |
| `product-specifications` | Through W09 and specification readiness. |
| `implementation-plan` | Through W12 and implementation readiness. |
| `implementation` | Through I02, including code and applicable verification. |
| `release` | Through I03 for the identified target and operating scope. |
| `outcome-review` | Through I04 using actual outcome evidence. |

If the endpoint is unclear, the assistant helps establish it. A request to define a foundation without broader scope starts with PM. A project can extend its endpoint later while reusing supported work.

The [workflow](method/workflow.md) defines the complete route and reviews. The [PM catalog](method/artifacts.md) and [SDD catalog](method/sdd/artifacts.md) define project paths and canonical schemas. The [generation protocol](method/generation.md) keeps the kit external.

## Generated project and source access

The assistant needs access to the source and a writable destination. It can read remotely or retrieve an external checkout.

Prefer a URL tied to a release, such as `https://github.com/hokus15/product-foundation-kit/tree/v1.2.0`, or its complete source archive. The version is illustrative, not an existing kit release. A release page identifies the version; the assistant still needs its source files. For a moving branch or latest-release URL, resolve the source once and pin all subsequent reads to that commit. Follow the [versioning policy](VERSIONING.md) for revision recovery and upgrades.

Only project-specific documents and authorized implementation appear in the destination. Method guides, template directories, and supplementary references stay in the kit. New areas are generated when their content is needed.

## Resume prompt

> Continue the project in `<project-location>`. Read its AGENTS.md, project-conventions.md, documentation-policy.md, project-state.md, and relevant definitions and profile records. Retrieve the recorded kit source and revision externally, and use that revision for all guides, catalogs, templates, and references. Do not switch to a newer release. If the revision is unknown or inaccessible, resolve the specific source issue before dependent work; do not silently substitute another version. Restore the endpoint, workflow mode, selected increment, intended profile, active hats, and earliest unresolved prerequisite. Continue within recorded scope without repeating answered topics.

Preserve existing definitions, IDs, decisions, and supported reviews. An update to the adopted kit revision is a maintenance decision recorded with the reconciled context.

## Update an existing project

Choose a specific target release, replacing `<release-tag>` below with a published tag. The project's recorded revision stays active until migration is complete. Follow the [upgrade procedure](VERSIONING.md#upgrade-a-project-deliberately); publishing a newer kit does not update existing projects.

To assess a change before deciding to adopt it:

> Assess updating the project in `<project-location>` to Product Foundation Kit from `https://github.com/hokus15/product-foundation-kit/tree/<release-tag>`. Read the project's instructions, policies, state, and relevant definitions. Retrieve its adopted kit revision and the target externally; resolve the target's full commit SHA. Compare compatibility and migration instructions, including intervening releases when relevant. Identify concrete affected paths, steps, reviews, and missing inputs. Report the migration proposal and preserve the adopted revision and product definitions. If saving the assessment in project-state.md, mark it as a proposal. This request covers assessment only.

To authorize the update:

> Update the project in `<project-location>` to Product Foundation Kit from `https://github.com/hokus15/product-foundation-kit/tree/<release-tag>`. Follow the target's VERSIONING.md upgrade procedure. Read existing project instructions and state first, retrieve both revisions externally, and resolve the target's full commit SHA. Compare the changed guides and schemas, establish a recoverable baseline, and apply the supported migration within the project's recorded scope. Preserve its decisions, languages, IDs, progress, and evidence. Record old and target provenance, actual changes, affected reviews, unresolved inputs, and next action in project-state.md. Keep the adopted source fields unchanged until conversion is complete, then set them to the target. Continue routine authorized migration without repeated confirmation; resolve missing knowledge or authority specifically. Do not expand the endpoint or implementation scope as part of the upgrade. Report adoption separately from workflow readiness.

A named beta or release candidate is an explicit prerelease selection. For another source host, replace the GitHub URL with its version-specific source location. Ordinary continuation uses the resume prompt and retains the adopted revision. An interrupted migration resumes from its recorded partial work before dependent wizard steps.

## Use another workflow

Set `workflow_mode` to `external` when choosing another SDD tool or team process. Use the [handoff rules](method/handoff.md); the receiving workflow defines its own phases, artifacts, and invocation syntax.

Use `workflow_mode: kit` to continue through the kit's own SDD and implementation route. A requested endpoint beyond PM follows that route by default when no external workflow is selected.
