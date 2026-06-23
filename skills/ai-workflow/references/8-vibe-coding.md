# Stage 8 — Vibe Coding

> Build the product feature by feature on the harness — the Orchestrator distributes work to the team, SDD drives every increment, and verification gates guard each step.

## Objective

Turn the plans into a running, deployed application. The shape of this stage is fixed by three forces working together: the **Orchestrator distributes** — it does not code monolithically, it fans work out to the 15-role team built in Stage 7; **SDD drives** — every increment starts from an approved, versioned spec, no code without one; and **gates guard** — tests, lint, and type-check must pass and a code review must clear before any increment integrates.

You are not "writing the app" in one long session. You are running a loop, many times, with the harness doing the parallel execution and you keeping the plan, the gates, and the deployment honest. The skeleton is live from day one; every finished slice ships to that live environment.

## Inputs

Everything from Stages 1–7 converges here — this is the stage that consumes all of it:

- `docs/product/` — the user stories and MVP→v1 phasing that order the build.
- `docs/prototype/` — the screens and flows each vertical slice realizes.
- `docs/brand/` — design tokens to wire into the foundation (not re-decide).
- `docs/stack/` — the chosen frameworks, runtime, and deploy target.
- `docs/instrumentation/` — the live services and the complete `.env` features call at runtime.
- The **HARNESS** from Stage 7 — the team definitions, the dispatch wiring, and the CI/deploy pipeline.

Before writing a line of feature code, confirm two things from Stage 7: the **Harness gate passed** (the team is wired and dispatchable) and **CI is green on the hello-world** (the skeleton builds, deploys, and the pipeline is real, not aspirational). If CI has never gone green, you have no place to ship to — fix that first. Building features on an unverified pipeline means discovering the pipeline is broken after ten slices are stacked on it.

## Capability routing

This stage *runs the harness*. The Orchestrator dispatches the 15-role subagents — Frontend, Backend, QA, and the rest — per slice, fanning out the work that a slice naturally parallelizes (UI against API against migration against tests). Lean on that fan-out: a vertical slice is exactly the unit that splits cleanly across roles.

Route the SDD backbone to the superpowers skills rather than improvising it:

- **`writing-plans`** — turn the increment's spec into a step-by-step build plan with checkpoints.
- **`subagent-driven-development`** / **`executing-plans`** — distribute the plan's independent tasks across the team and execute them.
- **`test-driven-development`** — drive each increment test-first, so the verification gate has something to pass.
- **`requesting-code-review`** + **`receiving-code-review`** — the review gate before integrate; request rigorously, receive without performative agreement.
- **`verification-before-completion`** — before declaring any increment done, run the gates and confirm output. Evidence before assertion, every time.

The spec → plan → build → verify → review flow is the same loop repeated; the skills above are its named stages.

## The build loop

Every increment runs the same loop. The unit is one vertical slice (or the foundation, for the first pass). Do not skip steps to save a round trip — the steps are the value.

1. **Spec.** The Orchestrator generates or approves a versioned SDD spec in `specs/` for this slice, fed by the PRD and the relevant user story. The spec states the behavior, the acceptance criteria, and the contract (data shapes, endpoints, UI states). No code begins without an approved spec — this is what keeps a parallel team from diverging.
2. **Plan.** Via `writing-plans`, decompose the spec into ordered, checkpointed tasks and identify which tasks are independent enough to parallelize.
3. **Distribute.** The Orchestrator fans the plan out to the team — Backend takes the endpoint and migration, Frontend takes the screen against the agreed contract, QA prepares the acceptance tests. `subagent-driven-development` is the mechanism.
4. **Execute.** The team builds, test-first. Each role writes tests then implementation for its part, working against the shared contract from the spec.
5. **Verify (the gates).** Before anything integrates, the increment must pass concrete gates — make them non-negotiable and automated:
   - **Tests** — unit and the slice's acceptance tests, green.
   - **Lint** — zero new violations.
   - **Type-check** — clean (`tsc --noEmit` or the stack's equivalent).
   - The build compiles. Run these via `verification-before-completion` and read the actual output; a slice is not done because it "should" pass.
6. **Code review.** Request review (`requesting-code-review`) against the spec's acceptance criteria. This is a human checkpoint — the slice does not integrate on a self-declared pass.
7. **Integrate.** Once gates are green and review clears, merge the slice into the main line.
8. **Deploy.** With the skeleton already live, the merged slice ships to the running environment automatically through CI. Then the loop restarts on the next increment.

If a gate fails, you do not integrate — you fix and re-verify. The gate exists precisely to stop a broken slice from contaminating a deployed, working app.

## Build order

Sequence the work so there is always something live and the risky/foundational pieces come first.

**Foundation first.** Before any feature, stand up the shared substrate every slice will lean on:

- **Auth** — the session/identity layer, wired to the provider from Stage 6.
- **Layout** — the app shell, navigation, and routing skeleton.
- **Design tokens** — `docs/brand/` tokens wired into the styling system, so features inherit the look rather than reinventing it.
- **Base infra** — database connection and the first migration, env loading from `.env`, error tracking, the shared component primitives.
- **CI deploy** — confirmed green and actually deploying (this came live in Stage 7; verify it still is).

**Deploy on day 1.** The walking skeleton — auth, an empty shell, one trivial authenticated page — goes to the live environment on the first day, before any feature. This forces the deploy path to be real early, when it is cheap to fix, and gives every subsequent slice a true target to ship to.

**Features as vertical slices.** Each feature is built top-to-bottom — UI through API through data — as a single shippable unit that delivers a complete user story, not a horizontal layer that does nothing until three other layers land. A vertical slice is independently verifiable, independently deployable, and the natural fan-out unit for the team. Order the slices by the MVP→v1 phasing from `docs/product/`: MVP-critical stories first, v1 niceties last.

## Steps

### 1. Break the MVP into an incremental build plan

Read `docs/product/` and lay out the slices in build order following the MVP→v1 phasing. The plan is a sequence of increments — foundation, then each vertical slice — each tied to a user story and a target screen from the prototype. This is the master tracker that `PROGRESS.md` mirrors.

### 2. Build foundation, deploy the skeleton

Build the foundation listed above, wire the brand tokens and `.env`, and push the walking skeleton live through CI. Do not start feature work until the skeleton is deployed and reachable. The day-1 deploy is the single most de-risking move in the stage.

### 3. Run the SDD loop per increment

For each slice, run the full build loop: the Orchestrator generates/approves the spec into `specs/`, plans it, distributes to the team, the team executes test-first, and the verification gates must pass before anything integrates. The spec comes first, always — the PRD feeds the spec, the spec feeds the plan.

### 4. Deploy continuously

With the skeleton live, every completed slice ships to the running environment as it integrates. There is no big-bang release at the end — the app grows in the live environment, one verified slice at a time. A slice that passes its gates and clears review is a slice that deploys.

### 5. Implement tracking/analytics and wire integrations

As the relevant slices land, implement the planned analytics/tracking events and wire the integrations against the `.env` from Stage 6. Instrumentation is part of the slice that needs it, not a forgotten afterthought — if a checkout slice ships, its analytics ship with it.

### 6. Code review, integrate, advance

Run the review gate, integrate on a clean pass, and move to the next increment. Capture anything learned — a stack quirk, a pattern that worked, a sharp edge — back into `knowledge/` so the next slice benefits. Knowledge compounds across increments.

### 7. Validate against success metrics

When the MVP slices are all in, validate the product against the user stories and the success metrics / acceptance criteria from Stage 2. This is the closing check: not "did it build" but "does it do what we said it would, measurably."

## Deliverables

Write to the repo (app code) plus the tracking and spec docs:

```
<repo>/                     # the functional MVP application, deployed from day 1
specs/                      # per-feature SDD specs, versioned — one per slice
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
- [ ] Every integrated increment passed its gates (tests, lint, type-check) and cleared code review.
- [ ] **CI green AND deployed** — the live environment runs the current main line.
- [ ] `PROGRESS.md` and `CHANGELOG.md` reflect the actual built state.
- [ ] Features **validated against user stories and success metrics** — not just built, but confirmed to do the job.

## The gate

This stage is different from the others: it has **recurring gates, one per increment**, not a single gate at the end.

**Per-increment checkpoint — code review before integrate.** Every slice stops at code review before it merges. Present the slice against its spec's acceptance criteria with the gate evidence — tests green, lint clean, type-check clean — and let the review clear before integrating. A slice does not merge on a self-declared pass; the review is a real human checkpoint, repeated every increment. This is what keeps a fast parallel team from quietly accumulating debt.

**Final validation — against success metrics.** When the MVP is built, the closing gate is validation against the user stories and success metrics from Stage 2. Present each MVP story as satisfied (with the deployed feature demonstrating it) and each success metric as measurable on the live app. Then stop for the user to confirm the MVP meets scope before the workflow declares done.

Propose, then stop — at each increment's review and at the final validation. The gates are the price of moving fast in parallel without shipping something broken to a live environment.
