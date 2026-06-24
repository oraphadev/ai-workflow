# Design Standards

> Conductor: this is the **experience & design standards contract** for the product — proposed by you in Stage 3 (Brand), confirmed (kept or changed) by the user at the batched gate, then **enforced** by Prototyping (Stage 4) and Vibe Coding (Stage 8).
> Fill each row with the agreed standard. Keep framer-motion / Swup.js as **defaults to reconcile at Stage 5 (Stack)** if the stack isn't web/React. Flex the depth by the Stakes tier in `docs/STATE.md`.

## 0. Status

- **Stakes tier:** `<throwaway | mvp | platform>`
- **ui-ux-pro-max routing:** `<installed & used | fallback to frontend-design (degraded rung) — reason>`
- **References used:** `<Mobbin sets / screenshots / live sites the visual direction was derived from>`

## 1. Mobile-first

- Design mobile-up; thumb-zone reachability; safe-area / notch insets.
- Touch targets: `<≥ 44–48px>`
- Breakpoints: `<the mobile-up breakpoints>`

## 2. Accessibility floor (non-negotiable)

- Input font-size: `<≥ 16px — prevents iOS zoom-on-focus>`
- Contrast: `<WCAG AA, ≥ 4.5:1 body text>`
- Semantic HTML + ARIA; visible focus; full keyboard navigation.
- Honor `prefers-reduced-motion`: `<how motion degrades>`

## 3. Motion (framer-motion — SEO-safe)

- Library: `<framer-motion (default) | reconciled equivalent — set at Stack>`
- Rule: purposeful motion on every element that benefits from it; never blocks render or causes layout shift (CLS); always gated by `prefers-reduced-motion`.
- Token-driven: durations/easings from `design-tokens.json` (`duration`, `easing`).

## 4. Navigation (Swup.js — app-like)

- Library: `<Swup.js (default) | reconciled equivalent — set at Stack>`
- Rule: page transitions feel like a native mobile app, especially between pages.

## 5. Visual consistency & component reuse (mandatory)

- Design a coherent component system; every screen inherits from the same primitive set — one visual language across every surface.
- No reinvention: the build reuses existing components rather than rebuilding them.

## 6. Forms & input masks

- Apply masks by default on convenient fields: `<which fields, which masks — e.g. numeric value via text field with mask>`
- Correct `inputmode` / input `type` / `autocomplete` per field for the right mobile keyboard.

## 7. Media

- Lazy-load images / video / gifs with a **blurhash** placeholder.
- Responsive delivery with modern, efficient formats.

## 8. Perceived performance & SEO budget

- Skeleton loaders / optimistic UI on data-backed views.
- `font-display: swap` + font preload (anti-CLS).
- Core Web Vitals budget: `<LCP / CLS / INP targets — the guard-rail that keeps motion honest>`

## 9. Designed states & shell

- Designed empty / loading / error / success states (feeds Stage 4 states-per-screen).
- PWA / installability: `<in scope?>`; entrance/scroll animations are purposeful and lightweight, never blocking interaction (motion library resolved at Stage 5).

## 10. Theming, iconography & i18n

- Dark mode / theming via tokens: `<in scope?>`
- Single iconography set: `<which>`
- i18n-ready copy & layout for the product's market language(s).

---

> Enforced downstream: Stage 4 (Prototyping) honors these per screen; Stage 5 (Stack) reconciles the motion/navigation libraries; Stage 8 (Vibe Coding) gates each UI slice against this contract.

_Related deliverables: VISUAL-IDENTITY.md (palette/type driving the accessibility contrast check), design-tokens.json (motion duration/easing referenced in §3), BRAND.md (naming/positioning context)._
