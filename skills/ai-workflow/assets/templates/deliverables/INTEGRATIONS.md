# External Integrations

> Every third-party service the app depends on, with a runbook to set each up.
> Keep the summary table in sync with the detailed blocks below.

## Summary

| Service | Provider | Purpose | Plan / Cost | Status |
| --- | --- | --- | --- | --- |
| `<Auth>` | `<provider>` | `<sign-in / sessions>` | `<Free / $X mo>` | `<active / planned>` |
| `<Email>` | `<provider>` | `<transactional email>` | `<...>` | `<...>` |
| `<Payments>` | `<provider>` | `<billing>` | `<...>` | `<...>` |
| `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |

---

## `<Service name>`

- **Purpose:** `<what this service does for us>`
- **Provider + rationale:** `<provider; why chosen over alternatives>`
- **Status:** `<active / planned / deprecated>`
- **Plan / cost:** `<tier, monthly cost, limits>`

### Setup steps (runbook)

1. `<Create account / project in the provider dashboard.>`
2. `<Generate API key / credentials.>`
3. `<Store secrets in 1Password/Vault; add keys to .env (see env.example).>`
4. `<Configure webhooks / redirect URLs / domains.>`
5. `<Verify locally, then in staging.>`

### Env vars used

- `<SERVICE_API_KEY>`
- `<SERVICE_WEBHOOK_SECRET>`

### Dashboard links

- Dashboard: `<url>`
- Docs: `<url>`

---

## `<Next service name>`

> Copy the block above for each additional service.

- **Purpose:** `<...>`
- **Provider + rationale:** `<...>`
- **Status:** `<...>`
- **Plan / cost:** `<...>`

### Setup steps (runbook)

1. `<...>`

### Env vars used

- `<...>`

### Dashboard links

- Dashboard: `<url>`
