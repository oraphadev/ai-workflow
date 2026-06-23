# AI Workflow — idea to deployed MVP, gate by gate

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Skills CLI](https://img.shields.io/badge/skills.sh-oraphadev%2Fai--workflow-black)](https://skills.sh/oraphadev/ai-workflow)
[![Made for Claude Code](https://img.shields.io/badge/made%20for-Claude%20Code-d97757)](https://claude.com/claude-code)

An agent skill that takes a project from an **empty directory to a deployed MVP** through one disciplined, resumable pipeline — research the market, specify the product, design the brand, choose the stack, provision the services, build the agent harness, and only then write code.

```bash
npx skills add oraphadev/ai-workflow --agent claude-code
```

<sub>Diagram source: [`assets/ai-workflow.excalidraw`](assets/ai-workflow.excalidraw) · interactive: [`assets/ai-workflow.html`](assets/ai-workflow.html)</sub>

```
1 Discovery → 2 Scope → 3 Brand → 4 Prototyping → 5 Stack → 6 Instrumentation → 7 Harness → 8 Vibe Coding
└──────────────────── planning (1–6) ────────────────────┘   └─ harness (7) ─┘  └─ build (8) ─┘
```

## Why

Vibe coding from zero fails for two reasons: the model invents what nobody specified, and it builds before there's a machine that keeps the build consistent. AI Workflow answers both with a **fixed, ordered pipeline**. Each of the 8 stages consumes the versioned artifacts of the ones before it, so nothing downstream rests on a decision that was never made. The planning stages (1–6) write durable artifacts into the repo; stage 7 turns those artifacts into a living Claude Code harness; stage 8 builds the product inside that harness, deploy-first.

The skill is an **orchestrator**, not a code generator. It plans, delegates to specialized subagents, verifies, and — critically — **stops at human gates**. It never barrels through eight stages in one shot, and it never lets you parachute into a late stage while earlier ones are undone.

## Two laws

1. **State machine with human gates.** Almost every stage ends where a human must decide — the competitor list, the MVP cut, a brand direction, the stack, the providers. The skill *proposes, then stops and waits.* Each stage's Definition of Done is the gate to the next. Approvals are recorded in `docs/GATES.md`; an unrecorded gate is an unpassed gate.

2. **Complete and continuous, no skipping.** The pipeline runs in order, fully. After a gate is approved it flows straight into the next stage — no re-summoning stage by stage. And if you ask it to jump ahead (e.g. *"just scaffold the harness"*) while earlier stages are missing, it names the gaps and steers you back to the earliest one instead of building on an empty base.

## How it works

| # | Stage | Produces | What happens |
|---|-------|----------|--------------|
| 1 | **Discovery** | `docs/discovery/` | Each competitor is its own **deep-research workflow** that fans out into many subagents — a 360° business panorama (9 dimensions) + a route-by-route map of the product. Consolidated into a `SUMMARY.md` of patterns, a competitor×feature matrix, and actionable opportunities. |
| 2 | **Scope** | `docs/product/` | Agent-led brainstorming converges the product: value prop, JTBD personas, the MVP cut by Impact×Effort, success metrics, and a `PRD.md` of user stories + acceptance criteria. |
| 3 | **Brand** | `docs/brand/` | Naming, voice & tone, a complete visual identity spec, and **W3C design tokens** (`design-tokens.json`) — stack-agnostic, ready to consume. Direction, not a generated logo. |
| 4 | **Prototyping** | `docs/prototype/` | All MVP screens materialized in the best-fit tool (Figma, code, …), every relevant state covered, validated against the PRD. |
| 5 | **Stack** | `docs/stack/` | Frontend, backend, data, auth, infra chosen per layer with justified trade-offs, plus the architecture: diagram + data model + folder structure + data flow. |
| 6 | **Instrumentation** | `docs/instrumentation/` + `.env` | Every external service derived from features + stack, providers recommended with cost, provisioned via CLI or per-service runbooks, ending in a complete, working `.env` (gitignored) + documented `.env.example`. |
| 7 | **Harness** | repo root + `.claude/` | The execution machine for *this* project: a lean `CLAUDE.md`, a 15-role agent team, slash commands, a versioned knowledge base, a code graph, tests + CI, and quality gates — green on a hello-world before it's done. |
| 8 | **Vibe Coding** | the product | The Orchestrator distributes work to the team; each feature flows `spec → plan → build → verify` with gates; deploy-first, vertical slices, validated against success metrics. |

### Core ideas

- **Artifacts are contracts.** Every deliverable is the literal input to a later stage. All progress lives under `docs/`; `docs/STATE.md` is the heartbeat and `docs/GATES.md` is the approval ledger. Any new session reads them and knows exactly where the project is — close the terminal whenever you want.
- **Orchestrator-first.** The lead never codes monolithically. It decomposes, delegates to subagents, verifies, integrates — from Discovery's nested fan-out to Vibe Coding's per-slice team.
- **Lean context, rich knowledge.** The root context (`CLAUDE.md`) stays minimal; depth is pushed into the knowledge base, skills, and subagent prompts — the spine here, the depth in per-stage references.
- **Triglot.** It converses in your language but writes every artifact in English, so the knowledge base stays portable.

## Installation

```bash
npx skills add oraphadev/ai-workflow --agent claude-code
```

Works with any agent supported by the [Skills CLI](https://skills.sh/) — swap the `--agent` flag accordingly.

## Usage

Start a session in an empty project directory and say something like:

```text
Tenho uma ideia: um app de gestão financeira pra MEIs no Brasil. Quero começar
do zero seguindo o workflow completo, do mercado ao MVP. Bora.
```

You don't need to name the skill — *"I have an idea for a Calendly competitor for barbershops, help me take it from market research to an MVP"* triggers it too. You can also enter at a single stage (*"just do a deep competitor research first"*) — Discovery is the front door — and continue from there.

The skill then:

1. **Locates the project.** Reads `docs/STATE.md` if it exists (and resumes), or scaffolds the planning tree + heartbeat for a zero project.
2. **Runs one stage at a time**, delegating fan-out work to subagents and writing each deliverable into `docs/<stage>/`.
3. **Stops at each gate**, presents the decision with a recommendation, records your approval, and flows into the next stage.

### What it does — and deliberately doesn't — create

The zero-project bootstrap scaffolds **only** the planning structure: `docs/<stage>/` folders plus `docs/STATE.md` and `docs/GATES.md`. It does **not** generate the `.claude/` harness up front — that is stage 7's job, designed against the chosen stack and brand, not guessed. Empty templates would be false state; an artifact exists only once its stage produced it.

## Recommended setup

Works with whatever the session provides, but shines with:

- **Web access** (search/fetch or browser tooling) — Discovery refuses to research from model memory.
- **Subagent / workflow support** — Discovery and the build run as parallel, sometimes nested, subagent fan-outs.
- **Figma MCP** — for the Prototyping stage (and materializing the visual identity).
- **A skill-discovery skill** (e.g. [find-skills](https://skills.sh/)) — each stage routes to specialized skills instead of hand-rolling.

## Repository layout

```
.
├── README.md                          ← you are here
├── LICENSE                            ← MIT
├── assets/
│   ├── ai-workflow.excalidraw         ← editable diagram source
│   └── ai-workflow.html               ← interactive, clickable pipeline
└── skills/
    └── ai-workflow/
        ├── SKILL.md                   ← the conductor: state machine, gates, conventions, routing
        ├── references/                ← 8 per-stage playbooks (read on entering each stage)
        ├── assets/templates/          ← deliverable templates, the 15-role harness team, state files
        └── scripts/                   ← scaffold_workflow.py (zero → docs/ + heartbeat)
```

## License

MIT.
