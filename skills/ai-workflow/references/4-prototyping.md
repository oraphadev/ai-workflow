# Stage 4 — Prototyping

> Turn the scope into a navigable artifact that proves the UX before a single line of production code.

## Objective

Materialize the MVP's screens and flows into a navigable representation, in the tool best fit for *this* project, so the human can validate the experience before coding starts. The prototype is a contract: when Stage 8 builds, it builds against this. Faithfulness here saves rework everywhere downstream.

## Inputs

Read before doing anything:

- `docs/product/` — the MVP sitemap and user stories. The sitemap defines *which* screens exist; the stories define *what each screen must let the user do*. Every screen you prototype must trace to one of these.
- `docs/brand/` — design tokens and visual identity. Colors, type, spacing, components. The prototype applies these, not placeholder defaults.
- `docs/brand/DESIGN-STANDARDS.md` — the experience & design standards confirmed in Brand (mobile-first, accessibility floor, motion, app-like navigation, component reuse, input masks, lazy + blurhash media). These are contracts: the prototype honors them, it doesn't re-litigate them.

Confirm the Brand gate passed before entering. Prototyping on un-approved tokens means re-skinning everything later. If `docs/brand/` or `docs/brand/DESIGN-STANDARDS.md` is absent or unapproved, stop and route back — don't improvise an identity here.

## Capability routing

Pick the tool *per project* — there is no default. Choose by what you need to validate, then record the choice and rationale in PROTOTYPE.md.

**Decision guide:**

- **Visual-first, layout/flow validation, stakeholder review** → Figma. Best when the question is "does it look and feel right" and when a designer or non-technical reviewer is in the loop.
- **High-fidelity, interactive, real behavior (forms, state, navigation)** → code prototype (React). Best when the question is "does the interaction actually work" and when the prototype can seed the Stage 8 build.
- **Fast exploratory passes / single screens** → Claude Design, Google Stitch, or similar generative tools. Best for breadth before committing to a fidelity.

You may mix: Figma for the visual system, a code prototype for the two flows that carry real risk.

**Tool wiring for this stage:**

- **`/ui-ux-pro-max:ui-ux-pro-max` — mandatory for any visual/design work** (same as Brand). Route every screen and component through it for refined, polished output; recommend installing it if absent, else degrade to `frontend-design` and note it in `PROTOTYPE.md`.
- **Figma** — go through the `figma-generate-design` skill to build screens in Figma from the scope + tokens (design-to-Figma). Any `use_figma` / `generate_figma_design` call is mediated by the `figma-use` / `figma-generate-design` skills — loading the relevant skill is a mandatory prerequisite, never call those MCP tools raw. Use this path to assemble screens section-by-section from the brand tokens rather than hardcoded values.
- **Code (React)** — use the `frontend-design` skill for a high-fidelity, navigable prototype. This is the path when interaction fidelity matters or when you want the prototype to become a build reference with real components.
- **Playwright MCP** — to capture and validate the states of a code prototype: navigate the running prototype, drive each screen into its empty/loading/error/success state, and screenshot for the exports folder.

**Production is HYBRID.** The agent generates wherever the tool allows automation (Figma via the skill, code via `frontend-design`, captures via Playwright). Where the tool needs a human — manual Figma polish, design judgment calls, account-gated tools — the *user* produces and the agent guides and documents. Either way, the agent owns the documentation: nothing ships out of this stage undocumented.

## Steps

1. **Choose tool and fidelity.** Decide using the guide above. Write the choice and the *why* into PROTOTYPE.md before building — the rationale is part of the deliverable, not an afterthought.

2. **Prototype all MVP screens.** Walk the sitemap top to bottom; every screen gets built. Apply the brand tokens and visual identity as you go — pull real colors, type, and spacing from `docs/brand/`, not approximations. A screen styled with default grays is not done.

3. **Cover the relevant states per screen.** For each screen, ask which of empty / loading / error / success actually apply, then build the ones that do. A list screen needs empty and populated; a form needs error and success; a fetch-backed view needs loading. Skip states that don't apply, but document that you considered them — missing-state surprises are what prototypes exist to prevent. For code prototypes, drive each state with Playwright and capture it.

4. **Validate each screen against the PRD and user stories.** This is the core of the stage, not a final check. For every user story, confirm there is a screen (and state) that lets the user complete it. Walk the main flows end to end as a navigable path. Where the prototype and the stories disagree, adjust the prototype — or flag the story if the scope itself is wrong, and surface that rather than silently diverging.

5. **Export and record as build reference.** Capture the prototype link and, where the tool allows, export screens into `docs/prototype/exports/`. These exports are what Stage 8 reads when building. Make the screen↔route inventory explicit so the build knows which artifact maps to which route.

## Deliverables

Write to `docs/prototype/`. Start from the template at `assets/templates/deliverables/PROTOTYPE.md`.

```
docs/prototype/
├── PROTOTYPE.md          # tool + rationale, link, screen↔route inventory, UX decisions, validation vs PRD
└── exports/              # exported screens (when the tool allows export)
    ├── home.png
    ├── login.png
    └── ...
```

`PROTOTYPE.md` carries:

- **Tool + rationale** — what you chose and why, per the decision guide.
- **Prototype link** — Figma URL, deployed code prototype, or wherever it lives.
- **Screen↔route inventory** — the table that ties screens to routes to artifacts. This is the bridge into Stage 8:

  | Screen | Route | States covered | Export / link | Source story |
  |--------|-------|----------------|---------------|--------------|
  | Home | `/` | empty, populated | `exports/home.png` | US-01 |
  | Login | `/login` | default, error, success | `exports/login.png` | US-02 |

- **UX decisions** — choices made during prototyping (navigation model, key interactions, what was deliberately deferred) and their reasoning.
- **Validation vs PRD** — story-by-story confirmation that the prototype satisfies the scope, with any divergences flagged.

Artifacts in English, regardless of conversation language.

## Definition of Done

- [ ] Tool and fidelity chosen, with rationale recorded in PROTOTYPE.md.
- [ ] All MVP screens from the sitemap prototyped.
- [ ] Brand identity and tokens applied — no placeholder styling.
- [ ] Experience & design standards from `docs/brand/DESIGN-STANDARDS.md` honored — mobile-first layout, accessibility floor (incl. ≥16px inputs, contrast, focus, `prefers-reduced-motion`), app-like motion/navigation (transitions may be CSS-stubbed for a code prototype — library wiring deferred to Stage 5), input masks on convenient fields, lazy + blurhash media, skeleton loaders / optimistic UI, `font-display: swap` + font preload, component reuse/consistency across screens, theming via tokens (dark mode if in scope), a single consistent iconography set, PWA installability if scoped, and i18n-ready layout and copy.
- [ ] Any visual/design work routed through `ui-ux-pro-max` (or the degraded fallback noted).
- [ ] Relevant states (empty / loading / error / success) covered per screen, with non-applicable states noted.
- [ ] Main flows navigable end to end.
- [ ] Every user story validated against a screen + state.
- [ ] Screen↔route inventory table complete.
- [ ] Exports recorded in `docs/prototype/exports/` where the tool allows, plus the live link.

## The gate

The human decision: **is this prototype a faithful, validated representation of the scope — solid enough to build against?** No code starts until this is approved.

Present, then stop:

1. The **screen↔route inventory** — every screen, its route, its covered states, its export/link.
2. The **validation summary** — each user story mapped to the screen that satisfies it, with any divergences or deferrals called out explicitly.
3. The **live prototype link** so the human can navigate the real thing.

Propose approval and STOP. Do not advance to Stage 5 or write any production code on your own judgment — the prototype's faithfulness is the human's call to make, and approving it is what unlocks the build.
