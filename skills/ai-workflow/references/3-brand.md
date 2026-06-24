# Stage 3 — Brand Definition

> Turn a validated product into a name, a voice, and a visual system precise enough that a machine can read it — direction and tokens, not a logo file.

## Objective

Define the COMPLETE brand identity — from name to design token — so every later word and pixel stays consistent. You are producing the *source of truth* for verbal and visual decisions: the name, how the product speaks, how it looks, and a stack-agnostic token file the prototype and build stages will consume directly.

This stage delivers a **specification and direction**, not generated artifacts. There is no `/assets` folder and no rendered logo here. The agent describes the logo's rules and rationale; a designer (or a later tool pass) renders it. Tokens, by contrast, *are* concrete and machine-consumable — they are the bridge into prototyping.

## Inputs

Read `docs/product/SCOPE.md` before proposing anything, and mine three sections specifically:

- **Positioning** — anchors naming, tagline, and the whole tonal register. A compliance tool and a consumer game earn opposite brands.
- **Personas** — who hears the voice and sees the interface. Vocabulary, formality, and visual maturity follow from them.
- **Differentiators** — what the brand must *signal*. The name and the visual direction should make the differentiator legible at a glance.

Confirm the Scope gate actually passed (SCOPE.md approved by the user) before starting. Brand built on an unratified scope is rework waiting to happen.

## Capability routing

- **`/ui-ux-pro-max:ui-ux-pro-max` plugin — mandatory for any design/visual work.** Every task that touches design or the visual layer — proposing visual directions, defining components, materializing tokens, any UI judgement call — routes through this plugin so the output is refined, optimized, and polished rather than templated. If it isn't installed in the target repo, **recommend the user install it** (via their plugin manager), then proceed. If they decline or it's unavailable, degrade gracefully to `frontend-design` + the design standards below and note the degraded rung in `DESIGN-STANDARDS.md` — routed tools are verify-at-use, per the thin-environment ladder.
- **Mobbin (and reference inputs) — design reference-driven, not from scratch.** Recommend the user pull real, current references — Mobbin (via its MCP if connected), screenshots, and live sites — and feed them in as the basis for the visual directions. Deriving palette, type, and component patterns from proven references beats inventing them blind; cite the references behind each direction.
- **Design extraction from reference images — when visual references are in context, extract, don't eyeball.** Whenever the user provides visual references as images — pasted screenshots, a Mobbin/MCP image pull, linked mockups or live-site captures — do not infer the design by eye. If the `find-skills` skill is available, use it to locate and load the best current skill for extracting design information from images (palette with exact values, type families + scale, spacing/rhythm, radii, elevation, component patterns, layout grid, iconography, motion cues); the current market leader is **`arvindrk/extract-design-system`** (`npx skills add arvindrk/extract-design-system`, ~124K installs) — treat that name as the best-known option to **verify at use**, not a guarantee. If `find-skills` is unavailable or no such skill is installed, **recommend the user install `arvindrk/extract-design-system`** and note it pays off across the whole journey (Brand here, Prototyping when matching references, Discovery on competitor screenshots) — then degrade gracefully: read the references through `frontend-design`/`ui-ux-pro-max` and note the degraded rung. The extracted design DNA is the **basis** for the visual directions and tokens below — cite which reference each value came from (VISUAL-IDENTITY §8, DESIGN-STANDARDS §0), so the look is *derived* from proven references, not invented.
- **`frontend-design` skill** — load it before proposing visual directions. It steers toward distinctive, intentional choices (real typographic personality, a palette with a point of view) and away from the templated defaults that make every option look the same. Use it to pressure-test that your N visual directions are genuinely different, not three shades of the same safe gray.
- **Figma MCP (optional)** — only if the user wants the palette or type scale *materialized* to look at. Useful as a preview. It does not change the deliverable: the source of truth stays `VISUAL-IDENTITY.md` + `design-tokens.json`, never a Figma file. Don't let a Figma round-trip become the artifact.
- **W3C Design Tokens** — the format for `design-tokens.json` (see Steps). Stack-agnostic on purpose, so it transforms later into CSS variables, Tailwind config, iOS, etc., without re-deciding anything.

## Steps

Brand is reversible and low-stakes — renaming or recoloring later costs little. So this stage uses **one batched approval, not a string of serial stops.** Work the five blocks below in order so each can inform the next, but **prepare them together and present them in a single batched gate** (see *The gate*): N genuinely distinct directions for naming, voice, and visual — each with trade-offs and a recommendation — plus the proposed experience & design standards for keep/change confirmation — so the user picks across all blocks in one pass, then you refine. The discipline per block is unchanged (distinct directions, a recommendation, the user's real choice); only the *cadence* changes — you stop once, not five times. This is the deliberate de-bloating of a reversible stage; don't re-fragment it into per-block stops.

Order still matters for *preparing* the options: let the naming candidates flavor the voice directions and the voice flavor the visual register, so the batched menu hangs together rather than reading as five unrelated lists.

### 1. Naming

Generate candidates concept-first, then validate at the concept level only — **availability checks (domains, trademarks) are out of scope here** and belong to a later operational step. Offer a spread of *approaches*, not just a list of words:

- **Descriptive** (says what it does), **evocative/metaphorical** (suggests a feeling), **invented/coined** (ownable, blank-slate), **compound/portmanteau**, **real-word repurpose**.
For each candidate give: meaning, why it fits the positioning, pronunciation/spelling risk, and rough connotations. Present a few approaches and recommend one with reasoning — carry these into the batched gate rather than stopping here. Refine the chosen name (spelling, casing, optional sub-brand or product-line logic) after the user picks.

### 2. Positioning

Draft the verbal core: **tagline** (one line, memorable), **core message** (the one-sentence promise), and **brand narrative** (a short paragraph — origin, problem, stance). Propose a couple of distinct angles (e.g. bold/contrarian vs. warm/reassuring) so the user steers the personality. Because positioning leans on the name, frame the angles so they read against your recommended name (and note how each shifts if the user picks a different one) — they go into the same batched gate, not a separate stop.

### 3. Voice & tone (complete)

This must be a usable guide, not adjectives. Produce all of:

- **Voice principles** — 3–5 durable traits, each with a one-line "we do / we don't" so it's actionable.
- **Tone by context** — voice is constant, tone flexes by situation. Give a table:

  | Context     | Goal                        | Tone                          | Example line                          |
  | ----------- | --------------------------- | ----------------------------- | ------------------------------------- |
  | Error       | reassure, unblock           | calm, plain, no blame         | "That didn't save. Try again?"        |
  | Success     | confirm, lightly celebrate  | warm, brief                   | "Done. Your changes are live."        |
  | Onboarding  | orient, lower the stakes    | encouraging, concrete         | "Let's set up your first project."    |
  | Marketing   | persuade, differentiate     | confident, vivid              | (on-brand headline)                   |

- **Do's & don'ts** — concrete pairs (preferred phrasing vs. avoided phrasing).
- **Examples** — a few rewrites showing the voice applied.
- **Brand glossary** — canonical terms: what to call features/objects, capitalization, words to avoid, product name usage rules.

### 4. Visual identity (complete spec — DIRECTION, not a generated logo)

Write the full specification. State explicitly that this is direction; the logo is described by *rules*, never rendered here. Cover every field:

- **Palette** — colors with **roles**, not just hex: primary, secondary/accent, surface/background, text, semantic (success/warning/error/info), plus neutrals. Roles are what tokens will reference.
- **Typography** — font choices (display/body/mono) and a **scale** (named steps with size/line-height/weight), plus usage rules.
- **Logo rules** — construction logic, clear space, min size, do's/don'ts, monochrome behavior. Direction only.
- **Iconography / illustration** — style, weight, grid, when each is used.
- **Spacing & grid** — base unit, spacing scale, layout grid/breakpoints.
- **Key components** — visual treatment direction for buttons, inputs, cards, etc. (states, radius, elevation language).
- **Mood / references** — adjectives, comparables, and what to deliberately avoid, so the direction is unambiguous.

### 5. Experience & design standards (proactive — propose, then confirm)

Modern AI-built products live or die on interaction quality, not just palette and type. So here you **proactively propose the current best-practice design/UX standards for this product** as one curated, opinionated default set — then ask the user what to **keep or change**. Unlike the other blocks, this is not N competing directions; it is a recommended baseline the user ratifies or edits. Record the agreed set in `DESIGN-STANDARDS.md` — it becomes a **contract** that Prototyping (4), Stack (5), and Vibe Coding (8) enforce.

Propose at least the following, each framed as *standard / why / how it reconciles at Stack*, and let the user adjust:

- **Mobile-first** — design mobile-up; thumb-zone reachability, safe-area/notch insets, touch targets ≥ 44–48px.
- **Accessibility floor (non-negotiable)** — input font-size ≥ 16px (prevents iOS zoom-on-focus), WCAG AA contrast (≥ 4.5:1 text), semantic HTML + ARIA, visible focus and full keyboard nav, and honoring `prefers-reduced-motion`.
- **Motion — framer-motion on every element, SEO-safe** — purposeful motion that never blocks render or shifts layout (CLS), always gated by `prefers-reduced-motion`. Named as the strong default; reconciled against the chosen framework at Stage 5.
- **Navigation — Swup.js app-like transitions** — page transitions that feel like a native mobile app, especially between pages. Strong default; reconciled at Stage 5.
- **Visual consistency & component reuse (mandatory)** — design a coherent component system where every screen inherits from the same primitive set; no reinvention, one visual language across every surface (the build then reuses existing components rather than rebuilding them).
- **Forms & input masks** — apply masks by default on convenient fields (e.g. a numeric value via a text field with a mask), and set the right `inputmode` / input `type` / `autocomplete` so mobile shows the correct keyboard.
- **Media** — lazy-load images/video/gifs with a blurhash placeholder; use responsive delivery and modern efficient formats.
- **Perceived performance** — skeleton loaders / optimistic UI; `font-display: swap` + font preload to avoid layout shift.
- **Performance budget (SEO guard-rail)** — a Core Web Vitals budget that keeps the motion and transitions honest; motion that hurts LCP/CLS/INP is out of budget, not on-brand.
- **Designed states** — empty / loading / error / success are designed, not afterthoughts (this feeds Stage 4's states-per-screen).
- **Theming & icons** — dark mode / theming driven by tokens; a single coherent iconography set.
- **App-like shell** — PWA / installability where it fits; entrance and scroll animations are purposeful and lightweight, never blocking interaction.
- **i18n-ready** — copy and layout ready for the product's market language(s) (separate from the artifacts-in-English convention — see Language policy in SKILL.md).

Flex by stakes — prepare these alongside the other blocks so the batched menu coheres, then carry them into the single gate:

- `throwaway` — confirm only the accessibility floor plus two or three standards; note the rest as deferred.
- `mvp` — confirm the full set (in the one batched gate).
- `platform` — the full set plus explicit performance budgets and measurement.

### 6. Design tokens (W3C)

Translate the chosen visual identity into `design-tokens.json` following the **W3C Design Tokens** format — a stack-agnostic source, transformed later into CSS vars, Tailwind, etc. Structure:

- Each token is an object with **`$value`** and **`$type`** (e.g. `"color"`, `"dimension"`, `"fontFamily"`, `"fontWeight"`).
- Group by domain: `color`, `typography`, `spacing`, plus `radius`/`elevation` as needed.
- Encode **roles**, not raw values, at the semantic layer — reference primitives with `{color.brand.500}` aliases so themes stay swappable.

```json
{
  "color": {
    "brand":   { "500": { "$value": "#3B5BFF", "$type": "color" } },
    "primary": { "$value": "{color.brand.500}", "$type": "color" },
    "surface": { "$value": "#FFFFFF", "$type": "color" },
    "text":    { "$value": "#0B0B0F", "$type": "color" }
  },
  "spacing": {
    "1": { "$value": "4px",  "$type": "dimension" },
    "2": { "$value": "8px",  "$type": "dimension" }
  },
  "typography": {
    "fontFamily": { "body": { "$value": "Inter", "$type": "fontFamily" } },
    "scale":      { "md":   { "$value": "16px",  "$type": "dimension" } }
  }
}
```

Tokens are the handoff: keep them complete and consumable, because prototype and build read them directly.

## Deliverables

```
docs/brand/
├── BRAND.md            # name, positioning, tagline, core message, narrative
├── VOICE-TONE.md       # voice principles, tone-by-context, do/don't, glossary
├── VISUAL-IDENTITY.md  # palette, type, logo rules, spacing, components, mood
├── DESIGN-STANDARDS.md # experience & design standards: mobile-first, a11y, motion, nav, reuse, masks, media
└── design-tokens.json  # W3C tokens — stack-agnostic source of truth
```

Use the templates as the skeleton for each file:

- `assets/templates/deliverables/BRAND.md`
- `assets/templates/deliverables/VOICE-TONE.md`
- `assets/templates/deliverables/VISUAL-IDENTITY.md`
- `assets/templates/deliverables/DESIGN-STANDARDS.md`
- `assets/templates/deliverables/design-tokens.json`

All written content is in English (artifacts-in-English convention — see Language policy in SKILL.md). Conversation with the user follows their language; the files do not.

## Definition of Done

- [ ] Product **name defined** and refined at concept level (availability out of scope).
- [ ] `BRAND.md` complete: name, tagline, core message, narrative.
- [ ] `VOICE-TONE.md` complete: principles + tone-by-context table + do/don'ts + examples + glossary.
- [ ] `VISUAL-IDENTITY.md` complete: palette w/ roles, type scale, logo rules, iconography, spacing/grid, components, mood — as **direction**, no rendered logo.
- [ ] If visual references were provided as images, their design info was **extracted via a design-extraction skill** (`arvindrk/extract-design-system` or the find-skills-located equivalent; the degraded fallback noted if absent) and the extracted values are cited to their source references in `VISUAL-IDENTITY.md` (§8) / `DESIGN-STANDARDS.md` (§0).
- [ ] `DESIGN-STANDARDS.md` complete: all standards from Step 5 proposed and confirmed (kept/changed) by the user — sections 0–10 of the template filled — with framer-motion/Swup.js marked as defaults to reconcile at Stack, and any `ui-ux-pro-max` fallback rung noted.
- [ ] `design-tokens.json` exported in W3C format with `$value`/`$type`, role-based aliases, ready to consume downstream.
- [ ] Each directional block (naming, voice, visual) was presented with N distinct options and chosen by the user; the experience & design standards were proposed as a recommended baseline and confirmed (kept or changed) — all via the single batched gate, not assumed.

## The gate

The human decision in this stage is the **brand selection** — and Brand uses **one batched gate, not a stop per block.** Brand is reversible and low-stakes; gating naming, positioning, voice, and visual as four serial stops is over-gating that just slows the user down. Prepare all the directions, then present them together and STOP once.

Present, in a single batched proposal, the N distinct directions for each block — naming options, voice options, visual options (with positioning angles attached to the naming/voice they belong to) — so the user picks across all of them in one pass. Then refine the chosen set.

What makes a good batched gate here:

- Each block still offers **N genuinely distinct directions** (different strategy, not cosmetic variants). Three near-identical names is a fake choice — batching the gate does not lower this bar.
- Each option states its **trade-off** — what it wins and what it costs against the positioning.
- Each block leads with a **recommendation and reasoning**, so the user can pick the whole recommended set in one word or override individual blocks.
- Keep the menu coherent: show how a choice in one block plays with the others (this name + this voice + this visual), so the single pass is a real decision, not five disconnected lists.
- Present the **experience & design standards** as a recommended set for keep/change confirmation (not N competing options) — the user ratifies or edits the defaults, and the agreed set is written to `DESIGN-STANDARDS.md` as the contract Stages 4, 5, and 8 enforce.
- After the user picks the visual direction, surface the W3C `design-tokens.json` for confirmation before writing the file — they are the contract prototyping inherits. This token confirmation is a quick check on the chosen direction, not a re-opening of the batched gate.

For a `throwaway` spike, this collapses further — a couple of token choices, or skip the gate entirely (see *Right-size by stakes*). Propose once, then stop. The user's selections are what make the brand theirs.
