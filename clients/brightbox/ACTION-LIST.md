# Action List for Archie

Three jobs, with exact steps. Findings verified July 18, 2026 against live HTTP status codes and
the GA4 and Search Console APIs.

---

# 1. The 301 redirects  [DONE July 18, 2026]

## Status: complete and verified

All nine redirects live. Every source returns 200 in one hop to the correct destination. All live
destinations still return 200 with zero hops, so no rule caught its own target.

The original problem, kept for reference:

The blog moved from root level URLs to `/blog/` and never got redirects. **All seven** blog slugs
return 404 at root level, not just the five that showed traffic. The redesign article also changed
slug at some point.

Five of these were pulling real traffic in the last 28 days, roughly 12 percent of all site sessions
landing on dead pages. The other four are 404ing quietly and may still have external links pointing
at them.

## Where to do it

WordPress admin, **Rank Math > General Settings > Redirections**. If the module is off, enable it at
Rank Math > Dashboard > Modules > Redirections.

Type: **301 Permanent Move** for every one.

## The list

| # | Redirect from | Redirect to | 28d sessions lost |
|---|---|---|---|
| 1 | `/should-i-redesign-my-website/` | `/blog/should-i-redesign-my-website/` | 18 |
| 2 | `/google-business-profile-the-ultimate-guide/` | `/blog/google-business-profile-the-ultimate-guide/` | 12 |
| 3 | `/should-i-redesign-my-website-signs-its-time/` | `/blog/should-i-redesign-my-website/` | 9 |
| 4 | `/local-seo-in-2025/` | `/blog/local-seo-in-2025/` | 6 |
| 5 | `/blog-new/` | `/blog/` | 5 |
| 6 | `/fort-wayne-web-design-2025/` | `/blog/fort-wayne-web-design-2025/` | 0 observed |
| 7 | `/is-your-website-secure/` | `/blog/is-your-website-secure/` | 0 observed |
| 8 | `/ai-logo-design-should-you-use-an-ai-logo-generator/` | `/blog/ai-logo-design-should-you-use-an-ai-logo-generator/` | 0 observed |
| 9 | `/fort-wayne-seo-guide-how-to-rank-your-business-locally-in-2025/` | `/blog/fort-wayne-seo-guide-how-to-rank-your-business-locally-in-2025/` | 0 observed |

Note on #3: it points at the **current** slug, not the old one. Do not chain it through
`/should-i-redesign-my-website/` or you create a two hop redirect.

Do 6 through 9 even though no traffic showed. They cost nothing and external links may exist that
GA4 cannot see.

## Also fix while you are in there

`/fort-wayne-seo/` currently takes **two hops** to reach its destination:

```
/fort-wayne-seo/  ->  /seo  ->  /seo/
```

Change that redirect to point straight at `https://brightboxdigital.io/seo/` with the trailing slash.

And remove `/fort-wayne-seo/` from the XML sitemap, since sitemaps should only list canonical
destinations. It is currently listed with a lastmod of 2025-12-22.

## Verify afterwards

```
./scripts/validate-links https://brightboxdigital.io/should-i-redesign-my-website/ \
  https://brightboxdigital.io/local-seo-in-2025/ https://brightboxdigital.io/fort-wayne-seo/
```

Each should show 200 with 1 hop. Two hops means a chain that needs collapsing.

Then in a few weeks, run `./scripts/performance-check --site --days 28` and confirm those paths
have stopped appearing in the GA4 page list.

---

# 2. GA4 key events

## Can Claude do this? No, and for two reasons

The service account has **read only** analytics scope by design, so it cannot write configuration.
That part could be changed.

The blocking reason is different: **there is no lead event to mark.** Marking a key event means
promoting an existing event. Nothing on the site currently fires one.

Here is every event GA4 collected in the last 28 days:

| Event | Count | What it is |
|---|---|---|
| `page_view` | 573 | Automatic |
| `user_engagement` | 422 | Automatic |
| `session_start` | 259 | Automatic |
| `scroll` | 186 | Enhanced measurement, 90 percent scroll depth |
| `first_visit` | 149 | Automatic |
| `click` | 55 | Enhanced measurement, outbound links only |

All six are GA4 defaults. **There is no `form_submit`, no `generate_lead`, no contact event of any
kind.** There is also no thank-you or confirmation page anywhere in 90 days of page path data.

So this is a two part job: make the site fire a lead event, then mark it as a key event.

## The most reliable fix: a thank-you page

No GTM, no code, works with any form plugin.

1. In your form plugin settings, change the contact form's post-submit behavior from an inline
   success message to a **redirect** to `https://brightboxdigital.io/thank-you/`.
2. Create that page. Keep it simple and useful. Confirm the message was received and say when you
   will respond.
3. Set the page to `noindex` so it stays out of search results.
4. Submit the form yourself once to generate real data.
5. Wait up to 24 hours, then in GA4: **Admin > Events > Create event**
   - Name: `generate_lead`
   - Condition: `event_name` equals `page_view` **and** `page_location` contains `/thank-you/`
6. **Admin > Key events > Mark as key event**, select `generate_lead`.

Why this rather than form tracking: a thank-you page view is unambiguous. It fires once, only on
success, and no plugin behavior can silently break it.

## Free thing to try first, takes two minutes

**Admin > Data Streams > select the web stream > Enhanced measurement > gear icon > enable
"Form interactions."**

That fires `form_start` and `form_submit` automatically. It costs nothing to turn on.

Be aware it frequently fails on AJAX submitted forms, which most modern WordPress form plugins use.
Turn it on, submit a test, and check whether `form_submit` appears within 24 hours. If it does, mark
that as your key event and skip the thank-you page. If it does not, the form is AJAX based and you
need the redirect method above.

## Worth adding too

Phone and email taps are leads and are currently invisible. `click` only tracks outbound links, not
`tel:` or `mailto:`.

If your theme or a plugin can fire an event on those, mark them as key events as well. This is
secondary to the form.

## Until this exists

The 28 and 90 day checks report traffic and engagement only, and must state plainly that conversion
data is unavailable. **Sessions are not leads and must never be presented as a proxy for them.**

---

# 3. GBP API access request  [SUBMITTED July 18, 2026]

## Where

Two entry points, same process:

- **The form:** [Business Profile APIs: Application Form For Basic Access](https://docs.google.com/forms/d/e/1FAIpQLSfC_FKSWzbSae_5rOpgwFeIUzXUF1JCQnlsZM_gC1I2UHjA3w/viewform)
- **The help walkthrough:** [Applying for Google Business Profile API access](https://support.google.com/business/workflow/16726127)

On the form, select **"Application for Basic API Access"** from the drop-down.

## Critical: sign in with the right account

The form must be submitted from an email that is listed as an **owner or manager** on the Brightbox
Google Business Profile. Submitting from any other Google account gets rejected regardless of how
good the application is.

## What the form asks for

You need your **Project Number**, which is not the same as the Project ID.

| | |
|---|---|
| Project **ID** | `brightbox-digita-1743176991871` |
| Project **Number** | `824815042391` |

The project number appeared in a Google API error response for this project, so it is almost
certainly right. **Confirm it on the Cloud console Dashboard in the Project info card** before
submitting rather than trusting this file.

## The justification text

Drafted in `gbp-api-request-draft.md`. Read it before pasting. It describes low volume, names the
specific endpoints, and explicitly rules out modifying business information, which is the part
Google scrutinizes.

## This is also why v4.9 was missing from your API list

Google's documentation confirms it:

> The Google My Business API is only visible in the Google API Console to users who submit and
> receive approval for their Google Account through the access request form.

So the three APIs you enabled are correct and sufficient for now. The posting API appears only after
approval. Nothing went wrong on your end.

## After submitting

Record the date in `gbp-api-request-draft.md`. Then check approval by quota, not by feel:

Cloud console > APIs & Services > Quotas. **0 QPM means pending. 300 QPM means approved.**

Expect weeks.

---

## Sources

- [Business Profile API prerequisites](https://developers.google.com/my-business/content/prereqs)
- [Business Profile API basic setup](https://developers.google.com/my-business/content/basic-setup)
- [Applying for GBP API access](https://support.google.com/business/workflow/16726127)
- [Application form for basic access](https://docs.google.com/forms/d/e/1FAIpQLSfC_FKSWzbSae_5rOpgwFeIUzXUF1JCQnlsZM_gC1I2UHjA3w/viewform)
