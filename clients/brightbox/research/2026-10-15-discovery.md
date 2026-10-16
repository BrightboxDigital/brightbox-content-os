# Discovery Run — 2026-10-15

Scheduled run (`brightbox-content-discovery`). Nothing in the tracker was in a waiting status, so this
run did a monitoring sweep and then discovery.

## Monitoring sweep summary

| Article | Published | Milestone status | Action this run |
|---|---|---|---|
| BBX-001 small Google Ads budget | ~2026-07-19 | 90-day due ~2026-10-17 | Not yet due. Next sweep. |
| BBX-002 LSA into Google Ads | 2026-08-03 | 90-day due 2026-11-01 | Not due |
| BBX-003 AEO/GEO/llms.txt | 2026-08-16 | 90-day due 2026-11-14 | Not due |
| BBX-004 GBP visibility refresh | 2026-09-15 | 7-day missed, 28-day due 2026-10-13 | **Ran.** See `performance/BBX-004-28day-2026-10-15.md` |

BBX-004 headline: 2 impressions and 1 session in the 28 days after the refresh, against 2 impressions
and 0 sessions in the 28 days before. That's too small to judge. The page is technically clean, and
the meta description problem from launch is fixed. Distribution for BBX-004 was never done.

There's no commit between 2026-09-15 and this run, so the 2026-10-01 sweep doesn't seem to have run.
That's why BBX-004's 7-day check was skipped.

## Which slot

The calendar is ahead of production. Cycles 4 (PPC, 09-15), 5 (Web Design, 10-01) and 6 (GBP, 10-15)
have no tracker rows. Current category balance: **PPC 2, SEO and AI Search 1, Local SEO and GBP 1,
Web Design and Development 0.** PPC isn't behind. Web Design hasn't had a single article from this
system. BBX-002 already took cycle 4's PPC slot. So the next open slot is **cycle 5: Web Design,
Evergreen, New, "AI Website Builders Versus Professional Web Design", supporting
`/web-design-fort-wayne/`.**

I'm not proposing cycle 6 (GBP messaging) this run. Google retired Business Profile chat and call
history in July 2024. The one source claiming it returned in 2026 is an agency blog, and I couldn't
find any confirmation from Google. The calendar note itself says "confirm current availability
before scheduling." Availability isn't confirmed, so I've put it on hold in the backlog.

## Demand evidence (site's own Search Console)

Pulled with `./scripts/performance-check --site --days 90` (window 2026-07-15 to 2026-10-13). Site
baseline recorded to `performance/baselines.csv`: 47,727 impressions, 87 clicks, avg position 8.9.
For the 90-day baseline before the system launched (2026-07-19), the figures were 22,408
impressions and 88 clicks.

The full query list sorted by impressions (598 queries) was pulled through the same API. Web design
terms make up the biggest Fort Wayne cluster:

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| web design fort wayne | 3,231 | 1 | 4.6 |
| fort wayne web design | 2,343 | 1 | 5.5 |
| web design agency fort wayne | 1,577 | 0 | 3.1 |
| website design fort wayne | 1,360 | 1 | 4.8 |
| fort wayne website design | 440 | 2 | 5.1 |
| seo fort wayne / seo company fort wayne / fort wayne seo | 2,399 / 2,421 / 1,904 | 0-1 | 3.9-5.8 |

The two largest queries, `digital marketing` (7,971) and `web development` (5,636), are almost
certainly showing local-pack impressions for the GBP-tagged location URL. They aren't real topical
demand. At page level, `/locations/fort-wayne/?utm_...gbp` alone has 31,056 impressions.

**What this tells us and what it doesn't:** people searching for web design in Fort Wayne already
see Brightbox, at positions 3 to 5, with almost no clicks. **No query about AI website builders shows
up in the site's Search Console.** That's normal, since the site has no content on the topic. Demand
for candidate 1 is inferred from the size of the web design cluster plus market events (below). It
isn't measured. No search volume figure appears anywhere in this report.

Side finding, not this run's job: `/fort-wayne-seo/` (a 301 to `/seo/`) still shows up for 1,492
impressions in 90 days at avg position 32.9. Google is still showing the redirected URL. It's worth
checking in Search Console's URL inspection that `/seo/` is the selected canonical.

## NeuronWriter overlap (read only, no query created)

- Brightbox project `eea0682a76fd76f0`: 4 queries (google ads small budget, local services ads
  performance max, aeo geo llms.txt myths, google business profile ranking factors). None overlap
  with any candidate below.
- Clients project `0bdb5139dc86fbe7`: `website design` (261c1d59c8ea60de, 2026-06-17),
  `web design fort wayne` and `fort wayne web design` (May 2025, service-page work),
  `professional vs ai logo design` (July 2025). They're adjacent to candidate 1 but none of them
  targets the AI-builder comparison. Nothing on call ads or spam updates.

---

## Candidate 1 — RECOMMENDED

**Working title:** AI Website Builders vs. a Professional Web Designer: What a Fort Wayne Business Actually Gets

- **Category:** Web Design and Development
- **Evergreen or timely:** Evergreen, with a current hook
- **New or update:** New
- **Proposed primary keyword:** `ai website builder vs web designer` (seed to be confirmed at the
  keyword gate. Alternatives: `is an ai website builder good enough`, `wix ai vs web designer`)
- **Search intent:** Commercial investigation. The owner is deciding whether to build it themselves
  with AI or hire someone.
- **Audience:** Fort Wayne and NE Indiana small business owners and contractors pricing out a new
  site
- **Why it matters now:** All the major builders now sell AI-first site creation. Wix launched Wix
  Harmony, which it calls its flagship AI builder, on 2026-01-21. Squarespace (Blueprint AI) and
  GoDaddy (Airo) push AI generation as the default way to start a site. Google also updated its
  guidance on using generative AI content on 2026-10-01. That guidance still requires AI-generated
  copy, titles, meta descriptions and alt text to be fact-checked and to meet Search Essentials and
  the scaled-content-abuse policy. Owners are hearing "a website in minutes" right when Google is
  restating the quality bar.
- **Evidence of interest:** Qualitative. Web design is the site's largest Fort Wayne demand cluster
  in GSC (table above). The calendar notes it as a question Archie is asked repeatedly. The market
  push is documented in the Wix press release and in trade coverage. There's no measured query-level
  demand for the AI comparison itself.
- **Questions people are asking (from builder marketing and the comparison SERP. To confirm with
  NeuronWriter after keyword approval):** Is an AI-built site good enough for a small business? Will
  it rank on Google? What does it really cost over a few years? Can I move off it later? What can't
  the AI do?
- **Relevant Brightbox service:** Web design (`/web-design-fort-wayne/`)
- **Internal pages supported:** `/web-design-fort-wayne/`, `/portfolio/`, `/seo/`,
  `/blog/should-i-redesign-my-website/`, `/blog/ai-logo-design-should-you-use-an-ai-logo-generator/`
  (a parallel argument about a different deliverable)
- **Potential cannibalization:** Low to moderate. `/blog/fort-wayne-web-design-2025/` is a generic
  "importance of professional web design" post. It's the cycle 12 refresh target and could compete if
  this article leans on the "why professional" argument. Keep this one tightly scoped to the AI
  builder decision and link to it from the 2025 post when that post is refreshed. It doesn't compete
  with `/web-design-fort-wayne/` (transactional) or `should-i-redesign` (timing decision).
- **Opportunity for original experience:** High. Archie's opinion, which the calendar notes he has.
  Real cases of businesses that came to Brightbox from a DIY or builder site (anonymized and supplied
  by Archie, never invented). Possibly a side-by-side test: generate a site in Wix Harmony for a
  sample local business and annotate what it got right and wrong. That would be an original
  screenshot set.

| Category | Score | Why |
|---|---|---|
| Service relevance | 5 | Web design is a core paid service, and the category has no system-produced article yet |
| Local relevance | 3 | The decision is universal. The local angle comes from Fort Wayne cost and support context, not the topic itself |
| Evidence of interest | 4 | Largest GSC cluster on the site, plus documented market push. The comparison query itself isn't measured |
| Freshness | 3 | Harmony is 9 months old. Google guidance updated 2026-10-01. Evergreen more than news |
| Firsthand contribution | 5 | A question Archie fields repeatedly, and an annotated build test is possible |
| Organic ranking opportunity | 3 | Comparison SERPs are crowded with builder-affiliate reviews. A practitioner angle is the gap |
| Conversion potential | 5 | The reader is actively deciding whether to pay for a site |
| **Total** | **28/35** | |

**Validated sources used:**
- Wix Harmony launch, Search Engine Journal, 2026-01-21:
  https://www.searchenginejournal.com/wix-introduces-harmony-ai-website-builder/565505/ (confirms
  launch date, AI agent "Aria", English rollout "in the coming weeks". The Nasdaq-hosted Wix press
  release timed out on fetch and needs rechecking before drafting.)
- Google Search Central, "Google Search's guidance on using generative AI content on your website",
  last updated 2026-10-01: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
  (fact-check AI output including titles, meta descriptions, alt text. Scaled content abuse warning.)
- Squarespace Blueprint AI and GoDaddy Airo are referenced from secondary roundups only. Check them
  against the vendors' own pages before any claim about them goes in a draft.

---

## Candidate 2

**Working title:** Google Is Turning Off Call-Only Ads in February 2027. What Service Businesses Need to Change Now

- **Category:** Google Ads and PPC
- **Evergreen or timely:** Timely (hard deadline)
- **New or update:** New. An alternative is a dated section added to BBX-001, but the topic is
  distinct enough for its own URL.
- **Proposed primary keyword:** `call only ads going away` (alternatives: `call ads to call assets`,
  `google call only ads 2027`)
- **Search intent:** Informational and urgent. "What do I need to do?"
- **Audience:** Contractors and home-service owners running their own Google Ads, especially
  phone-first trades
- **Why it matters now:** You haven't been able to create new call-only ads since February 2026.
  Google Ads Help says all existing call-only ads stop receiving impressions in February 2027, about
  four months from now. Any ad group whose only ad is a call-only ad stops showing on that date. The
  replacement is a responsive search ad with call assets. Calls also drive the `phone_call_click`
  key event Brightbox already measures.
- **Evidence of interest:** Qualitative. Google's own "Action Required" help article, the API
  deprecation notice, and trade coverage (Search Engine Land, ppc.land). No related query in the
  site's GSC. No search volume claimed.
- **Questions people are asking:** Will my call ads just stop? What replaces them? Do call assets
  work the same way? Will I lose call reporting? Do I have to rebuild my ad groups?
- **Relevant Brightbox service:** `/google-and-facebook-ads/`
- **Internal pages supported:** `/google-and-facebook-ads/`, BBX-001, BBX-002, `/locations/fort-wayne/`
- **Potential cannibalization:** None. No existing page covers call ads.
- **Opportunity for original experience:** Moderate to high, *if* Archie manages or has migrated
  accounts that used call-only ads. That needs confirming. If he hasn't, this turns into a mostly
  documentation-driven piece and the score drops.

| Category | Score | Why |
|---|---|---|
| Service relevance | 5 | Directly the PPC service, building out the thin PPC hub |
| Local relevance | 4 | Phone-first local trades are exactly who used call-only ads |
| Evidence of interest | 3 | Google flagged it "Action Required". No measured demand on this site |
| Freshness | 4 | Hard deadline 4 months out, but the announcement is a year old and widely covered |
| Firsthand contribution | 3 | Depends on whether Archie has real migrations to show. Unconfirmed |
| Organic ranking opportunity | 3 | Several trade explainers already rank. A contractor-specific angle is the gap |
| Conversion potential | 4 | Owners at risk of ads going dark are good leads |
| **Total** | **26/35** | |

This was scored 29/35 on 2026-07-19 and backlogged for the 09-15 slot. It drops now because a year
of trade coverage has saturated the basic explainer. **Shelf life:** after about January 2027 it
stops being actionable. If it isn't chosen now, it should be cycle 9 (2026-12-01, PPC) at the latest.

**Validated sources used:**
- Google Ads Help, "Action Required: Transition from call ads to call assets", posted 2025-10-03:
  https://support.google.com/google-ads/answer/16598240?hl=en (Feb 2026 creation removed. Feb 2027
  existing call-only ads stop receiving impressions.)
- Google Ads API, Feature deprecations: https://developers.google.com/google-ads/api/docs/deprecations
  (creation unsupported as of 2026-01-01 via API. Serving stops February 2027. "Use Responsive Search
  Ads with call assets instead.") Note: the API page and the Help page differ on the creation cutoff
  (January vs February 2026). The serving end date matches on both.
- Google Ads Help, "How to transition from call ads to call assets":
  https://support.google.com/google-ads/answer/16619010?hl=en (seen via search result only, open
  before drafting)

---

## Candidate 3

**Working title:** Three Google Spam Updates in Four Months: How to Tell Whether One Actually Hit Your Site

- **Category:** SEO and AI Search
- **Evergreen or timely:** Timely hook on an evergreen diagnostic (this is calendar cycle 11's topic,
  brought forward)
- **New or update:** New
- **Proposed primary keyword:** `google spam update traffic drop` (alternatives:
  `september 2026 spam update`, `why did my website traffic drop`)
- **Search intent:** Informational and diagnostic
- **Audience:** Local business owners who noticed a traffic or lead change and are worried
- **Why it matters now:** The Google Search Status Dashboard lists the June 2026 spam update (from
  06-24), the August 2026 spam update (from 08-18), and the September 2026 spam update. The September
  update was announced 2026-09-24 as global and all-language, and completed 2026-10-08 after about
  13.5 days. It finished last week. No core update is listed for June to October 2026.
- **Evidence of interest:** Weak on this site. No related query in GSC. The interest is inferred from
  how often updates have come out, not measured.
- **Questions people are asking:** Was I hit? How long until it recovers? Is it the update or
  seasonality? What does a spam update target, compared with a core update?
- **Relevant Brightbox service:** `/seo/`
- **Internal pages supported:** `/seo/`, BBX-003
- **Potential cannibalization:** None
- **Opportunity for original experience:** Moderate. Archie's real diagnostic process on a client
  account would carry it. Without that, it's a generic explainer.

| Category | Score | Why |
|---|---|---|
| Service relevance | 4 | SEO service, though most local businesses aren't spam-update targets |
| Local relevance | 2 | Spam updates aren't local-specific |
| Evidence of interest | 2 | No on-site demand signal. Inferred only |
| Freshness | 5 | Rollout completed 2026-10-08 |
| Firsthand contribution | 3 | Needs a real client diagnosis to be distinctive |
| Organic ranking opportunity | 3 | News sites own the update-name queries. "How to diagnose" is more winnable |
| Conversion potential | 3 | A worried owner can be a lead, but intent is mostly informational |
| **Total** | **22/35** | Below the usual 24 threshold |

**Validated sources used:**
- Google Search Status Dashboard, ranking history:
  https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history
- September 2026 spam update incident:
  https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu ("Released the September 2026 spam
  update, which applies globally and to all languages", 2026-09-24. "The rollout was complete as of
  October 8, 2026.")

---

## Why Candidate 1 is recommended

It fills the only category with zero articles from this system. It lines up with the largest real
demand cluster in the site's own Search Console, where Brightbox already ranks positions 3 to 5 but
gets almost no clicks. And it has the strongest firsthand angle. Candidate 2 is the better news hook
and is time-limited, but a year of trade coverage has thinned its originality, and it's only strong
if Archie has real call-ad migrations to show. It should take the 12-01 PPC slot if it isn't chosen
now. Candidate 3 scores below threshold and is included for coverage.

## Research notes and limits

- Reddit not used (per the scheduled task's instruction for this run).
- GBP messaging (calendar cycle 6) is on hold. The 2026 "return of messaging" claim is unconfirmed by
  Google. Recorded in `topic-backlog.md`.
- Several secondary GBP "2026 updates" roundups make claims that contradict each other (for example,
  Q&A both "discontinued" and "AI-drafted answers"). None were used.
- No retrieved page contained instructions addressed to the agent.

## Files changed this run

- `clients/brightbox/research/2026-10-15-discovery.md` (this file)
- `clients/brightbox/performance/BBX-004-28day-2026-10-15.md`
- `clients/brightbox/performance/baselines.csv` (2 rows appended: BBX-004 28-day page, site 90-day)
- `clients/brightbox/content-tracker.csv` (BBX-004 review fields, new BBX-005 row)
- `clients/brightbox/topic-backlog.md` (GBP messaging on hold. Call-only ads rescored)
