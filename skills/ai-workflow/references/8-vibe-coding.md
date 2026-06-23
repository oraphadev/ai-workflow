# Stage 8 — Vibe Coding

> Build the product feature by feature on the harness — the Orchestrator distributes work to the team, SDD drives every increment, and verification gates guard each step.

## Objective

Turn the plans into a running, deployed application. The shape of this stage is fixed by three forces working together: the **Orchestrator distributes** — it does not code monolithically, it fans work out to the 15-role team built in Stage 7; **SDD drives** — every increment starts from an approved, versioned spec, no code without one; and **gates guard** — tests, lint, and type-check must pass and a code review must clear before any increment integrates.

You are not "writing the app" in one long session. You are running a loop, many times, with the harness doing the parallel execution and you keeping the plan, the gates, and the deployment honest. Each increment's loop runs **autonomously between gates** — spec, plan, distribute, build, verify, learn, refine, iterating until the slice's acceptance criteria are met and the verification gates pass — then halts at the human review gate. The skeleton is live from day one where the stakes warrant it; every finished slice ships to that environment. And the machine sharpens as it runs: each increment feeds learnings back into `knowledge/` and refines the agents, and when a slice reveals a need no current agent covers, you mint a new specialist for it.

## Inputs

Everything from Stages 1–7 converges here — this is the stage that consumes all of it:

- `docs/product/` — the user stories and MVP→v1 phasing that order the build.
- `docs/prototype/` — the screens and flows each vertical slice realizes.
- `docs/brand/` — design tokens to wire into the foundation (not re-decide).
- `docs/stack/` — the chosen frameworks, runtime, and deploy target.
- `docs/instrumentation/` — the live services and the complete `.env` features call at runtime.
- The **HARNESS** from Stage 7 — the team definitions, the dispatch wiring, the CI/deploy pipeline, and the two improvement mechanisms it ships: `/harness-improve` (ratify refinements to agent prompts and skills) and `/add-specialist-agent` (mint a new project-specialized agent on demand).
- `docs/STATE.md` — read the **stakes tier** here first; it sets how heavy this stage runs (see *Flex by stakes* below).

Before writing a line of feature code, confirm two things from Stage 7: the **Harness gate passed** (the team is wired and dispatchable) and **CI is green on the hello-world** (the skeleton builds, deploys, and the pipeline is real, not aspirational). If CI has never gone green, you have no place to ship to — fix that first. Building features on an unverified pipeline means discovering the pipeline is broken after ten slices are stacked on it.

## Capability routing

This stage *runs the harness*. The Orchestrator dispatches the 15-role subagents — Frontend, Backend, QA, and the rest — per slice, fanning out the work that a slice naturally parallelizes (UI against API against migration against tests). Lean on that fan-out: a vertical slice is exactly the unit that splits cleanly across roles.

Route the SDD backbone to the superpowers skills rather than improvising it:

- **`writing-plans`** — turn the increment's spec into a step-by-step build plan with checkpoints.
- **`subagent-driven-development`** / **`executing-plans`** — distribute the plan's independent tasks across the team and execute them.
- **`test-driven-development`** — drive each increment test-first, so the verification gate has something to pass.
- **`requesting-code-review`** + **`receiving-code-review`** — the review gate before integrate; request rigorously, receive without performative agreement.
- **`verification-before-completion`** — before declaring any increment done, run the gates and confirm output. Evidence before assertion, every time.

And lean on the two Stage-7 harness commands as the loop runs:

- **`/harness-improve`** — propose refinements to agent prompts and skills from what an increment taught, applied once the human ratifies them at the review gate.
- **`/add-specialist-agent`** — define, register, and dispatch a new project-specialized agent when a slice surfaces work no current role covers.

The spec → plan → build → verify → learn → refine flow is the same loop repeated; the skills above are its named stages. The loop is autonomous between gates and stops at the human review gate.

## The build loop

Every increment runs the same loop — and it is a **loop, not a one-shot pass**. The unit is one vertical slice (or the foundation, for the first pass). Steps 1–6 run **autonomously between gates**: the team iterates spec → plan → distribute → build → verify → learn → refine without stopping for the human, looping back on each failure, until the slice's acceptance criteria are met and every verification gate is green. *Then* the autonomy halts at the review gate (step 7) — the human ratifies, and only then does the next increment begin. Do not skip steps to save a round trip — the steps are the value.

1. **Spec.** The Orchestrator generates or approves a versioned SDD spec in `specs/` for this slice, fed by the PRD and the relevant user story. The spec states the behavior, the acceptance criteria, and the contract (data shapes, endpoints, UI states). No code begins without an approved spec — this is what keeps a parallel team from diverging.
2. **Plan.** Via `writing-plans`, decompose the spec into ordered, checkpointed tasks and identify which tasks are independent enough to parallelize.
3. **Distribute.** The Orchestrator fans the plan out to the team — Backend takes the endpoint and migration, Frontend takes the screen against the agreed contract, QA prepares the acceptance tests. `subagent-driven-development` is the mechanism. If the slice needs work no current role covers, mint a specialist first (see *Dynamic agents* below) rather than forcing a generic role onto unfamiliar ground.
4. **Build.** The team builds, test-first. Each role writes tests then implementation for its part, working against the shared contract from the spec.
5. **Verify (the gates).** Before anything integrates, the increment must pass concrete gates — make them non-negotiable and automated. And the evidence must be *real*: a slice is "done" only on actual test/CI output you ran and saw, exercising the code for real — never a claim, and never a vacuous placeholder test that passes without touching the behavior.
   - **Tests** — unit and the slice's acceptance tests, genuinely exercising the slice, green.
   - **Lint** — zero new violations.
   - **Type-check** — clean (`tsc --noEmit` or the stack's equivalent).
   - The build compiles. Run these via `verification-before-completion` and read the actual output; a slice is not done because it "should" pass.
6. **Learn → refine (close the loop).** Two outcomes feed back here. If a gate failed or the acceptance criteria aren't met, loop back — fix and re-verify, iterating until green; you do not integrate a broken slice. If the slice is green, harvest what it taught: append learnings to `knowledge/` (an ADR, a pattern, an anti-pattern) and stage any prompt/skill refinements via `/harness-improve`. **The loop's exit condition:** the slice meets its acceptance criteria *and* every verification gate is green. Until then, keep iterating; once met, stop and present at the review gate.
7. **Review, integrate, deploy.** Request review (`requesting-code-review`) against the spec's acceptance criteria with the gate evidence in hand. This is the human checkpoint — the autonomous loop halts here; the slice does not integrate on a self-declared pass. The human also ratifies the increment's staged refinements (the `knowledge/` additions and any `/harness-improve` proposals). On a clean review, merge into the main line; with the skeleton already live, CI ships the merged slice to the running environment. Then the next increment's loop begins — on a slightly sharper machine than the last.

The verify-and-learn loop is what makes the increment converge; the review gate is where the human re-enters. Speed comes from the autonomy between gates, safety from the gate at the end of each loop.

## Build order

Sequence the work so there is always something live and the risky/foundational pieces come first.

**Foundation first.** Before any feature, stand up the shared substrate every slice will lean on:

- **Auth** — the session/identity layer, wired to the provider from Stage 6.
- **Layout** — the app shell, navigation, and routing skeleton.
- **Design tokens** — `docs/brand/` tokens wired into the styling system, so features inherit the look rather than reinventing it.
- **Base infra** — database connection and the first migration, env loading from `.env`, error tracking, the shared component primitives.
- **CI deploy** — confirmed green and actually deploying (this came live in Stage 7; verify it still is).

**Deploy on day 1.** For greenfield `mvp` and `platform` projects this is the default: the walking skeleton — auth, an empty shell, one trivial authenticated page — goes to the live environment on the first day, before any feature. This forces the deploy path to be real early, when it is cheap to fix, and gives every subsequent slice a true target to ship to. But "live from day 1" is not a blanket rule. For a brownfield app with live users, or a regulated product without the right gates in place, you don't push to production on day 1 — there, the bar becomes **shippable/releasable**: each slice is built to a deploy-ready, gated state and released deliberately rather than auto-live. Read the stakes and the context (see *Flex by stakes*) and pick the right reading of deploy-first for the project in front of you.

**Features as vertical slices.** Each feature is built top-to-bottom — UI through API through data — as a single shippable unit that delivers a complete user story, not a horizontal layer that does nothing until three other layers land. A vertical slice is independently verifiable, independently deployable, and the natural fan-out unit for the team. Order the slices by the MVP→v1 phasing from `docs/product/`: MVP-critical stories first, v1 niceties last.

## Flex by stakes

Read the **stakes tier** from `docs/STATE.md` and run the stage at the matching weight. The loop is the same shape at every tier; what changes is how heavy the gates are and how the increment ships.

- **`throwaway`** — ship fast. Keep the loop, but run light gates (tests where they earn their keep, not a full pyramid), and treat deploy as optional rather than required. The point is to learn quickly; don't pour `platform` ceremony into a spike.
- **`mvp`** — run the full SDD loop and deploy-first. Every slice goes through spec → plan → build → verify → learn → refine with the real gates, and the live environment grows one verified slice at a time.
- **`platform`** — full gates plus a **post-launch note**: when the MVP is in, add the operational layer the build doesn't cover on its own — monitoring and alerting wired, a runbook for the live service, and a rollback path that's been thought through (and ideally rehearsed). A platform isn't done at "it deploys"; it's done at "it can be operated."

When the tier and the context disagree (a `mvp`-tier rebuild that nonetheless has live users), let the context tighten the gates — the tier sets the floor, the live system sets the constraint.

## Self-improvement — the machine sharpens each increment

The harness is not static across the build; it gets better as it runs. At the learn step of each increment, harvest what the slice taught into the versioned `knowledge/` base — an ADR for a decision made, a pattern that worked, an anti-pattern to avoid, a learning for the next slice — so the next increment starts from more than the last. And propose concrete refinements to the agents themselves: if the Backend agent kept missing a stack idiom, or a skill's procedure proved too loose, draft the prompt or skill edit via `/harness-improve` (the Stage-7 mechanism). These refinements are **staged, not silently applied** — they ride along to the review gate and take effect once the human ratifies them. The result is compounding: by the tenth slice the team is measurably sharper than at the first, because every increment fed it.

## Dynamic agents — define a specialist when a slice needs one

The 15-role roster from Stage 7 is a seed, not a ceiling. When a slice surfaces work no current agent covers — a payments integration with its own correctness rules, a search-relevance problem, a migration pattern the generic Data agent doesn't know — don't force a generic role to fumble through unfamiliar work. Instead the Orchestrator **defines a new project-specialized agent on the fly** via the Stage-7 `/add-specialist-agent` mechanism: write its prompt against the actual need and stack, register it in `.claude/agents/`, and dispatch it for the slice. A purpose-built agent does focused, unfamiliar work far better than a generalist stretched to cover it. Like the prompt refinements, a newly minted agent is presented at the review gate so the human sees the team grow.

## Steps

### 1. Break the MVP into an incremental build plan

Read `docs/product/` and lay out the slices in build order following the MVP→v1 phasing. The plan is a sequence of increments — foundation, then each vertical slice — each tied to a user story and a target screen from the prototype. This is the master tracker that `PROGRESS.md` mirrors.

### 2. Build foundation, deploy the skeleton

Build the foundation listed above, wire the brand tokens and `.env`, and push the walking skeleton live through CI. Do not start feature work until the skeleton is deployed and reachable. The day-1 deploy is the single most de-risking move in the stage.

### 3. Run the SDD loop per increment

For each slice, run the full build loop **autonomously between gates**: the Orchestrator generates/approves the spec into `specs/`, plans it, distributes to the team (minting a specialist via `/add-specialist-agent` if the slice needs one), the team builds test-first, verifies on real output, and learns — looping back on any failure until the acceptance criteria are met and the gates are green. Only then does it stop, at the review gate. The spec comes first, always — the PRD feeds the spec, the spec feeds the plan. The loop iterates; it is not a single pass.

### 4. Deploy continuously

For `mvp`/`platform` greenfield with the skeleton live, every completed slice ships to the running environment as it integrates — there is no big-bang release at the end; the app grows in the live environment, one verified slice at a time. For `throwaway`, deploy is optional. For brownfield-with-users or regulated products, "ships" means released through the right gates rather than auto-live. In every reading, a slice that passes its gates and clears review is a slice that's deploy-ready.

### 5. Implement tracking/analytics and wire integrations

As the relevant slices land, implement the planned analytics/tracking events and wire the integrations against the `.env` from Stage 6. Instrumentation is part of the slice that needs it, not a forgotten afterthought — if a checkout slice ships, its analytics ship with it.

### 6. Review, ratify refinements, integrate, advance

Run the review gate where the autonomous loop halted: present the slice with its real gate evidence, and the increment's harvested learnings and any staged agent/skill refinements (`/harness-improve`) or newly minted specialist (`/add-specialist-agent`). On a clean review the human ratifies all of it; integrate, and move to the next increment on a sharper machine. Capture anything learned — a stack quirk, a pattern that worked, a sharp edge — into `knowledge/` so the next slice benefits. Knowledge compounds, and so does the team.

### 7. Validate against success metrics

When the MVP slices are all in, validate the product against the user stories and the success metrics / acceptance criteria from Stage 2. This is the closing check: not "did it build" but "does it do what we said it would, measurably."

## Deliverables

Write to the repo (app code) plus the tracking and spec docs:

```
<repo>/                     # the functional MVP app — shipped at the level the stakes require
specs/                      # per-feature SDD specs, versioned — one per slice
knowledge/                  # appended each increment: ADRs, patterns, anti-patterns, learnings
.claude/agents/             # may grow — specialists minted on demand during the build
PROGRESS.md                 # build tracker: increments done / in-flight / pending
CHANGELOG.md                # incremental record of what shipped each increment
```

Templates live at `assets/templates/deliverables/`:
- `spec.md` — the SDD spec template (behavior, acceptance criteria, contract); copy it into `specs/` per feature and version it.
- `PROGRESS.md` — the build tracker; keep it current as the live state of the plan.
- `CHANGELOG.md` — append an entry per integrated increment.

Keep `specs/` versioned: when a slice's behavior changes, revise its spec rather than letting code drift from an outdated one. The spec is the source of truth the team builds against, so a stale spec is a defect.

## Definition of Done

- [ ] MVP implemented per scope and prototype — every MVP user story has a shipped vertical slice.
- [ ] Foundation (auth, layout, tokens, base infra) in place and the skeleton deployed from day 1.
- [ ] Each feature has an approved, versioned spec in `specs/`; no code shipped without one.
- [ ] Integrations wired against `.env`; planned tracking/analytics implemented.
- [ ] Every integrated increment passed its gates (tests, lint, type-check) on **real, code-exercising output you ran and saw** — no asserted or placeholder passes — and cleared code review.
- [ ] **CI green AND shipped** to the level the stakes/context require — live main line for greenfield `mvp`/`platform`; deploy-ready/released for `throwaway`, brownfield-with-users, or regulated products.
- [ ] Each increment's learnings landed in `knowledge/`, and any agent/skill refinements or new specialists were ratified at the review gate — the harness is sharper than it started.
- [ ] For `platform`: a post-launch note exists (monitoring/alerting, runbook, rollback path).
- [ ] `PROGRESS.md` and `CHANGELOG.md` reflect the actual built state.
- [ ] Features **validated against user stories and success metrics** — not just built, but confirmed to do the job.

## The gate

This stage is different from the others: it has **recurring gates, one per increment**, not a single gate at the end.

**Per-increment checkpoint — code review before integrate.** The autonomous loop runs the increment to a green, criteria-met state on its own, then halts here. Present the slice against its spec's acceptance criteria with the gate evidence — and the evidence must be **real test/CI output you ran and saw**, exercising the code, not a claim and not a placeholder test that passes vacuously. Present alongside it the increment's harvested learnings and any staged refinements (agent/skill edits via `/harness-improve`, or a new specialist via `/add-specialist-agent`) for the human to ratify. Let the review clear before integrating. A slice does not merge on a self-declared pass; the review is a real human checkpoint, repeated every increment. This is what keeps a fast parallel team from quietly accumulating debt — and it is where the human ratifies the machine's self-improvement before it takes effect.

**Final validation — against success metrics.** When the MVP is built, the closing gate is validation against the user stories and success metrics from Stage 2. Present each MVP story as satisfied (with the deployed feature demonstrating it) and each success metric as measurable on the live app. Then stop for the user to confirm the MVP meets scope before the workflow declares done.

Propose, then stop — at each increment's review and at the final validation. The loop is autonomous *between* these gates and halts *at* them: the team iterates to green on its own, the human ratifies, the next increment begins. The gates are the price of moving fast in parallel without shipping something broken to a live environment.
