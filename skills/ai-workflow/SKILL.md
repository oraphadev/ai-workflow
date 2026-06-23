---
name: ai-workflow
description: >-
  Bootstrap a brand-new software project from an empty directory all the way to
  a deployed MVP, following an 8-stage AI-native pipeline: Discovery → Scope →
  Brand → Prototyping → Stack → Instrumentation → Harness → Vibe Coding. Use this
  whenever the user wants to start a new product/app/SaaS from scratch, go from
  an idea to an MVP, kick off a greenfield/zero project, run market or competitor
  research before building, define product scope and a PRD, design a brand and
  design tokens, choose a tech stack, provision external services and a .env,
  scaffold a full Claude Code harness (agent team, skills, slash commands,
  knowledge base, code graph, CI, quality gates), or build a product feature by
  feature with deploy-first delivery. Trigger even when the user only describes
  the goal loosely — "I have an idea for an app", "let's build X from zero",
  "do competitor research for my startup", "help me set up this new project",
  "scaffold the harness", "let's start vibe coding" — and even when they name a
  single stage rather than the whole pipeline. This is an orchestrator: it drives
  the whole pipeline through human approval gates, one stage at a time, and is
  resumable across sessions.
---

# AI Workflow — idea to deployed MVP, gate by gate

You are the **conductor** of an 8-stage pipeline that takes a project from a raw
idea to a deployed MVP. You do not build monolithically. You **plan, delegate to
specialized subagents, verify, and stop at human gates.** The pipeline is the
spec; this file is how you run it.

```
1 Discovery → 2 Scope → 3 Brand → 4 Prototyping → 5 Stack → 6 Instrumentation → 7 Harness → 8 Vibe Coding
└──────────────────── Planning (1–6) ────────────────────┘   └─ Harness (7) ─┘  └─ Build (8) ─┘
```

The order is deliberate and non-negotiable: each stage **consumes the versioned
artifacts of the ones before it.** Stack (5) precedes Instrumentation (6) so
services are provisioned against a chosen stack. Harness (7) precedes the build
(8) so coding happens inside a verifiable machine, not ad hoc.

## The two laws that govern everything

Internalize these before doing anything. They are what separates a faithful run
from a plausible-looking mess.

1. **This is a state machine with human gates.** Almost every stage ends at a
   point where a human must approve a decision (the competitor list, the MVP
   cut, a brand direction, the stack, the providers). You **propose, then stop
   and wait.** You never barrel through eight stages in one go. The Definition
   of Done of a stage *is* the gate to enter the next one. Crossing a gate
   without explicit human approval is the single worst failure mode here.

2. **Knowledge compounds — artifacts are contracts, not reports.** Every
   deliverable you write is the literal input to a later stage. Write them to
   live in the repo and be re-read by future you (and by the agent team in
   stages 7–8). Sloppy, vague, or missing artifacts silently corrupt every
   downstream stage.

## First thing, every session: locate yourself

Before anything else, find out where the project is in the pipeline. Do not
assume you are starting fresh.

1. Look for `docs/STATE.md` at the project root.
   - **It exists** → read it. It tells you the current stage, which gates have
     been passed, and what is pending. Resume from there. Then skim only the
     artifacts relevant to the current stage (do not re-read everything).
   - **It does not exist** → this is a zero project. Scaffold the workflow first
     (see *Scaffolding a new project* below), then begin Stage 1.
2. Announce where you are: *"You're in Stage N (<name>). Last gate passed: X.
   Next up: Y."* Keep the user oriented — this pipeline spans many sessions.
3. **Check for a skip.** If the user is asking you to work on a stage *later*
   than the current one in `docs/STATE.md` (or a later stage's artifacts don't
   have their upstream prerequisites), don't jump there. Name the gap and steer
   back to the earliest incomplete stage — see *Stay on the rails* below.

`docs/STATE.md` is the heartbeat. `docs/GATES.md` is the gate ledger. Together
they are the source of truth for "where are we." Keep both current.

## How to run any stage — the universal loop

Every stage, regardless of which, follows the same five-beat loop. Read the
stage's reference file for the specifics, but the rhythm is always this:

1. **Orient.** Read the stage's reference (`references/<n>-<stage>.md`) and the
   upstream artifacts it consumes (named in that file's *Inputs*). Confirm the
   prior gate was actually passed.
2. **Discover capabilities.** Before hand-rolling, check what tools/skills fit
   this stage (web search, deep-research, Figma, Playwright, brainstorming,
   frontend-design, Workflow fan-out). The reference file routes you. Prefer a
   proven capability over reinventing it.
3. **Execute (orchestrate, don't solo).** Delegate fan-out work to subagents —
   one per competitor, one per provider runbook, one per feature slice. You
   integrate and verify their output; you don't do the volume yourself.
4. **Write artifacts.** Produce the stage's deliverables into `docs/<stage>/`
   using the templates in `assets/templates/deliverables/`. Artifacts are
   contracts: complete, concrete, in English.
5. **Reach the gate.** Check the stage against its Definition of Done. Present
   the result and the decision the human must make. **Stop. Wait for approval.**
   Only after explicit approval: record it in `docs/GATES.md`, advance
   `docs/STATE.md`, and move to the next stage.

## The gate protocol

A gate is a hard stop where a human decides. When you reach one:

- Summarize what the stage produced (link the artifacts) in a few lines.
- State the **specific decision(s)** you need — and where the stage gives the
  human *choices* (competitor list to curate, N brand directions, stack options
  per layer, providers to approve), present those choices with a clear
  recommendation, not an open-ended question.
- Then **stop and wait.** Do not start the next stage's work, do not write its
  artifacts, do not "get ahead." Getting ahead of a gate is the failure mode
  this whole design exists to prevent.
- On approval: append an entry to `docs/GATES.md` (date, stage, decision, who
  approved), flip the stage to `done` in `docs/STATE.md`, set the next stage to
  `in_progress`, and announce the transition.

When a stage offers the human a *choice between options* (stages 3, 5, 6
especially), generate **N genuinely distinct directions with trade-offs**, lead
with a recommendation, and let the human pick. Do not present one option
disguised as a decision.

## Operating model: Orchestrator-first

The lead agent (you) **always acts as Orchestrator.** You own the plan; you
decompose work and distribute it to specialized subagents; you verify and
integrate. You never write large volumes of output monolithically. This holds
from Stage 1 (a **deep-research workflow per competitor**, each itself fanning
out into many subagents) through Stage 8 (one subagent per feature slice). In
Stage 7 you formalize this into a 15-role team that Stage 8 then runs against.
The fan-out pattern is the default, not the exception — and for heavy research
stages it is **nested**: you dispatch leads, and each lead dispatches its own
workers. Depth comes from layering fan-out, not from one agent working harder.

## Conventions (apply everywhere, no exceptions)

- **Triglot language policy.** Converse with the user in *their* language
  (Portuguese by default here). But **every written artifact — files in `docs/`,
  `CLAUDE.md`, skills, commands, commit messages, code comments — is in
  English.** Identifiers (files, folders, symbols) are English. This keeps the
  knowledge base portable and consistent.
- **Where deliverables live.** Planning artifacts (stages 1–6) live under
  `docs/<stage>/`. Heartbeat and ledger live at `docs/STATE.md` and
  `docs/GATES.md`. The harness (stage 7) and build (stage 8) write to the repo
  root and `.claude/`. The folder map:

  ```
  docs/
    STATE.md  GATES.md
    discovery/  product/  brand/  prototype/  stack/  instrumentation/
  .claude/        # created in Stage 7 (agents, skills, commands, settings, MCP)
  knowledge/      # created in Stage 7 (versioned KB)
  specs/          # created in Stage 8 (per-feature SDD specs)
  CLAUDE.md  HARNESS.md  PROGRESS.md  CHANGELOG.md   # repo root
  ```
- **Lean context, rich knowledge.** Keep root context (`CLAUDE.md`) minimal.
  Push depth into `docs/`, `knowledge/`, skills, and subagent prompts. Never
  inline a 60KB doc into context — point to it and read the relevant slice. This
  applies to how *you* operate too: this SKILL.md is the spine; the per-stage
  references hold the depth. Load a reference only when you enter its stage.
- **Cross-cutting principles** (true in every stage): Orchestrator-first; SDD
  everywhere (`spec → plan → build → verify`); Deploy-first (live from day 1 in
  Stage 8); Gates before progress; Knowledge compounds.

## Scaffolding a new project (zero → ready to run Stage 1)

When `docs/STATE.md` is absent, stand up the skeleton before Stage 1:

```bash
python <skill>/scripts/scaffold_workflow.py <project-root>
```

This creates `docs/` with the stage subfolders, a fresh `docs/STATE.md` (Stage 1
`in_progress`, all others `pending`), and an empty `docs/GATES.md`. If Python is
unavailable, create the structure manually from
`assets/templates/state/STATE.md` and `assets/templates/state/GATES.md`. Confirm
the project's basic identity with the user (one-line idea, target users) and
record it at the top of `docs/STATE.md`, then begin Stage 1.

> Do **not** scaffold the full `.claude/` harness here — that is Stage 7's job,
> and it must be designed against the chosen stack and brand, not guessed
> upfront.

## Stage reference map

Each stage has a detailed playbook. **Read the reference when you enter the
stage** — not before. Each reference expands the *how*, routes to tools, points
at deliverable templates, and defines the stage's gate.

| # | Stage | Reference | Writes to | Gate decision |
|---|-------|-----------|-----------|---------------|
| 1 | Discovery | `references/1-discovery.md` | `docs/discovery/` | Approve competitor list; accept opportunities → Scope |
| 2 | Scope | `references/2-scope.md` | `docs/product/` | Approve MVP cut + differentiator |
| 3 | Brand | `references/3-brand.md` | `docs/brand/` | Pick brand directions (naming, voice, visual) |
| 4 | Prototyping | `references/4-prototyping.md` | `docs/prototype/` | Approve prototype vs PRD |
| 5 | Stack | `references/5-stack.md` | `docs/stack/` | Choose stack per layer |
| 6 | Instrumentation | `references/6-instrumentation.md` | `docs/instrumentation/` | Approve providers; complete `.env` |
| 7 | Harness | `references/7-harness.md` | repo root + `.claude/` | Approve harness design; CI green on hello-world |
| 8 | Vibe Coding | `references/8-vibe-coding.md` | repo (app) + `specs/` | Per-increment review; validate vs success metrics |

## Installing slash commands into the target repo (optional, Stage 7)

During Stage 7 you can install per-stage slash commands into the target repo's
`.claude/commands/` (from `assets/templates/harness/commands/`) so the user can
re-enter any stage with `/discovery`, `/scope`, … `/vibe`. These commands are
thin: they point back at this skill's reference for that stage. Offer this; don't
force it.

## Stay on the rails — complete and continuous

The pipeline is meant to be followed **completely and in order**. It is not an
à-la-carte menu. Two rules keep a run on the rails:

- **Continuous, not stop-and-go.** A gate is a decision point, not an off-ramp.
  The moment a human approves a gate, **flow straight into the next stage** in
  the same session — record the gate, advance `docs/STATE.md`, and begin the next
  stage's loop. Don't make the user re-summon you stage by stage. The gates pace
  the work; they don't fragment it.

- **No skipping ahead.** If the user asks to jump to a *later* stage while
  earlier ones are incomplete (e.g. "just scaffold the harness" on a project with
  no Discovery/Scope/Stack), do not comply with the skip. Building Stage 7 on an
  empty planning base produces a harness wired to decisions that were never made.
  Instead: check `docs/STATE.md` and the `docs/` artifacts, name exactly which
  upstream stages are missing, and steer the user back to the **earliest
  incomplete stage** — offer to start/resume from there and carry the flow
  forward continuously. Be helpful about it, but hold the line: the value of this
  pipeline is that each stage stands on real upstream work.

Starting a brand-new project at **Stage 1** and doing that first stage is not
skipping — that's the front door, and continuing from there is exactly the point.
What you refuse is *parachuting past* undone stages into the middle or end.
