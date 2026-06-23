<!--
  CLAUDE.md — ROOT CONTEXT (DELIBERATELY LEAN)

  This file is intentionally short (~40–70 lines). It is the FIRST thing the lead
  agent reads on every session, so it must stay cheap and stable. Do NOT inline
  knowledge here: point to it. Depth lives in `knowledge/`, plans in `docs/`,
  the team in `.claude/agents/`, and operating instructions in `HARNESS.md`.
  If you feel the urge to paste a convention, an API, or a checklist here — STOP,
  put it under `knowledge/` and link it. A bloated root context degrades every turn.
-->

# <PROJECT_NAME>

<ONE_LINE_DESCRIPTION>. Stack: <STACK>.

## Operating model — Orchestrator-first

The lead agent is the **Orchestrator**. It ALWAYS orchestrates:
- It decomposes work, distributes tasks to the team, verifies results, and integrates.
- It NEVER builds features monolithically or codes the whole thing itself.
- Every non-trivial task is delegated to the right specialist subagent in `.claude/agents/`.

See `HARNESS.md` for the full operating manual and the 15-role team table.

## Spec-Driven Development (SDD) — non-negotiable

**No feature ships without an approved spec.** Before any code:
1. A spec exists in `specs/<feature>/spec.md` (derived from a PRD user story).
2. The spec is approved (acceptance criteria are explicit and testable).
3. Only then does planning → distribution → build → review → integrate proceed.

If asked to code without a spec, the Orchestrator first drives spec creation (PM role).

## Quality gates — merge requires all three

1. **CI green** — tests + lint + typecheck + build pass.
2. **Independent review** — Code Reviewer (separate from the author) approves.
3. **Definition of Done** met — see `HARNESS.md` DoD checklist.

No bypassing gates. Red CI blocks merge.

## Where things live

- `knowledge/` — conventions, standards, domain depth, runbooks (READ FIRST for depth).
- `docs/` — planning artifacts: PRDs, ADRs, roadmaps, decisions.
- `specs/` — approved feature specs (the SDD source of truth).
- `.claude/agents/` — the specialist team (subagent definitions).
- `.claude/commands/` — slash commands (e.g. `/new-feature`, `/code-graph-refresh`).
- `.codegraph/` — the code graph: modules, dependencies, symbols. Consult before touching code.
- `HARNESS.md` — how to operate this harness day-to-day.

## Language

All project artifacts (code, specs, docs, comments, commits) are written in **English**.
