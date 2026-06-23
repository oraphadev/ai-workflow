---
description: Regenerate the .codegraph/ map of modules, dependencies, and symbols so agents have an accurate picture before touching code.
---

# /code-graph-refresh

Refresh `.codegraph/` — the generated map of the codebase's modules, their dependencies, and
exported symbols. Agents MUST consult this map before editing code, to understand impact and
avoid duplicating what already exists.

## Steps

1. Scan the repo for source modules and their dependency edges (imports/exports).
2. Extract exported symbols (functions, classes, types, components, endpoints) per module.
3. Write/overwrite the map under `.codegraph/` (e.g. `modules.json`, `dependencies.json`,
   `symbols.json`, plus a human-readable `.codegraph/README.md` summary).
4. Note removed or newly added modules versus the previous run.
5. Report a short summary: module count, notable new/removed edges, and any cycles detected.

## When to run

- After any structural change (new modules, moves, renames, deleted code).
- Before large refactors, so impact analysis is accurate.
- Ideally wired into CI by DevOps so the map never goes stale.

## Reminder for all agents

Before touching code, **read `.codegraph/`** to find the right module, reuse existing symbols,
and assess blast radius. Do not duplicate code the graph already shows exists.
