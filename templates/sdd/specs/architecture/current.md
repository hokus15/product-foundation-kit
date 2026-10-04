---
active_profile: null
frontend_profile: null
backend_profile: null
other_implementations: []
---

# Current architecture

## Profile selection

No profile selected. Select a stable profile under `profiles/` once the increment's requirements and technical decisions support it. This file is the source of truth for the active combination. Other profiles can coexist and implement the same shared product definition.

An explicitly requested profile is the context for that task. Use this active selection when the task names none. Creating or evaluating a profile preserves the active selection until an instruction or decision changes it.

## Implementation selection

Frontend and backend selections are pending. Record their source directories under `implementation/` when applicable. For CLI tools, libraries or other products, list the relevant implementation directories in `other_implementations`.

## Activation references

Pending: link the selected profile and its accepted decisions. Add profile-specific development and validation navigation to the root README when those guides exist.
