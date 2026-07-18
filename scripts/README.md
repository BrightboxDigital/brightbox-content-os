# Scripts

- `validate-links` — check that URLs resolve and report redirect chains. Resolving is necessary but
  not sufficient. Claim-level validation per `shared/source-validation.md` is still required.
- `build-utm` — generate a GBP destination URL with the standard UTM parameters.

Not yet built, pending connections:

- `gbp-post` — requires Google Business Profile API access.
- `performance-check` — requires Search Console and GA4.

These are intentionally absent rather than stubbed, so nothing can appear to run a check it cannot
actually perform.

## performance-check

Pulls Search Console and GA4 data for an article or the whole site.

```
./scripts/performance-check --check                    # verify access
./scripts/performance-check --site --days 28           # whole site
./scripts/performance-check should-i-redesign-my-website --days 90
```

`performance-check` is a bash wrapper around `performance_check.py`. The wrapper exists because
shebang lines cannot contain spaces and the repository path does. Do not collapse them.

Dependencies live in `.venv/` (gitignored). Recreate with:

```
python3 -m venv .venv
.venv/bin/pip install google-analytics-data google-api-python-client google-auth
```

Credentials come from `~/.config/brightbox/service-account.json`, never from this repository.
Property identifiers are in `clients/brightbox/analytics-config.json`.

The script reports only what the APIs return. When a call fails or returns nothing, it says so
rather than estimating.

### Status, July 18, 2026

- Search Console: working. Property auto-detected as `https://brightboxdigital.io/`.
- GA4: blocked. The Google Analytics Data API is not enabled on the Cloud project.
