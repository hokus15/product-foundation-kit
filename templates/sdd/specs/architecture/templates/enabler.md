# ENAB-XXX — <Technical capability>

- Status: draft
- Date: YYYY-MM-DD

<!-- Use the creation date for new records; use "Date: not recorded" when
expanding an existing record whose original date is unknown.
Statuses: draft (scope being defined), ready (scope agreed, work not started),
in-progress (implementation or verification underway), done (all acceptance
criteria verified), deprecated (no longer applicable).
Remove all instructions and placeholders from the finished document. -->

## Objective and context

<Describe the technical capability and the need it enables. An enabler specifies
work and its verification; an ADR records a decision and its rationale. Link
relevant decisions rather than making new architectural choices implicitly.
Define a bounded capability reusable by features, independently of business
entities or use cases that have not been specified.>

## Scope

### Included

- <Concrete capability or deliverable>.

### Excluded

- <Relevant boundary that prevents scope ambiguity>.

## Dependencies

- <Relative link to required ADRs, contracts, specifications, or other enablers>.

<!-- Distinguish prerequisites from informative references. If none exist, say so.
Do not introduce dependencies solely to fill this section. -->

## Technical approach

<Describe implementation boundaries, affected ports and adapters, and relevant
constraints. Keep business rules in product specifications. Avoid prescribing
incidental code details or duplicating ADR rationale. Explain how feature
implementation consumes the capability and which integration work belongs to
each feature. Record technology-specific feature-to-enabler links within the
architecture profile, keeping product specifications technology-independent.>

## Planned files and source boundaries

| Concrete path | Capability deliverable | Decision or specification source | Source or generated | Create or update | Verification |
| --- | --- | --- | --- | --- | --- |

<Identify files owned by this reusable capability, including tests and shared tooling where applicable. Record generated paths, their sources, and the regeneration command or pending definition. Feature plans reference this inventory for shared files and own their Feature-specific integration. Planning does not establish execution or validation evidence.>

## Acceptance criteria

- [ ] AC-01 — <Observable result with a clear pass/fail condition>.
- [ ] AC-02 — <Relevant error case, boundary, or integration result>.

## Validation

<Map each acceptance criterion to a proportionate check, its environment and
required fixtures. Distinguish planned checks from executed checks. Record
results or link evidence before marking criteria complete. Do not require
automated tests for every low-impact change. Prefer synthetic fixtures and
test-only consumers for shared capabilities; keep business acceptance in the
relevant feature. Reassess completion evidence when a criterion changes scope.>

## Current state and remaining work

<Describe existing implementation, link evidence, and list the remaining work
and pending checks. State concrete gaps and their impact directly.>

## References

- <Supporting implementation, documentation, or related records>.

<!-- Mark implementation and tooling evidence with the Markdown title
"evidence": `[Description](relative-path "evidence")`. Keep navigation to
resulting operating guides in the profile README. -->
