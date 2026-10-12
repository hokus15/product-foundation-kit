# Hand the product foundation to SDD

W05 reviews the product foundation and selected increment before specification. It is a checkpoint in the kit's complete route and a portable handoff to any other SDD tool or team process.

The handoff is the selected increment's authoritative PM review and its referenced sources. Ordinary kit continuation uses them directly. Generate `pm/sdd-handoff.md` only when a receiving workflow or participant needs a separate mapping or transfer record; it links the authoritative review source. Source ownership is independent of providers, commands, and receiving formats. Selecting an external tool is optional; a PM-only project can leave continuation pending.

## Handoff contents

| Content | Authoritative project source |
| --- | --- |
| Working rules, languages, participants, and delegated decisions | `project-conventions.md`, AGENTS, and a separate language policy only when it exists. |
| Problem and its evidence | `pm/initiative.md`. |
| Value, actors, scope, capabilities, quality needs, and necessary vocabulary | `specs/product/foundation.md` or retained/extracted product definitions. |
| Objectives, evidence, hypotheses, risks, priority rationale, and sequence | `pm/initiative.md` and relevant PM records. |
| Selected outcome, boundaries, dependencies, and evaluation approach | The selected `pm/INC-NNN-short-description.md`. |
| PM-SDD-01–07 results, reviewed baseline, question references, and next action | The selected INC's review, or its retained authoritative review source. State links it. |
| Early technical constraints, feasibility evidence, and scoped decisions, when present | Initiative constraints, RES or VAL records, and the intended profile's existing ADRs. |
| Method provenance and conversation progress | `project-state.md`. |

Use actual relative links in review and transfer records. Include evidence records only when they exist. Record an unknown revision as unknown; a dated list of reviewed files can identify the baseline when no repository revision exists. The seven PM criteria are defined in the [increment schema](../templates/pm/increment.md); a transfer does not create a second review.

## Transfer procedure

1. Complete W05 and record its outcome. With `needs-discovery`, resolve the blocking questions before transfer; with `cancelled`, retain the rationale and stop that increment.
2. With `ready`, report the PM outcome. For a broader kit endpoint, continue at W06 with the recorded scope and roles; no separate external tool selection is needed. For external mode, record the receiving workflow, participant, and first action. A PM-only project stops with its next action recorded.
3. Carry forward supported early technical records and their baseline, profile, status, limitations, and revisit conditions. Read the receiving workflow's instructions and existing destination configuration. When it uses a tool, consult that tool's official instructions and record its actual version or revision when identifiable.
4. When a separate mapping is needed, record it in the conditional transfer document: each source, downstream artifact, source ownership, and profile context. Ordinary kit continuation uses catalog destinations and existing source references. Register concrete outputs before creating them.
5. Provide the receiving assistant with the existing foundation and selected increment. Reuse established answers. Clarify only behavior or constraints still unresolved; record new product decisions in their responsible shared sources.
6. Follow the selected route's requirements and gates. Kit mode uses W09, W12, and applicable I activities; external mode uses native gates. State records actual progress. A separate transfer record, when present, owns its mappings and consumption evidence; state links it.

PM readiness and transfer progress are separate. Preparing a mapping does not establish that the receiving workflow has consumed it.

## Source ownership and changes

Product documents own shared product decisions. PM records own evidence, priorities, investment choices, and outcome evaluation. A downstream specification adds observable detail and traceability; it must remain consistent with those sources.

Record which document owns each new behavior definition. When a tool-native specification is authoritative for new shared behavior, register its actual path in the transfer mapping and keep it independent of stack and profile. When adapting an existing specification, link its stable IDs and baseline to its authoritative source.

Tool-native technical plans and tasks belong to an identified architecture profile. Record their actual locations in that profile's overview or delivery records. A tool's fixed directory conventions do not change semantic ownership. Do not relocate generated tool files without checking the tool's supported configuration.

Technical limitations are profile gaps. Resolve a proposed behavior change as a product decision and review all affected specifications and profiles. Adding a profile reuses the shared definition and records separate coverage and verification evidence.

## Roles and review boundaries

At transfer, the human remains Product Owner and the assistant acts as Product Manager / Quality Analyst. At downstream behavior definition, use a Functional Reviewer and Functional Analyst; technical planning uses a Technical Decision Owner and Software Architect. The receiving workflow can refine these assignments.

Declare the active hats and needed contribution at transitions. Respect existing decision ownership and delegation. PM review, specification review, technical readiness, and executed verification retain distinct evidence.

## Available continuations

- The project's chosen SDD workflow: apply the generic transfer procedure and the receiving workflow's own instructions.
- [The kit's SDD and execution module](sdd/README.md): W06–W12 and applicable I01–I04 up to the selected endpoint.

This guide remains in the external method source. Only the project's own handoff, mappings, definitions, and applicable downstream artifacts are generated locally. Native tool integration, automated export, and synchronization require a separately scoped implementation.
