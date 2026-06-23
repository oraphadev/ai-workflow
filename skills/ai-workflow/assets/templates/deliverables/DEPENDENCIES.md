# Key Dependencies

> The important libraries that shape how the app is built, grouped by domain.
> This is not an exhaustive `package.json` dump — list only decisions worth recording.
> Keep versions pinned to what is actually installed; update on upgrades.

| Library | Version | Domain | Purpose | Notes / Compatibility |
| --- | --- | --- | --- | --- |
| `<react-hook-form>` | `<^7.x>` | Forms | `<form state & submission>` | `<pairs with zod resolver>` |
| `<zod>` | `<^3.x>` | Validation | `<schema validation, shared client/server>` | `<...>` |
| `<zustand>` | `<^5.x>` | State | `<client global state>` | `<...>` |
| `<@tanstack/react-query>` | `<^5.x>` | Data fetching | `<server-state caching>` | `<requires provider at root>` |
| `<drizzle-orm>` | `<^0.x>` | Data | `<typed DB access>` | `<see STACK.md>` |
| `<...>` | `<...>` | `<UI>` | `<...>` | `<...>` |
| `<...>` | `<...>` | `<Auth>` | `<...>` | `<...>` |
| `<...>` | `<...>` | `<Dates / i18n>` | `<...>` | `<...>` |
| `<...>` | `<...>` | `<Testing>` | `<...>` | `<...>` |

## Domains to cover (delete what you don't use)

- Forms
- Validation
- State management
- Data fetching / server state
- UI / components
- Auth
- Database / ORM
- Dates / formatting / i18n
- Testing / mocking
- Tooling (linting, formatting, build)

## Notes

- `<Record any known version conflicts, peer-dependency pins, or upgrade caveats here.>`
