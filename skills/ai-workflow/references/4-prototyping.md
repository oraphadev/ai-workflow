# Stage 4 — Prototyping

> Turn the scope into a navigable artifact that proves the UX before a single line of production code — by **deciding content and components first, then assembling screens**, not improvising them.

## Objective

Materialize the MVP's screens and flows into a navigable representation, in the tool best fit for *this* project, so the human can validate the experience before coding starts. The prototype is a contract: when Stage 8 builds, it builds against this. Faithfulness here saves rework everywhere downstream.

The failure this stage exists to prevent: screens improvised pixel by pixel, padded with irrelevant information and generic AI-written copy, each one reinventing buttons and cards from scratch. The cure is **decision before drawing** — define each screen's real content and information architecture, build the full reusable component arsenal, and only then assemble screens by composition. Prototyping then becomes execution of what's already decided, not invention.

## Inputs

Read before doing anything:

- `docs/product/` — the MVP sitemap, the user stories, and the PRD. The sitemap defines *which* screens exist; the stories define *what each screen must let the user do*; the PRD's data entities/fields and acceptance criteria define *what real content each screen carries*. Every screen — and every piece of content on it — traces back to these.
- `docs/brand/` — design tokens and visual identity. Colors, type, spacing, components. The prototype applies these, not placeholder defaults.
- `docs/brand/DESIGN-STANDARDS.md` — the experience & design standards confirmed in Brand (mobile-first, accessibility floor, motion, app-like navigation, component reuse, input masks, lazy + blurhash media). These are contracts: the prototype honors them, it doesn't re-litigate them.
- `docs/brand/VOICE-TONE.md` — the voice and tone every word of real copy you write here must follow.

Confirm the Brand gate passed before entering. Prototyping on un-approved tokens means re-skinning everything later. If `docs/brand/` or `docs/brand/DESIGN-STANDARDS.md` is absent or unapproved, stop and route back — don't improvise an identity here.

## Capability routing

Pick the tool *per project* — there is no default. **Whatever the tool, the four-phase discipline below (define → arsenal → assemble → wire flows) is mandatory.** Choose by what you need to validate, then record the choice and rationale in PROTOTYPE.md.

**Decision guide:**

- **Visual-first, layout/flow validation, stakeholder review** → Figma. Best when the question is "does it look and feel right" and when a designer or non-technical reviewer is in the loop.
- **High-fidelity, interactive, real behavior (forms, state, navigation) that can seed the build** → code prototype (React). Best when the question is "does the interaction actually work" — and when the arsenal's components can become Stage 8's real components, the tightest path into the build.
- **Fast exploratory passes / single screens** → Claude Design, Google Stitch, or similar generative tools. Best for breadth before committing to a fidelity.

You may mix: Figma for the visual system, a code prototype for the two flows that carry real risk. Whichever you pick, the component arsenal is built before screens and the screens reuse it — Figma components/variants in the Figma path, real coded components in the code path.

**Tool wiring for this stage:**

- **`/ui-ux-pro-max:ui-ux-pro-max` — mandatory for any visual/design work** (same as Brand). Route every screen and component through it for refined, polished output; recommend installing it if absent, else degrade to `frontend-design` and note it in `PROTOTYPE.md`.
- **Figma** — go through the `figma-generate-design` skill to build screens in Figma from the scope + tokens (design-to-Figma). Any `use_figma` / `generate_figma_design` call is mediated by the `figma-use` / `figma-generate-design` skills — loading the relevant skill is a mandatory prerequisite, never call those MCP tools raw. Use this path to assemble screens section-by-section from the brand tokens rather than hardcoded values.
- **Code (React)** — use the `frontend-design` skill for a high-fidelity, navigable prototype. This is the path when interaction fidelity matters or when you want the prototype to become a build reference with real components.
- **Playwright MCP** — to capture and validate the states of a code prototype: navigate the running prototype, drive each screen into its empty/loading/error/success state, and screenshot for the exports folder.

**Production is HYBRID.** The agent generates wherever the tool allows automation (Figma via the skill, code via `frontend-design`, captures via Playwright). Where the tool needs a human — manual Figma polish, design judgment calls, account-gated tools — the *user* produces and the agent guides and documents. Either way, the agent owns the documentation: nothing ships out of this stage undocumented.

## Steps

Run the stage as a four-phase pipeline. Phases A→B→C→D are ordered; the arsenal checkpoint between B and C is a hard internal stop the conductor self-verifies. The single human gate is at the end (unchanged). Write the choice of tool and the *why* into PROTOTYPE.md before building — the rationale is part of the deliverable, not an afterthought.

### Phase A — Define content & information architecture (no pixels yet)

Before building anything, decide *what every screen says and shows*. Walk the MVP sitemap; for each screen derive — from the PRD, SCOPE, the competitor ROUTES maps, and Brand — a content & IA spec:

- **Purpose**, traced to the user-story IDs (`US-NN`) it serves.
- **Content blocks and their hierarchy** — what appears, and in what order of importance, top to bottom.
- **Real data shown** — the actual entities and fields from the PRD, populated with realistic, representative domain values (a real-looking invoice, a real category name), never `lorem ipsum` or placeholder rectangles.
- **Real copy for every text element** — headings, labels, helper/microcopy, empty/error/success messages, and CTA labels — written to `VOICE-TONE.md`. This is the cure for AI-filler copy: the words are decided here, deliberately, not improvised at draw time.
- **Applicable states** — which of empty / loading / error / success this screen actually has.

**Hard rule — no invention, no filler.** Every block, datum, and string traces to a story, a PRD data entity, or a defined value proposition. Irrelevant content and generic AI copy are defects, not drafts. If the source for some content genuinely doesn't exist upstream (a story or field was never specified), **stop and flag it — re-open Scope** per the SKILL's gate-reopening protocol — rather than inventing it. A prototype that shows information nobody decided to show is exactly the failure this phase prevents.

Record the per-screen content spec in `PROTOTYPE.md` (§ *Screen content & copy spec*).

### Phase B — Build the component arsenal first (mandatory)

From the content specs, derive the **complete component inventory** the screens will need — atoms (button, input, badge), molecules (form field, list item, card), organisms (nav bar, header, modal, data table). Then **prototype every component before any screen exists**:

- Every **variant** (primary/secondary button; default/featured card) and every relevant **state** (default, hover, focus, disabled, loading, error, empty) the component can take.
- In **both desktop and mobile** form.
- Built from Brand tokens and the design standards — never ad-hoc values.

Document each in `PROTOTYPE.md` (§ *Component inventory*): the component, its variants, its states, its props/usage, and that both viewports exist.

**Hard internal checkpoint — the conductor self-verifies before Phase C and does not cross it until it is true:** *the arsenal is complete — every component the content specs call for is prototyped, with its variants, states, and both viewports, and documented in the inventory.* No screen assembly begins before this holds. This is the conductor's own checkpoint, not a human stop — the flow stays continuous; it exists so screens can't be built on a half-built arsenal.

### Phase C — Assemble screens by composition

Now build each screen **purely by composing arsenal components** — "assembling the puzzle" — filled with the real content from its Phase A spec. Build the states the spec marked applicable.

- **Every screen in both desktop and mobile.** Mobile-first is the *design order* — lay out mobile-up, then expand to desktop — but **both viewports are deliverables**, captured and validated.
- **No new primitives invented inside a screen.** If assembly reveals a genuinely new custom component is needed, **return to Phase B**: add it to the arsenal (prototyped, all states, both viewports, documented), *then* use it. A one-off component built straight into a screen is a defect — it breaks the reuse the whole stage exists to guarantee.

### Phase D — Wire navigable, cohesive flows

Connect the assembled screens into **navigable end-to-end flows that simulate the real app** — real navigation between screens, transitions per the design standards, and state changes as the user acts. Walk each path in the MVP's *Main Flows* end to end as a clickable journey. The goal is a prototype a human can *use* like the finished product, and that the Stage 8 team can turn into the real app by following it rather than re-deciding it.

Then **validate against the PRD and user stories**: for every story, confirm a screen + state + flow lets the user complete it. Where the prototype and the stories disagree, adjust the prototype — or flag the story if the scope itself is wrong, and surface that rather than silently diverging.

### Export and record as build reference

Capture the prototype link and, where the tool allows, export both the components and the screens (desktop + mobile) into `docs/prototype/exports/`. These exports plus the documented inventory are what Stage 8 reads when building. Make the screen↔route inventory explicit — including which arsenal components each screen uses — so the build knows which artifact maps to which route and which components to reuse.

## Deliverables

Write to `docs/prototype/`. Start from the template at `assets/templates/deliverables/PROTOTYPE.md`.

```
docs/prototype/
├── PROTOTYPE.md          # tool + rationale, link, screen content & copy spec,
│                         # component inventory, screen↔route inventory (w/ viewports
│                         # + components used), UX decisions, validation vs PRD
└── exports/
    ├── components/       # the arsenal — exported components (where the tool allows)
    └── screens/          # per screen, desktop + mobile
        ├── home-desktop.png
        ├── home-mobile.png
        └── ...
```

`PROTOTYPE.md` carries:

- **Tool + rationale** — what you chose and why, per the decision guide.
- **Prototype link** — Figma URL, deployed code prototype, or wherever it lives.
- **Screen content & copy spec** — per screen: purpose (→ `US-NN`), content blocks + hierarchy, real data shown, the real copy for every text element, and applicable states. This is the contract Phase C renders — not improvised at draw time.
- **Component inventory** — the arsenal: each component, its variants, states, usage, and both viewports. Built and documented before any screen.
- **Screen↔route inventory** — the table tying screens to routes to artifacts, now including viewports and the arsenal components each screen composes:

  | Screen | Route | US (stories) | States | Viewports | Components used | Export / link |
  |--------|-------|--------------|--------|-----------|-----------------|---------------|
  | Home | `/` | US-01 | empty, populated | desktop, mobile | Header, Card, EmptyState | `exports/screens/home-*.png` |
  | Login | `/login` | US-02 | default, error, success | desktop, mobile | AuthForm, Button | `exports/screens/login-*.png` |

- **UX decisions** — choices made during prototyping (navigation model, key interactions, what was deliberately deferred) and their reasoning.
- **Validation vs PRD** — story-by-story confirmation that the prototype satisfies the scope, with any divergences flagged.

Artifacts in English, regardless of conversation language.

## Definition of Done

- [ ] Tool and fidelity chosen, with rationale recorded in PROTOTYPE.md.
- [ ] **Phase A — content & IA defined before any pixel:** every MVP screen has a content & copy spec — purpose (→ US-NN), content blocks + hierarchy, real data, and the real copy for every text element (per VOICE-TONE.md) — with **no invented/filler content**; any missing upstream source was flagged/re-opened, not fabricated.
- [ ] **Phase B — arsenal complete before screens:** the full component inventory is prototyped (every variant + relevant state, desktop + mobile, from Brand tokens) and documented, and the conductor verified this before assembling any screen.
- [ ] **Phase C — screens assembled by composition:** all MVP screens built purely from arsenal components, in **both desktop and mobile**, with applicable states; any new custom component was added to the arsenal first, never one-off in a screen.
- [ ] Brand identity and tokens applied — no placeholder styling.
- [ ] Experience & design standards from `docs/brand/DESIGN-STANDARDS.md` honored — mobile-first layout, accessibility floor (incl. ≥16px inputs, contrast, focus, `prefers-reduced-motion`), app-like motion/navigation (transitions may be CSS-stubbed for a code prototype — library wiring deferred to Stage 5), input masks on convenient fields, lazy + blurhash media, skeleton loaders / optimistic UI, `font-display: swap` + font preload, component reuse/consistency across screens, theming via tokens (dark mode if in scope), a single consistent iconography set, PWA installability if scoped, and i18n-ready layout and copy.
- [ ] Any visual/design work routed through `ui-ux-pro-max` (or the degraded fallback noted).
- [ ] Relevant states (empty / loading / error / success) covered per screen, with non-applicable states noted.
- [ ] **Phase D — main flows navigable end to end**, simulating the real app.
- [ ] Every user story validated against a screen + state + flow.
- [ ] Screen↔route inventory table complete, including viewports and components-used per screen.
- [ ] Exports recorded in `docs/prototype/exports/` (components + screens desktop/mobile) where the tool allows, plus the live link.

**Flex by stakes** (read the tier from `docs/STATE.md`): the four-phase order and the both-viewports rule hold at every tier; only the *depth* flexes. `throwaway` — a lean arsenal (the key components only) and the primary viewport built with the other noted, copy still real but lighter. `mvp` — the full pipeline, both viewports complete. `platform` — adds intermediate/tablet breakpoints and visual-regression / measurement on the exported screens.

## The gate

The human decision: **is this prototype a faithful, validated representation of the scope — solid enough to build against?** No code starts until this is approved.

Present, then stop:

1. The **screen content & copy spec** and the **component inventory** — proof the content was decided (not improvised) and the arsenal is complete and reused.
2. The **screen↔route inventory** — every screen, its route, covered states, viewports, components used, export/link.
3. The **validation summary** — each user story mapped to the screen + state + flow that satisfies it, with any divergences or deferrals called out explicitly.
4. The **live prototype link** so the human can navigate the real thing.

Propose approval and STOP. Do not advance to Stage 5 or write any production code on your own judgment — the prototype's faithfulness is the human's call to make, and approving it is what unlocks the build.
