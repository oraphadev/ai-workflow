# Stage 5 — Stack Definition

> Pick every layer on purpose, with the trade-offs on the table: the user chooses frontend, backend, data, auth, and infra, and you lock in versions and an architecture concrete enough to provision against and build on.

## Objective

Choose and justify the full technical stack — frontend, backend, data, auth, infra — aligned to the scope (`docs/product/`) and the prototype (`docs/prototype/`), then define an architecture concrete enough to build from: a diagram, a data model, a folder structure, and the data flow.

Stack depth flexes by the `docs/STATE.md` Stakes tier: a *throwaway* project wants minimal sane defaults and little ceremony, while a *platform* warrants the full treatment — every layer justified, versions pinned, and ADRs for the load-bearing calls. Scale the rigor below to the tier; don't gold-plate a throwaway or under-document a platform.

This stage precedes Instrumentation deliberately, and that ordering is the whole point: services get provisioned *against a decided stack*, not guessed at. Instrumentation reads `STACK.md` to know which database to stand up, which auth provider to wire, which hosting target to configure — so if the stack is vague or undecided here, Instrumentation has nothing firm to provision. Decide the stack first; provision second. Likewise, the Harness scaffolds *on* this stack — the folder structure and framework choices you record become the skeleton the next stage fills. Knowledge compounds forward only if the decisions are explicit and versioned.

## Inputs

You are choosing technology to fit decisions already made — so read them before recommending anything:

- **Scope — `docs/product/`.** The MVP cut, the must-have features, the non-functional constraints (scale, latency, compliance, budget). These bound the stack: a real-time collaborative feature pushes toward a particular data layer; a tight budget rules out certain managed services. Don't recommend in a vacuum — recommend against the scope.
- **Prototype — `docs/prototype/`.** The shape of the UI and the interaction model inform frontend framework, styling approach, and UI library. If the prototype leans on rich client state or heavy interactivity, that's a signal for the frontend decision.
- **Initial data entities — from `PRD.md` (Stage 2).** The PRD already names the core entities. Pull that list forward as the *seed* of the data model; this stage elaborates them into relations, fields, and constraints. You are not inventing the entity list here — you are maturing an existing one.

Confirm the Prototyping gate has passed: `docs/GATES.md` should record acceptance of Stage 4 and `docs/STATE.md` should show Stage 5 `in_progress`. If the prototype wasn't accepted, the UI signals you'd lean on aren't trustworthy yet — resolve that before deciding the frontend.

## Capability routing

- **Per-layer recommendation is the gate mechanic.** For each layer you present options *with explicit trade-offs* and the human chooses. Don't pre-decide and ask for rubber-stamping — surface real alternatives so the choice is informed (see The gate).
- **`claude-api` skill — for any AI/LLM feature.** If the scope includes AI features (chat, generation, classification, agents, RAG…), route to `claude-api` for model ids, pricing, context windows, and capabilities. Do not pull model details from memory — they drift, and a wrong model id or stale price poisons every downstream cost and capability assumption. Treat the skill as the source of truth for anything Claude/Anthropic-shaped.
- **Architecture diagram — Figma or inline Mermaid.** For the diagram in `ARCHITECTURE.md`, either route to the `figma-generate-diagram` skill (which renders Mermaid into FigJam) or write an inline Mermaid block directly in the markdown. Inline Mermaid is the lighter default and keeps the diagram versioned next to the prose; reach for Figma when the user wants a shareable visual artifact.

## Steps

### 1. Recommend options per layer — the user chooses each

For every layer — frontend, backend, data, auth, infra — present a small set of viable options with honest trade-offs (maturity, ecosystem, hosting fit, learning curve, cost, lock-in). Lead with a recommendation per layer and say *why* it fits this scope, but keep at least one credible alternative live so the user can push back. The user decides each layer; you don't decide for them. This is the human-in-the-loop that defines the stage — the layers are the gate.

**When the user is non-technical, translate the choice — don't dilute it.** For a non-technical founder, frame each layer in **plain-language consequences they actually own — cost, lock-in, and speed-to-build** — with a clear recommendation, and tuck the engineering trade-offs (maturity, ecosystem, peer requirements) behind a short "details" fold for whoever reviews it later. The accommodation is *presentation*, not abdication: it must stay a **real, recommended-and-confirmed decision** — you surface a credible alternative they could pick instead and they actively confirm, never a rubber-stamp where the AI picks and they only click yes. If they can't tell you *why* one option beats the other in their own terms, you haven't explained the consequences plainly enough — keep going until the choice is genuinely theirs.

### 2. Decide the five layers

Drive each layer to a concrete decision, not a hand-wave:

- **Frontend** — framework, styling approach, UI component library.
- **Backend** — runtime, framework, API style (REST / GraphQL / RPC).
- **Data** — database, ORM/query layer, cache (if any).
- **Auth** — provider/approach (managed service vs. self-rolled, session vs. token).
- **Infra / deploy / hosting** — where it runs, how it ships, the deploy target. The *shippable artifact* form depends on project type — a live URL, an npm/pip package, a compiled binary, a mobile app build (TestFlight/Play) — so name the artifact, not just "deploy".

> **AI-native overlay — only if the product is AI-native.** Skip this entirely for a product that merely *has* an AI feature; engage it when the LLM *is* the product (a RAG app, an agent, a generation pipeline). Then the stack gains a sixth decision: the **model** (id, context window, fallback — sourced from `claude-api`, not memory), the **vector store / retrieval layer** (if it does RAG), and an explicit **cost-and-latency-per-query budget** so the unit economics are a decision, not a surprise at the bill. Treat these like any other layer — recommended with alternatives, chosen by the user at the gate.

Each choice should trace back to a scope or prototype signal — a decision with no rationale is a decision you can't defend at the gate or revisit later. Keep choices compatible across layers (the ORM must support the database; the hosting must run the runtime); incompatibility surfaced now is cheap, surfaced at Harness time is expensive.

### 3. Decide key libraries per domain

Below the framework level, name the workhorse libraries: forms, validation, client/server state, data fetching, dates, testing, and so on. These aren't afterthoughts — they shape the developer experience and the code the Harness will scaffold. Pick deliberately and record each with its purpose, so the next stage isn't improvising.

Also record the **test / lint / type-check / build commands for *this* stack** — they are chosen per stack, not assumed to be the JS/web set. Python is pytest/ruff/mypy; Rust is cargo test/clippy/build; Go is go test/vet/build; iOS is xcodebuild. Capture the exact commands so specs (Verification) and the Harness run the right ones rather than defaulting to `npm`.

### 4. Record decisions, trade-offs, versions, and compatibilities

For every decision capture *why it won*, the *alternatives considered*, the *pinned version*, and the *compatibility notes* (peer requirements, known conflicts, minimum runtime). Versions matter: "Next.js" is not a decision, "Next.js 15.x on Node 20" is. Pinning now is what lets Instrumentation provision the right service versions and the Harness install a coherent dependency set on the first try. Unversioned choices defer the hard part to a worse moment.

### 5. Define the architecture

Produce a buildable architecture, not a sketch:

- **Diagram** — components and their relationships (client, server, data store, auth, third-party services). Inline Mermaid in `ARCHITECTURE.md` or via `figma-generate-diagram`.
- **Data model** — entities, fields, types, and relations. Start from the PRD's initial entities (Stage 2) and elaborate them: keys, foreign keys, cardinalities, indexes that the scope implies. An ER diagram (Mermaid `erDiagram`) reads well here.
- **Folder structure** — the directory layout the Harness will scaffold against. Make it concrete enough that the next stage copies it rather than reinvents it.
- **Data flow** — how a representative request moves through the system (UI → API → data → back), including where auth and validation sit. This is what catches design gaps before any code exists.

## Deliverables

Write into `docs/stack/`, in English, using the templates at `assets/templates/deliverables/`:

```
docs/stack/
  STACK.md          # template: deliverables/STACK.md         — the five layers + per-layer justification
  DEPENDENCIES.md   # template: deliverables/DEPENDENCIES.md  — key libraries + pinned versions + purpose
  ARCHITECTURE.md   # template: deliverables/ARCHITECTURE.md  — diagram + data model + folder structure + data flow
```

- **`STACK.md`** — frontend, backend, data, auth, infra, each with the decision, the alternatives weighed, and the justification tied to scope/prototype.
- **`DEPENDENCIES.md`** — the key libraries per domain, each with a pinned version, its purpose, and compatibility notes.
- **`ARCHITECTURE.md`** — the architecture diagram, the elaborated data model (entities/relations), the folder structure, and the data flow.

## Definition of Done

- [ ] All five layers (frontend, backend, data, auth, infra) decided by the user, each with a justification tied to scope or prototype.
- [ ] Key libraries per domain chosen, each recorded with a pinned version and its purpose.
- [ ] Versions and cross-layer compatibilities verified and recorded — no unversioned decisions.
- [ ] AI/LLM model details (if any) sourced from `claude-api`, not memory — and for an **AI-native** product, the model + vector store + a cost/latency-per-query budget are decided.
- [ ] `ARCHITECTURE.md` defines diagram + data model (elaborated from PRD entities) + folder structure + data flow.
- [ ] All three deliverables written to `docs/stack/`, in English, following the templates.
- [ ] Stack is concrete enough to provision services (Instrumentation) and scaffold the harness (Harness).

## The gate

The human decision here is *choosing the stack, layer by layer*. Don't present a finished stack as a fait accompli — present it as a recommendation with the alternatives visible, so the user is choosing rather than approving.

Lay out, per layer, your recommended pick with its trade-offs and one or two credible alternatives — frontend, backend, data, auth, infra — plus the key libraries and the proposed architecture (diagram, data model, folder structure, data flow). Lead with what you'd choose and why it fits the scope and prototype, then make the alternatives easy to select instead.

Then **stop and wait.** Do not start Instrumentation: don't provision databases, don't create accounts, don't wire auth, don't write `docs/instrumentation/`. The user may accept a layer, swap a layer, or send you back to reconsider one. On explicit acceptance of the full stack, record the decision in `docs/GATES.md` (date, stage, decision, approver), finalize the three deliverables to reflect any swaps, flip Stage 5 to `done` and Stage 6 to `in_progress` in `docs/STATE.md`, and announce the transition to Instrumentation.
