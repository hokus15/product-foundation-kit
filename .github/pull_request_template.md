## Change

Describe the resulting behavior and the affected kit resources.

## Release impact

- Use a Conventional Commit PR title when squash merging (`feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, or `ci`).
- Mark incompatible public-contract changes with `!` and explain them in a `BREAKING CHANGE:` paragraph in the squash commit body.
- Add or update `### Compatibility` and `### Migration` under `CHANGELOG.md` → `Unreleased` for this change. Review all pending changes together. Actions calculates the version and date after merge.
- For the prepared initial release, update its existing dated entry instead.

## Validation

Record the manual review and any applicable checks actually performed.
