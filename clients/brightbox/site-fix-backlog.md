# Site Fix Backlog

Baseline audit July 18, 2026. Read only. **Nothing on the live site was modified.**

Items are ordered by how much they undermine the content program. Each needs Archie's approval
before anyone touches the site.

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
