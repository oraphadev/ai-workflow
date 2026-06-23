# HARNESS.md — How to operate <PROJECT_NAME>

This harness turns the repo into an Orchestrator-driven, spec-first delivery system.
The lead agent orchestrates a team of specialist subagents through a Spec-Driven
Development (SDD) loop, gated by CI and independent review. The team is **dynamic**
(funneled to this project and grown on demand), the build is **loop-driven**, and the
harness is **self-improving** — it gets sharper each increment, but only with human
ratification at the gate.

## What the harness contains

- **`CLAUDE.md`** — lean root context (operating model + pointers). Read every session.
- **`knowledge/`** — the knowledge base: conventions, anti-patterns, domain depth, runbooks, learnings.
- **`docs/`** — planning artifacts: PRDs, ADRs, roadmaps, decision logs.
- **`specs/`** — approved feature specs; the SDD source of truth.
- **`.claude/agents/`** — the activated specialist team, funneled to this project.
- **`.claude/agents/_registry.md`** — who exists (active + dormant), when to dispatch, and the log of on-demand specialists added during the build.
- **`.claude/commands/`** — slash commands (`/new-feature`, `/add-specialist-agent`, `/harness-improve`, `/code-graph-refresh`).
- **`.codegraph/`** — generated map of modules, dependencies, and symbols *(present only if the stack supports it; otherwise documented-optional, see below)*.

## The team — a funneled core, grown on demand

The 15-role roster is the **available menu**, not a fixed cast. This project runs an
**activated subset**, each agent **funneled to this stack/domain** — never generic.
A "generic Frontend agent" is a bug; what lives in `.claude/agents/` knows *this*
framework, *these* tokens, and *this* project's anti-patterns.

**Activated core team** (always on):

| Role | Owns | Dispatch when… |
|------|------|----------------|
| **Orchestrator** | The plan: decompose, distribute, verify, integrate | Always the entry point; coordinates everything |
| **PM / Architect** | Specs, acceptance criteria, scope guardrails, system design, ADRs | A feature needs a spec, or a significant tech decision |
| **Builder / Engineer** | Implementation against the spec on `<STACK>` | Building or changing the application |
| **Code Reviewer** | Independent review against standards before merge | Every change, before merge — independent of author |
| **QA** | Test strategy, test authoring, gate enforcement | Defining/writing tests or enforcing gates |

**Activated for this project** (added by the Gate-1 brainstorm — fill in):

| Role | Owns | Dispatch when… |
|------|------|----------------|
| <e.g. **Frontend (Next.js)**> | <UI against tokens> | <building user-facing UI> |
| <e.g. **Security**> | <authz/authn, secrets> | <auth or sensitive surfaces> |

**Available-but-dormant** (in the menu, not yet instantiated — activate via the brainstorm
or grow via `/add-specialist-agent`): <list the unused roles — e.g. Observability,
DevOps, Data/DBA, UX/Design, Growth/SEO, Data Analyst, Docs>. The full menu and dispatch
rules live in `.claude/agents/_registry.md`.

### Growing the team on demand

The roster is a **seed, not a ceiling**. When the build surfaces a need the team doesn't
cover — a realtime-gateway specialist, an LGPD-compliance auditor, a Stripe-webhooks
agent — the Orchestrator runs **`/add-specialist-agent`** to define a new agent funneled
to this project's stack and conventions, write it into `.claude/agents/`, and register it
in `_registry.md`. New agents are funneled like every other; a generic add is still a bug.

## The SDD loop (loop-driven)

A feature runs as an iterating loop, not a single linear pass. The Orchestrator drives
`/new-feature`, which loops `build → verify → learn → refine` until the acceptance
criteria and gates pass, then **stops at the human review gate**.

1. **Spec** — PM converts a PRD user story into `specs/<feature>/spec.md` with testable
   acceptance criteria. Approved before any code.
2. **Plan** — Orchestrator + Architect break the spec into tasks; ADRs for big decisions.
3. **Distribute** — Orchestrator dispatches tasks to specialist subagents (parallel where independent).
4. **Build** — specialists implement against the spec, consulting `knowledge/` (and `.codegraph/` where present).
5. **Verify** — QA confirms tests cover the acceptance criteria; CI must be green; AI evals pass where they apply.
6. **Learn → refine** — capture learnings; if a verify gate failed, refine and loop back to build.
7. **Review (human gate)** — independent Code Reviewer approves, then the human ratifies. The loop's autonomy halts here.
8. **Integrate / Deploy** — Orchestrator merges once gates pass; DevOps/Observability/Data Analyst confirm where activated.

## The self-improvement loop

Each increment's learnings feed back into the harness so it gets sharper over time —
without silently rewriting the machine. Run **`/harness-improve`** at the increment's
review gate:

1. **Harvest** the increment's learnings — new ADRs, patterns, anti-patterns, and `knowledge/learnings/` entries.
2. **Update `knowledge/`** with what was learned.
3. **Propose** refinements to agent prompts and skills (a pitfall the Builder should now warn about, a convention the Reviewer should now enforce).
4. **Ratify at the gate.** Learnings accumulate autonomously between gates, but changes to the agents/skills land only with human sign-off. Self-improving, never self-rewriting.

## The code graph

- **What it is:** `.codegraph/` is a generated map of modules, their dependencies, and exported
  symbols. It lets agents understand impact before editing and avoid duplicating code.
- **How it's maintained:** regenerated via `/code-graph-refresh` (run after structural changes,
  and ideally in CI). Agents consult it before touching code.
- **Conditional:** if no solid code-graph tooling exists for `<STACK>`, the graph is
  *documented-optional* — agents navigate via the conventions and module map in `knowledge/`
  instead. We do not ship a faked or perpetually-stale graph.

## Knowledge base layout

- `knowledge/conventions/` — coding standards, naming, structure.
- `knowledge/patterns/` — project patterns **and anti-patterns** (what to do, what to avoid).
- `knowledge/stack/` — `<STACK>`-specific patterns and gotchas.
- `knowledge/domain/` — business/domain knowledge.
- `knowledge/runbooks/` — operational procedures and incident response.
- `knowledge/learnings/` — accumulated by the self-improvement loop, appended over time.

Keep `CLAUDE.md` lean: depth goes here, not in the root context.

## Quality gates

**CI gate** — every change must have: tests pass, lint clean, typecheck clean, build succeeds.

**PR checklist:**
- [ ] Linked to an approved spec in `specs/`.
- [ ] Acceptance criteria covered by tests.
- [ ] `knowledge/` (and `.codegraph/` where present) consulted; no needless duplication.
- [ ] Docs/runbooks updated if behavior changed.
- [ ] Independent Code Reviewer approved.

**Definition of Done (per feature):**
- [ ] Spec approved and implemented.
- [ ] All acceptance criteria met and tested.
- [ ] CI green (tests + lint + typecheck + build).
- [ ] Independent review approved; human ratified at the gate.
- [ ] Observability + security reviewed where those roles are activated.
- [ ] Learnings harvested into `knowledge/`; any harness refinements proposed.
- [ ] Docs updated.

**AI evals** — *where the system uses LLM behavior and eval tooling exists for the stack*,
eval suites guard quality; treat failing evals like failing tests (they block merge). Where
there's no LLM behavior to evaluate, evals are documented-optional rather than a hollow suite.

## Day-to-day operation

- Start a feature: `/new-feature <user story>` → runs the loop-driven SDD loop, stopping at the review gate.
- Need a specialist the team lacks: `/add-specialist-agent <the gap>` → funnels and registers a new agent.
- Close an increment: `/harness-improve` → harvest learnings, update `knowledge/`, propose refinements for ratification.
- Refresh the map after structural changes (if present): `/code-graph-refresh`.
- Always let the Orchestrator decompose and delegate — do not code monolithically.
- When in doubt about depth, read `knowledge/`; about the plan, read `docs/` and `specs/`.

## Definition of Done — for the harness itself

- [ ] `CLAUDE.md` is lean (~40–70 lines) and points to knowledge, not inlines it.
- [ ] The **activated subset** of roles exists in `.claude/agents/`, funneled to this project (none generic); dormant roles are documented in `_registry.md`.
- [ ] `_registry.md` exists and `/add-specialist-agent` works — the team can grow on demand.
- [ ] `/new-feature` is loop-driven; `/harness-improve` runs the self-improvement loop; `/code-graph-refresh` present if a code graph is used.
- [ ] `knowledge/`, `docs/`, `specs/` directories exist (and `.codegraph/` if the stack supports it).
- [ ] CI configured with the CI gate (tests + lint + typecheck + build).
- [ ] **Tests + lint + CI are green on a hello-world commit.**
- [ ] SDD rule enforced: no feature without an approved spec.
- [ ] Harness scope matches the project's stakes tier.
