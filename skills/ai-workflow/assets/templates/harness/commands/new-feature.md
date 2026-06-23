---
description: Kick off the Spec-Driven Development loop for a new feature — from a PRD user story to a deployed, gated change.
---

# /new-feature

Start the SDD loop for a new feature. Input: a PRD user story (use `$ARGUMENTS` if provided,
otherwise ask for it). The Orchestrator runs this end to end and NEVER codes monolithically.

## Steps

1. **Spec** — Dispatch **PM** to convert the user story into `specs/<feature>/spec.md` with
   explicit, testable acceptance criteria and clear scope. Get it approved before any code.
2. **Plan** — Dispatch **Architect** to design the solution, record ADRs in `docs/`, and break
   the spec into tasks. Consult `.codegraph/` for impact and reuse.
3. **Distribute** — As **Orchestrator**, assign tasks to the right specialists
   (Frontend, Backend, Data/DBA, DevOps, etc.). Run independent tasks in parallel.
4. **Build** — Specialists implement against the spec, reusing existing modules per the
   code graph and following `knowledge/conventions/`.
5. **Verify gates** — Dispatch **QA** to confirm every acceptance criterion is tested and CI
   is green (tests + lint + typecheck + build). Failing AI evals block too.
6. **Review** — Dispatch the independent **Code Reviewer** to approve against standards and
   the PR checklist. Block merge on any unresolved finding.
7. **Integrate** — As Orchestrator, merge only when CI is green, review is approved, and the
   Definition of Done is met.
8. **Deploy** — Dispatch **DevOps** to ship; **Observability** confirms health; **Data Analyst**
   validates tracking; **Docs** updates knowledge/runbooks.

## Done when

- Spec approved and implemented; all acceptance criteria tested and passing.
- CI green, independent review approved, Definition of Done met.
- Deployed, healthy, tracked, and documented.
