# HARNESS.md — How to operate <PROJECT_NAME>

This harness turns the repo into an Orchestrator-driven, spec-first delivery system.
The lead agent orchestrates a team of specialist subagents through a Spec-Driven
Development (SDD) loop, gated by CI and independent review.

## What the harness contains

- **`CLAUDE.md`** — lean root context (operating model + pointers). Read every session.
- **`knowledge/`** — the knowledge base: conventions, standards, domain depth, runbooks.
- **`docs/`** — planning artifacts: PRDs, ADRs, roadmaps, decision logs.
- **`specs/`** — approved feature specs; the SDD source of truth.
- **`.claude/agents/`** — the 15-role specialist team (subagent definitions).
- **`.claude/commands/`** — slash commands (`/new-feature`, `/code-graph-refresh`).
- **`.codegraph/`** — generated map of modules, dependencies, and symbols.

## The team (15 roles)

| Role | Owns | Dispatch when… |
|------|------|----------------|
| **Orchestrator** | The plan: decompose, distribute, verify, integrate | Always the entry point; coordinates everything |
| **PM** | Specs, priorities, acceptance criteria, scope guardrails | A feature needs a spec or scope is unclear |
| **Architect** | System design, data model, technical decisions, ADRs | Cross-cutting design or a significant tech decision |
| **Frontend** | UI against prototype + design tokens | Building or changing user-facing UI |
| **Backend** | APIs, business logic, data layer | Server-side endpoints or logic |
| **DevOps** | Repo, CI/CD, deploy, IaC, environments | Pipeline, infra, or deployment work |
| **QA** | Test strategy, test authoring, gate enforcement | Defining/writing tests or enforcing gates |
| **Security** | Threat modeling, secrets hygiene, authz/authn review | Auth, secrets, or security-sensitive surfaces |
| **Observability** | Logging, metrics, tracing, alerting | Instrumentation or production visibility |
| **UX Design** | Flows, interaction, visual consistency with brand | Interaction design or visual consistency |
| **Data/DBA** | Schema, migrations, query performance | Schema changes, migrations, query tuning |
| **Code Reviewer** | Independent review against standards before merge | Every PR, before merge — independent of author |
| **Docs** | Knowledge base, READMEs, runbooks | Documentation or runbook updates |
| **Growth/SEO** | Discoverability, metadata, conversion surfaces | Public pages, metadata, conversion work |
| **Data Analyst** | Metrics/tracking validation, funnel analysis | Tracking validation or funnel/metrics analysis |

## The SDD loop

1. **Spec** — PM converts a PRD user story into `specs/<feature>/spec.md` with testable
   acceptance criteria. Spec is approved before any code.
2. **Plan** — Orchestrator + Architect break the spec into tasks; ADRs for big decisions.
3. **Distribute** — Orchestrator dispatches tasks to specialist subagents (parallel where independent).
4. **Build** — specialists implement against the spec, consulting `.codegraph/` and `knowledge/`.
5. **Verify** — QA confirms tests cover acceptance criteria; CI must be green.
6. **Review** — Code Reviewer (independent) approves against standards.
7. **Integrate** — Orchestrator merges once all gates pass.
8. **Deploy** — DevOps ships; Observability confirms health; Data Analyst validates tracking.

## The code graph

- **What it is:** `.codegraph/` is a generated map of modules, their dependencies, and exported
  symbols. It lets agents understand impact before editing and avoid duplicating code.
- **How it's maintained:** regenerated via `/code-graph-refresh` (run after structural changes,
  and ideally in CI). Agents MUST consult it before touching code.

## Knowledge base layout

- `knowledge/conventions/` — coding standards, naming, structure.
- `knowledge/stack/` — `<STACK>`-specific patterns and gotchas.
- `knowledge/domain/` — business/domain knowledge.
- `knowledge/runbooks/` — operational procedures and incident response.

Keep `CLAUDE.md` lean: depth goes here, not in the root context.

## Quality gates

**CI gate** — every PR must have: tests pass, lint clean, typecheck clean, build succeeds.

**PR checklist:**
- [ ] Linked to an approved spec in `specs/`.
- [ ] Acceptance criteria covered by tests.
- [ ] `.codegraph/` consulted; no needless duplication.
- [ ] Docs/runbooks updated if behavior changed.
- [ ] Independent Code Reviewer approved.

**Definition of Done (per feature):**
- [ ] Spec approved and implemented.
- [ ] All acceptance criteria met and tested.
- [ ] CI green (tests + lint + typecheck + build).
- [ ] Independent review approved.
- [ ] Observability + security reviewed where relevant.
- [ ] Docs updated.

**AI evals** — where the system uses LLM behavior, eval suites guard quality; treat failing
evals like failing tests (they block merge).

## Day-to-day operation

- Start a feature: `/new-feature <user story>` → runs the SDD loop end to end.
- Refresh the map after structural changes: `/code-graph-refresh`.
- Always let the Orchestrator decompose and delegate — do not code monolithically.
- When in doubt about depth, read `knowledge/`; about the plan, read `docs/` and `specs/`.

## Definition of Done — for the harness itself

- [ ] `CLAUDE.md` is lean (~40–70 lines) and points to knowledge, not inlines it.
- [ ] All 15 agent roles exist in `.claude/agents/` with clear dispatch descriptions.
- [ ] `/new-feature` and `/code-graph-refresh` commands present and runnable.
- [ ] `knowledge/`, `docs/`, `specs/`, `.codegraph/` directories exist.
- [ ] CI configured with the CI gate (tests + lint + typecheck + build).
- [ ] **Tests + lint + CI are green on a hello-world commit.**
- [ ] SDD rule enforced: no feature without an approved spec.
