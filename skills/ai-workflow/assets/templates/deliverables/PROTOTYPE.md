# Prototype

> Conductor: fill each section. This documents the interactive prototype — the content decided per screen,
> the reusable component arsenal built before any screen, the screens composed from it, the UX decisions
> made, and how it validates against the PRD and user stories.
> Order is a contract: define content (§3) → build the arsenal (§4) → assemble screens (§5). No screen is
> assembled before the arsenal is complete; any new custom component is added to the arsenal first.

## 1. Tool & rationale

- **Tool chosen:** `<e.g. Figma | v0 | Framer | code (Next.js + Tailwind) | other>`
- **Why this tool:** `<2–3 sentences. Consider: fidelity needed, team familiarity, speed,
  handoff target (does it become real code?), interactivity required, cost.>`
- **Fidelity:** `<low / mid / high>`
- **ui-ux-pro-max routing:** `<installed & used | fallback to frontend-design (degraded rung) — reason>`
- **Alternatives considered:** `<tool — why not>`

## 2. Prototype link

- **Live link:** `<URL>`
- **Access:** `<public | requires account | password: …>`
- **Version / last updated:** `<vX — YYYY-MM-DD>`

## 3. Screen content & copy spec (Phase A — decided before any pixel)

> For every MVP screen, decide the content BEFORE drawing it. Every block, datum, and string traces to a
> user story, a PRD data entity, or a defined value prop. Real, representative data only — never lorem /
> placeholder. Real copy only — written to VOICE-TONE.md, never improvised AI filler. If a content source
> doesn't exist upstream, flag it / re-open Scope — do not invent it.

<!-- DISPOSABLE example block — duplicate per screen, replace contents. -->
### Screen: `<Home>` — serves `<US-01>`

- **Purpose:** `<the one job this screen does for the user>`
- **Content blocks (top → bottom, by importance):**
  1. `<block — what it is, why it's here>`
  2. `<block — …>`
- **Real data shown:** `<entities/fields from the PRD + realistic representative values>`
- **Real copy:**
  - Heading: `<exact text>`
  - CTA(s): `<exact label(s)>`
  - Microcopy / helper: `<exact text>`
  - Empty / error / success messages: `<exact text for the applicable states>`
- **Applicable states:** `<empty | loading | error | success — which apply, which don't and why>`

## 4. Component inventory (Phase B — the arsenal, built before any screen)

> Derive every component the screens need from §3, then prototype each one — all variants, all relevant
> states, BOTH desktop and mobile, from brand tokens — before assembling any screen. The conductor's hard
> internal checkpoint: no screen is assembled until this inventory is complete.

<!-- DISPOSABLE example rows — replace, don't ship verbatim. -->
| Component | Level | Variants | States | Viewports | Props / usage |
| --------- | ----- | -------- | ------ | --------- | ------------- |
| `<Button>` | atom | `<primary, secondary, ghost>` | `<default, hover, focus, disabled, loading>` | desktop, mobile | `<label, onClick, icon?>` |
| `<Card>` | molecule | `<default, featured>` | `<default, loading, empty>` | desktop, mobile | `<title, body, action?>` |
| `<NavBar>` | organism | `<top, bottom-mobile>` | `<default, active-item>` | desktop, mobile | `<items, current>` |

- [ ] Arsenal complete: every component §3 calls for is prototyped (variants + states, desktop + mobile) and listed above — checked before any screen in §5 was assembled.

## 5. Screen ↔ route inventory (Phase C — screens composed from the arsenal)

<!-- DISPOSABLE example rows below — replace, don't ship verbatim.
     The US column lists the PRD user-story IDs (US-NN) each screen serves.
     Components used must all exist in §4 — screens compose the arsenal, they don't invent. -->
| Screen | Route | US (stories) | States covered | Viewports | Components used | Status |
| ------ | ----- | ------------ | -------------- | --------- | --------------- | ------ |
| `<Home>` | `/` | `<US-01>` | `<default, loading, empty>` | `<desktop, mobile>` | `<Header, Card, EmptyState>` | `<Done / WIP / Todo>` |
| `<Login>` | `/login` | `<US-02>` | `<default, error, success>` | `<desktop, mobile>` | `<AuthForm, Button>` | `<...>` |

> Cover meaningful states (loading / empty / error / success), not just the happy path.
> Every screen has both **desktop and mobile** viewports, and every component in "Components used" exists in §4.

## 6. UX decisions log

Record notable decisions and their reasoning so future changes have context.

| # | Decision | Rationale | Trade-off / alternative |
| - | -------- | --------- | ----------------------- |
| 1 | `<e.g. Single-page onboarding>` | `<reduce drop-off>` | `<less room to explain features>` |
| 2 | `<...>` | `<...>` | `<...>` |

## 7. Validation vs PRD / user stories

Check each requirement and user story is represented in the prototype.

- [ ] `<US-01: As a user, I can …>` — covered by `<screen/route>` (`<states>`, desktop + mobile)
- [ ] `<US-02: …>` — covered by `<screen/route>`
- [ ] All PRD core flows have a corresponding screen and a navigable end-to-end path (Phase D)
- [ ] Every screen has an entry and an exit path (no dead ends)
- [ ] Error / empty / loading states exist for primary flows
- [ ] All screen copy is the real copy from §3, written to VOICE-TONE.md — no AI filler or placeholder text
- [ ] Visuals follow VISUAL-IDENTITY.md / design-tokens.json and DESIGN-STANDARDS.md

**Gaps / out of scope:** `<anything in the PRD intentionally not prototyped, and why>`

## 8. Exports

- **Component arsenal:** `<exports/components/ — where the tool allows export>`
- **Screens (desktop + mobile):** `<exports/screens/<screen>-{desktop,mobile}.png>`
- **Assets exported:** `<icons / images — format, location>`
- **Handoff notes:** `<specs, redlines, or "use design-tokens.json for values">`
- **Next step:** `<e.g. hand to engineering / build into the app — reuse the arsenal as the build's components>`

---

_Related deliverables: VISUAL-IDENTITY.md, VOICE-TONE.md, DESIGN-STANDARDS.md, design-tokens.json, and the project PRD / user stories._
