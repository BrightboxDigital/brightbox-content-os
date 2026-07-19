# Discovery Report: Cycle 1, August 1, 2026

**Run date:** July 19, 2026
**Slot:** Cycle 1, publication August 1, 2026
**Planned category:** Google Ads and PPC
**Planned designation:** Evergreen, new article
**Calendar working title:** Where Small Google Ads Budgets Get Wasted
**Status:** Topic Approval Needed

---

## Research method and limits

**Window:** last 90 days, roughly April 19 to July 19, 2026.

**Sources used:** Google Ads Help official documentation and announcements, the Google Ads product
blog, and industry coverage used only to gauge attention, never as factual authority.

**Two honest limits on this report:**

1. **Reddit was not consulted.** The research tooling is blocked from reddit.com, so the workflow's
   Reddit step could not run. Nothing in this report claims Reddit as evidence. Community pain
   points are inferred from Search Console data and published practitioner commentary instead.
2. **No search volume figures appear anywhere in this report.** No keyword tool was consulted.
   Where interest is claimed, the evidence is named and is either Brightbox's own Search Console
   data or dated primary documentation.

---

## What Search Console actually shows

Real data, 90 days, April 18 to July 17, 2026. Brightbox's property.

| Query | Impressions | Clicks | Avg position |
|---|---|---|---|
| digital ads company near me | 132 | 0 | 40.6 |
| digital ads business near me | 109 | 0 | 21.4 |
| google ads management fort wayne | 11 | 0 | 32.4 |
| fort wayne ad agencies | 7 | 0 | 48.9 |
| google ads management newhaven | 6 | 0 | 48.0 |
| ad agencies in fort wayne | 4 | 0 | 53.2 |
| ppc management fort wayne | 1 | 0 | 56.0 |

**274 ads-related impressions. Zero clicks. Average position ranges from 21.4 to 56.**

These figures are now recorded as an immutable baseline in
`clients/brightbox/performance/query-baselines.csv`, snapshot dated 2026-07-19, label
"PPC gap baseline". Any future claim that the PPC article helped must be measured against that row,
not against recollection.

Site wide and page level baselines were captured the same day:

| Scope | Impressions | Clicks | Avg position | Sessions | Key events |
|---|---|---|---|---|---|
| Entire site, 90d | 22,408 | 88 | 13.67 | 641 | 0 |
| `/google-and-facebook-ads/`, 90d | 47 | 1 | 11.28 | 11 | 0 |
| `/blog/`, 90d | 159 | 1 | 11.29 | 123 | 0 |

The zero key events are expected and not a finding: key events were only configured on 2026-07-19,
so the counter starts at zero by definition. It is recorded anyway, because a baseline of zero is
still a baseline.

Brightbox is visible for paid-advertising queries and ranks nowhere near where anyone clicks. This
is direct measured evidence that the PPC gap identified in the site audit is real, not theoretical.

**Important qualification, and it constrains what this article can do.** Every one of those queries
is *service intent*, someone looking to hire an agency. A blog article will not rank for
"google ads management fort wayne", and it should not try. That is the service page's job. What a
blog article can do is build genuine topical support around `/google-and-facebook-ads/`, which
currently has zero supporting content on the entire site.

**Cannibalization risk: none.** Brightbox has published seven articles and not one covers Google Ads
or PPC. There is nothing to compete with.

---

## What changed in the last 90 days

### 1. Target-based bid strategies change on August 17, 2026. Confirmed.

**Primary source:** [Changes to target based bid strategies, Google Ads Help](https://support.google.com/google-ads/answer/17061251)

- **Announced and dated:** takes effect **August 17, 2026**
- **Who is affected:** campaigns with **"Limited by budget"** status using a target-based bid
  strategy such as Target CPA or Target ROAS
- **Campaign types:** Search, Shopping, Performance Max, Demand Gen, Display, Hotel, Travel.
  App, Video reach and Video view campaigns keep previous behavior
- **Confirmed, not a test.** This is official Google documentation, not an industry observation
- **Google's own example, quoted:** "If your campaign's Target CPA is $10, but your recent actual
  CPA performance is $5, your campaign will deliver more closely to a $10 actual CPA starting
  August 17, 2026."
- **Preparation tool:** the Bid Target Adjustment Tool became available **July 6, 2026**

**Why this matters enormously for Brightbox's audience.** "Limited by budget" is, by definition,
the status of small advertisers. Budget-limited campaigns frequently *overperform* their targets
because Smart Bidding enters only the cheapest winnable auctions. Google's own example describes a
campaign whose real cost per lead could move from $5 toward $10 unless the advertiser lowers the
target first.

This is not a subtle change for a small local business. It is a potential doubling of cost per lead
for exactly the businesses Brightbox serves, on a fixed date, with a required manual action.

**What remains uncertain, and must be stated as uncertain in any article:** Google says budgets and
targets will not change automatically without manual action. How much any individual account's
actual CPA moves is unknown and will vary. **No article may promise a specific outcome.**

### 2. Call-only ads are being retired. Confirmed.

**Primary source:** [Action Required: Transition from call ads to call assets, Google Ads Help](https://support.google.com/google-ads/answer/16598240)

- **February 2026:** "All options to create a new call-only ad will be removed." Already passed
- **February 2027:** "All existing call-only ads will stop receiving impressions."
- **Required action, quoted:** "To continue generating valuable phone call leads, you must
  transition to using call assets within responsive search ads (RSAs)."

Directly relevant to contractors and home service businesses, for whom a phone call is the lead.

### 3. AI Max reached general availability and DSA migration moved. Confirmed.

**Primary source:** [Google's Dynamic Search Ads are upgrading to AI Max](https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/)

- AI Max for Search reached general availability **April 15, 2026**
- On **June 11, 2026** Google **postponed** automatic DSA migration from September 2026 to
  **February 2027**
- The postponement applies **only to DSA**. The September 2026 deadline for Automatically Created
  Assets and campaign-level broad match was **not** changed

This corrects the topic backlog entry, which flagged uncertainty about whether AI Max still existed
under that name. It does, and it is now GA.

---

## Candidates

### Candidate 1: The Google Ads change on August 17 that could double your cost per lead

| | |
|---|---|
| Category | Google Ads and PPC |
| Type | Timely, new article |
| Proposed primary keyword | google ads bidding change august 2026 |
| Search intent | Informational, urgent. "What is happening and what do I do before the date" |
| Audience | Small local advertisers running budget-limited campaigns, and anyone managing their own account |
| Supports | `/google-and-facebook-ads/` |

**Why it matters now:** hard deadline 16 days after publication, affecting precisely the
budget-limited advertisers Brightbox serves.

**Evidence of interest:** Google published a dedicated help article and a preparation tool. Industry
publications covered it and Search Engine Journal reported that Google issued a follow-up
clarification after advertiser concerns, which indicates enough pushback to warrant a response.

**Questions people are asking:** Will my costs go up? Do I have to do anything? What happens if I
ignore it? How do I find out if my campaigns are budget limited?

**Original value opportunity:** Archie can check real client accounts for "Limited by budget" status
and describe what he actually found and what he changed. Screenshot of the Bid Target Adjustment
Tool would be an original asset.

**Cannibalization:** none.

**The problem with this candidate:** its useful life ends on August 17. Brightbox would also be
publishing weeks after Search Engine Journal, ppc.land, JumpFly and numerous agencies already
covered it. Winning a news race against established publications with a two-week-old story is not
a realistic goal, and after the date passes the article is a historical record.

**Score: 29 / 35**

| Category | Score | Reason |
|---|---|---|
| Brightbox service relevance | 5 | Google Ads is a core service |
| Fort Wayne / local relevance | 4 | Hits local advertisers hard, but the change itself is global |
| Evidence of current interest | 5 | Google published a clarification in response to advertiser concern |
| Freshness / timeliness | 5 | Hard confirmed date, 16 days out |
| Archie firsthand opportunity | 4 | Real account checks available, subject to his verification |
| Organic ranking opportunity | 2 | Crowded, late, and demand collapses after August 17 |
| Conversion potential | 4 | Urgency drives account audit requests |

---

### Candidate 2: Where small Google Ads budgets actually get wasted — RECOMMENDED

| | |
|---|---|
| Category | Google Ads and PPC |
| Type | Evergreen, new article, with one dated section |
| Proposed primary keyword | google ads small budget (to be refined at keyword approval) |
| Search intent | Informational, commercial investigation. "I am spending money and not sure it is working" |
| Audience | Local service businesses spending roughly $500 to $3,000 a month, managing it themselves or through a cheap agency |
| Supports | `/google-and-facebook-ads/`, `/contact/` |

**The structural idea:** the evergreen article the calendar planned, with the August 17 change as
its most urgent and concrete section rather than as the whole piece. The reader gets the timely
warning now and a genuinely useful article afterward.

**Why it matters now:** small advertisers waste money in a small number of repeatable ways, and one
of them acquires a hard deadline on August 17. That is a real reason to read it this month rather
than someday.

**Evidence of interest:** Brightbox's own Search Console shows 274 ads-related impressions with zero
clicks over 90 days, confirming local demand around paid advertising that Brightbox is not
capturing. The August 17 change has documented practitioner attention. No search volume figure is
claimed for the article's own keyword.

**Questions people are asking:** Am I wasting money? Why is my cost per lead going up? Should I be
running Performance Max? Is my agency doing anything? What is a reasonable cost per lead?

**Original value opportunity, and this is the strongest of the three:** Archie audits real accounts.
He can supply what he actually finds most often, a real anonymized example of waste and what it cost,
his own checklist for a budget-limited account, and a defensible view on what small budgets should
and should not attempt. This is the candidate where his experience carries the most weight.

**Cannibalization:** none.

**Shelf life:** long. The August 17 section can be revised in place afterward without the article
losing its purpose, which is exactly the refresh pattern the system is built to handle.

**Score: 31 / 35**

| Category | Score | Reason |
|---|---|---|
| Brightbox service relevance | 5 | Core service, and the site's largest content gap |
| Fort Wayne / local relevance | 4 | Written for local service businesses, though not geographically bound |
| Evidence of current interest | 4 | Measured Search Console demand plus documented attention on the dated change |
| Freshness / timeliness | 4 | A dated confirmed hook inside an evergreen frame |
| Archie firsthand opportunity | 5 | Strongest of the three. Real audits, real waste, real numbers if he can substantiate them |
| Organic ranking opportunity | 4 | Long runway, less head-on competition than the news story |
| Conversion potential | 5 | Leads naturally to an ad account review, which is a service Brightbox sells |

---

### Candidate 3: Google is retiring call-only ads. What service businesses need to do.

| | |
|---|---|
| Category | Google Ads and PPC |
| Type | Timely with a long deadline, new article |
| Proposed primary keyword | call only ads deprecated |
| Search intent | Informational, action oriented |
| Audience | Contractors, home service and any business whose leads arrive by phone |
| Supports | `/google-and-facebook-ads/`, `/locations/fort-wayne/` |

**Why it matters now:** new call-only ads can no longer be created as of February 2026, and existing
ones stop serving in February 2027. Any service business still relying on them has a deadline.

**Evidence of interest:** Google labeled its own documentation "Action Required," which is
unusually direct language for Google Ads Help.

**Questions people are asking:** Will my phone stop ringing? What replaces call-only ads? Do I have
to rebuild my campaigns? Will this cost more?

**Original value opportunity:** phone calls are how most of Brightbox's audience receives leads, and
Archie sets up call tracking for clients. There is a natural tie to measurement, which Brightbox has
just implemented on its own site.

**Cannibalization:** none.

**Why it did not win:** the February 2027 deadline is far enough away that urgency is weak, and the
audience is narrower, only advertisers still using call-only ads specifically.

**Score: 29 / 35**

| Category | Score | Reason |
|---|---|---|
| Brightbox service relevance | 5 | Core service |
| Fort Wayne / local relevance | 5 | Phone calls are the primary lead for contractors, Brightbox's core audience |
| Evidence of current interest | 3 | Confirmed and documented, but less discussed than the bidding change |
| Freshness / timeliness | 4 | Confirmed dated deprecation, still actionable |
| Archie firsthand opportunity | 4 | Real call tracking setup experience |
| Organic ranking opportunity | 4 | Less saturated than the bidding change |
| Conversion potential | 4 | Clear path to an ad account review |

---

## Recommendation

**Candidate 2, at 31 out of 35.**

Three reasons it beat the others.

**It is the only one Brightbox can realistically win.** Candidate 1 is a news story that Search
Engine Journal, ppc.land and several agencies published two weeks ago. Brightbox is a one person
business arriving late to a story that expires on August 17. That is not a fight worth picking. The
evergreen frame competes on a different axis, where Archie's actual account experience is the
differentiator rather than speed.

**It carries the most of Archie's experience.** The originality gate requires at least two genuine
original-value elements. Candidate 2 supports the most: what he actually finds when auditing small
accounts, a real anonymized waste example, and his own checklist. Candidate 1 is mostly a summary of
Google's announcement, which is the weakest possible foundation for an article.

**It keeps the timely value without the timely cost.** The August 17 change goes in as a dated,
primary-sourced section with a clear deadline and a specific action. Readers get the urgent warning.
After August 17 that section gets revised and the article keeps working, rather than becoming an
archive of something that already happened.

It also matches what the calendar planned for this slot, which specified evergreen for cycle 1 and
reserved cycle 4 on September 15 for the timely PPC piece. **Candidate 3 is a strong fit for that
September 15 slot** and should go to the topic backlog rather than being discarded.

---

## Source ledger for this report

| Claim | Source | Type | Date checked | Supports the claim |
|---|---|---|---|---|
| Bid strategy change takes effect August 17, 2026, affects budget-limited campaigns, $10/$5 CPA example, tool available July 6, 2026 | [Google Ads Help 17061251](https://support.google.com/google-ads/answer/17061251) | Primary | 2026-07-19 | Yes, quoted directly |
| Call-only ad creation removed February 2026, existing stop serving February 2027 | [Google Ads Help 16598240](https://support.google.com/google-ads/answer/16598240) | Primary | 2026-07-19 | Yes, quoted directly |
| AI Max GA April 15, 2026, DSA auto-migration moved to February 2027 on June 11, 2026 | [Google blog, DSA upgrade to AI Max](https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/) | Primary | 2026-07-19 | Yes |
| Google issued a clarification after advertiser concerns | [Search Engine Journal](https://www.searchenginejournal.com/google-clarifies-smart-bidding-update-after-advertiser-concerns/581804/) | Secondary | 2026-07-19 | Used only as evidence of attention, not as fact |
| 274 ads-related impressions, zero clicks, 90 days | Brightbox Search Console via `performance-check` | Primary, first party | 2026-07-19 | Yes |
| Zero existing PPC articles on the site | `site-inventory.csv`, seven posts audited | Primary, first party | 2026-07-19 | Yes |

**Not consulted:** Reddit, blocked to the research tooling. No keyword volume tool was used and no
volume figure is claimed anywhere in this report.

---

## Next action

Archie chooses:

1. **Topic 1** — the August 17 bidding change, timely news piece
2. **Topic 2** — where small budgets get wasted, evergreen with a dated section (**Recommended**)
3. **Topic 3** — call-only ads retirement for service businesses
4. Request different ideas
5. Update an existing article instead

**No NeuronWriter analysis will be created until both the topic and the seed keyword are approved.**
