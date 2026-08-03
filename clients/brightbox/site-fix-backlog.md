# Site Fix Backlog

Baseline audit July 18, 2026. Read only. **Nothing on the live site was modified.**

Items are ordered by how much they undermine the content program. Each needs Archie's approval
before anyone touches the site.

---

## Critical

### 0. RESOLVED July 18, 2026. Traffic was landing on 404 pages with no redirects.

Found July 18, 2026, from GA4 page path data cross checked against live HTTP status codes.
This was not visible in the read only audit and only surfaced once analytics was connected.

GA4 recorded sessions on these paths in the last 28 days. Every one of them returns **404 with no
redirect**:

| Path | Sessions (28d) | Status |
|---|---|---|
| `/should-i-redesign-my-website/` | 18 | 404, no redirect |
| `/google-business-profile-the-ultimate-guide/` | 12 | 404, no redirect |
| `/should-i-redesign-my-website-signs-its-time/` | 9 | 404, no redirect |
| `/local-seo-in-2025/` | 6 | 404, no redirect |
| `/blog-new/` | 5 | 404, no redirect |

That is **50 sessions out of 405 site wide, roughly 12 percent of all traffic, landing on a page
that does not exist.**

The live versions all sit under `/blog/`:
`/blog/should-i-redesign-my-website/`, `/blog/google-business-profile-the-ultimate-guide/`,
`/blog/local-seo-in-2025/` all return 200.

**What this looks like:** the blog moved from root level URLs to `/blog/` at some point, and the
slug of the redesign article changed from `should-i-redesign-my-website-signs-its-time` to
`should-i-redesign-my-website`. Neither migration got 301 redirects. `/blog-new/` looks like a
staging page that was removed while still receiving traffic.

**Why it matters:** these are real people, plus whatever external links and existing Google results
point at the old URLs. All of that is being thrown away. Any ranking signal accumulated by the old
URLs is lost rather than passed forward.

**Fixed July 18, 2026.** Archie added all nine redirects in Rank Math, plus corrected the
`/fort-wayne-seo/` destination to include its trailing slash.

Verified: every source returns 200 in exactly one hop to the correct destination, and all nine live
destinations still return 200 with zero hops, confirming no rule caught its own target and no loop
was created.

The original mappings, kept for reference:

| From | To |
|---|---|
| `/should-i-redesign-my-website/` | `/blog/should-i-redesign-my-website/` |
| `/should-i-redesign-my-website-signs-its-time/` | `/blog/should-i-redesign-my-website/` |
| `/google-business-profile-the-ultimate-guide/` | `/blog/google-business-profile-the-ultimate-guide/` |
| `/local-seo-in-2025/` | `/blog/local-seo-in-2025/` |
| `/blog-new/` | `/blog/` |

**Root cause worth remembering:** the original `/fort-wayne-seo/` redirect pointed at
`https://brightboxdigital.io/seo` without a trailing slash, and WordPress then redirected again to
`/seo/`. A missing trailing slash on a destination silently creates a second hop. Always end
destination URLs with a slash.

**Follow up:** re-run `./scripts/performance-check --site --days 28` in a few weeks. The root level
paths should stop appearing in the GA4 page list. If they persist, something still links to them
internally and those links should be updated to point at the canonical URL directly rather than
relying on the redirect.

The crawl confirmed all seven blog slugs 404ed at root, not only the five with observed traffic.
All seven are now redirected.

### 0b. OPEN. GA4 has no key events configured, so leads cannot be measured

The 28 day pull returned **keyEvents 0** across 405 sessions. Not zero conversions. Zero
**configured** key events.

This means GA4 currently cannot answer whether any article produced a lead, which is the measure the
content system is built around. Engagement rate is 65.2 percent and contact page sessions exist, so
there is activity to measure. Nothing is set up to record it.

**Fix:** configure key events in GA4 for the actions that represent a lead. At minimum a contact
form submission. Ideally also phone link clicks and any quote or review request.

Until this exists, the 28 and 90 day checks can report traffic and engagement but must state
plainly that conversion data is unavailable. **Do not infer leads from sessions.**

### 0c. RESOLVED July 18, 2026. A site navigation link pointed at a 404

`/social-media-marketing/` is linked from the site navigation and returns **404**. The real page is
`/social-media-marketing-fort-wayne/`, which returns 200.

This link appears in the header or footer, so it is on every page of the site.

**Fixed July 18, 2026.** Menu link corrected. Verified `/social-media-marketing/` no longer appears
in the navigation on any page checked.

**Still open:** no 301 exists for `/social-media-marketing/` itself, which still returns 404. Worth
adding, since the wrong URL may have been shared or indexed externally.

**Still open:** body links to `/fort-wayne-seo/` remain on the homepage (3) and About page (1). The
redirect handles them, but each click costs an unnecessary hop. Update to `/seo/` directly.

Also on the contact page: the nav links to `/fort-wayne-seo/`, which now 301s correctly but still
costs a redirect hop on every click. Update menu links to point at `/seo/` directly. Redirects are
a safety net for external links, not a substitute for correct internal linking.

### 0d. Phone number hrefs are inconsistent and two formats contain a leading space

The click to call button appears on every page. Across the site the same number is marked up three
different ways, and two of them have a URL encoded leading space inside the `tel:` value:

```
tel:%20260.222.2880        leading space
tel:%20(260)%20222-2880    leading space
tel:2602222880             clean
```

Most modern dialers tolerate the leading space and strip punctuation, so this is probably not
costing calls today. But it is fragile, it depends on forgiving behavior rather than correctness,
and it makes reporting messier because the same number appears as three distinct values.

**Fix:** normalize every phone link to E.164:

```
tel:+12602222880
```

Display text can stay formatted however it reads best, for example (260) 222-2880. Only the `href`
needs to change. The tracking snippet in `phone-tracking-snippet.html` already normalizes these to
a digits only value for reporting, so this is about the links themselves, not the measurement.

---

## High priority

### 1. Authorship is inconsistent across the blog

`should-i-redesign-my-website` carries "By Archie Brady." `local-seo-in-2025` carries
"Brightbox Digital Team." Two different authors are presented for the same blog with no explanation.

This is the exact conflict the editorial standards prohibit, and it undermines the experience signal
that the whole content program depends on.

**Fix:** decide on Archie Brady as the single visible author, update every post's byline, and confirm
the Article or BlogPosting markup agrees with the visible byline on each one.

### 2. No author page exists

`https://brightboxdigital.io/author/archie/` returns 404. No post links to an author bio.

**Fix:** create a substantive author page for Archie covering his role, real experience, the services
he works on, the market he serves, and a photo. Link every article byline to it. Until it exists,
author links should point to `/about/`.

### 3. A redirecting URL is listed in the XML sitemap

`https://brightboxdigital.io/fort-wayne-seo/` appears in `page-sitemap.xml` with a lastmod of
2025-12-22, but it returns a 301 to `https://brightboxdigital.io/seo`.

Sitemaps should list canonical destinations only.

**Fix:** remove `/fort-wayne-seo/` from the sitemap in Rank Math, or restore it as a real page if the
Fort Wayne SEO query deserves its own destination. Then audit internal links across the site for
anything still pointing at the old URL and update them to `/seo/`.

**Confirmed: this is a two hop redirect chain.** The 301 target is `/seo` without a trailing slash,
which then redirects again to `/seo/`. Verified with `./scripts/validate-links`:

```
200      2      https://brightboxdigital.io/fort-wayne-seo/
         -> final: https://brightboxdigital.io/seo/
```

Point the redirect straight at `https://brightboxdigital.io/seo/` to remove the extra hop.

### 4. Blog archive hides 3 of 7 posts

The archive surfaces 4 posts with no pagination. Three published posts are not reachable from it:
the GBP ultimate guide, the AI logo design post, and the Fort Wayne SEO guide.

**Fix:** enable pagination or raise the posts per page count. Confirm category archives list every
post. This is an internal linking and discoverability problem, not a cosmetic one.

**Confirmed still broken 2026-08-03**, checked as part of BBX-002's post publication technical QA.
`https://brightboxdigital.io/blog/` returns 200 but contains no link or title text for
`local-services-ads-moving-to-google-ads`, same symptom as the original finding, now on an eighth
post.

### 4b. Two PPC articles are split across two different categories

Confirmed 2026-08-03, technical QA after BBX-002 published. The site has two separate categories
that both read as "the PPC category" to a human, but are different taxonomy terms with different
slugs:

| Category | id | slug | Posts in it |
|---|---|---|---|
| Google Ads | 23 | `google-ads` | BBX-001 (`does-a-small-google-ads-budget-work`) |
| Google Ads and PPC | 28 | `google-ads-and-ppc` | BBX-002 (`local-services-ads-moving-to-google-ads`) |

Category 28 did not exist before BBX-002. `scripts/wp-draft` creates a category by exact name match
if none exists (`resolve_category`, `scripts/wp_draft.py`), and "Google Ads and PPC" (the content
category name used in `content-tracker.csv` and throughout this repo) did not exactly match the
existing "Google Ads" category on the site, so a new one was created rather than reused.

**Effect:** `/blog/category/google-ads/` and `/blog/category/google-ads-and-ppc/` each show only one
of the two PPC articles. Neither shows both. This directly undermines the hub and cluster model in
`internal-links.md`, where the PPC hub is supposed to have a growing set of supporting articles
visible together.

**Fix:** pick one category as canonical (`google-ads` already has BBX-001 and an established slug;
recommend keeping it and moving BBX-002 into it, then deleting or merging category 28) and update
`scripts/wp_draft.py`'s category name to match exactly, or update `resolve_category` to do a
case/punctuation-insensitive match before creating a new one, so this cannot recur on BBX-003 and
beyond. Needs Archie's decision on which name is canonical before either the site or the script
changes.

### 4c. Featured image on BBX-002 has empty alt text

Confirmed 2026-08-03. The featured image (`google-lead-service-ads.webp`, media id 5756) renders
with `alt=""` on the live page. `scripts/wp-draft --featured` only sets `featured_media`; it does not
set alt text, and none was set manually after Archie uploaded the image himself.

**Fix:** set alt text on media id 5756 in the WordPress media library, e.g. "Local Services Ads
listing transitioning into a Google Ads Performance Max campaign, with icons for plumbing, HVAC,
electrical, roofing, and cleaning." Low effort, straightforward accessibility and image-SEO fix.

### 5. Likely cannibalization on Fort Wayne local SEO

`local-seo-in-2025` and `fort-wayne-seo-guide-how-to-rank-your-business-locally-in-2025` appear to
target the same intent. The `/seo/` service page is a third competitor for related queries.

**Fix:** decide which URL is the canonical answer, then consolidate or clearly differentiate. This
should be settled before any new local SEO article is commissioned.

---

## Medium priority

### 6. Outdated statistics presented as current

`local-seo-in-2025` cites a BrightLocal study identified on the page as 2020, and a "46% of Google
searches seek local information" figure attributed to HubSpot with no primary source.

Both fail the source validation standard. The 46% figure in particular circulates widely without a
traceable methodology.

**Fix:** revalidate every statistic against a primary source with accessible methodology, replace
what cannot be substantiated, and remove what cannot be replaced.

### 7. Year stamped titles and slugs, now stale

Three posts carry 2025 in the title and slug while it is July 2026:
`fort-wayne-web-design-2025`, `local-seo-in-2025`, and
`fort-wayne-seo-guide-how-to-rank-your-business-locally-in-2025`.

**Archie's position, July 18, 2026:** worth doing, but not a first priority, since the content is
only a year old and is not necessarily outdated. Scheduled late in the calendar accordingly
(cycles 8 and 12). Do not front load these.

**One distinction worth keeping separate.** Whether the *content* is stale and whether the *title*
is stale are two different problems. The content may well be fine. But a searcher scanning results
in 2026 sees "2025" in the title and reads it as last year's advice before clicking. That is a
click-through cost that applies even to accurate content, and it gets worse every month.

If the year stamps become a priority ahead of schedule, the cheap version is a title and slug change
with a 301, without a full content rewrite. That is a much smaller job than a refresh and can be
done independently.

**Fix, when scheduled:** move to evergreen titles and slugs. Changing a slug requires a 301 from the
old URL. Do not simply swap 2025 for 2026, that recreates the same problem next year.

### 8. Two posts are a year old and cover fast moving subjects

`google-business-profile-the-ultimate-guide` (July 2025) and
`ai-logo-design-should-you-use-an-ai-logo-generator` (July 2025). Both subjects have moved
substantially in twelve months.

**Fix:** schedule as refresh candidates. Only update the visible date after a substantive rewrite.

---

## Low priority

### 9. Title against brand voice

"Is your website secure? Protect your visitors with an SSL certificate!" uses an exclamation point
and reads as older marketing copy. The post also has limited strategic value for the services
Brightbox sells.

**Fix:** consolidation candidate. Consider folding the useful content into a web design or
maintenance page.

### 10. Review the niche landing page pattern

`seo-web-design-car-detailing-fort-wayne` is a niche specific landing page. One is fine. If this
pattern gets replicated per niche with swapped nouns, it becomes doorway content.

**Fix:** confirm the page has genuinely original content for that niche before creating siblings.

### 11. Footer year on a 2025 dated article

`local-seo-in-2025` shows a 2026 footer copyright against a February 2025 publication date. Normal
for a dynamic footer, but confirm no other date is being auto-updated in a way that misrepresents
freshness.

---

## Not yet checked

These need a browser session or a connected tool and were out of scope for a read only baseline:

- Mobile rendering across templates
- Page speed and Core Web Vitals
- Canonical tags on individual posts
- Article schema presence and validity per post
- Category organization and whether every post has one
- Visible internal editing notes or placeholder copy on pages not yet opened
- Full internal link crawl for links still pointing at `/fort-wayne-seo/`
- Whether at least two existing pages link into each published post
