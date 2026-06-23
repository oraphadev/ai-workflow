# Prototype

> Conductor: fill each section. This documents the interactive prototype, the screens it covers,
> the UX decisions made, and how it validates against the PRD and user stories.

## 1. Tool & rationale

- **Tool chosen:** `<e.g. Figma | v0 | Framer | code (Next.js + Tailwind) | other>`
- **Why this tool:** `<2–3 sentences. Consider: fidelity needed, team familiarity, speed,
  handoff target (does it become real code?), interactivity required, cost.>`
- **Fidelity:** `<low / mid / high>`
- **Alternatives considered:** `<tool — why not>`

## 2. Prototype link

- **Live link:** `<URL>`
- **Access:** `<public | requires account | password: …>`
- **Version / last updated:** `<vX — YYYY-MM-DD>`

## 3. Screen ↔ route inventory

| Screen | Route | States covered | Status |
| ------ | ----- | -------------- | ------ |
| `<Home>` | `/` | `<default, loading, empty>` | `<Done / WIP / Todo>` |
| `<Login>` | `/login` | `<default, error, loading>` | `<...>` |
| `<Dashboard>` | `/dashboard` | `<default, empty, error>` | `<...>` |
| `<Detail>` | `/items/:id` | `<default, not-found>` | `<...>` |
| `<...>` | `<...>` | `<...>` | `<...>` |

> Cover meaningful states (loading / empty / error / success), not just the happy path.

## 4. UX decisions log

Record notable decisions and their reasoning so future changes have context.

| # | Decision | Rationale | Trade-off / alternative |
| - | -------- | --------- | ----------------------- |
| 1 | `<e.g. Single-page onboarding>` | `<reduce drop-off>` | `<less room to explain features>` |
| 2 | `<...>` | `<...>` | `<...>` |
| 3 | `<...>` | `<...>` | `<...>` |

## 5. Validation vs PRD / user stories

Check each requirement and user story is represented in the prototype.

- [ ] `<US-1: As a user, I can …>` — covered by `<screen/route>`
- [ ] `<US-2: …>` — covered by `<screen/route>`
- [ ] `<US-3: …>` — covered by `<screen/route>`
- [ ] All PRD core flows have a corresponding screen
- [ ] Every screen has an entry and an exit path (no dead ends)
- [ ] Error / empty / loading states exist for primary flows
- [ ] Copy follows VOICE-TONE.md
- [ ] Visuals follow VISUAL-IDENTITY.md / design-tokens.json

**Gaps / out of scope:** `<anything in the PRD intentionally not prototyped, and why>`

## 6. Exports

- **Design files:** `<link or path>`
- **Assets exported:** `<icons / images — format, location>`
- **Handoff notes:** `<specs, redlines, or "use design-tokens.json for values">`
- **Next step:** `<e.g. hand to engineering / build into the app>`

---

_Related deliverables: VISUAL-IDENTITY.md, VOICE-TONE.md, design-tokens.json, and the project PRD / user stories._
