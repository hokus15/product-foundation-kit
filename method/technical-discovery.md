# Technical discovery during PM

Technical questions can affect feasibility, scope, cost, sequence, or an investment decision before detailed specification. Resolve them when they matter within W02–W04; new evidence can reopen them at any PM step.

Keep product definitions independent of implementation choices. Record technical constraints, findings, and decisions in their responsible sources, then carry them into the handoff.

## Decide what is needed

| Situation | Action and source |
| --- | --- |
| An existing platform, integration, access restriction, budget, or operating condition constrains the initiative. | Record the constraint and its basis in the initiative brief; reference it from affected risks and quality needs. |
| A technical assumption could change scope, cost, priority, or the decision to proceed. | Define a question and use a RES research record or VAL validation record for a proportionate investigation. |
| An architectural approach, technology, or integration strategy needs a consequential decision now. | Record it in an identified profile and a scoped ADR, using available product context and evidence. |
| A choice has no current decision consequence. | Record any relevant preference or question and revisit it when needed. |

A declared preference is not a mandatory constraint. An imposed constraint has an identifiable basis; its consequences may still need investigation. A feasibility finding has a defined scope and evidence; it does not prove complete product viability.

## Follow the conditional branch

1. Identify the affected product or investment decision, the technical uncertainty, and the smallest answer needed.
2. Explain the working hats: Human — Technical Decision Owner or contributor with relevant operating knowledge; AI — Software Architect. Record missing input, authority, and delegated scope.
3. Read existing product context, constraints, risks, applicable architecture principles, intended profile, and prior ADRs. Use an explicitly named profile; otherwise read the existing active selection when available. Keep a new evaluation profile separate from active selection.
4. Register applicable outputs through the [PM catalog](artifacts.md#conditional-technical-records). Reuse existing RES and VAL schemas. For an architectural decision, use the canonical [profile](../templates/sdd/specs/architecture/templates/profile.md) and [ADR](../templates/sdd/specs/architecture/templates/adr.md) schemas.
5. Investigate within authorized scope. Attribute official sources and record actual checks, limitations, and findings. A bounded prototype or executable experiment requires scope covering that work; its planned or executed paths and evidence belong to the investigation record and artifact register.
6. Record the consequential technical decision in the profile's ADR. New ADRs start as `proposed` unless explicit instructions or evidence establish acceptance. Keep assumptions, costs, unknowns, and the conditions that would reopen the decision.
7. Feed conclusions into the responsible PM sources. A change to scope, behavior, or quality remains an explicit product decision in its shared definition. Reference the technical finding or decision as supporting context without encoding the selected stack into the requirement.
8. Return to the interrupted PM step and its Product Manager hat. Preserve the technical context for W05.

An early technical decision can use profile and ADR schemas independently of the full W06–W12 sequence. Its profile and ADR schemas can be read independently. Preserve main sections and use specific pending work or non-applicability for detail not yet defined.

## Record the decision's boundaries

An early profile identifies the constraints and intended architectural direction actually known. Its overview references the existing product baseline and ADRs; later plans, coverage, enablers, and operating details remain pending or non-applicable.

Use stable profile names and profile-local `ADR-NNNN` numbering. An ADR's date is the record creation date. Creating an evaluation profile does not activate it or imply that its implementation exists.

A technical decision is scoped to its profile and recorded product context. A new profile reuses the shared product definition and evaluates its own choices. Significant changes to accepted ADRs follow supersession; new evidence can change an investment decision through its PM record.

## Review at W05

Reference existing constraints, investigations, profile decisions, unresolved assumptions, and revisit conditions in the handoff. Identify whether technical uncertainty blocks selection or specification of the increment and why.

Resolve decision-blocking uncertainty or record an explicitly accepted bounded risk with its responsible owner and basis. Retain nonblocking questions with impact and next action. PM readiness, ADR acceptance, and executed feasibility evidence are distinct results; the receiving workflow refines technical detail as specifications mature.
