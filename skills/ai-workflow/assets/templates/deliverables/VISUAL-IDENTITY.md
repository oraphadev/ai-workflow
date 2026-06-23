# Visual Identity

> Conductor: this is a **visual SPEC / direction document — NOT a rendered logo or generated asset.**
> It describes how the brand should look so a designer or a tokens file (design-tokens.json) can implement it.
> Keep consistent with BRAND.md (personality) and VOICE-TONE.md.

## 1. Direction

`<2–4 sentences describing the overall visual feeling: e.g. "Minimal, high-contrast,
confident. Generous whitespace, one strong accent color, geometric type." Tie back to brand personality.>`

- Keywords: `<3–5 adjectives>`
- Avoid: `<visual clichés / styles that would feel off-brand>`

## 2. Color palette

Each color has a **role**, not just a hex. Implement exact values in `design-tokens.json`.

| Token role | Example hex | Role / when to use |
| ---------- | ----------- | ------------------ |
| Primary | `#<hex>` | `<main brand color — primary actions, key accents>` |
| Secondary | `#<hex>` | `<support color — secondary actions, accents>` |
| Surface | `#<hex>` | `<backgrounds, cards, containers>` |
| Text | `#<hex>` | `<default body text on surface>` |
| Success (semantic) | `#<hex>` | `<positive states, confirmations>` |
| Warning (semantic) | `#<hex>` | `<caution states>` |
| Error (semantic) | `#<hex>` | `<destructive / failure states>` |

- Contrast: `<note WCAG target, e.g. text/surface ≥ 4.5:1>`
- Dark mode: `<in scope? mapping notes if so>`

## 3. Typography

| Role | Font family | Size | Weight | Use |
| ---- | ----------- | ---- | ------ | --- |
| Display | `<font>` | `<e.g. 48px>` | `<e.g. 700>` | `<hero headlines>` |
| Heading | `<font>` | `<e.g. 32px>` | `<e.g. 600>` | `<section titles>` |
| Body | `<font>` | `<e.g. 16px>` | `<e.g. 400>` | `<paragraphs>` |
| Caption | `<font>` | `<e.g. 13px>` | `<e.g. 400>` | `<labels, metadata>` |
| Mono | `<font>` | `<e.g. 14px>` | `<e.g. 400>` | `<code, numeric data>` |

- Type scale ratio: `<e.g. 1.25 (major third)>`
- Line height: `<e.g. body 1.5, headings 1.2>`

## 4. Logo rules

> Described in words — **no logo is rendered or generated in this document.**

- Concept: `<wordmark | symbol + wordmark | monogram — described>`
- **Clear space:** `<e.g. minimum padding = height of the "x" / logo mark on all sides>`
- **Minimum size:** `<e.g. 24px tall on screen>`
- **Do:** `<e.g. use on approved surface colors; keep proportions locked>`
- **Don't:** `<e.g. recolor, stretch, add shadows, place on busy backgrounds>`

## 5. Iconography & illustration

- Icon style: `<e.g. line icons, 2px stroke, rounded joins, 24px grid>`
- Illustration direction: `<e.g. flat geometric, limited palette, no gradients>`
- Source / set: `<e.g. Lucide, custom, etc.>`

## 6. Spacing & grid

- Base unit: `<e.g. 4px>`
- Spacing scale: `<e.g. 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64>`
- Grid: `<e.g. 12-column, max content width 1200px, gutter 24px>`
- Corner radii: `<e.g. 4px controls, 8px cards, full for pills>`

## 7. Key components

`<List the core UI components this identity must cover. e.g.:>`

- Buttons (primary / secondary / ghost / destructive)
- Inputs & form fields (default / focus / error / disabled)
- Cards
- Navigation (top bar / sidebar)
- Modals & toasts
- `<...>`

## 8. Mood & references

- Mood: `<one line>`
- References: `<links or named examples and what to borrow from each>`

---

> **Note:** This document is **direction / spec only**. No rendered logo asset is produced here.
> Color/type/spacing values should be encoded in `design-tokens.json` for implementation.
