---
description: Define a NEW project-specialized subagent on demand — funnel it to this stack/domain/conventions, write it into .claude/agents/, and register it. For when the build surfaces a need the roster doesn't cover.
---

# /add-specialist-agent

Grow the team. The 15-role roster is a seed, not a ceiling — when an increment surfaces a
need no existing agent covers (a realtime-gateway specialist, an LGPD-compliance auditor, a
Stripe-webhooks agent), define a *new* agent funneled to this project and register it.

Input: the gap/need (use `$ARGUMENTS` if provided, otherwise ask: "What capability is
missing, and what work will this agent own?").

A generic add is still a bug. The leverage is an agent that knows *this* codebase — its
stack, conventions, and anti-patterns — not a reusable role description.

## Steps

1. **Name the gap.** State precisely what work the team can't currently do well, and why an
   existing agent (or `/harness-improve`-refining one) isn't the right fit. If an existing
   agent should just be sharpened instead, do that via `/harness-improve` and stop here.
2. **Check the registry.** Read `.claude/agents/_registry.md` to confirm no activated or
   dormant role already covers this. If a *dormant* role fits, activate and funnel that one
   rather than inventing a new agent.
3. **Funnel the agent to this project.** Draft the agent file: name it to the
   stack/domain/module (e.g. *Realtime-Gateway (WebSocket) Specialist*), give it a precise
   responsibility and dispatch trigger, and bind it to the real conventions and anti-patterns
   from `knowledge/` and the decisions in `docs/`. No generic boilerplate.
4. **Write it** into `.claude/agents/<agent-name>.md`.
5. **Register it.** Add a row to `.claude/agents/_registry.md`: name, what it specializes in,
   when to dispatch it, and that it was added on demand (with the date and the triggering need).
6. **Confirm.** Report the new agent and how the Orchestrator should dispatch it.

## Done when

- A new, project-funneled agent exists in `.claude/agents/` (not generic).
- `_registry.md` records it with its dispatch rule and provenance.
- The Orchestrator can now route the previously-uncovered work to it.
