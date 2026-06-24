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

## Right-size by stakes — one pipeline, three depths

This pipeline was designed for a serious greenfield product, but it must not pour
enterprise machinery into a weekend spike — that mismatch is the #1 reason a
generic pipeline gets abandoned. A single **stakes** tier, captured at scaffold
time and stored in `docs/STATE.md`, dials the depth of every stage:

| Stakes | Discovery | Brand | Stack/Arch | Harness (7) | Build (8) |
|--------|-----------|-------|-----------|-------------|-----------|
| `throwaway` | quick scan of 1–3 references, **no** deep fan-out | skip / a few tokens + a11y floor | minimal, sane defaults | skip, or a tiny core (Orchestrator + Builder + Reviewer) | ship fast, light gates |
| `mvp` | 2–4 direct rivals deep, the rest light | full but batched; design standards confirmed | full, justified | core team + the roles this project actually needs | SDD loop, deploy-first |
| `platform` | full nested deep research | full + perf budgets | full + ADRs | full harness, all warranted roles | full gates + post-launch |

Each stage's reference says how it flexes for the tier. **The full maximal
pipeline is the `platform` setting — never the unconditional default.** When
unsure, ask the user to confirm the tier rather than assuming big.

## First thing, every session: locate yourself

Before anything else, find out where the project is in the pipeline. Do not
assume you are starting fresh.

1. Look at the project root.
   - **`docs/STATE.md` exists** → read it. It names the current stage, the stakes
     tier, which gates passed, and what's pending. Resume from there; skim only
     the artifacts relevant to the current stage. Before acting, **reconcile**:
     cross-check `docs/STATE.md` against `docs/GATES.md` and the real `docs/`
     tree — if they disagree, durable evidence (actual files and ledger entries)
     wins over a stale header, and you fix the header.
   - **No `docs/STATE.md` and the repo is empty** → a true zero project. Scaffold
     the workflow (see *Scaffolding a new project*), then begin Stage 1.
   - **No `docs/STATE.md` but the repo is NOT empty** (it has code, a manifest,
     `.git`, an existing `.claude/` or CI) → a **brownfield** project. Don't treat
     it as zero, and don't clobber anything. See *Working in an existing repo*.
2. Announce where you are: *"You're in Stage N (<name>), stakes: <tier>. Last
   gate: X. Next: Y."* Keep the user oriented — this spans many sessions.
3. **Handle entry intent.** If the user asks to work on a stage other than the
   current one, neither blindly comply nor blindly refuse — apply *Stay on the
   rails*: support legitimate entries (brownfield, already-have-artifacts, a
   `throwaway` scope-down) with a one-line caveat; refuse only a *hollow* skip
   onto missing upstream work, and steer back.

`docs/STATE.md` is the heartbeat. `docs/GATES.md` is the gate ledger. Together
they are the source of truth for "where are we." Keep both current. They're
append-only and merge-friendly by design, so on a **shared repo with several
people**, reconcile on pull and let each gate entry name *who* approved — the
ledger is the team's shared truth, not one operator's memory.

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
- On approval: append an entry to `docs/GATES.md` — and a gate is only *passed*
  once that entry **quotes (or faithfully paraphrases, with a timestamp) the
  user's actual approval words.** Don't self-attest a gate you weren't granted:
  you propose, the human grants, the ledger records *their* decision. Then flip
  the stage to `done` in `docs/STATE.md`, set the next to `in_progress`, and
  announce the transition.
- **Verification gates are evidence, not assertion.** Where a gate claims
  something ran green (CI, a complete `.env`, a passing test), it must rest on
  *actual output you ran and saw* — and a "CI green" gate needs a test that
  genuinely exercises the code, not a vacuous placeholder. The whole safety model
  rests on the ledger and these checks being honest, so never fabricate either.

When a stage offers the human a *choice between options* (stages 3, 5, 6
especially), generate **N genuinely distinct directions with trade-offs**, lead
with a recommendation, and let the human pick. Do not present one option
disguised as a decision.

## When a gate must re-open — pivots and late learning

The pipeline flows forward, but real projects learn late: Stack may reveal the
Scope is infeasible, Instrumentation may kill a feature on cost, the build may
falsify an assumption the PRD rested on. When a *later* stage invalidates an
*earlier* approved gate, don't silently patch around it and don't plow on — that
is how a project ends up shipping something nobody actually approved.

Instead: **stop, name what changed, and re-open the affected gate.** Record it in
`docs/GATES.md` as a re-opening (the new evidence that forced it, the prior
decision it overturns), update the upstream artifact, and **cascade** — any
downstream artifact that leaned on the overturned decision is flagged stale and
revisited. Then get the human's re-approval before continuing. A re-opened gate
is normal and healthy; a silently-contradicted one is exactly the corruption the
ledger exists to prevent.

## Sad paths — failures, blocks, and thin environments

Things go wrong mid-stage, and how you handle the sad path is where trust is won
or lost. One rule sits under all of it: **a gap is reported, never fabricated.**

- **A fan-out worker fails, times out, or returns garbage.** Retry or replace it.
  If a slice genuinely can't be completed, mark that part *partial / unverified*
  in the artifact and flag it at the gate — never invent plausible content to
  paper over the hole.
- **An external step is blocked** (a provider signup that needs the human, access
  you don't have). Set the stage or sub-task to `blocked` in `docs/STATE.md`,
  state precisely what you need, and stop — don't fake past it.
- **The environment is thin.** Degrade gracefully and *say which rung you're on*:

  | Missing | Degrade to |
  |---------|-----------|
  | No subagents / Workflow | run the fan-out serially and smaller |
  | No web access | mark research `*inferred*`, lean on the user for facts |
  | No Figma | prototype in code, or as a described spec |
  | No hosted CI / deploy target | a green **local** test run + a documented deploy plan counts as verified — `verified` ≠ `hosted-CI-green` |
  | Weaker model | treat DoD checklists as presence checks; warn that depth may be shallow |
  | A routed skill/provider absent or renamed | use the fallback named in the reference, or the closest equivalent — routed names are suggestions to verify at use, not guarantees |

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

But fan-out is **expensive** — nested deep research can spin up dozens to
hundreds of subagents. Treat depth as a dial, not a default: scale it to the
project's stakes (see *Right-size by stakes*), cap it sensibly, and surface a
rough token/time cost at the relevant checkpoint *before* you spend it, so the
human opts in with eyes open. Depth that no one reads before the next gate is
just burned budget.

**Hard return contract for workers.** A subagent's memory is siloed, and its raw
output is the most common way junk floods the lead's window — so every fan-out
worker **writes its bulk output to a file path and returns only a short digest (a
paragraph or two) + that path + a pass/fail verdict.** The conductor reads the
path when it needs the detail; the transcript stays flat. Durable state flows
through shared files, never through what a worker "remembers".

## Conventions (apply everywhere, no exceptions)

- **Language policy.** Converse with the user in *their* language — detect it
  from how they write to you, or ask once at the start, and record it in
  `docs/STATE.md` (`conversation_language`). But **every written artifact — files
  in `docs/`, `CLAUDE.md`, skills, commands, commit messages, code comments — is
  in English**, and identifiers are English, so the knowledge base stays
  portable. (This is the *internal* rule. *User-facing product copy* follows the
  product's market language, decided in Brand — keep the two separate.)
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
- **Context budget & placement.** Treat the context window as a *depletable
  budget*, not free space: reliability decays with how many tokens are live (the
  trustworthy working set is a fraction of the advertised window), so keep each
  stage's working set lean and never let one thread grow unbounded. Fight
  *lost-in-the-middle* — put the **active gate/spec at the top** of a stage or
  subagent prompt and **repeat the key decision at the bottom**; keep the most
  recent tool results as a "hot tail" and let older, re-fetchable ones fall away.
- **Cheapest lever first when context fills.** Manage it in this order: (1) push
  durable facts to **files** (STATE/GATES/knowledge/specs), (2) **isolate** heavy
  work in a subagent that returns only a digest, (3) **prune** re-fetchable tool
  results (large file reads, grep dumps, build logs) once their conclusion is
  recorded, and only as a **last resort** (4) summarize/compact — and even then
  only at a gate safe-point, never mid-increment, writing the summary straight
  back into STATE.md. The write-barrier under all of it: **never drop a tool
  result until the conclusion it supports is persisted to a file** — crystallize
  before you clear.
- **Cache-friendly prompts.** Put the *stable* part first (the skill, the
  pipeline invariants, the tool set) and the *volatile* part last (current stage,
  latest results); keep timestamps, run-ids, and re-serialized JSON out of the
  stable prefix, so this long, repetitive pipeline keeps hitting the prompt cache
  instead of paying full price every turn.
- **Cross-cutting principles** (true in every stage): Orchestrator-first; SDD
  everywhere (`spec → plan → build → verify`); Deploy-first (live from day 1 in
  Stage 8, where the stakes warrant it); Gates before progress; Knowledge
  compounds. And in the build half specifically — the harness is
  **self-improving** (each increment's learnings feed `knowledge/` and refine the
  agents/prompts), execution is **loop-driven** (build → verify → learn → refine,
  running autonomously *between* gates), and the agent team is **dynamic** (the 15
  roles are a seed that Stage 7 specializes to the project and Stage 8 grows on
  demand). Stages 7–8 define these mechanisms; their autonomy always halts at the
  increment's review gate.

## Scaffolding a new project (zero → ready to run Stage 1)

When the repo is empty and `docs/STATE.md` is absent, stand up the skeleton
before Stage 1. First capture three things from the user (ask once, briefly):
the **one-line idea + target users**; the **stakes tier** (`throwaway` | `mvp` |
`platform` — default `mvp` and say so if unsure); and the **conversation
language**.

Then run the scaffold script. It lives in *this skill's own directory* — the file
you are reading is `<skill>/SKILL.md`, so the script is at
`<skill>/scripts/scaffold_workflow.py`; if you can't resolve that path, just
create the structure by hand from `assets/templates/state/`:

```bash
python <skill>/scripts/scaffold_workflow.py <project-root> \
  --idea "<one-line idea>" --stakes <throwaway|mvp|platform> --lang <language>
```

This creates `docs/` with the stage subfolders, a `docs/STATE.md` seeded with the
idea, stakes, and language (Stage 1 `in_progress`, the rest `pending`), and an
empty `docs/GATES.md`. The script never overwrites an existing STATE.md/GATES.md.
Then begin Stage 1.

> Do **not** scaffold the `.claude/` harness here — that's Stage 7's job,
> designed against the chosen stack and brand, not guessed upfront.

## Stage reference map

Each stage has a detailed playbook. **Read the reference when you enter the
stage** — not before. Each reference expands the *how*, routes to tools, points
at deliverable templates, and defines the stage's gate.

| # | Stage | Reference | Writes to | Gate decision |
|---|-------|-----------|-----------|---------------|
| 1 | Discovery | `references/1-discovery.md` | `docs/discovery/` | Approve competitor list; accept opportunities → Scope |
| 2 | Scope | `references/2-scope.md` | `docs/product/` | Approve MVP cut + differentiator |
| 3 | Brand | `references/3-brand.md` | `docs/brand/` | Pick brand directions (naming, voice, visual); confirm design standards |
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

- **No building onto a hollow base.** The thing to prevent is building a *later*
  stage on planning that was never done — scaffolding the harness (Stage 7) on a
  project with no Scope or Stack. If the upstream artifacts a stage genuinely
  needs don't exist, don't fabricate them by skipping: name exactly what's
  missing, state the concrete risk of proceeding anyway, and steer to the
  earliest real gap. Hold *that* line — it's the core value.

  But distinguish a *hollow skip* from a **legitimate entry**, and support the
  legitimate ones with at most a one-line caveat — don't argue with a user who
  has a real reason (that's the fastest way to get uninstalled):
  - **Brownfield / existing repo** — there's already code, a stack, maybe a PRD
    or brand. Adopt it (see *Working in an existing repo*), don't refuse.
  - **Already-have-artifacts** — the user did upstream work elsewhere (a Figma
    prototype, a Linear PRD, a chosen stack). Map those onto the `docs/` stages
    as done-by-import with provenance, then proceed.
  - **Intentional scope-down** — a `throwaway` spike may legitimately skip Brand,
    deep Discovery, or the full harness. Honor it; flag the debt; move on.

  The failure mode is *silent* building on nothing. A warned, user-confirmed entry
  on real (or imported) ground is exactly what a helpful conductor does.

Starting a brand-new project at **Stage 1** is the front door, not a skip;
continuing from there is the point. What you refuse is *silently* parachuting onto
planning that doesn't exist.

## Working in an existing repo (brownfield)

A non-empty repo with no `docs/STATE.md` is a brownfield adoption, not a zero
project. Two unbreakable rules:

1. **Never clobber.** An existing `CLAUDE.md`, `.claude/`, CI config, or app
   config is reconciled or left alone — never overwritten. Ask before touching
   anything that's already there. (The scaffold script is already idempotent for
   STATE/GATES; extend that instinct to everything.)
2. **Ingest before you plan.** Read the manifest/lockfiles, the schema, and any
   existing PRD/brand/stack/design docs. Map what exists onto the `docs/` stages
   as *done-by-import* (record provenance in `docs/STATE.md` and a `docs/GATES.md`
   note), then enter the pipeline at the earliest stage that's genuinely missing —
   a legitimate mid-pipeline entry, not a skip.

For a rebuild/migration, add data-migration and cutover to the build plan, and
treat the live system's users as a constraint (no reckless deploy-first).

## When NOT to use this skill / non-goals

Be honest about fit so a wrong-fit user doesn't commit before discovering the
mismatch:

- **Not a single-task tool.** A bug fix, adding one feature to a mature app, a
  one-off competitor report, or "set up CI on my repo" is better done directly —
  this skill is for taking a *project* through the pipeline. If a request is
  clearly a one-shot task on an existing system, say so and offer the direct path
  (or brownfield adoption if they genuinely want the full process).
- **Not a logo/asset generator** — Brand delivers direction + tokens, not art.
- **Not ceremony for a throwaway** — if someone just wants to hack, point them at
  building directly, or run the deliberately-thin `throwaway` tier.

It still triggers on loose "I have an idea, take it to an MVP" phrasing — that's
the target. The non-goals above are where you redirect instead of running the
whole machine.
