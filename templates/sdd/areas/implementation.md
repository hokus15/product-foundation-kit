# Executable implementation

Create source directories after the corresponding specification and technical profile have been defined and implementation is authorized.

For products with distinct frontend and backend implementations:

```text
implementation/
├── frontend/<frontend-profile>/
└── backend/<backend-profile>/
```

For other products, use meaningful boundaries such as `cli/<profile>/` or `library/<profile>/`. The selected directories are recorded in `specs/architecture/current.md`.

Keep behavior tests with their implementation. Keep local setup and deployment instructions in the architecture profile. Document the source of truth and generation procedure for regenerated assets.
