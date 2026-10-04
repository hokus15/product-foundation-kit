---
status: draft
---

# Architecture principles

## Selected principles

Pending: select the shared constraints the initiative needs across profiles. Consider testable business boundaries, replaceable infrastructure, security and operational needs where relevant. Assign stable `AP-NN` identifiers and describe each principle's consequence.

| ID | Principle | Need or constraint | Consequence |
| --- | --- | --- | --- |

## Product and interaction boundaries

Define the product once, independently of architectural patterns and programming stacks. Product specifications own business behavior and quality requirements; reusable UI owns framework-independent experience; interaction contracts own transport-independent operations.

Technical profiles specify the architectural approaches and technologies that satisfy these shared sources. Each profile maps its implementation to the same acceptance criteria and records coverage, evidence, and gaps independently.

Keep common architecture principles proportional to constraints required across profiles. Profile-specific patterns and stack choices belong to their profiles. A technology change updates its profile and implementation; changing shared behavior requires a product decision.

## Pending decisions

Pending: identify constraints that need clarification before selecting a profile. Architecture patterns, frameworks and runtimes are selected from the initiative's needs.
