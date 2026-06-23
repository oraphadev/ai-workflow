# Stage 1 — Discovery

> Map the whole arena before choosing a weapon: a panorama of the market and a route-level teardown of the rivals that matter, so opportunities are *found*, not guessed — at a depth the project's stakes actually justify.

## Objective

Build a deep, structured understanding of the space the product wants to enter. Not a vibe-check — a panorama. For each competitor that warrants it you produce a 360º business teardown and a route map of their product, then consolidate everything into a cross-competitor synthesis whose payload is *actionable opportunities*. Scope (Stage 2) reads that synthesis to decide what to actually build. The quality of the MVP cut downstream is bounded by the quality of the gaps you surface here — but depth nobody reads before the MVP cut is just burned budget, so spend it where it pays.

## Flex by stakes

Read the **Stakes** field from `docs/STATE.md` first and let it set the dial for the whole stage (this mirrors *Right-size by stakes* in SKILL.md):

- **`throwaway`** — a quick scan of 1–3 references, **no** deep fan-out. A short opportunities note is the deliverable, not a full panorama.
- **`mvp`** — the **2–4 most important direct rivals** get the deep nested research; indirect/analogous competitors get a light single-pass scan. This is the default shape of the steps below.
- **`platform`** — full nested deep research across the approved set; the soft cap exists mainly to make cost visible, not to hold you back.

When the stakes field is missing or ambiguous, ask the user to confirm the tier rather than defaulting to the heaviest run.

## Inputs

This is the first stage, so there is almost no upstream artifact to inherit — the inputs are the raw idea and the criteria you set with the user:

- **The product idea / hypothesis.** Read it from `docs/STATE.md` (the scaffold records the one-line idea and target users at the top). If it is thin or ambiguous, get one or two clarifying sentences from the user before generating a competitor list — a vague idea yields a noisy list.
- **Competitor-type criteria.** Agree with the user on what counts as a competitor along three axes:
  - *Direct* — same problem, same audience, overlapping solution.
  - *Indirect* — same problem or job-to-be-done, different solution shape.
  - *Analogous* — different market, but a pattern/mechanic/UX worth stealing.
  Knowing which axes matter steers both the candidate list and how widely you cast. Some projects want all three; some only want direct rivals.

Confirm `docs/STATE.md` shows Stage 1 `in_progress`. There is no prior gate to verify here — this is the front door.

## Capability routing

Don't hand-roll research you can delegate to a proven capability. Route by need:

- **`WebSearch` / `WebFetch`** — the workhorses for fast competitor lookup, pricing pages, docs, changelogs, review sites. Use them directly inside a subagent when a question is shallow and singular.
- **`deep-research` skill** — reach for this when a competitor warrants a *fact-checked, multi-source dossier* (real pricing, real positioning, traction signals) rather than a single-page skim. It fans out searches, cross-checks sources, and cites. Prefer it for the heavyweight rivals where being wrong is costly.
- **Nested `Workflow` fan-out — the engine of this stage, reserved for the rivals that matter.** A *deeply researched* competitor is **not** a single subagent; it is its own **deep-research workflow** that fans out into many workers. The orchestration is *three tiers*: you (conductor) dispatch one **competitor lead** per deep-set competitor; each lead in turn dispatches **workers** — one per panorama dimension that warrants depth, a few for route mapping, a few mining reviews / SEO / tech-fingerprint sources — then synthesizes that competitor's artifacts. Depth comes from this layered fan-out, not from one agent skimming ten tabs. But this nested machinery runs **only for the 2–4 most important direct rivals** (the deep set); indirect/analogous competitors get a single light worker, not a sub-workflow. Use the `deep-research` skill to power each deep-set competitor's investigation when web breadth matters.
- **Playwright MCP** (`browser_navigate`, `browser_snapshot`, `browser_take_screenshot`) — optional, for capturing key *public* routes of a competitor when a visual record adds signal (Step 5). `browser_snapshot` gives you the accessibility tree (great for enumerating UI elements and states cheaply); `browser_take_screenshot` gives the pixel record. Don't screenshot everything — only routes where the visual is load-bearing.

## Steps

### 1. Propose a candidate competitor list — then let the user curate it

From the idea and the agreed criteria, generate a candidate list of competitors. Cast wide on the *candidate* list — it's cheaper to cut a name than to miss a category — but mark which ones you'd put in the **deep set** (the 2–4 most important direct rivals that earn the nested fan-out) versus the **light set** (everything else, a single-pass scan). Group candidates by type (direct / indirect / analogous) and add a one-line *why this one* for each, so the user can judge relevance fast.

Apply a **soft default cap of ~6–8 competitors in the deep set**. It's a default, not a wall: the user can raise it right here at the checkpoint. The cap exists because every deep name multiplies into a whole sub-workflow, and depth nobody reads before the MVP cut is waste.

This is a **checkpoint, not a gate** — a lightweight human-in-the-loop before you spend fan-out budget, and the cheapest place to be wrong. When you present it:

- Show the grouped list with the deep/light split and your recommended deep set.
- **Surface the cost you're about to authorize** — a rough token/time estimate of the fan-out, e.g. *"~3 deep rivals × nested deep research ≈ dozens of subagents (plus ~N light scans); roughly tens of minutes and a meaningful token spend."* The user should opt in knowing the size of the bill.
- Ask the user to add/remove/reclassify, move names between the deep and light sets, and raise the cap if they want.

Wait for an approved final list (and its deep/light split) before dispatching anything. Scale the whole proposal to the stakes tier above — a `throwaway` skips this fan-out entirely.

### 2. Fan out — tier the work by importance

Split the approved list into two tracks. The split follows the stakes tier: at `mvp` the deep set is the 2–4 most important direct rivals; at `platform` it's the full approved set; a `throwaway` has no deep set at all.

**Deep set (2–4 direct rivals) — one deep-research *workflow* each.** For each, dispatch a **competitor lead**, not a single do-it-all subagent. Send the leads concurrently; they're independent. Each lead runs a *real* investigation of its one competitor by fanning out its **own** workers, then synthesizes. This is the layer that makes Discovery deep rather than a skim. A good decomposition for each lead:

- **One worker per panorama dimension that warrants depth** — pricing/monetization, business model, detectable tech stack, user sentiment/reviews mining, channels/traction/SEO. Shallow dimensions can be combined, but the money / sentiment / feature dimensions each deserve a dedicated worker so nothing is glossed.
- **Route-mapping workers** — for the key user journeys and the feature surface Scope needs; split a large surface across a few workers so each maps a coherent slice at full granularity (see Step 4 for what's default vs opt-in).
- The lead **synthesizes** its workers' returns into that competitor's `DISCOVERY.md` (9 dimensions) + `ROUTES.md`, tags every unverifiable claim as `*inferred*` and every quantitative claim with a source (see *Anti-fabrication* below), and writes to `docs/discovery/<competitor-name>/`.

**Light set (everyone else) — one single-pass scan each.** Indirect/analogous competitors get *one* worker apiece (or `deep-research` only if a specific one surprises you), capturing the headline dimensions and the journeys worth stealing — not a nested fan-out. Promote a light name to the deep set only if it turns out to be a closer rival than the checkpoint assumed; flag that change to the user since it raises the cost.

Hand each lead/worker the deliverable templates by path so shapes come back uniform — uniformity is what makes the cross-competitor matrix in Step 6 possible. You (the conductor) receive the artifacts, sanity-check them, and own the cross-competitor synthesis. You do **not** write dossiers yourself, and leads do **not** skim. If the `Workflow` tool is available, each deep-set lead is naturally a sub-workflow; otherwise approximate it with a lead subagent that dispatches a batch of `Agent` workers and consolidates them.

**Anti-fabrication (A3).** Research invents confident numbers when unchecked, and Scope will treat them as fact. Two guards:

- **Every quantitative claim — pricing, traction, user counts, revenue, growth — carries a source URL, or is tagged `*inferred*`.** No bare numbers. This extends the `*inferred*` provenance convention from a logged-in nicety to a rule for all figures.
- Before you consolidate `SUMMARY.md`, **spot-check a sample** of the workers' returns against their cited sources — enough to catch a hallucinating worker. A single fabricated pricing tier poisons the feature matrix, so verify before you trust.

### 3. Per competitor → `DISCOVERY.md` (the 9-dimension panorama)

Each subagent fills a full 360º business teardown across these nine dimensions. They are the contract — don't drop any; mark a dimension *unknown* rather than omitting it:

1. **Value proposition & positioning** — what they promise, how they frame it, who they say they're for.
2. **Audience & personas** — segments, ICP, the jobs-to-be-done they serve.
3. **Pricing & monetization** — tiers, prices, free/trial mechanics, what's gated.
4. **Business model** — how money actually moves (subscription, usage, marketplace, ads…).
5. **Strengths & weaknesses** — honest, evidence-backed; weaknesses are proto-opportunities.
6. **Detectable tech stack** — front/back framework, hosting, analytics, anything fingerprintable (BuiltWith-style signals, response headers, JS bundles).
7. **Channels, traction & SEO** — acquisition channels, growth signals, keyword/SEO posture, social presence.
8. **User sentiment & reviews** — what customers praise and complain about (review sites, app stores, forums). Recurrent complaints are gold for Step 6.
9. **Core features** — the headline capabilities, named consistently so they can be cross-tabulated later.

### 4. Per competitor → `ROUTES.md` (key journeys by default, exhaustive on request)

This is the differentiator of the stage — a route-level teardown, not a feature blurb. But an every-route, logged-in, mostly-inferred inventory is the costliest instruction in the playbook, and Scope reads only a fraction of it. So default to **the key user journeys plus the feature surface Scope actually needs**, and capture for each route:

- **Path / URL** and a short **purpose**.
- **Access**: `public` or `logged`.
- **Features / elements** present on the route.
- **UI components** (nav, tables, forms, modals, cards…).
- **States**: empty / loading / error / populated — the states reveal product maturity.
- **CTAs / actions** available to the user.
- **Displayed data** — what information the route surfaces.

**Exhaustive mode is opt-in.** The full per-route inventory of *every* route is worth it for a close `platform`-tier rival, but it's a deliberate ask — make it opt-in at the checkpoint rather than the silent default, so the depth lands only where someone will read it.

**Logged-in area — gate on actual access, don't infer a full inventory.** If the user provides real access or screenshots, map the logged-in routes for real. If they don't, capture only what public evidence genuinely supports — docs, demo videos, changelogs, reviews, marketing — and tag each such route **`*inferred*`**; do **not** manufacture a complete logged-in state inventory from guesswork. An honest "logged-in area not accessed; these few flows inferred from docs" beats a fabricated 30-route teardown. Scope must know which findings are observed fact versus educated guess.

### 5. (Optional) Screenshot key public routes

Where a visual record adds real signal, use Playwright to navigate and capture key *public* routes into `docs/discovery/<competitor-name>/screenshots/`. This is per-project and optional — skip it when text capture already tells the story. Logged-in screenshots only ever come from the user.

### 6. Consolidate → `docs/discovery/SUMMARY.md`

This is the part only you (the conductor) do, because it requires seeing across all the dossiers at once. Synthesize the fan-out returns into:

- **Patterns** — what nearly everyone does (table stakes) and what no one does.
- **Feature matrix** — competitor × feature grid; this only works because Step 2 kept feature naming uniform. It makes white space visible at a glance.
- **Gaps** — unmet needs, recurring complaints (Dimension 8), under-served segments.
- **Opportunities** — the payload. Concrete, defensible openings the product could take.
- **Recommendations for Scope** — translate opportunities into candidate directions Stage 2 can act on.

SUMMARY.md is the artifact Scope actually reads. If it's vague, Scope inherits the vagueness. Make every opportunity specific and traceable back to evidence in the per-competitor files.

## Deliverables

Write into `docs/discovery/`, in English, using the templates at `assets/templates/deliverables/`:

```
docs/discovery/
  <competitor-name>/
    DISCOVERY.md        # template: deliverables/DISCOVERY.md  — 9-dimension panorama (deep set; lighter for light set)
    ROUTES.md           # template: deliverables/ROUTES.md     — key journeys by default; exhaustive when opted in
    screenshots/        # optional — key public routes
  SUMMARY.md            # template: deliverables/SUMMARY.md     — patterns, matrix, gaps, opportunities
```

One `<competitor-name>/` folder per approved competitor; one `SUMMARY.md` for the whole stage. Light-set competitors get a thinner `DISCOVERY.md` and a journeys-only `ROUTES.md`; the deep set gets the full treatment.

## Definition of Done

- [ ] Depth is scaled to the stakes tier in `docs/STATE.md` (no deep fan-out for `throwaway`).
- [ ] User has approved the final competitor list **and its deep/light split** (the early checkpoint), having seen the rough cost estimate.
- [ ] Every deep-set competitor has a complete `DISCOVERY.md` covering all 9 dimensions (unknowns marked, not omitted); light-set competitors have a proportionate scan.
- [ ] Each competitor has a `ROUTES.md` covering at least its key journeys + the surface Scope needs (exhaustive only where opted in); inferred routes are flagged `*inferred*` and logged-in depth matches actual access.
- [ ] Every quantitative claim carries a source URL or is tagged `*inferred*`, and a sample of worker returns was spot-checked before consolidation.
- [ ] Optional screenshots captured where they add signal (or consciously skipped).
- [ ] `SUMMARY.md` consolidates patterns + a competitor×feature matrix + gaps + **actionable opportunities** with recommendations feeding Scope.
- [ ] All artifacts are in English and follow the templates.

## The gate

Discovery has two human decision points:

1. **Early checkpoint — approve the competitor list and the spend.** Lightweight, before the fan-out. Present the grouped candidate list with the deep/light split, your recommendation, and a rough token/time cost estimate of the fan-out it authorizes. Let the user curate, move names between sets, and raise the soft cap. Wait for the approved list before dispatching subagents.

2. **Stage gate — accept the consolidated opportunities → Scope.** Once SUMMARY.md is done, summarize in a few lines: the competitors covered, the headline patterns, and the top opportunities you recommend carrying into Scope. Link the artifacts. Lead with your recommendation — *"these are the openings I'd take into Scope"* — rather than an open-ended "what now?".

Then **stop and wait.** Do not start Stage 2: don't draft scope, don't pick the MVP cut, don't write `docs/product/`. On explicit approval, record it in `docs/GATES.md` (date, stage, decision, approver), flip Stage 1 to `done` and Stage 2 to `in_progress` in `docs/STATE.md`, and announce the transition to Scope.
