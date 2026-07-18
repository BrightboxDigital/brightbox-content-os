# Scripts

- `validate-links` — check that URLs resolve and report redirect chains. Resolving is necessary but
  not sufficient. Claim-level validation per `shared/source-validation.md` is still required.
- `build-utm` — generate a GBP destination URL with the standard UTM parameters.

Not yet built, pending connections:

- `gbp-post` — requires Google Business Profile API access.
- `performance-check` — requires Search Console and GA4.

These are intentionally absent rather than stubbed, so nothing can appear to run a check it cannot
actually perform.
