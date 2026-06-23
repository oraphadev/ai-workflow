# Stage 2 — Scope Definition

> Turn what Discovery learned into a sharp, lean definition of what gets built — product, differentiator, and the MVP cut — through a brainstorming you lead, not a survey you run.

## Objective

Converge Discovery's findings into a defensible product definition: the value proposition, the one differentiator that wins against competitors, JTBD personas, a prioritized feature set, and an MVP cut small enough to ship yet whole enough to prove the thesis. This stage is an **assertive, agent-led brainstorming** — you drive toward a decision, you don't just collect the user's opinions. The output is the contract every downstream stage builds against: Brand styles the positioning, Prototyping draws the screens, Stack sizes the build — all from the artifacts you write here.

## Inputs

Read these before doing anything else; this stage is only as good as what it consumes:

- `docs/discovery/SUMMARY.md` — opportunities, patterns, gaps, target users.
- `docs/discovery/ROUTES.md` (competitor route maps) — what competitors actually ship, screen by screen. Your differentiator and your feature gaps both come from here.

Confirm Discovery's gate was passed in `docs/GATES.md`. If it wasn't, stop — scoping on top of an unapproved competitor list and unaccepted opportunities corrupts everything downstream. Skim the artifacts; do not re-summarize them back to the user.

## Capability routing

- **`brainstorming` skill (superpowers)** — this stage *is* a brainstorming. Route to it to structure the convergence on vision and MVP cut. Use it to drive, not to interrogate: bring hypotheses formed from Discovery and pressure-test them with the user.
- **Impact × Effort** is the explicit lens for the MVP cut (scoring method below). Don't prioritize by gut or by "what competitors have."
- **Subagent fan-out (optional)** — once the MVP cut is *locked*, you may fan out PRD authoring: one subagent per MVP feature drafting its user stories, requirements, business rules, and edge cases against a shared template. Do not fan out before the cut is locked — you'd be writing specs for features that won't survive.

## Steps

### 1. Agent-led brainstorming → vision + MVP thesis
Open with a stance, not a blank page. From Discovery, propose a candidate one-line vision and the core thesis ("the wedge is X because competitors all miss Y"). Then refine it *with* the user — challenge, narrow, kill darlings. The deliverable is convergence, not a list of options. Lead. Drive to a single vision the user signs off on conversationally before you write `SCOPE.md`.

### 2. Value proposition, positioning, differentiators
State the value prop in one sentence (for [persona] who [need], we [do X] unlike [competitor] by [differentiator]). Position explicitly against the `ROUTES.md` competitors: name what they do, name the gap, name your wedge. The differentiator must be specific and defensible — "better UX" is not a differentiator; "the only one that does X in one screen" is.

### 3. Personas as JTBD (concrete fields)
For each persona (2–4 max), fill real fields, not adjectives:
- **Context** — who they are, when/where the need fires.
- **Job-to-be-done** — the functional + emotional job ("when ___, I want to ___, so I can ___").
- **Pains** — what's broken today (tie to Discovery findings).
- **Gains** — what success feels like.
A persona with no concrete job is decoration; cut it.

### 4. Candidate features
Derive the feature list from two sources: patterns common across competitors (table stakes) and the gaps Discovery surfaced (your opportunities). Tag each feature as *table-stakes* or *differentiating* — this tagging feeds the cut.

### 5. Prioritize and cut the MVP — Impact × Effort
Score every candidate feature on two axes:
- **Impact** (1–5): how much it moves the north-star / proves the thesis / serves the primary persona's job. Differentiating features and table stakes the product is broken without score high.
- **Effort** (1–5): build cost — complexity, dependencies, unknowns.

Plot them and draw the cut line:
- **MVP** = high-impact features, preferring low effort; always include the differentiator even if costly (without it there's no reason to exist), plus the minimum table stakes the differentiator needs to function.
- **v1** = high-impact / high-effort that can wait, and impactful nice-to-haves.
- **Backlog** = low-impact regardless of effort.

The MVP must be *complete enough to prove the thesis and shippable*. If it's huge, cut harder — defer, don't pad. Record each feature's scores and its phase so the line is auditable, not asserted.

### 6. Success metrics
Define one **north-star** metric (the single number that means the thesis is working), 2–4 **supporting KPIs**, and concrete **MVP acceptance criteria** (the observable bar that says "the MVP is done and working"). These become the validation target in Stage 8.

### 7. User stories + requirements (PRD)
For each MVP feature write stories as **"As [persona], I want [capability], so that [outcome]"**, each with **acceptance criteria** in testable Given/When/Then form. Add functional requirements, non-functional requirements (performance, security, accessibility), business rules, edge cases / empty-error-loading states, and the initial data entities the feature touches. This is the layer that makes the MVP buildable without guessing.

## Deliverables

Write all three to `docs/product/`, in English, using the templates in `assets/templates/deliverables/`:

```
docs/product/
  SCOPE.md   # vision, value prop, positioning, JTBD personas, differentiators,
             # success metrics + north-star, candidate features, macro sitemap
  MVP.md     # features phased MVP→v1→backlog w/ Impact×Effort scores,
             # MVP sitemap/screens, main flows, MVP success criteria
  PRD.md     # per MVP feature: user stories + acceptance criteria, functional &
             # non-functional reqs (perf/security/a11y), business rules,
             # edge cases/states, initial data entities/model
```

- `SCOPE.md` → template `assets/templates/deliverables/SCOPE.md`
- `MVP.md` → template `assets/templates/deliverables/MVP.md`
- `PRD.md` → template `assets/templates/deliverables/PRD.md`

The macro sitemap in `SCOPE.md` and the MVP sitemap in `MVP.md` are the seed Prototyping turns into screens — make them real navigation trees, not bullet lists.

## Definition of Done

- [ ] Discovery gate confirmed passed; `SUMMARY.md` + `ROUTES.md` read.
- [ ] Vision, value prop, and positioning converged and written.
- [ ] Differentiator is specific and clearly stronger than the `ROUTES.md` competitors.
- [ ] Personas written as JTBD with concrete jobs/pains/gains/context.
- [ ] Candidate features tagged; every feature scored Impact × Effort.
- [ ] MVP cut closed and prioritized; the cut line (MVP / v1 / backlog) is auditable from the scores.
- [ ] North-star + supporting KPIs + MVP acceptance criteria defined.
- [ ] Per-MVP-feature user stories + acceptance criteria, requirements, business rules, and edge cases written — detailed enough to prototype and build.
- [ ] `SCOPE.md`, `MVP.md`, `PRD.md` written to `docs/product/`.

## The gate

The human decides two things: **the MVP cut** and **the differentiator**. Don't ask "what do you think?" — present a recommendation and the reasoning, then stop.

- Summarize the vision and the differentiator in two lines, linking `docs/product/SCOPE.md`, `MVP.md`, `PRD.md`.
- Present the cut as a decision: **what's in the MVP, what's deferred to v1, what's backlog — and why**, grounded in the Impact × Effort scores (especially: why the differentiator is in and why each notable feature was deferred).
- Make the differentiator explicit and ask the human to confirm it's the wedge worth betting on.
- Then **stop and wait.** Do not start Brand, do not draw screens, do not write `docs/brand/`.
- On approval: append the decision to `docs/GATES.md` (date, the approved cut + differentiator, who approved), flip Stage 2 to `done` and Stage 3 to `in_progress` in `docs/STATE.md`, and announce the transition to Brand.
