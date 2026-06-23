#!/usr/bin/env python3
"""Scaffold the AI Workflow planning structure into a target project root.

Creates docs/<stage>/ folders plus a fresh STATE.md heartbeat and an empty
GATES.md ledger, so a zero project is ready to begin Stage 1. Idempotent: never
overwrites an existing STATE.md or GATES.md (those carry live state).

Usage:
    python scaffold_workflow.py <project-root> [--idea "one-line idea"]
"""
import argparse
import os
import sys
from datetime import date

STAGES = [
    "discovery",
    "product",
    "brand",
    "prototype",
    "stack",
    "instrumentation",
]

STAGE_ROWS = [
    ("1", "Discovery", "in_progress"),
    ("2", "Scope", "pending"),
    ("3", "Brand", "pending"),
    ("4", "Prototyping", "pending"),
    ("5", "Stack", "pending"),
    ("6", "Instrumentation", "pending"),
    ("7", "Harness", "pending"),
    ("8", "Vibe Coding", "pending"),
]


def state_md(idea: str, today: str, stakes: str, lang: str) -> str:
    rows = "\n".join(
        f"| {n} | {name} | `{status}` | {'— (active)' if status == 'in_progress' else '—'} |"
        for n, name, status in STAGE_ROWS
    )
    return f"""# Workflow State — heartbeat

> Read this FIRST on every session. It is the single source of truth for where
> the project is in the pipeline. Reconcile it against GATES.md + the docs/ tree
> on resume, and keep its header current after every transition.

- **Project idea:** {idea or "TODO — capture the one-line idea + target users"}
- **Stakes:** {stakes}   <!-- throwaway | mvp | platform — dials the depth of every stage -->
- **Conversation language:** {lang or "TODO — detect or ask, then record here"}
- **Created:** {today}
- **Current stage:** 1 — Discovery
- **Last gate passed:** none yet

## Pipeline

| # | Stage | Status | Notes |
|---|-------|--------|-------|
{rows}

Statuses: `pending` · `in_progress` · `blocked` · `done`

## Next action

Begin Stage 1 (Discovery): propose a competitor list for the user to curate.
See the skill's `references/1-discovery.md`.

## Resume

> What a fresh session needs to pick up cleanly. Keep it to a few lines.

- **Blockers:** none
- **During the build (Stage 8):** the per-increment handoff lives in
  `PROGRESS.md` -> Resume notes (next gate, critical files+lines, failed
  approaches). Read it before resuming a slice.
"""


GATES_MD = """# Gates Ledger

> Append-only record of every human approval gate crossed. One entry per gate.
> A gate is only "passed" once recorded here with explicit approval.

<!-- Template for each entry:

## Gate — Stage N (<stage name>)
- **Date:** YYYY-MM-DD
- **Decision approved:** <what the human approved — e.g. final competitor list,
  MVP cut, chosen stack per layer, approved providers>
- **Approved by:** <name / "user">
- **Artifacts:** <links to the deliverables this gate signs off>
- **Notes:** <anything material — deferred items, conditions>

-->

_No gates passed yet._
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", help="target project root")
    ap.add_argument("--idea", default="", help="one-line project idea")
    ap.add_argument("--stakes", default="mvp",
                    choices=["throwaway", "mvp", "platform"],
                    help="stakes tier — dials the depth of every stage")
    ap.add_argument("--lang", default="", help="conversation language")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    docs = os.path.join(root, "docs")
    os.makedirs(docs, exist_ok=True)
    for s in STAGES:
        os.makedirs(os.path.join(docs, s), exist_ok=True)

    today = date.today().isoformat()

    state_path = os.path.join(docs, "STATE.md")
    if os.path.exists(state_path):
        print(f"skip  {state_path} (already exists — preserving live state)")
    else:
        with open(state_path, "w") as f:
            f.write(state_md(args.idea, today, args.stakes, args.lang))
        print(f"write {state_path}")

    gates_path = os.path.join(docs, "GATES.md")
    if os.path.exists(gates_path):
        print(f"skip  {gates_path} (already exists — preserving live state)")
    else:
        with open(gates_path, "w") as f:
            f.write(GATES_MD)
        print(f"write {gates_path}")

    print("\nScaffold complete. docs/ tree:")
    print(f"  {docs}/")
    print("    STATE.md  GATES.md")
    print("    " + "  ".join(s + "/" for s in STAGES))
    print("\nNext: confirm the project idea with the user, then begin Stage 1.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
