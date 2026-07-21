# push-social: blog posts to GoHighLevel Social Planner

Pushes an article's social posts into the GHL Social Planner as **drafts**. Never publishes.
Archie reviews and schedules them inside GHL.

## Setup (one time)

Credentials in `~/.config/brightbox/ghl.json`, mode 600, never in the repo:

```json
{"location_id": "...", "private_token": "pit-...", "user_id": "..."}
```

- **private_token**: GHL Settings, Private Integrations, new token with the Social Planner scopes.
- **location_id**: the sub-account/location ID.
- **user_id**: your GHL user ID (Settings, My Staff, click your user, the id is in the page URL).
  Needed because the create-post API requires a posting user. The `/users/` API endpoint is blocked
  by GHL's bot protection, so this one value is copied from the UI by hand.

## Use

```
./scripts/push-social --check                 # verify token, list connected accounts
./scripts/push-social --from path/to/posts.json
```

`posts.json` is a list of `{"platform": "...", "caption": "...", "media": "optional url"}`.
Platforms map to whatever is connected: facebook, instagram, linkedin, google (GBP), pinterest.
A platform that is not connected is skipped with a note, never silently dropped.

Every post is created with `status: "draft"`. There is no publish path in this script.

## Connected accounts (verified 2026-07-20)

facebook, instagram, linkedin (personal + company page), google (GBP), pinterest.
Not connected: tiktok, youtube. Those stay manual.

## The GBP unblock

GBP is connected in the GHL Social Planner, so Google Business Profile launch and follow-up posts
route through GHL as drafts. This removes the dependency on Google's own GBP API approval for
posting. Insights/reads may still want the GBP API later, but posting no longer waits on it.
