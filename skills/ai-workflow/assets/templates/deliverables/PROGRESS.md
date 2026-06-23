# Build Progress

> Live tracker of vertical slices and foundation work. Update as you ship.
> Status legend: ⬜ not started · 🟡 in progress · ✅ done · ⛔ blocked

## Slices

| Slice | Status | Spec | Deployed? | Notes |
| --- | --- | --- | --- | --- |
| `<Slice 1 — name>` | ⬜ | `<specs/slice-1.md>` | No | `<...>` |
| `<Slice 2 — name>` | ⬜ | `<specs/slice-2.md>` | No | `<...>` |
| `<...>` | ⬜ | `<...>` | No | `<...>` |

## Resume notes (active increment)

> The handoff for "one increment, one context": enough for a FRESH session to
> resume this slice without re-walking dead ends. Overwrite per increment.

- **Active slice:** `<slice name + specs/ path>`
- **Next unmet gate:** `<the specific check still red — e.g. "Verify: payment webhook test failing">`
- **Critical files (with line numbers):** `<path:line — why it matters>`
- **Failed approaches (don't retry):** `<what was tried + why it didn't work>`

## Foundation checklist

> Day-1 scaffolding that everything else builds on. Aim to deploy on day one.

- [ ] Auth (sign-up / sign-in / sessions)
- [ ] App layout + navigation shell
- [ ] Design tokens / theme
- [ ] Base infra (DB, migrations, env wiring)
- [ ] CI pipeline (lint, type-check, test)
- [ ] Deploy day-1 (staging URL live, even if empty)

## Pending items

> Known work not yet captured in a slice. Promote to a slice when picked up.

- [ ] `<pending item>`
- [ ] `<pending item>`
