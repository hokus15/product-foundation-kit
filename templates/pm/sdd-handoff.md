---
status: draft
owner: null
updated_on: null
---

# PM-to-SDD handoff

This review determines whether a bounded increment has enough definition to begin specification in the selected SDD workflow. The handoff references the reusable product foundation; detailed behavior and technical planning follow the receiving workflow.

## Selected increment

Pending: link the `INC-NNN` record, identify the objective, and bound the outcome to specify.

## Product foundation

| Source | Information needed for this increment |
| --- | --- |
| [Vision](../product/vision.md) | Problem, intended users, and value proposition. |
| [Actors](../product/actors.md) | Participants and known responsibilities. |
| [Scope](../product/scope.md) | Included capability, boundaries, and exclusions. |
| [Capabilities](../product/capabilities.md) | Position of the increment in the functional map. |
| [Quality](../product/quality-requirements.md) | Known shared conditions and relevant open decisions. |

## Reviewed baseline and source ownership

- Reviewed source revision or dated baseline: pending.
- Review scope: pending.
- Applicable project conventions and documentation policy: pending.
- Relevant initiative objectives, evidence, hypotheses, risks, and priority decisions: pending.

<!-- Generate actual links to existing project sources. With no identifiable
repository revision, record the review date and reviewed file list; leave the
revision unknown. Preserve earlier baselines and reviews in their INC records. -->

The referenced product sources own shared product decisions. PM records own evidence, priorities, investment choices, and outcome evaluation. Downstream artifacts reference this baseline; record the authoritative owner when downstream specifications add shared behavior.

## Early technical context

<!-- Include when technical discovery or decisions exist. Link actual initiative
constraints, RES/VAL evidence, profile overview, and ADRs. Otherwise omit this
section. Keep decision status separate from investigation evidence. -->

| Constraint, feasibility question, or decision | Existing source and intended profile | Evidence or decision status | Effect on scope or investment | Remaining question or revisit condition |
| --- | --- | --- | --- | --- |

## Readiness for specification

- [ ] PM-SDD-01 — The problem, actor, and expected outcome are identified.
- [ ] PM-SDD-02 — The priority has an explicit rationale and the increment has boundaries.
- [ ] PM-SDD-03 — Available evidence is referenced and relevant hypotheses are distinguished.
- [ ] PM-SDD-04 — Known quality conditions and constraints are recorded.
- [ ] PM-SDD-05 — Questions that prevent bounding the outcome are resolved.
- [ ] PM-SDD-06 — Remaining questions have an impact, owner, and next action.
- [ ] PM-SDD-07 — The method for evaluating the increment's outcome is defined.

Technical uncertainty that blocks selection or specification needs resolution or an explicitly accepted bounded risk with its owner and basis. Keep other feasibility questions with impact and next action; a complete architecture or selected stack is not a universal prerequisite.

Required evidence depends on uncertainty and the cost of being wrong. A familiar internal use case can start from operational observations and a documented decision; an adoption hypothesis may require an experiment.

## Pending questions

| Question | Impact | Does it block the SDD handoff? | Owner | Next action |
| --- | --- | --- | --- | --- |

## Downstream workflow and transfer

- Workflow mode: pending (`kit` or `external`).
- Receiving workflow: pending.
- Known tool version or revision: unknown.
- Requested downstream endpoint: pending.
- Receiving participant or assistant and working hats: pending.
- Transfer status: `not-started` (`not-started`, `prepared`, or `consumed`).
- Evidence of consumption and next action: pending.

<!-- Tool selection is optional at PM completion. prepared means the mapping
and receiving action are recorded; consumed requires evidence of actual
downstream use. Neither token implies successful specification or implementation.
Do not create tool configuration or downstream files for a PM-only request. -->

### Source-to-artifact mapping

| Shared source and stable IDs | Receiving artifact: actual path | Source ownership and baseline | Architecture profile, when technical | Status and next action |
| --- | --- | --- | --- | --- |

<!-- Populate only when downstream work is requested. Register native types
and concrete paths through the project extension/artifact registers before
creation, using the receiving tool's official templates. Omit the empty mapping
from a PM-only generated document.
Shared behavior stays independent of stack and profile. Technical plans,
tasks, code, and conformance belong to their identified profile even when a
tool requires a different physical directory layout. -->

## Review outcome

- Decision: pending (`ready`, `needs-discovery`, or `cancelled`).
- Review date: pending.
- Owner: pending.
- Reviewed sources or evidence: pending.
- Next action: pending.

At a PM-only endpoint, report the outcome and next action. With `ready`, kit mode, and a broader endpoint, continue at W06 using recorded scope. External mode transfers the referenced foundation to its receiving workflow. A PM-only project can leave that selection pending. Retain earlier reviews in their increment records when selecting another increment.

<!-- Authoring resources remain external: method/handoff.md defines
transfer and source ownership. The receiving workflow owns later authoring;
method/sdd/ defines the kit continuation; external mode uses its receiving workflow. -->
