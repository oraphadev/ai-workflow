---
description: Run the loop-driven SDD loop for a new feature — spec → plan → distribute → build → verify → learn → refine, iterating until the acceptance criteria and gates pass, then stopping at the human review gate.
---

# /new-feature

Run the loop-driven SDD loop for a new feature. Input: a PRD user story (use `$ARGUMENTS`
if provided, otherwise ask for it). The Orchestrator drives this and never codes
monolithically — it decomposes, delegates, verifies, and integrates.

This is a **loop**, not a one-way pass. The middle steps iterate
(`build → verify → learn → refine`) until every acceptance criterion and every gate is
green, then the loop **stops at the human review gate**.

## Steps

1. **Spec** — Dispatch **PM** to convert the user story into `specs/<feature>/spec.md` with
   explicit, testable acceptance criteria and clear scope. Get it approved before any code.
2. **Plan** — Dispatch **Architect** to design the solution, record ADRs in `docs/`, and break
   the spec into tasks. Consult `knowledge/` (and `.codegraph/` where present) for impact and reuse.
   If the work needs a specialist the team lacks, run `/add-specialist-agent` first.
3. **Distribute** — As **Orchestrator**, assign tasks to the right specialists (parallel where
   independent), each one funneled to this project per `.claude/agents/_registry.md`.
4. **Build** — Specialists implement against the spec, reusing existing modules and following
   `knowledge/conventions/` and the project's anti-patterns.
5. **Verify** — Dispatch **QA** to confirm every acceptance criterion is tested and CI is green
   (tests + lint + typecheck + build). Failing AI evals block too, where they apply.
6. **Learn → refine** — Capture what this increment taught (note candidates for
   `knowledge/learnings/`). **If any verify gate failed, refine and loop back to step 4.**
   Iterate until acceptance criteria + gates pass — then continue.
7. **Review (human gate)** — Dispatch the independent **Code Reviewer** to approve against
   standards and the PR checklist; block on any unresolved finding. Then **STOP** and present
   for human ratification. The loop's autonomy ends here.
8. **Integrate / Deploy** — Once the human ratifies: as Orchestrator, merge with CI green and
   the Definition of Done met. Dispatch **DevOps** to ship, **Observability** to confirm health,
   **Data Analyst** to validate tracking, and **Docs** to update knowledge/runbooks — where those
   roles are activated.
9. **Close the increment** — Run `/harness-improve` to harvest learnings into `knowledge/` and
   propose any agent/prompt/skill refinements for ratification.

## Done when

- Spec approved and implemented; all acceptance criteria tested and passing.
- CI green, independent review approved, human ratified, Definition of Done met.
- Deployed/healthy/tracked/documented where those roles apply.
- Learnings harvested and any harness refinements proposed.
