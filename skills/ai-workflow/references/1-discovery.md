# Stage 1 — Discovery

> Map the whole arena before choosing a weapon: a full panorama of the market and an exhaustive route-level teardown of every competitor, so opportunities are *found*, not guessed.

## Objective

Build a deep, structured understanding of the space the product wants to enter. Not a vibe-check — a panorama. For each competitor you produce a 360º business teardown and a route-by-route map of their product, then consolidate everything into a cross-competitor synthesis whose payload is *actionable opportunities*. Scope (Stage 2) reads that synthesis to decide what to actually build. The quality of the MVP cut downstream is bounded by the quality of the gaps you surface here.

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
- **Nested `Workflow` fan-out — the engine of this stage.** A competitor is **not** a single subagent; it is its own **deep-research workflow** that fans out into many workers. The orchestration is *three tiers*: you (conductor) dispatch one **competitor lead** per approved competitor; each lead in turn dispatches **dozens of workers** — one per panorama dimension that warrants depth, several for route mapping (public + logged), several mining reviews / SEO / tech-fingerprint sources — then synthesizes that competitor's two artifacts. Depth per competitor comes from this layered fan-out, not from one agent skimming ten tabs. Use the `deep-research` skill to power each competitor's investigation when web breadth matters.
- **Playwright MCP** (`browser_navigate`, `browser_snapshot`, `browser_take_screenshot`) — optional, for capturing key *public* routes of a competitor when a visual record adds signal (Step 5). `browser_snapshot` gives you the accessibility tree (great for enumerating UI elements and states cheaply); `browser_take_screenshot` gives the pixel record. Don't screenshot everything — only routes where the visual is load-bearing.

## Steps

### 1. Propose a candidate competitor list — then let the user curate it

From the idea and the agreed criteria, generate a candidate list of competitors. No fixed cap — completeness beats brevity here; it's cheaper to cut a name than to miss a category. Group candidates by type (direct / indirect / analogous) and add a one-line *why this one* for each, so the user can judge relevance fast.

This is a **checkpoint, not a gate** — a lightweight human-in-the-loop before you spend fan-out budget. Present the grouped list, ask the user to add/remove/reclassify, and wait for an approved final list. Do not start the per-competitor fan-out against an unapproved list; every name you keep multiplies into a full dossier, so curating here is the cheapest possible place to be wrong.

### 2. Fan out — one deep-research *workflow* per approved competitor

For each competitor, dispatch a **competitor lead** — not a single do-it-all subagent. Send the leads concurrently; they're independent. Each lead's mandate is to run a *real* deep investigation of its one competitor by fanning out its **own** workers, then synthesize. This is the layer that makes Discovery deep rather than a skim — every competitor gets dozens of worker-agents, not one.

A good decomposition for each competitor lead:

- **One worker per panorama dimension that warrants depth** — pricing/monetization, business model, detectable tech stack, user sentiment/reviews mining, channels/traction/SEO. Shallow dimensions can be combined, but the money / sentiment / feature dimensions each deserve a dedicated worker so nothing is glossed.
- **Route-mapping workers** — split public vs logged-in, and split large surfaces (an app with 40+ routes) across several workers so each maps a coherent slice at full granularity.
- The lead **synthesizes** its workers' returns into that competitor's `DISCOVERY.md` (9 dimensions) + `ROUTES.md` (every route), tags unverifiable claims as `*inferred*`, and writes to `docs/discovery/<competitor-name>/`.

Hand each lead the deliverable templates by path so shapes come back uniform — uniformity is what makes the cross-competitor matrix in Step 6 possible. You (the conductor) receive the per-competitor artifacts, sanity-check them, and own the cross-competitor synthesis. You do **not** write dossiers yourself, and leads do **not** skim. If the `Workflow` tool is available, each competitor lead is naturally a sub-workflow; otherwise approximate it with a lead subagent that itself dispatches a batch of `Agent` workers and consolidates them.

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

### 4. Per competitor → `ROUTES.md` (every route, full granularity)

This is the differentiator of the stage — a route-level teardown, not a feature blurb. Map **every** route, public *and* logged-in. For each route capture:

- **Path / URL** and a short **purpose**.
- **Access**: `public` or `logged`.
- **Features / elements** present on the route.
- **UI components** (nav, tables, forms, modals, cards…).
- **States**: empty / loading / error / populated — the states reveal product maturity.
- **CTAs / actions** available to the user.
- **Displayed data** — what information the route surfaces.

**Logged-in area:** decide at runtime, with the user, how to reach it. If the user provides access or screenshots, map it for real. Otherwise *infer* the logged-in routes from public sources — docs, demo videos, changelogs, reviews, marketing — and explicitly tag each inferred route as **`*inferred*`**. Honesty about provenance matters: Scope must know which findings are observed fact versus educated guess.

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
    DISCOVERY.md        # template: deliverables/DISCOVERY.md  — 9-dimension panorama
    ROUTES.md           # template: deliverables/ROUTES.md     — every route, full granularity
    screenshots/        # optional — key public routes
  SUMMARY.md            # template: deliverables/SUMMARY.md     — patterns, matrix, gaps, opportunities
```

One `<competitor-name>/` folder per approved competitor; one `SUMMARY.md` for the whole stage.

## Definition of Done

- [ ] User has approved the final competitor list (the early checkpoint).
- [ ] Every approved competitor has a complete `DISCOVERY.md` covering all 9 dimensions (unknowns marked, not omitted).
- [ ] Every approved competitor has a `ROUTES.md` mapping all routes with the full per-route fields; inferred logged-in routes are flagged `*inferred*`.
- [ ] Optional screenshots captured where they add signal (or consciously skipped).
- [ ] `SUMMARY.md` consolidates patterns + a competitor×feature matrix + gaps + **actionable opportunities** with recommendations feeding Scope.
- [ ] All artifacts are in English and follow the templates.

## The gate

Discovery has two human decision points:

1. **Early checkpoint — approve the competitor list.** Lightweight, before the fan-out. Present the grouped candidate list with a recommendation and let the user curate. Wait for the approved list before dispatching subagents.

2. **Stage gate — accept the consolidated opportunities → Scope.** Once SUMMARY.md is done, summarize in a few lines: the competitors covered, the headline patterns, and the top opportunities you recommend carrying into Scope. Link the artifacts. Lead with your recommendation — *"these are the openings I'd take into Scope"* — rather than an open-ended "what now?".

Then **stop and wait.** Do not start Stage 2: don't draft scope, don't pick the MVP cut, don't write `docs/product/`. On explicit approval, record it in `docs/GATES.md` (date, stage, decision, approver), flip Stage 1 to `done` and Stage 2 to `in_progress` in `docs/STATE.md`, and announce the transition to Scope.
