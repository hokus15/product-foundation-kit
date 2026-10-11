# Product Foundation Kit

Product Foundation Kit is an AI-guided toolkit for defining a reusable product foundation and carrying it through specification-driven development (SDD), implementation, and validation.

It starts with product management: the problem, users, value, scope, evidence, priorities, and intended outcomes. The same kit can then guide detailed specifications, architecture profiles, delivery plans, code, verification, release, and outcome review. Each project selects its endpoint and can continue with another workflow at any checkpoint.

## Define the product once

Keep product behavior independent of development tools, implementation architecture, and programming stack. Shared product, UI, contracts, quality needs, and acceptance criteria describe what each implementation must satisfy.

Architecture profiles connect that shared definition to different implementations. Each profile owns its technical choices, plans, operating guides, and conformance evidence. Changing a stack updates its profile; changing product behavior updates its authoritative source and triggers a review of affected implementations.

## A complete route with selectable endpoints

| Stage | Kit steps | Result |
| --- | --- | --- |
| Product foundation | W00–W05 | Project conventions, discovery, evidence, selected increment, and PM-to-SDD review. |
| Product specifications | W06–W09 | Domain, Features, applicable UI and contracts, acceptance, and specification review. |
| Technical planning | W10–W12 | Intended profile, decisions, bounded delivery plans, and implementation readiness. |
| Implementation and verification | I01–I02 | Requested behavior implemented and checked against shared specifications and profile decisions. |
| Release | I03 | Delivery to the requested target with recorded operating evidence. |
| Outcome review | I04 | Actual observations compared with the increment's evaluation plan and a subsequent product decision. |

A project can stop after PM, specifications, planning, or verified implementation. Release and outcome review follow their requested scope and available evidence. Recorded authorization covers subsequent work within that scope; checkpoints do not require repeating permission for routine actions.

The assistant asks focused questions, explains human and AI working hats, saves answers in their responsible documents, and preserves progress across sessions. Discovery depth follows uncertainty and the cost of a wrong decision.

## Technical decisions can start during PM

PM can investigate viability and decide an architecture, platform, or integration when the initiative needs that answer. [Technical discovery](method/technical-discovery.md) records constraints and evidence in PM and consequential architectural choices in the intended profile's ADRs.

Later planning reuses supported early decisions and reviews them against refined specifications. An accepted decision and executed feasibility evidence remain distinct.

## Use the kit or another SDD workflow

The kit's [workflow](method/workflow.md) supports the full route. Its [SDD module](method/sdd/README.md) supplies the execution guide, roles, authoring rules, and artifact catalog for W06–W12 and I01–I04.

Projects can instead use another SDD tool or process. The [handoff rules](method/handoff.md) preserve source ownership, reviewed baselines, and early decisions across that transition. Tool selection does not change the shared product definition.

## Repository structure

This repository distributes the method and its authoring resources.

```text
product-foundation-kit/
├── README.md
├── LICENSE
├── AGENTS.md
├── GETTING_STARTED.md
├── CONTRIBUTING.md
├── MAINTAINING.md
├── VERSIONING.md
├── CHANGELOG.md
├── method/
│   ├── workflow.md       # complete route, endpoints, and checkpoints
│   ├── guide.md          # conversation and resumption
│   ├── roles.md          # PM hats and links to SDD hats
│   ├── generation.md     # external source and project output rules
│   ├── artifacts.md      # PM and early technical output catalog
│   ├── handoff.md
│   ├── technical-discovery.md
│   └── sdd/              # SDD, planning, implementation, and follow-up guides
├── templates/
│   ├── project/
│   ├── pm/
│   ├── product/
│   └── sdd/              # additional specification and profile schemas
└── reference/            # supplementary collaboration resources
```

The [PM catalog](method/artifacts.md) and [SDD catalog](method/sdd/artifacts.md) define canonical input schemas, generated destinations, creation conditions, and identifiers. Supplementary [reference resources](reference/README.md) support coordination when needed.

## What appears in a generated project

The initiative receives its own rules, language policy, saved progress, and applicable PM and product documents. Specifications, profiles, technical plans, code, and operating records are added as the selected route reaches them.

The kit's `method/`, `templates/`, and `reference/` remain in the external source. Project destinations are independent of the source layout. Navigation points to existing project outputs, and `project-state.md` records the source URL, known revision, selected endpoint, workflow mode, increment, and intended profile.

## Start from a URL

[Getting started](GETTING_STARTED.md) provides start and resume prompts. The assistant needs access to the method and a writable project destination; any source checkout stays outside that destination.

The GitHub distribution repository is [hokus15/product-foundation-kit](https://github.com/hokus15/product-foundation-kit). Select a published version from [Releases](https://github.com/hokus15/product-foundation-kit/releases) and use `https://github.com/hokus15/product-foundation-kit/tree/<release-tag>` as the method URL.

Use a version-specific source URL and record its resolved commit in project state. All guides and templates come from that adopted revision, including when resuming later. New releases do not update existing projects automatically. [Versioning](VERSIONING.md) defines compatibility and revision recovery. For an existing project, follow the [upgrade procedure](VERSIONING.md#upgrade-a-project-deliberately) and use the [assessment or update prompt](GETTING_STARTED.md#update-an-existing-project). [The changelog](CHANGELOG.md) records release changes.

Kit documentation is in English. Each initiative chooses its conversation and documentation languages by area, AI assistant, repository host, downstream tools, architectures, and stacks.

An assistant executes this documented method within the project's requested scope.

## Contribute to the kit

Follow [Working on the repository](CONTRIBUTING.md) when changing Product Foundation Kit itself. The procedure covers branches, changes, commits, PRs, changelog review, and release verification using your preferred tools. [Contributing with an AI assistant](CONTRIBUTING.md#contributing-with-an-ai-assistant) defines how an assistant handles contribution scope, existing work, validation evidence, and the requested completion point. [Maintaining the kit](MAINTAINING.md) owns maintenance and distribution procedures.

## License and attribution

Product Foundation Kit, including its documentation, templates, and maintenance tooling, is licensed under the [MIT License](LICENSE). You may use, modify, distribute, sublicense, and sell copies, including for commercial projects.

When copying or distributing the kit or substantial portions of it, preserve the copyright notice identifying hokus15, Product Foundation Kit, and its source repository, together with the full license notice. Keeping the [LICENSE](LICENSE) file with those materials satisfies this requirement; copied or adapted material included in a generated project can carry the same notice in that project's third-party notices.

Using the method does not require a public credit in your product's interface. Your original project content and code remain under your chosen license; preserve the kit's notices for any substantial kit material you copy or adapt. The kit is provided without warranty, as stated in the license.
