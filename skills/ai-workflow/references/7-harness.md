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

**Refuse to parachute onto a hollow base — but adopt a real one.** This is the most-skipped-to stage — people love to jump straight to "scaffold me a harness" on a project with little or no upstream planning. The harness is the *crystallization* of Stages 1–6: the agent team is shaped by the stack, the knowledge base is seeded from discovery/scope/brand, the gates verify against the PRD, the env wiring depends on instrumentation. Building it on nothing is building machinery for decisions nobody made. Before you scaffold anything, check `docs/STATE.md` and the `docs/` tree: if Discovery, Scope, Brand, Prototyping, Stack, or Instrumentation is genuinely missing or unapproved, **name exactly what's incomplete and steer the user back to the earliest gap** — offer to start/resume the workflow there and flow forward. Refuse only a *genuinely hollow* base; this is consistent with SKILL.md's *Stay on the rails*.

But a base that *exists* — whether built through Stages 1–6 here or imported — is a base to adopt, not refuse. Two legitimate paths in:
- **Equivalent artifacts under other names** — map them to the `docs/` stages first (record provenance), then proceed. Never invent the missing planning to justify skipping ahead.
- **Brownfield adoption.** A repo that already has code, a `CLAUDE.md`, a `.claude/`, or CI is not zero. Before designing the harness, *map the existing artifacts*: read the manifest/lockfiles, the schema, any existing agents, commands, knowledge, and CI. Treat what exists as the substrate the harness reconciles with — see *Reconcile, never clobber* below. Refuse only when the base is hollow (no real stack, no scope, no planning to crystallize); a populated brownfield repo is a base to extend.

## Capability routing

- **`brainstorming` skill (superpowers)** — Step 1 *is* an agent-led brainstorming of the harness design. Drive the harness shape (which roles to activate, which skills and commands to author, how deep the gates go) through this skill, not by guessing. The brainstorm starts from a **minimal core team** and *adds* the roles this project actually needs — see *Agent team* below. The brainstorm output is what the human approves at the gate before you apply anything.
- **Agent team → `.claude/agents/*.md`** — the 15 roles are a **seed roster, not the final team**. Instantiate only the *activated subset* from the role templates at `assets/templates/harness/agents/` and **funnel each one to THIS project** — named to the stack/domain/module, carrying the project's real conventions and anti-patterns from `knowledge/`. A generic Frontend agent is a bug; the Frontend agent must name the framework from STACK, point at the tokens from brand, and cite the project's own patterns. The roster also stays **dynamic**: Stage 8 defines and adds *new* specialized agents on demand (see *Dynamic, project-specialized agents* below).
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

### Dynamic, project-specialized agents

**What:** the 15 roles are a **seed roster, not the final team**. Two moves make the team real for *this* project:

1. **Funnel every activated agent to the project.** Each instantiated agent must be named and written to *this* stack, domain, and module — carrying the project's real conventions and anti-patterns from `knowledge/`, never a generic role description. A "generic Frontend agent" is a bug; what belongs in `.claude/agents/` is, say, a *Next.js App-Router Frontend* agent that names the framework, points at the brand tokens, and cites the project's own component patterns and pitfalls.

2. **Add new specialists on demand.** Stand up a **mechanism + registry** so the Orchestrator can *define and add new specialized agents during Stage 8* — not just pick from the seed 15. Maintain a registry at **`.claude/agents/_registry.md`** that lists every agent (seed-derived and on-demand), what it specializes in, and when to dispatch it. When the build surfaces a need the roster doesn't cover — a *realtime-gateway specialist*, an *LGPD-compliance auditor*, a *Stripe-webhooks agent* — the Orchestrator writes a new funneled agent file into `.claude/agents/` and records it in the registry. Seed this mechanism in Stage 7 and point the team at the **`/add-specialist-agent`** command, which defines a new project-specialized subagent on demand and registers it.

**Why:** a static roster of generic roles teaches the Orchestrator nothing it didn't already know. The leverage is in agents that *know this codebase* — its conventions, its sharp edges — and in being able to grow the team when reality outruns the plan. The registry keeps that growth legible instead of a sprawl of untracked agent files.

### Self-improvement loop

**What:** a harness mechanism where **each build increment's learnings feed back into the harness**. After an increment, harvest what was learned — new ADRs, patterns, anti-patterns, and `knowledge/learnings/` entries — *and* propose refinements to the agent prompts and skills (a recurring pitfall the Frontend agent should now warn about; a convention the Reviewer should now enforce). These refinements run autonomously *between* gates, but they are **proposed and ratified at the increment's review gate** — the human ratifies before the machine is rewritten. Point the team at the **`/harness-improve`** command, which runs this loop: harvest learnings → update `knowledge/` → propose agent/prompt/skill refinements for ratification.

**Why:** a harness that never learns re-makes the same mistakes every increment; the knowledge base and the agents should get sharper as the project runs. But silent self-modification is dangerous — an agent quietly rewriting its own prompt is how a harness drifts out from under the humans. Gating the ratification keeps the harness *self-improving* without becoming *self-rewriting*: learnings accumulate continuously, changes to the machine land only with human sign-off at the gate. This is the build-half cross-cutting principle from SKILL.md made concrete.

### Loop-driven execution support

**What:** the harness must equip Stage 8 for a **loop-driven build**: `build → verify → learn → refine`, running autonomously *between* gates and halting at each increment's review gate. Stage 7 defines the loop, its verify gates (which tests/lint/evals run, what "green" means here), and the learn/refine step (where learnings land and how refinements are proposed). The `/new-feature` command encodes this loop; `/harness-improve` encodes its learn/refine step.

**Why:** the build half isn't a single linear pass — it's an iterating loop that self-corrects within an increment and self-improves across increments. The harness is what makes that loop safe to run autonomously: well-defined verify gates stop drift inside the loop, and the hard stop at the human review gate keeps the autonomy bounded. If the harness doesn't define the loop and its gates, Stage 8 has nothing to iterate against.

### Skill-driven + subagent-driven execution

**What:** recurring know-how becomes skills (`.claude/skills/`); units of work get dispatched to subagents. The team executes through skills (the superpowers gate skills, plus any project-specific skills the brainstorm surfaces) and through delegated subagent tasks.

**Why:** skills make procedures repeatable and reviewable; subagent dispatch keeps each task's context clean and lets independent work run in parallel. This is the mechanism behind orchestrate-don't-code: the Orchestrator's job is to choose skills and dispatch subagents, not to hold every detail itself.

**Subagent task-spec checklist.** The prompt string is the *only* channel from parent to child — nothing is inherited — so every dispatch inlines:

- **Objective** — the one outcome this worker owns, stated up top.
- **Inputs** — the exact file paths (and the specific excerpts) it needs; never assume it can see the lead's context.
- **Output** — the required format *and* a size cap.
- **Boundaries** — its tool, permission, and model limits.
- **Return contract** — write bulk output to `<path>`; return a short digest + that path + a pass/fail verdict.
- Scale the briefing effort to the fan-out: a single worker is cheap; a 2–4 fan-out or a wide Workflow run warrants tighter specs.

### Slash commands

**What:** author commands for the operations you'll run dozens of times — at minimum `/spec`, `/plan`, `/review`, `/codegraph` (regenerate the map), and whatever the brainstorm identifies. Seed from `assets/templates/harness/commands/`.

**Why:** commands compress a multi-step ritual into one invocation and make it consistent across the team. They are how SDD and the gates stop being documentation and become muscle memory.

### Code graph (conditional — stack-dependent)

**What:** a generated, auto-maintained map of modules, dependencies, and symbols, living in `.codegraph/`. When solid tooling exists for the stack, stand up both the generation tooling and the maintenance hook so the map regenerates as code changes (a post-edit hook or a `/codegraph` command the team runs).

**Why:** before an agent touches code, it consults the graph to find where a symbol lives and what depends on it — this is the single biggest reducer of hallucination in a non-trivial codebase. An agent that greps blind invents plausible-but-wrong file paths and APIs; an agent that reads the graph navigates the real structure. The map is only useful if it stays current, hence the auto-maintenance.

**Conditional, never faked.** If no solid code-graph tooling exists for the chosen stack, don't fake one — demote it to *documented-optional*: record in `HARNESS.md` that the graph is unavailable for this stack and that agents navigate via the conventions in `knowledge/` and a maintained module map instead. A fabricated or perpetually-stale `.codegraph/` is worse than none, because the team trusts it. Activate it for `platform`-stakes builds where the tooling is real; skip it cleanly otherwise.

### Knowledge base

**What:** a complete, versioned `knowledge/` holding ADRs/decisions, project patterns, library docs, and accumulated learnings — seeded from Stages 1–6 and updated continuously thereafter. It is committed to the repo and reviewed like code.

**Why:** this is the rich half of "lean context, rich knowledge." It's where the depth that doesn't belong in CLAUDE.md actually lives, queryable by any agent on demand. Versioning matters because decisions change; an ADR that records *why* a path was taken prevents the team from re-litigating or silently reversing it. Learnings accumulate here so the harness gets smarter as the project runs.

### Verification & quality gates

**What:** the gates a change must pass before it merges — automated gates (green CI: tests, lint, type-check, format), a PR/code-review checklist, a written **Definition of Done**, and — **conditionally** — AI evals. Test depth (unit / integration / e2e) is defined **per project** in the brainstorm, not assumed. Back the gates with the superpowers skills: `test-driven-development`, `requesting-code-review`, `verification-before-completion`.

Two further line-items belong on the merge/review gate (flexed by stakes — not new stages):

- **Product-security review (distinct from secrets hygiene).** Beyond keeping secrets out of the repo, the **Security agent threat-models the built product**: authn/authz review, the injection/abuse surface, and **dependency scanning (SAST/SCA)** wired into the merge gate for `platform`/regulated builds. Pull the product's **abuse/misuse cases from the PRD** into the build's verification so the threat model checks against real stated risks, not generic ones. For `throwaway`/`mvp` this can be a lightweight checklist; for `platform`/regulated it's an automated, must-be-green gate.
- **Accessibility check (any product with a UI).** The **UX/Design agent owns an a11y line-item at the review gate** — keyboard navigation, contrast, and semantics — flexed by stakes (a quick manual pass for `mvp`, automated axe-style checks plus manual review for `platform`). Record it as a gate line-item, not a separate review stage.

**Why:** gates are what make "fast" safe. In a multi-agent build, speed without gates is just faster drift. The written DoD gives every agent the same finish line; green CI makes "it works" mechanical rather than claimed; independent review and AI evals catch what the author missed. The gate skills give the team concrete procedures so the standard is enforced the same way every time.

**AI evals are conditional (stack/domain-dependent).** Stand them up where the system has real LLM-driven behavior to guard *and* solid eval tooling exists for the stack — then treat a failing eval like a failing test. Where there's no LLM behavior to evaluate, or no credible eval harness for the stack, demote evals to *documented-optional* in `HARNESS.md` rather than shipping a hollow suite that passes vacuously.

## The 15-role agent team — the seed menu

This roster is the **available menu**, not a mandatory cast. The brainstorm at Gate 1 activates a **subset**: start from a **minimal core team** and *add* the roles this project actually needs.

**Minimal core team (the default that always activates):** Orchestrator, PM/Architect, a Builder/Engineer (the stack's primary implementer), Code Reviewer, QA. Everything else is opt-in.

From there the Gate-1 brainstorm adds the warranted roles — a Frontend and UX/Design agent for a token-driven UI, Security and Data/DBA for an auth-heavy data app, Observability and DevOps for a platform, and so on. The roles *not* activated are **documented as available-but-dormant** (named in `HARNESS.md`/the registry as ready to activate later), not instantiated. And the roster is a *seed*, not a ceiling — Stage 8 grows it with on-demand specialists (see *Dynamic, project-specialized agents*).

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

**Instantiate the activated subset and funnel each to the project.** Each role has a template at `assets/templates/harness/agents/`. For every *activated* role, copy it into `.claude/agents/` and rewrite it against this project: name the actual framework and language from `docs/stack/`, point the Frontend and UX agents at the real tokens in `docs/brand/`, give the Architect the decisions from the planning docs, wire the DevOps and Observability agents to the services from `docs/instrumentation/`, and load each with the conventions and anti-patterns from `knowledge/`. The funneling is the work — a roster of generic role descriptions teaches the Orchestrator nothing it didn't already know. Don't ship them generic, and don't instantiate the dormant ones; record those in `.claude/agents/_registry.md` as available-but-dormant. Register every activated agent in `_registry.md` so the team — and the on-demand `/add-specialist-agent` flow — has one map of who exists and when to dispatch them.

## Flex the harness by stakes

The harness is not one fixed size — its scope scales with the `stakes` tier from `docs/STATE.md` (see SKILL.md's *Right-size by stakes*). Pour `platform` machinery into a weekend spike and the harness gets abandoned; under-build a serious product and the gates can't hold.

- **`throwaway`** → **skip the harness, or stand up a tiny core**: Orchestrator + a Builder + a Code Reviewer, lean gates, no code graph, no evals. Just enough to keep a spike honest.
- **`mvp`** → **core team + the roles this project actually needs**, the SDD loop, real CI gates, code graph and evals only where the stack supports them cheaply.
- **`platform`** → **the full harness**: all warranted roles, code graph, AI evals, the self-improvement loop, deep gates. The maximal harness is the `platform` setting, never the unconditional default.

When unsure, confirm the tier with the user rather than defaulting big.

## Reconcile, never clobber (brownfield)

When the repo already has harness-shaped artifacts — a `CLAUDE.md`, a `.claude/` directory, agents, commands, a CI config, a `knowledge/` base — **reconcile or ask; never overwrite**. This mirrors SKILL.md's brownfield rule.

- **Map before you write.** Read what exists and treat it as the substrate. An existing `CLAUDE.md` is merged toward the lean-root shape (not replaced wholesale); existing agents are catalogued in `_registry.md` and funneled further, not discarded; an existing CI config is extended to add the missing gates, not swapped out.
- **Ask on conflict.** When the existing artifact disagrees with the harness design, surface the conflict and let the human decide — don't silently impose the template. A reconciled merge keeps the team's prior decisions; a clobber throws them away.
- **Refuse only a hollow base.** A populated brownfield repo is a base to extend. Refuse to scaffold only when the planning genuinely isn't there to crystallize.

## Steps

Build order matters; each step leans on the ones before it.

1. **Brainstorm the harness.** Run the `brainstorming` skill with the agent over the inputs. Starting from the **minimal core team**, decide which additional roles activate for this project (and which stay dormant), which skills and slash commands to author, how the knowledge base is organized, whether the code graph and AI evals are warranted *and* tooling-supported for this stack, and how deep the gates and test pyramid go. Scale all of this to the `stakes` tier. Output a concrete harness design. This design is what the human approves at the gate before anything is applied.

2. **Scaffold the repo on the chosen stack.** Initialize the project per `docs/stack/` — framework, package manager, directory layout, a runnable hello-world. This is the substrate everything else attaches to; get it building before you wire the harness onto it. In a brownfield repo, *adopt* the existing app instead of re-scaffolding, and reconcile rather than clobber.

3. **Write the lean root + Orchestrator operating model.** Create `CLAUDE.md`/`AGENTS.md` from `assets/templates/harness/CLAUDE.md`. Keep it minimal per the table above: declare the lead an Orchestrator, list the activated roster, state the SDD loop, and point to `knowledge/` and the gates. Resist inlining depth. If a `CLAUDE.md` already exists, merge toward this shape rather than overwriting.

4. **Configure the team, skills, commands, and MCP.** Instantiate the **activated subset** into `.claude/agents/`, funnel each to the project (see above), and record both activated and dormant roles in `.claude/agents/_registry.md`. Stand up the **on-demand agent mechanism** so Stage 8 can add new specialists — author `/add-specialist-agent` and `/harness-improve` alongside the rest. Author the skills into `.claude/skills/` and the slash commands into `.claude/commands/` from their templates. Wire MCP servers in settings against the services from `docs/instrumentation/`.

5. **Stand up the code graph (if warranted).** When the stack has solid code-graph tooling and the stakes justify it, install/configure the generation tooling, generate the first `.codegraph/` map, and wire its maintenance (a hook or `/codegraph` command) so it stays current; verify an agent can read it. If no solid tooling exists, **don't fake it** — record it as documented-optional in `HARNESS.md` and rely on the module map and conventions in `knowledge/`.

6. **Seed the knowledge base.** Transcribe Stages 1–6 into `knowledge/` as versioned docs: ADRs from the architecture decisions, patterns and anti-patterns from the conventions chosen, library docs for the key dependencies, and an initially-empty `learnings/` space the self-improvement loop appends to. Structure it so agents can find a topic fast.

7. **Configure tests, lint, type-check, format, and CI.** Set up the toolchain at the depth decided in the brainstorm, with at least one passing example test. Write the CI config (e.g. `.github/workflows`) that runs tests + lint + type-check + format on every push and must be green to merge. Extend an existing CI config rather than replacing it.

8. **Define the quality gates and the loops.** Write the green-CI gate, the PR/code-review checklist, the Definition of Done, the **product-security review** (Security agent: authn/authz + injection/abuse surface + SAST/SCA wired in for `platform`/regulated, checking the PRD's abuse cases), the **accessibility line-item** (UX/Design agent, for any UI, flexed by stakes), and — where warranted — the AI evals, recording them in `HARNESS.md`. Document the **loop-driven build** (`build → verify → learn → refine`) with its verify gates and its hard stop at the human review gate, and the **self-improvement loop** (learnings feed `knowledge/`; agent/prompt/skill refinements are proposed and ratified at the gate). Bind each gate to its backing skill (`test-driven-development`, `requesting-code-review`, `verification-before-completion`).

## Deliverables

Applied in the repo — at the root and under `.claude/`:

```
<repo root>/
├── CLAUDE.md / AGENTS.md      # LEAN root + Orchestrator operating model   ← templates/harness/CLAUDE.md
├── HARNESS.md                 # what the harness is, the team, the gates,  ← templates/harness/HARNESS.md
│                              #   how to operate it
├── .claude/
│   ├── agents/                # the ACTIVATED subset, funneled to project    ← templates/harness/agents/
│   │   └── _registry.md       #   who exists (active + dormant), when to dispatch, on-demand log
│   ├── skills/                # project + gate skills
│   ├── commands/              # /spec /plan /review /new-feature
│   │                          #   /add-specialist-agent /harness-improve …   ← templates/harness/commands/
│   └── settings.json          # settings + MCP server config
├── knowledge/                 # VERSIONED KB seeded from Stages 1–6
│   ├── adr/                   #   architecture decisions + reasoning
│   ├── patterns/              #   project conventions + anti-patterns
│   ├── libs/                  #   library docs
│   └── learnings/             #   accumulated by the self-improvement loop
├── .codegraph/                # generated code graph + maintenance (if stack supports it)
├── tests/                     # setup + at least one passing example
├── .github/workflows/         # CI: tests + lint + type-check + format
└── <scaffolded app>           # runnable hello-world on the chosen stack
```

Which template seeds what: lean `CLAUDE.md` and `HARNESS.md` from `assets/templates/harness/`; the activated agents from `assets/templates/harness/agents/` (funneled to the project, not copied verbatim); slash commands — including `/add-specialist-agent` and `/harness-improve` — from `assets/templates/harness/commands/`. The `knowledge/` base is seeded from the `docs/` artifacts of Stages 1–6, not from a template — it's project-specific by nature. The code graph and AI evals appear only when the stack supports them; otherwise they're documented-optional, not faked.

All harness files and `CLAUDE.md` are written in English, regardless of conversation language.

## Definition of Done

- [ ] Repo scaffolded on the chosen stack (or the existing app adopted), with a runnable hello-world.
- [ ] Lean `CLAUDE.md`/`AGENTS.md` written — minimal root, Orchestrator operating model, pointers to `knowledge/` (merged, not clobbered, if one existed).
- [ ] **The activated subset of roles is instantiated and project-specialized** in `.claude/agents/` (none generic); **the remaining roles are documented as available-but-dormant** in `.claude/agents/_registry.md`.
- [ ] The **on-demand agent mechanism** is in place: `_registry.md` plus the `/add-specialist-agent` command, so Stage 8 can define and add new specialists.
- [ ] The **self-improvement loop** is defined: learnings feed `knowledge/`, and agent/prompt/skill refinements are proposed and ratified at the increment's review gate (`/harness-improve`).
- [ ] The **loop-driven build** (`build → verify → learn → refine`) is documented with its verify gates and its hard stop at the human review gate.
- [ ] Skills, slash commands, and MCP servers configured.
- [ ] Code graph generated **and auto-maintained if the stack supports it** — otherwise documented-optional in `HARNESS.md`, not faked.
- [ ] `knowledge/` seeded from Stages 1–6 (ADRs, patterns, anti-patterns, lib docs, learnings space), versioned.
- [ ] Tests, lint, type-check, format, and CI configured at the per-project depth.
- [ ] **Tests + lint + CI green on the hello-world** — verified by running them, not asserted. This is the load-bearing gate: a harness that doesn't go green on a trivial change is not done.
- [ ] Quality gates written: green-CI gate + PR checklist + Definition of Done + AI evals **where warranted**, recorded in `HARNESS.md`.
- [ ] **Product-security review** wired as a gate line-item — Security agent threat-models authn/authz + injection/abuse surface, with SAST/SCA in the merge gate for `platform`/regulated and the PRD's abuse cases pulled into verification.
- [ ] **Accessibility check** wired as a review-gate line-item owned by UX/Design for any product with a UI (keyboard nav, contrast, semantics), flexed by stakes.
- [ ] `HARNESS.md` documents what the harness contains, the team, the gates, the loops, and how to operate it.
- [ ] Harness scope matches the `stakes` tier (tiny core for `throwaway`, core + needed roles for `mvp`, full for `platform`).

## The gate

There are **two human decisions** in this stage — one before applying, one before declaring done.

**Gate 1 — approve the harness design (before applying).** The brainstorm (Step 1) produces a concrete harness design: which roles activate, which skills and commands, how the knowledge base is structured, how deep the tests and gates go. Present this design and propose approval. Do not scaffold the repo or write a single harness file on your own judgment — applying an un-approved harness means re-doing the whole stage if the human wanted it shaped differently. Present, then STOP.

What to present for Gate 1:
1. The **activated roster** — the minimal core plus the roles this project adds, each funneled to the stack/domain, and which roles stay dormant. Include the **on-demand mechanism** (`_registry.md` + `/add-specialist-agent`) so the team can grow in Stage 8.
2. The **skills and slash commands** to be authored — including `/harness-improve` for the self-improvement loop.
3. The **knowledge base structure** and what seeds it from Stages 1–6.
4. The **test depth and gate plan** — the per-project pyramid, the DoD shape, whether the code graph and AI evals are warranted *and* tooling-supported, and how the build loop and self-improvement loop run between gates.
5. The **stakes-scaled scope** — confirm the harness depth matches the tier.

**When the user is non-technical, present Gate 1 as plain-language consequences.** Frame each design choice (how heavy the gates, whether a code graph, how big the team) in terms the founder owns — **cost, lock-in, and speed** — lead with a clear recommendation, and tuck the engineering rationale behind a short "details" fold. Keep it a **real, recommended-and-confirmed decision**, not a rubber-stamp: surface the credible alternative they could pick (e.g. "lighter gates, ship faster but catch less" vs. "deeper gates, slower but safer") and have them actively confirm — the gate is theater if the only move is to click yes.

**Gate 2 — confirm green on hello-world (before declaring done).** After applying, run the gates against the scaffolded hello-world and present the **actual output** of tests + lint + type-check + CI going green. Do not claim the harness is ready on the strength of the files existing — readiness is proven by the gates passing on a real (trivial) change. Show the evidence, then propose the stage complete.

Approving Gate 1 unlocks the build of the harness; the green evidence at Gate 2 is what declares the environment ready. The human owns both calls — your job is to make each decision concrete and stop for it.
