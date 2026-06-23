# Stage 6 — Instrumentation

> Provision and wire up every external service the app needs, ending with one complete, working `.env`.

## Objective

Stand up all the external services this product depends on — storage, email, analytics, auth, payments, error tracking, whatever the features demand — configure each for the product's actual use, and consolidate every credential into a single complete `.env` that lets the project run end to end. This is the stage where the app stops being a stack-on-paper and gains the live backing services it will call at runtime.

The hard deliverable is a `.env` that contains *everything* the project needs. Later stages (Harness, build) consume it directly, so a gap here surfaces as a confusing runtime failure three stages downstream. Aim for completeness, not just "the services we provisioned today."

## Inputs

- `docs/product/` — the feature set. Each external service must trace back to a concrete product need. If nothing in the product requires payments, you do not provision Stripe.
- `docs/stack/` — the chosen stack. Providers are picked to align with it (e.g. if the stack is Next.js on Vercel with Postgres on Neon, prefer providers with first-class integrations; don't bolt on an orthogonal platform).

Before doing anything, confirm the Stack gate passed. Provisioning against an unsettled stack means re-doing service choices when the stack shifts — and re-issued keys, dangling buckets, and billing you have to unwind. If `docs/stack/` isn't finalized, stop and say so.

## Capability routing

Provisioning is a hybrid of what you can automate and what only a human can do. Be explicit about which path each service takes, because the user needs to know exactly when they're on the hook.

**CLI / API provisioning (you drive).** Where a provider ships a CLI or API you can call, do the provisioning yourself: create the project, the bucket, the database, the API key. Examples: `vercel`, `gh`, `supabase`, `wrangler`, `aws`, `gcloud`, `stripe`. Run these, capture the output, and fold the resulting credentials into `.env` directly. Prefer this path — it's faster, reproducible, and leaves a command trail.

**Human runbooks (the user drives).** Signup, billing/credit-card entry, identity verification, and copying a secret key that a dashboard only shows once — these require a human. For each, write a precise PER-SERVICE RUNBOOK: numbered steps, exact dashboard URLs, exactly which values to copy, and which `.env` key each value maps to. The user executes it and pastes the values back to you. A vague runbook ("set up Stripe") wastes a round trip; a precise one ("1. Go to dashboard.stripe.com/apikeys 2. Copy the key starting `sk_test_` 3. Paste it as `STRIPE_SECRET_KEY`") gets it done in one pass.

**Secrets hygiene — non-negotiable.** The real `.env` is gitignored and never committed. `.env.example` carries the *keys* with placeholder/empty values and zero real secrets. Never print a real secret value into INTEGRATIONS.md or any other tracked doc, and never echo a pasted secret back in full. When the user pastes a key, write it to `.env` and refer to it by name thereafter. Note in `.env.example` where the real secrets live (1Password, Vault, the platform's env settings) so a teammate knows where to look.

## Steps

### 1. Derive the service list from features + stack, then recommend providers

Walk the feature set and enumerate every capability that needs an external service. For each, name the need ("user-uploaded images" → object storage), then RECOMMEND a provider with:

- **A primary pick** justified by stack alignment and the product's scale/needs.
- **One or two alternatives**, so the choice is informed rather than imposed.
- **Cost** — free-tier limits and what the realistic paid tier costs. The user is approving spend; surface it honestly.

These are auto-provisioned services that bill *real money* and run until someone stops them. For each pick, also note three runtime facts so the user isn't surprised later — keep them brief at `throwaway` (a free tier + how to delete it), full at `platform`:

- **Spend cap / budget alert** — does the provider support a hard cap or a budget-threshold alert? Note what you'll set, so a runaway service can't silently run up a bill.
- **Teardown / rollback path** — how this service gets deprovisioned or rolled back (CLI command, dashboard delete, `terraform destroy`), so a throwaway or abandoned project can be cleanly torn down rather than leaking accounts and charges.
- **Data residency** — where this service physically stores data (region/jurisdiction), tied to the privacy/PII note from Scope. This is an LGPD/GDPR fact, not a nicety — a service holding EU/BR personal data in the wrong region is a compliance problem before it's a cost one.

Tie every recommendation to a specific feature or stack decision. Don't provision speculative services "because most apps need them" — an analytics provider with no analytics requirement is just an unused key and a privacy surface. If the product genuinely needs it, the feature doc will show it.

Present this whole list as the first gate (see below). Provisioning costs money and creates accounts; the user approves before you touch anything.

### 2. Provision — CLI/API where possible, runbooks for the rest

Once approved, for each service choose its path:

- **Automatable:** run the provider CLI/API, create the resources, capture credentials.
- **Human-required:** emit the per-service runbook and wait for the user to run it and paste values back.

Process them in a sensible order — services others depend on first (e.g. the database before the thing that connects to it). Track status per service so the gate at the end is accurate.

### 3. Configure each service for the product's actual use

Provisioning gives you an account; configuration makes it fit the product. This is where real value is added and where it's easy to stop too early:

- **Storage:** create the actual bucket(s), set CORS, public/private access, lifecycle rules.
- **Email:** verify the sending domain, add SPF/DKIM/DMARC records, set the from-address.
- **Analytics:** create the property/site, get the measurement ID.
- **Auth:** configure redirect URIs, allowed origins, OAuth providers.
- **Payments/webhooks:** register webhook endpoints and capture signing secrets.

Configure for this product specifically — the bucket name, the domain, the redirect URLs that match this app, not generic defaults.

While configured into each service, set the **spend cap / budget alert** the provider supports (a billing budget on the cloud account, a usage cap, a low-balance alert), pin the **data-residency region** to match what Scope's privacy/PII note requires, and capture the **teardown command** for the resources you just created. Skip this for free-tier-only `throwaway` services beyond noting the delete path. Everything you set or capture here lands in INTEGRATIONS.md (next step).

### 4. Consolidate the complete `.env`

Gather every credential — automated and pasted — into a single `.env` at the repo root. Then audit it against the full service list: is every key present, is anything still a placeholder, would the app boot with exactly this file? The deliverable is *complete*, not "the keys we happened to collect." A missing key here is a downstream runtime mystery.

### 5. Document each integration in INTEGRATIONS.md

For every service, record purpose, provider + rationale, setup steps (or the runbook), the env vars it uses (names only, never values), dashboard links, plan/cost, status — plus the **spend cap / budget alert** set, the **data residency** (region), and the **teardown / rollback** command. This is the operational memory: when a key rotates, a bill spikes, a compliance question lands, or the project is abandoned and must be cleanly torn down, this doc says what it is, where it lives, and how to kill it.

## Deliverables

Write to `docs/instrumentation/` plus the env files at the repo root:

```
docs/instrumentation/
└── INTEGRATIONS.md      # per service: purpose, provider + rationale, setup steps,
                         #   env vars used (names only), dashboard links, plan/cost, status,
                         #   spend cap, data residency, teardown/rollback
.env                     # repo root, GITIGNORED — real secret values, never committed
.env.example             # repo root, tracked — all keys, NO secret values,
                         #   note where real secrets live (1Password / Vault)
```

Templates live at `assets/templates/deliverables/`:
- `INTEGRATIONS.md` — the per-service integration record.
- `env.example.txt` — the template for `.env.example`.

**The `.env` / `.env.example` relationship.** Same keys, different content. `.env` holds the working secret values and is gitignored. `.env.example` holds the same key names with empty/placeholder values, a one-line comment per key, and a pointer to where the real values live. A teammate clones the repo, copies `.env.example` to `.env`, and fills in values from the secret store. Confirm `.env` is in `.gitignore` before any commit — and if `.gitignore` doesn't exist yet, create it with `.env` as the first line.

## Definition of Done

- [ ] Every required external service is identified and traced to a feature/stack decision (no speculative services).
- [ ] All required services are provisioned (via CLI/API or completed runbook) and configured for the product's actual use.
- [ ] `.env` exists at repo root, is gitignored, and is complete — the app would run with exactly these values.
- [ ] `.env.example` documents every key, contains no secret values, and notes where real secrets live.
- [ ] Every integration is recorded in INTEGRATIONS.md (purpose, provider, rationale, setup, env vars, links, cost, status, spend cap, data residency, teardown/rollback).
- [ ] Where the provider supports it, a spend cap / budget alert is set so no service can silently run up a bill; data residency matches Scope's privacy/PII requirement (flex to minimal for `throwaway`).
- [ ] Secrets-storage strategy is noted (1Password / Vault / platform env settings).

## The gate

Two human decision points bracket this stage.

**Gate A — approve the provider list before provisioning.** Present the full service list with, per service: the need it serves, the recommended provider, alternatives, cost (free tier + realistic paid tier), and — for anything that bills — the spend cap you'll set, the data-residency region, and the teardown path. Then STOP. The user is approving real spend and real accounts — they may swap a provider, defer a service, or stay on free tiers. Do not provision until they approve.

**Gate B — confirm the completed `.env` works.** After provisioning, configuring, and consolidating, present the state: every service's status, the complete (key-names-only) `.env` inventory, and confirmation that `.env` is gitignored and `.env.example` is documented. Then STOP for the user to confirm the `.env` is complete and the project can run on it.

Propose, then stop. Don't spend money or chain into the next stage on assumed approval.
