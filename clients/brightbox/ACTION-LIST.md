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

## Correction to earlier advice

I previously told you to try the GA4 Enhanced Measurement "Form interactions" toggle first as a free
two minute attempt. **That will not work on this site and you should not bother.** I gave that advice
before inspecting the contact page.

## Why: the contact form is a cross domain iframe

The form on `/contact/` is not a WordPress form. It is a GoHighLevel LeadConnector widget embedded
in an iframe:

```
https://api.leadconnectorhq.com/widget/form/sOSZ2rUX7lJynwVlU9uR
```

There is no `<form>` element anywhere in the page HTML. The form lives entirely on
`leadconnectorhq.com`.

**GA4 cannot see inside a cross origin iframe.** The browser blocks it. This is a security boundary,
not a configuration problem. No GA4 setting, no Enhanced Measurement toggle and no amount of tag
configuration on brightboxdigital.io will ever record that submission, because the submit event
happens on a domain GA4 has no access to.

This is why `form_submit` has never appeared in the event list, and never would have.

## What GA4 currently collects

| Event | 28d count | What it is |
|---|---|---|
| `page_view` | 573 | Automatic |
| `user_engagement` | 422 | Automatic |
| `session_start` | 259 | Automatic |
| `scroll` | 186 | Enhanced measurement, 90 percent depth |
| `first_visit` | 149 | Automatic |
| `click` | 55 | Enhanced measurement, **outbound links only** |

All six are defaults. No lead event of any kind. No thank-you or confirmation page in 90 days of
page path data.

## The fix: redirect out of the iframe to a thank-you page

The lead signal has to be created on the Brightbox domain, because that is the only place GA4 can
observe it. A page view on a thank-you page is that signal.

### Step 1. Add the GHL embed script

The page currently loads the iframe **without** GoHighLevel's companion script. The standard GHL
embed is two parts:

```html
<iframe src="https://api.leadconnectorhq.com/widget/form/sOSZ2rUX7lJynwVlU9uR" ...></iframe>
<script src="https://link.msgsndr.com/js/form_embed.js"></script>
```

Only the iframe is present. That script is what lets the iframe talk to the parent page, and without
it a redirect configured in GHL will very likely navigate **inside the iframe** rather than taking
the whole browser to the thank-you page. A redirect that only moves the iframe produces no page view
on brightboxdigital.io, so GA4 still sees nothing.

Add the script to the contact page, in Elementor via an HTML widget below the form.

### Step 2. Create the thank-you page

`https://brightboxdigital.io/thank-you/`

Keep it genuinely useful. Confirm the message was received, say when you will respond, and give a
next step. Set it to **noindex** so it stays out of search results.

### Step 3. Point the GHL form at it

In GoHighLevel, open the form, go to Settings, and set the on submit action to **Redirect to URL**:

```
https://brightboxdigital.io/thank-you/
```

### Step 4. Test it, and confirm the address bar changes

Submit the form yourself. **Watch the browser address bar.** It must change to
`brightboxdigital.io/thank-you/`.

If the thank-you content appears but the address bar still says `/contact/`, the redirect happened
inside the iframe and step 1 did not take effect. GA4 will record nothing. Fix that before continuing.

### Step 5. Create the key event

Once a real thank-you page view exists in GA4, wait up to 24 hours, then:

**Admin > Events > Create event**
- Name: `generate_lead`
- Condition: `event_name` equals `page_view` **and** `page_location` contains `/thank-you/`

Then **Admin > Key events > Mark as key event** and select `generate_lead`.

### Step 6. Verify

```
./scripts/performance-check --site --days 28
```

`keyEvents` should stop reading 0 once submissions come in.

## Phone taps are also invisible

The contact page carries three `tel:` links and one `mailto:`. For a local service business these are
probably a larger share of real leads than the form.

GA4's `click` event only covers **outbound links**. It does not capture `tel:` or `mailto:`.

Elementor Pro can fire a custom event on a link click, or a small listener on `a[href^="tel:"]` can
push one. Worth doing after the form is working, and worth marking as a second key event. Track it
separately from the form so you can tell which channel produces business.

## Until this exists

The 28 and 90 day checks report traffic and engagement only, and must state plainly that conversion
data is unavailable. **Sessions are not leads and must never be presented as a proxy for them.**

## A note on GoHighLevel

GHL records these submissions on its own side, so you are not losing the leads themselves. What is
missing is the connection between a lead and the article or search query that produced it. That
connection is the entire point of the 28 and 90 day reviews, and it only exists if GA4 sees the
conversion.

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
