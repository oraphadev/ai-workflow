# Stage 7 — Harness Definition

> The boss stage: turn six stages of planning into a living Claude Code harness wired into the repo, so every line built afterward is fast, consistent, and verifiable.

## Objective

Through an agent-led brainstorming, design the ideal harness fully customized for *this* project — then apply it to the repo. The harness is the machinery that makes Vibe Coding work: the team, the rules, the knowledge, the gates. Everything before this was planning; this is where the planning becomes an operating environment.

**The core principle — non-negotiable, encoded everywhere:** the project's lead agent always acts as **Orchestrator**. It never builds monolithically. It plans, decomposes, delegates to a technology team, verifies, and integrates. Every artifact you write in this stage exists to make that operating model real: the lean root context tells the lead it is an orchestrator, the agent roster gives it a team to delegate to, the gates give it a standard to verify against. If a deliverable doesn't reinforce orchestrate-don't-code, it doesn't belong.

This is the densest stage. You are not writing one document — you are scaffolding a repo and configuring a multi-agent system. Move in build order, apply as you go, and verify against a hello-world at the end.

## Inputs

Everything from Stages 1–6 is now knowledge to seed, not work to redo:

- `docs/stack/` — STACK and ARCHITECTURE. These decide *what* you scaffold and *how* the agents and code graph are configured. The harness is shaped to this stack, never generic.
- `docs/brand/` — design tokens. The Frontend and UX/Design agents are customized to consume these.
- `docs/product/` — PRD and user stories. These feed the SDD spec pipeline; the PM agent guards scope against them.
- `docs/instrumentation/` — the `.env` and configured services. The harness wires MCP servers and CI secrets against what was provisioned here.
- All planning docs (Stages 1–6) — discovery, scope, brand, prototype, and everything else. These become the seed corpus of `knowledge/`.

Confirm the **Instrumentation gate (Stage 6) passed** before entering. The harness configures MCP servers, CI secrets, and environment wiring against services that must already exist and be reachable. If `docs/instrumentation/` is absent or its gate is unapproved, stop and route back — standing up CI against unprovisioned services produces a harness that's green on paper and broken in practice.

**Refuse to parachute into this stage.** This is the most-skipped-to stage — people love to jump straight to "scaffold me a harness" on a project with little or no upstream planning. Don't. The harness is the *crystallization* of Stages 1–6: the agent team is shaped by the stack, the knowledge base is seeded from discovery/scope/brand, the gates verify against the PRD, the env wiring depends on instrumentation. Building it without those is building machinery for decisions nobody made. Before you scaffold anything, check `docs/STATE.md` and the `docs/` tree: if Discovery, Scope, Brand, Prototyping, Stack, or Instrumentation is missing or unapproved, **name exactly what's incomplete and steer the user back to the earliest gap** — offer to start/resume the workflow there and flow forward. A harness is only worth building once it has six stages of real planning to crystallize. (If a user genuinely has equivalent artifacts under other names, map them to the `docs/` stages first, then proceed — but never invent the missing planning to justify skipping ahead.)

## Capability routing

- **`brainstorming` skill (superpowers)** — Step 1 *is* an agent-led brainstorming of the harness design. Drive the harness shape (which roles to activate, which skills and commands to author, how deep the gates go) through this skill, not by guessing. The brainstorm output is what the human approves at the gate before you apply anything.
- **Agent team → `.claude/agents/*.md`** — the 15 roles are implemented as subagent definitions. Instantiate them from the role templates at `assets/templates/harness/agents/` and **customize each to this project's stack and brand**. A generic Frontend agent is a bug; the Frontend agent must name the framework from STACK and point at the tokens from brand.
- **Knowledge base → `knowledge/`** — seeded *from* Stages 1–6. The `docs/` artifacts become queryable knowledge, joined by project patterns and library docs. You are not authoring knowledge from scratch; you are transcribing decisions already made into a versioned, agent-readable base.
- **Quality gates ← superpowers skills** — the gates are backed by skills the team will actually run: `test-driven-development` (no implementation before a failing test), `requesting-code-review` (independent review before merge), and `verification-before-completion` (evidence before any "it's done" claim). Reference these by name as the gate backbone so the team has concrete procedures, not aspirations.
- **Slash commands → `.claude/commands/`** — author recurring operations from the command templates at `assets/templates/harness/commands/`.

## The components

Each component is both *defined* (written down) and *applied* (live in the repo). Build them in roughly the order below; later ones depend on earlier ones.

### SDD — Spec-Driven Development

**What:** the law of the harness is `spec → plan → build → verify`. No feature is coded without an approved spec; the PRD feeds the specs; the spec feeds the plan; the plan drives the build; the build is checked against the spec at verify. Encode this as a written workflow in `HARNESS.md` and back it with slash commands (`/spec`, `/plan`) and the PM agent.

**Why:** SDD is what keeps a fast multi-agent build from drifting. The spec is the contract the Orchestrator delegates against and the Code Reviewer reviews against. Without it, agents invent requirements and you discover the divergence at integration. With it, every build traces to an approved intent.

### Context-engineering with a lean root

**What:** `CLAUDE.md` / `AGENTS.md` stay minimal. The root context says who the lead is (an Orchestrator), names the team, and *points to* `knowledge/` for depth. It does not inline architecture, conventions, or library notes — those live in the knowledge base, the skills, and the subagent prompts.

**Why:** root context is loaded into every interaction; depth inlined there is paid for on every turn and crowds out the actual task. The discipline is "lean context, rich knowledge" — keep the always-on layer thin, push the on-demand depth to where it's pulled only when relevant. A bloated CLAUDE.md is the single most common way a harness degrades.

What belongs where:

| Belongs in `CLAUDE.md` (lean root) | Belongs in `knowledge/` (pulled on demand) |
|------------------------------------|---------------------------------------------|
| "You are the Orchestrator; delegate, don't code monolithically." | The full architecture and module map |
| The agent roster and when to call each | The data model, schema, and migration history |
| Pointers: "consult `knowledge/` before touching code" | ADRs and the reasoning behind each decision |
| The SDD loop and the location of gates | Project patterns, conventions, library docs, learnings |
| How to run tests / lint / the code graph | Anything you'd only need for a specific task |

If you're tempted to add a paragraph to CLAUDE.md, that paragraph almost certainly belongs in `knowledge/` with a one-line pointer from the root.

### Agent team

**What:** the 15-role roster (table below), each a `.claude/agents/*.md` subagent, activated as needed — not all 15 run on every task. The Orchestrator dispatches the right roles for the work in front of it.

**Why:** specialized subagents keep context focused and review independent. The Code Reviewer reviewing in a fresh context catches what the author's context blinds them to; the Security agent threat-models without being anchored to the implementation. Separation of roles is what makes the verification real rather than self-attested.

### Skill-driven + subagent-driven execution

**What:** recurring know-how becomes skills (`.claude/skills/`); units of work get dispatched to subagents. The team executes through skills (the superpowers gate skills, plus any project-specific skills the brainstorm surfaces) and through delegated subagent tasks.

**Why:** skills make procedures repeatable and reviewable; subagent dispatch keeps each task's context clean and lets independent work run in parallel. This is the mechanism behind orchestrate-don't-code: the Orchestrator's job is to choose skills and dispatch subagents, not to hold every detail itself.

### Slash commands

**What:** author commands for the operations you'll run dozens of times — at minimum `/spec`, `/plan`, `/review`, `/codegraph` (regenerate the map), and whatever the brainstorm identifies. Seed from `assets/templates/harness/commands/`.

**Why:** commands compress a multi-step ritual into one invocation and make it consistent across the team. They are how SDD and the gates stop being documentation and become muscle memory.

### Code graph

**What:** a generated, auto-maintained map of modules, dependencies, and symbols, living in `.codegraph/`. Stand up both the generation tooling and the maintenance hook so the map regenerates as code changes (a post-edit hook or a `/codegraph` command the team runs).

**Why:** before an agent touches code, it consults the graph to find where a symbol lives and what depends on it — this is the single biggest reducer of hallucination in a non-trivial codebase. An agent that greps blind invents plausible-but-wrong file paths and APIs; an agent that reads the graph navigates the real structure. The map is only useful if it stays current, hence the auto-maintenance.

### Knowledge base

**What:** a complete, versioned `knowledge/` holding ADRs/decisions, project patterns, library docs, and accumulated learnings — seeded from Stages 1–6 and updated continuously thereafter. It is committed to the repo and reviewed like code.

**Why:** this is the rich half of "lean context, rich knowledge." It's where the depth that doesn't belong in CLAUDE.md actually lives, queryable by any agent on demand. Versioning matters because decisions change; an ADR that records *why* a path was taken prevents the team from re-litigating or silently reversing it. Learnings accumulate here so the harness gets smarter as the project runs.

### Verification & quality gates

**What:** the gates a change must pass before it merges — automated gates (green CI: tests, lint, type-check, format), a PR/code-review checklist, a written **Definition of Done**, and AI evals. Test depth (unit / integration / e2e) is defined **per project** in the brainstorm, not assumed. Back the gates with the superpowers skills: `test-driven-development`, `requesting-code-review`, `verification-before-completion`.

**Why:** gates are what make "fast" safe. In a multi-agent build, speed without gates is just faster drift. The written DoD gives every agent the same finish line; green CI makes "it works" mechanical rather than claimed; independent review and AI evals catch what the author missed. The gate skills give the team concrete procedures so the standard is enforced the same way every time.

## The 15-role agent team

| Role | Responsibility |
|------|----------------|
| Orchestrator (lead) | Owns the plan; decomposes work, distributes, verifies, integrates. Never works monolithically. |
| PM | Specs, priorities, acceptance criteria, scope guardrails. |
| Architect | System design, data model, technical decisions, ADRs. |
| Frontend | UI implementation against prototype + design tokens. |
| Backend | APIs, business logic, data layer. |
| DevOps | Repo, CI/CD, deploy, infra-as-code, environments. |
| QA | Test strategy, test authoring, gate enforcement. |
| Security | Threat modeling, secrets hygiene, authz/authn review. |
| Observability | Logging, metrics, tracing, alerting. |
| UX/Design | Flows, interaction, visual consistency with brand. |
| Data/DBA | Schema, migrations, query performance. |
| Code Reviewer | Independent review against standards before merge. |
| Docs | Knowledge base, READMEs, runbooks. |
| Growth/SEO | Discoverability, metadata, conversion surfaces. |
| Data Analyst | Metrics/tracking validation, funnel analysis. |

**Instantiate and customize from templates.** Each role has a template at `assets/templates/harness/agents/`. Copy it into `.claude/agents/` and rewrite it against this project: name the actual framework and language from `docs/stack/`, point the Frontend and UX agents at the real tokens in `docs/brand/`, give the Architect the decisions from the planning docs, wire the DevOps and Observability agents to the services from `docs/instrumentation/`. The customization is the work — a roster of generic role descriptions teaches the Orchestrator nothing it didn't already know. Don't ship them generic.

## Steps

Build order matters; each step leans on the ones before it.

1. **Brainstorm the harness.** Run the `brainstorming` skill with the agent over the inputs. Decide which of the 15 roles activate for this project, which skills and slash commands to author, how the knowledge base is organized, and how deep the gates and test pyramid go for *this* stack. Output a concrete harness design. This design is what the human approves at the gate before anything is applied.

2. **Scaffold the repo on the chosen stack.** Initialize the project per `docs/stack/` — framework, package manager, directory layout, a runnable hello-world. This is the substrate everything else attaches to; get it building before you wire the harness onto it.

3. **Write the lean root + Orchestrator operating model.** Create `CLAUDE.md`/`AGENTS.md` from `assets/templates/harness/CLAUDE.md`. Keep it minimal per the table above: declare the lead an Orchestrator, list the roster, state the SDD loop, and point to `knowledge/` and the gates. Resist inlining depth.

4. **Configure the team, skills, commands, and MCP.** Instantiate the 15 agents into `.claude/agents/` and customize each (see above). Author the skills into `.claude/skills/` and the slash commands into `.claude/commands/` from their templates. Wire MCP servers in settings against the services from `docs/instrumentation/`.

5. **Stand up the code graph.** Install/configure the generation tooling, generate the first `.codegraph/` map of the scaffolded repo, and wire its maintenance (a hook or `/codegraph` command) so it stays current as code changes. Verify an agent can read it.

6. **Seed the knowledge base.** Transcribe Stages 1–6 into `knowledge/` as versioned docs: ADRs from the architecture decisions, patterns from the conventions chosen, library docs for the key dependencies, and an initially-empty learnings space the team appends to. Structure it so agents can find a topic fast.

7. **Configure tests, lint, type-check, format, and CI.** Set up the toolchain at the depth decided in the brainstorm, with at least one passing example test. Write the CI config (e.g. `.github/workflows`) that runs tests + lint + type-check + format on every push and must be green to merge.

8. **Define the quality gates.** Write the green-CI gate, the PR/code-review checklist, the Definition of Done, and the AI evals — and record them in `HARNESS.md` so the team operates from one source. Bind each gate to its backing skill (`test-driven-development`, `requesting-code-review`, `verification-before-completion`).

## Deliverables

Applied in the repo — at the root and under `.claude/`:

```
<repo root>/
├── CLAUDE.md / AGENTS.md      # LEAN root + Orchestrator operating model   ← templates/harness/CLAUDE.md
├── HARNESS.md                 # what the harness is, the team, the gates,  ← templates/harness/HARNESS.md
│                              #   how to operate it
├── .claude/
│   ├── agents/                # the 15-role team (customized)              ← templates/harness/agents/
│   ├── skills/                # project + gate skills
│   ├── commands/              # /spec /plan /review /codegraph …           ← templates/harness/commands/
│   └── settings.json          # settings + MCP server config
├── knowledge/                 # VERSIONED KB seeded from Stages 1–6
│   ├── adr/                   #   architecture decisions + reasoning
│   ├── patterns/              #   project conventions
│   ├── libs/                  #   library docs
│   └── learnings/             #   accumulated, appended over time
├── .codegraph/                # generated code graph + maintenance tooling
├── tests/                     # setup + at least one passing example
├── .github/workflows/         # CI: tests + lint + type-check + format
└── <scaffolded app>           # runnable hello-world on the chosen stack
```

Which template seeds what: lean `CLAUDE.md` and `HARNESS.md` from `assets/templates/harness/`; the 15 agents from `assets/templates/harness/agents/` (customized, not copied verbatim); slash commands from `assets/templates/harness/commands/`. The `knowledge/` base is seeded from the `docs/` artifacts of Stages 1–6, not from a template — it's project-specific by nature.

All harness files and `CLAUDE.md` are written in English, regardless of conversation language.

## Definition of Done

- [ ] Repo scaffolded on the chosen stack, with a runnable hello-world.
- [ ] Lean `CLAUDE.md`/`AGENTS.md` written — minimal root, Orchestrator operating model, pointers to `knowledge/`.
- [ ] All 15 agents instantiated in `.claude/agents/` and **customized** to this stack/brand (none generic).
- [ ] Skills, slash commands, and MCP servers configured.
- [ ] Code graph generated in `.codegraph/` and its auto-maintenance wired.
- [ ] `knowledge/` seeded from Stages 1–6 (ADRs, patterns, lib docs, learnings space), versioned.
- [ ] Tests, lint, type-check, format, and CI configured at the per-project depth.
- [ ] **Tests + lint + CI GREEN on the hello-world** — verified by running them, not asserted. This is the load-bearing gate: a harness that doesn't go green on a trivial change is not done.
- [ ] Quality gates written: green-CI gate + PR checklist + Definition of Done + AI evals, recorded in `HARNESS.md`.
- [ ] `HARNESS.md` documents what the harness contains, the team, the gates, and how to operate it.

## The gate

There are **two human decisions** in this stage — one before applying, one before declaring done.

**Gate 1 — approve the harness design (before applying).** The brainstorm (Step 1) produces a concrete harness design: which roles activate, which skills and commands, how the knowledge base is structured, how deep the tests and gates go. Present this design and propose approval. Do not scaffold the repo or write a single harness file on your own judgment — applying an un-approved harness means re-doing the whole stage if the human wanted it shaped differently. Present, then STOP.

What to present for Gate 1:
1. The **activated roster** — which of the 15 roles this project runs, and why the rest are dormant.
2. The **skills and slash commands** to be authored.
3. The **knowledge base structure** and what seeds it from Stages 1–6.
4. The **test depth and gate plan** — the per-project pyramid and the DoD shape.

**Gate 2 — confirm green on hello-world (before declaring done).** After applying, run the gates against the scaffolded hello-world and present the **actual output** of tests + lint + type-check + CI going green. Do not claim the harness is ready on the strength of the files existing — readiness is proven by the gates passing on a real (trivial) change. Show the evidence, then propose the stage complete.

Approving Gate 1 unlocks the build of the harness; the green evidence at Gate 2 is what declares the environment ready. The human owns both calls — your job is to make each decision concrete and stop for it.
