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

- **`frontend-design` skill** — load it before proposing visual directions. It steers toward distinctive, intentional choices (real typographic personality, a palette with a point of view) and away from the templated defaults that make every option look the same. Use it to pressure-test that your N visual directions are genuinely different, not three shades of the same safe gray.
- **Figma MCP (optional)** — only if the user wants the palette or type scale *materialized* to look at. Useful as a preview. It does not change the deliverable: the source of truth stays `VISUAL-IDENTITY.md` + `design-tokens.json`, never a Figma file. Don't let a Figma round-trip become the artifact.
- **W3C Design Tokens** — the format for `design-tokens.json` (see Steps). Stack-agnostic on purpose, so it transforms later into CSS variables, Tailwind config, iOS, etc., without re-deciding anything.

## Steps

The spine of this stage is one repeated gate rhythm: **for each block, propose N distinct directions → user picks one → you refine it.** Naming, positioning, voice, and visual each run this loop independently. Don't bundle all four into one mega-proposal — the user makes a *real* choice per block, and each chosen block constrains the next (the picked name flavors the voice; the voice flavors the visual register). Run them in order; let earlier picks inform later options.

### 1. Naming

Generate candidates concept-first, then validate at the concept level only — **availability checks (domains, trademarks) are out of scope here** and belong to a later operational step. Offer a spread of *approaches*, not just a list of words:

- **Descriptive** (says what it does), **evocative/metaphorical** (suggests a feeling), **invented/coined** (ownable, blank-slate), **compound/portmanteau**, **real-word repurpose**.
For each candidate give: meaning, why it fits the positioning, pronunciation/spelling risk, and rough connotations. Present a few approaches; recommend one with reasoning, then stop for the pick. Refine the chosen name (spelling, casing, optional sub-brand or product-line logic) after selection.

### 2. Positioning

From the chosen name, draft the verbal core: **tagline** (one line, memorable), **core message** (the one-sentence promise), and **brand narrative** (a short paragraph — origin, problem, stance). Propose a couple of distinct angles (e.g. bold/contrarian vs. warm/reassuring) so the user steers the personality before you write the voice guide on top of it.

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

### 5. Design tokens (W3C)

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
└── design-tokens.json  # W3C tokens — stack-agnostic source of truth
```

Use the templates as the skeleton for each file:

- `assets/templates/deliverables/BRAND.md`
- `assets/templates/deliverables/VOICE-TONE.md`
- `assets/templates/deliverables/VISUAL-IDENTITY.md`
- `assets/templates/deliverables/design-tokens.json`

All written content is in English (artifacts triglot rule). Conversation with the user follows their language; the files do not.

## Definition of Done

- [ ] Product **name defined** and refined at concept level (availability out of scope).
- [ ] `BRAND.md` complete: name, tagline, core message, narrative.
- [ ] `VOICE-TONE.md` complete: principles + tone-by-context table + do/don'ts + examples + glossary.
- [ ] `VISUAL-IDENTITY.md` complete: palette w/ roles, type scale, logo rules, iconography, spacing/grid, components, mood — as **direction**, no rendered logo.
- [ ] `design-tokens.json` exported in W3C format with `$value`/`$type`, role-based aliases, ready to consume downstream.
- [ ] Each block was chosen by the user via the N-directions gate, not assumed.

## The gate

The human decisions in this stage are the **selections per block** — there are several gates, not one. For each block (naming, positioning, voice, visual), present **N distinct options** with their trade-offs and a clear recommendation, then STOP and wait for the pick. Refine only after the user chooses; carry the choice into the next block.

What makes a good gate here:

- Options must be **genuinely distinct** (different strategy, not cosmetic variants). Three near-identical names is a fake choice.
- Each option states its **trade-off** — what it wins and what it costs against the positioning.
- Give a **recommendation with reasoning**, so the user can defer to judgment or override.
- After the visual pick, surface tokens for confirmation before writing the file — they are the contract prototyping inherits.

Propose, then stop. The user's selections are what make the brand theirs.
