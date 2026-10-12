# Architecture templates

| Template | Destination |
| --- | --- |
| [Profile overview](profile.md) | `profiles/<profile>/README.md`. |
| [ADR](adr.md) | `profiles/<profile>/adr/ADR-NNNN-short-description.md`. |
| [Enabler](enabler.md) | `profiles/<profile>/enablers/ENAB-NNN-short-description.md`. |
| [Feature implementation plan](feature-implementation.md) | `profiles/<profile>/implementation/FEAT-NNN-short-description.md`. |
| [Development guide](development.md) | `profiles/<profile>/development.md`. |
| [CI guide](ci.md) | `profiles/<profile>/ci.md`, when automation is selected. |
| [Deployment guide](deployment.md) | `profiles/<profile>/deployment.md`, when release procedures are in scope. |
| [Conformance record](conformance.md) | `profiles/<profile>/conformance.md`. |

Use language choices in [project conventions](../../../../project/conventions.md) or a separate authoritative documentation policy when present, and keep template section meanings. Remove instructions and placeholders from completed records. New ADRs start as `proposed`; enablers as `draft`. Record dates and evidence accurately. Accepted decisions can be clarified in place; changed decisions require supersession.

Follow the [artifact catalog](../../../../../method/sdd/artifacts.md) for creation conditions and paths. A new guide type follows its extension rule. Record unknown commands as pending and proposed procedures as unexecuted. Keep technology-specific links from Features to enablers in the profile's implementation plans.
