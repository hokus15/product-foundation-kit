# Technical profiles

Each profile maps the shared product, reusable UI, and interaction contracts to an architectural approach and programming stack. Multiple profiles can implement the same product definition with different technical choices.

Create each profile under a stable kebab-case name following the project's naming convention. Use the [profile template](../templates/profile.md) for its overview.

```text
profiles/<profile>/
├── README.md
├── adr/
├── enablers/
├── implementation/
├── conformance.md
└── development.md
```

The tree shows available locations. Create conditional guides and record directories when their catalog conditions apply.

Add `ci.md` using the [CI template](../templates/ci.md) when automation is selected. Add `deployment.md` using the [deployment template](../templates/deployment.md) when release or distribution is in scope. Use the [artifact catalog](../../../../../method/sdd/artifacts.md) for the required and conditional planning records. Keep frontend and backend implementation selections distinct where applicable.

## Reuse the shared definition

Reference existing Features, rules, UI, contracts, quality requirements, and acceptance criteria from each profile's plans. Keep architecture, stack, transport mappings, and operating procedures within that profile. Adding another profile preserves existing profiles and their decisions; supersession applies when an accepted decision changes within its profile.

For an already specified increment, verify the existing PM and specification reviews and repeat W10–W12 from the [workflow](../../../../../method/sdd/workflow.md). Track the increment, specification revision, and profile in its implementation handoff review.

Each profile maintains its own conformance record. Coverage or test results from one implementation establish no coverage for another without applicable evidence.

## Profile catalog

| Profile | Purpose | Implementation combination | Overview |
| --- | --- | --- | --- |

## Activation and coverage

An explicitly named profile determines the task's technical context. Activate a profile explicitly in [current.md](../current.md) when it becomes the default combination. Its conformance record identifies the specification revision, covered criteria, executed checks and remaining gaps. A profile's presence does not establish selection or completion.
