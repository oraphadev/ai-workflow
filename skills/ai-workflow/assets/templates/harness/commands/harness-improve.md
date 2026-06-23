---
description: Run the self-improvement loop — harvest the latest increment's learnings into knowledge/, then PROPOSE agent/prompt/skill refinements for ratification at the review gate. Self-improving, never self-rewriting.
---

# /harness-improve

Make the harness sharper after an increment, without silently rewriting the machine.
Learnings accumulate autonomously between gates; changes to the agents/skills land only
with human sign-off at the review gate.

Run this at an increment's review gate (typically right after `/new-feature` reaches its
human gate). Input: the increment just completed (use `$ARGUMENTS`, otherwise infer from
the latest spec/PR).

## Steps

1. **Harvest learnings.** Review what this increment taught — bugs and their root causes,
   pitfalls hit, conventions that emerged, decisions made. Pull from the spec, the diff, the
   review findings, and any verify-loop retries.
2. **Update `knowledge/`.** Write the durable learnings where they belong:
   - new or changed **ADRs** in `knowledge/adr/` (or `docs/`) for decisions made;
   - **patterns and anti-patterns** in `knowledge/patterns/`;
   - stack gotchas in `knowledge/stack/`;
   - append entries to `knowledge/learnings/`.
   These knowledge updates are part of the increment and can land directly.
3. **Propose agent/prompt/skill refinements — do not apply silently.** Identify where an
   agent or skill should change so the team doesn't re-make this increment's mistakes
   (a pitfall the Builder should now warn about; a convention the Reviewer should now enforce;
   a missing check in a gate skill). Draft the concrete edits and present them as a proposal.
4. **Ratify at the gate.** Present the proposed refinements for human sign-off. Apply only
   what's ratified. This is the line between self-improving and self-rewriting — never cross it.
5. **Record.** Note the ratified refinements (and who approved) so the harness's evolution
   stays legible; update `_registry.md` if an agent's dispatch rule changed.

## Done when

- The increment's learnings are captured in `knowledge/`.
- Concrete agent/prompt/skill refinements are proposed (not silently applied).
- Ratified refinements are applied and recorded; unratified ones are left for the human to decide.
