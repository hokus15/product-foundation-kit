# SDD and execution working roles

Apply these hats as the selected kit route reaches W06–W12 or I01–I04. The [PM role guide](../roles.md) owns W00–W05. Decision authority and delegation come from the project's conventions; a hat establishes neither expertise nor approval.

## Wizard step roles

| Step | Human hat | Human contribution | AI hat | AI responsibility |
| --- | --- | --- | --- | --- |
| W06 — Domain and rules | Domain Contributor | Explain business concepts, processes, exceptions, and rules, with examples and relevant sources. | Business Analyst | Model the domain and shared rules; identify missing knowledge and external criteria requiring review. |
| W07 — Features | Functional Reviewer | Describe and assess correct behavior, preconditions, failures, and boundaries for each task. | Functional Analyst | Author Features with stable requirements, use cases, and verifiable acceptance criteria. |
| W08 — UI | Experience Reviewer | Walk through tasks, information needs, navigation, feedback, and accessibility expectations. | UX/UI Designer | Define applicable framework-independent patterns, pages, states, and flows. |
| W08 — Contracts | Interaction Consumer | Explain what a caller supplies, receives, and observes in success and failure. | Functional Analyst | Define transport-independent operations supported by product behavior and shared rules. |
| W09 — Acceptance and review | Acceptance Reviewer | Examine examples and boundaries and identify what would make an outcome correct or unacceptable. | Quality Analyst | Check coverage, contradictions, and verifiability; record SDD-READY criterion outcomes. |
| W10 — Architecture | Technical Decision Owner | Supply technical and operating constraints, preferences, and trade-off decisions or delegation. | Software Architect | Define the intended profile's architecture and stack, justify choices, and record technical gaps. |
| W11 — Delivery planning | Delivery Owner | Clarify delivery capacity, dependencies, reusable needs, and practical work constraints. | Technical Lead | Bound enablers and Feature plans, concrete files, source boundaries, and validation mappings. |
| W11 — Operating guides | Operating Owner | Describe available environments, access, support, and release needs when applicable. | DevOps Engineer | Document applicable setup, CI, and deployment procedures for the chosen profile. |
| W12 — Implementation handoff | Product Owner / Technical Decision Owner | Address remaining functional and technical choices and establish the next requested scope. | Quality Analyst / Software Architect | Review BUILD-READY criteria, traceability, plans, and unresolved implementation blockers. |

Switch hats with the task: experience, contracts, delivery planning, and operating procedures need different contributions. Explain human and AI hats at transitions and record actual participants and unresolved input.

## Authorized implementation roles

The documentation wizard ends at its requested stage. For an explicitly authorized implementation task, use the following activity hats in the [implementation cycle](workflow.md#authorized-implementation-and-follow-up).

| Activity | Human hat | Human contribution | AI hat | AI responsibility |
| --- | --- | --- | --- | --- |
| I01 — Implement | Technical Decision Owner | Supply missing environment constraints, resolve choices, or delegate bounded technical decisions. | Software Engineer | Build only the requested behavior through the intended profile, using shared specifications and profile plans. |
| I02 — Verify | Acceptance Reviewer | Clarify disputed expected behavior and assess user-facing results when needed. | Quality Engineer | Execute applicable checks and map actual results and gaps to source criteria and revisions. |
| I03 — Release, when requested | Operating Owner | Establish the target, available access, operating constraints, and release authority. | DevOps Engineer | Follow the selected profile's release procedure and record actual deployment evidence and any executed recovery checks. |
| I04 — Evaluate outcomes, when requested | Product Owner | Provide observed outcomes and decide priorities or delegate the next bounded planning choice. | Product Manager | Compare observations with the increment's evaluation plan and document the subsequent decision. |

The technical hat implements the shared product definition. A stack limitation is recorded in the profile; a proposed behavior change returns to the relevant product owner and source.


## Conversation and review

Use the [PM conversation rules](../guide.md) and [handoff boundaries](../handoff.md#roles-and-review-boundaries). Preserve existing source ownership and declarations of authority. Keep authoring review separate from executed implementation evidence.
