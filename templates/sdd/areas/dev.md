# Development tooling

Add tools when the selected profile establishes an executable development workflow.

- Keep local execution, generation and synchronization tools here.
- Keep reusable executable checks in `dev/ci/`. Add orchestration in the location required by the selected automation tool or service when applicable.
- Keep frontend, backend and other behavior tests with their implementation.
- Select runtime versions, locked dependencies and validation commands with the technical profile.
- Document commands in the profile's development and CI guides.

Run automated documentation checks only when explicitly requested. Applicable implementation and tooling checks run after changes affecting those areas. Record executed checks and results in the corresponding profile.

Each initiative selects whether to use local automation, a hosted CI service, or both. Record that choice and its configuration in the technical profile.
