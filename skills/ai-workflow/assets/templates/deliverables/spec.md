# Spec: <SPEC-ID> — <Title>

> One feature spec per file, living in `specs/`. Embodies the loop:
> **spec → plan → build → verify**. Keep it small and shippable as one slice.

- **Spec ID:** `<SPEC-001>`
- **Title:** `<short descriptive name>`
- **Linked user story:** `<PRD reference, e.g. US-12 "As a user, I can ...">`
- **Status:** `<draft / approved / in progress / done>`

## Goal

`<One or two sentences: what user outcome this delivers and why it matters.>`

## Scope

**In scope**

- `<what this slice will do>`

**Out of scope**

- `<explicitly excluded; defer to a later spec>`

## Plan

> Ordered, concrete build steps. Each should be independently reviewable.

1. `<step>`
2. `<step>`
3. `<step>`

## Acceptance criteria

> Observable, testable conditions. Use Given/When/Then where helpful.

- [ ] `<Given ... when ... then ...>`
- [ ] `<...>`

## Verification

> Commands and checks that must pass before this spec is "done".

- [ ] Tests: `<command, e.g. npm test -- feature>`
- [ ] Lint: `<npm run lint>`
- [ ] Type-check: `<npm run typecheck>`
- [ ] Manual check: `<what to click/observe>`

## Rollout / deploy

`<Deploy note: feature flag? migration to run? backfill? staging-first?
Update PROGRESS.md and CHANGELOG.md when shipped.>`
