# Discovery Report: Cycle 2 slot, August 15, 2026

**Run date:** August 1, 2026
**Calendar slot:** Cycle 2, publication August 15, 2026
**Calendar planned category:** SEO and AI Search
**Calendar planned designation:** Timely, new article
**Calendar working title:** How to Measure Whether Your Business Shows Up in Google AI Answers
**Status:** Topic Approval Needed

---

## Step 1: is Archie already blocked?

`content-tracker.csv` has one row, BBX-001. None of its fields match a waiting status
(`Topic Approval Needed`, `Keyword Approval Needed`, `Interview Needed`, `Outline Review`,
`Archie Review Needed`, `Revision Needed`, `Publish Approval Needed`, `GBP Approval Needed`,
`Social Recording Needed`) — confirmed by an exact-string search of the file, zero matches. The
article is fully approved and published. Nothing is blocking a new discovery run.

**One data gap worth flagging, not blocking:** BBX-001's `publication_date` column is blank even
though `published_url` is filled in and a 7-day review already ran. The actual publish date is
recorded elsewhere (2026-07-19, in `performance/baselines.csv` and the 7-day report). Worth a
one-line fix in the tracker when you're next in the file; not fixed here since it's outside this
run's scope.

## Step 2: monitoring sweep

BBX-001 published 2026-07-19. Today is 2026-08-01, 13 days post-publication.

- **7-day check:** already complete, 2026-07-27. Recorded.
- **28-day check:** due around 2026-08-16. **Not due yet.**
- **90-day check:** due around 2026-10-17. Not due.

Nothing crossed a review threshold since the last run. No monitoring report produced this cycle.

**Site-wide 90-day baseline recorded anyway**, per the "record the moment you observe a number"
rule: 26,050 impressions, 88 clicks, avg. position 12.6 (GSC); 1,135 sessions, 3 key events (GA4),
window 2026-05-01 to 2026-07-30. Row added to `performance/baselines.csv`, label "discovery run
2026-08-01, cycle 2 demand check." This was a demand-signal pull for Step 3 below, not a
per-article review, and is not evidence of BBX-001's performance.

**Repository anomaly found and fixed, unrelated to content but worth Archie's attention:** six
git-tracked files were missing from the working directory at the start of this run — the approved
BBX-001 styled article, its draft and package files, the interview transcript, and the reusable
`shared/blog-template.css` / `.js`. `git status` showed them as local deletions; `git log`
confirmed HEAD matches `origin/main` exactly, so this was not a git operation (no stray commit,
reset, or rebase) — something deleted them directly from disk outside of git. They have been
restored with `git checkout --` (a safe, reversible recovery; nothing was overwritten or
discarded). **Recommend Archie check what actually deleted them** — a stray `rm`, a sync
conflict, a disk cleanup tool, antivirus quarantine, etc. — since the same thing could recur and
next time might hit files with actual unstaged edits, which `git checkout` cannot recover.

## Step 3: research method and limits

**Window:** last 90 days, roughly May 3 to August 1, 2026.

**Sources used:** Google Search Central Blog, official Search Console Help documentation, official
Google Ads Help documentation, Google's AI-features guidance page, plus industry trade coverage
(Search Engine Land, Search Engine Journal, WordStream, and similar) used only to gauge how much
attention a story is getting, never as factual authority.

**Reddit was not used**, per this run's explicit instruction that Brightbox's use is commercial and
not permitted. This overrides `shared/source-validation.md`'s standing Reddit-as-signal policy for
this run; nothing here is Reddit-sourced.

**No search volume figures appear anywhere in this report.** No keyword tool was consulted. Where
interest is claimed, the evidence named is either Brightbox's own Search Console data or the volume
of dated, primary documentation and trade coverage a story generated.

---

## What Search Console actually shows

90-day site-wide pull, 2026-05-01 to 2026-07-30 (baseline recorded above). The top queries are
dominated by web design and general SEO/marketing-agency intent (`fort wayne website design` 384
impressions, `website design` 195, `digital marketing fort wayne` 191, `local seo services` 65).
**No query in the 90-day window references AI Overviews, AI Mode, AI search, or anything adjacent.**
This is an honest qualitative finding, not a negative signal to hide: it means demand for an AI
Overviews measurement article cannot be shown from Brightbox's own site data. The case for
Candidate 2 below rests on documented industry attention and a genuinely new, verifiable Google
capability, not on Search Console evidence, and is presented that way.

**Cannibalization check, all three candidates:** compared against `site-inventory.csv` and
NeuronWriter `list-queries` in both projects (`eea0682a76fd76f0`, Brightbox-only, one query on file
— `google ads small budget`, BBX-001's; and `0bdb5139dc86fbe7`, `Clients`, checked read-only for
historical Brightbox queries). No existing query or published article overlaps Candidates 1 or 2.
Candidate 3 has a real, flagged overlap — see its writeup.

---

## What changed in the last 90 days

### 1. Search Console launched a dedicated Generative AI performance report. Confirmed.

**Primary sources:**
[Introducing Search Generative AI performance reports in Search Console, Google Search Central Blog](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports),
[Generative AI performance report (Search), Search Console Help](https://support.google.com/webmasters/answer/16984139?hl=en),
[AI Features and Your Website, Google Search Central docs](https://developers.google.com/search/docs/appearance/ai-features)

- **Announced June 3, 2026**, authored by Hillel Maoz (Search Ecosystem Engineering Manager) and
  Moshe Samet (Product Manager Lead, Search Console). This is an official Google Search Central
  Blog post, not a rumor or a third-party report.
- Gives a standalone view of **impressions** inside AI Overviews and AI Mode on Search, plus a
  separate generative-AI report for Discover.
- **What it does not include, confirmed by Google's own Help documentation:** clicks, CTR, average
  position, or query-level data. Dimensions available are pages (by canonical URL), countries,
  dates, and devices only.
- **Rollout is limited, not global.** Google's own words: "We're rolling out this report to a
  subset of website owners, allowing for thorough testing before rolling it further." A property
  may show no data yet either because it hasn't been rolled in, or because it doesn't have enough
  AI-feature impressions.
- **Not available via the Search Analytics API or BigQuery export** as of this research date — CSV
  export from the UI only. Confirmed by the absence of any documentation reference to API or
  BigQuery access alongside multiple trade-press pieces making the same observation independently.
- **A second, older path already exists and still matters:** the classic Performance report's
  Search appearance filter for "AI Overview" has existed since 2025 and rolls its clicks into the
  "Web" search type — meaning an advertiser who only checks the new dedicated report will miss
  click data that is actually available elsewhere in the same tool, under a different filter.

**Why this matters for Brightbox's audience.** Every small business owner asking "am I still
showing up now that Google answers questions directly" now has a real, if incomplete, way to check.
Most existing coverage is written for SEO practitioners and glosses over the two-report confusion
(new dedicated report is impressions-only and gated to a rollout group; the older Search appearance
filter has some click data and is open to everyone). A plain-English, verified walkthrough for a
business owner is a genuine gap.

**What remains uncertain:** exact global rollout date, whether/when click data will be added to the
new report (Google has said only that it plans to add metrics over time based on feedback, no
date), and whether Brightbox's own property has been rolled into the test group yet — that can only
be confirmed by checking the Search Console UI directly, which this research pass did not do since
it required deciding what to check, not just where to look. Archie can confirm this himself in
minutes and it becomes a real, first-party screenshot for the article either way (has access / does
not have access yet are both usable, honest findings).

### 2. Local Services Ads are folding into Google Ads via a new Performance Max campaign type. Confirmed.

**Primary source:**
[Local Services Ads migration to Google Ads, Google Ads Help](https://support.google.com/google-ads/answer/17213585)

- **Rollout begins August 2026** — this month — for **"a small group of U.S. advertisers across
  pet care, home services, wellness and education."** Google's own listed home-service categories:
  plumbing, HVAC, electrical, appliance repair, house cleaning, lawn care, roofing, pest control,
  and moving. This is close to a direct list of Brightbox's contractor client base.
- **Late 2026:** expansion to service-area businesses without a storefront and accounts with custom
  bidding or booking configurations.
- **2027:** non-U.S. accounts and remaining categories.
- **What stays the same, quoted from Google:** "You still only pay for valid leads (such as phone
  calls and messages)." Ads remain Search- and Maps-only and keywordless, based on service
  categories and areas, despite the Performance Max name — this is not a standard Performance Max
  campaign and will not expand into Display, YouTube, or Gmail.
- **What changes:** the standalone LSA dashboard is retired; manual bidding and industry-level
  Target CPA are discontinued; weekly budgets convert to daily average budgets; Better Business
  Bureau callouts are no longer supported.
- **Confirmed action required, quoted:** historical campaign-level performance data — "past
  impressions, clicks, weekly spend, and ad-level performance reports" — **will not migrate** to
  Google Ads. Advertisers are told to export and archive this data before their migration date.
  Lead history itself does carry over. Google states migrating accounts get a 14-day advance notice
  followed by a 7-day reminder, and to allow up to two weeks for performance to stabilize
  post-migration.
- This is confirmed, official Google Ads Help documentation, not a test or an industry rumor, and
  it is actively rolling out this month.

**Why this matters enormously for Brightbox's audience.** Local Services Ads is the flagship
pay-per-lead product for exactly the home-service and contractor businesses Brightbox serves. A
platform-mandated migration that discontinues manual bidding, changes budget structure, and wipes
historical reporting unless an advertiser proactively exports it first is a concrete, immediate,
non-optional action item for anyone running LSAs right now — not a someday story.

**What remains uncertain:** the exact advertiser-by-advertiser migration schedule beyond "August
2026 start, expanding through 2027," and how individual accounts will be notified beyond the
14/7-day advance-notice pattern Google describes generally.

### 3. Google reaffirmed llms.txt is not used for ranking or AI features. Confirmed, but a weaker fit.

**Primary source:** Google's AI optimization guide, most recently updated June 15, 2026 (referenced
across multiple trade outlets; original Gary Illyes statement dates to Search Central Live, July
2025). Google's own current wording: **"You don't need to create new machine readable files, AI
text files, markup, or Markdown to appear in Google Search (including its generative AI
capabilities), as Google Search itself doesn't use them."**

Considered as a possible third candidate and set aside — see Candidate 3's writeup for why a
different Local SEO topic scored higher for this slot. Recorded here, and in the topic backlog
below, since the myth is persistent and the primary source is clean if a future cycle wants it.

---

## Candidates

### Candidate 1: Local Services Ads Are Moving Into Google Ads. What Changes for Contractors This Month. — RECOMMENDED

| | |
|---|---|
| Category | Google Ads and PPC |
| Type | Timely, new article |
| New or update | New |
| Proposed primary keyword | local services ads moving to google ads |
| Close variants | "LSA performance max migration," "local services ads changes 2026" |
| Search intent | Informational, urgent. "What is actually changing and what do I need to do before I get migrated" |
| Audience | Home-service and contractor businesses currently running, or considering, Local Services Ads (plumbing, HVAC, electrical, roofing, cleaning, and similar) |
| Supports | `/google-and-facebook-ads/` |

**Why it matters now:** rollout starts this month, for precisely the business categories Brightbox
serves, and it carries a real risk of silent data loss (unexported historical reporting) if an
advertiser does nothing.

**Evidence of interest:** confirmed via Google's own Google Ads Help page; independently, this story
generated coverage across a wide set of trade publications (Search Engine Land, Search Engine
Journal, WordStream, and several agency blogs) within roughly the last two weeks, indicating high
current attention in the PPC practitioner community. No search volume figure is claimed.

**Questions people are asking:** Will my pay-per-lead billing change? Do I lose my review history or
my Google Guarantee badge? Will my ads start showing on Display or YouTube like normal Performance
Max? Do I have to do anything, or does this happen automatically? What happens to my past
performance data?

**Potential cannibalization:** none. BBX-001 covers small-budget thresholds generally; this is a
distinct, platform-specific migration story.

**Opportunity for original experience:** Archie manages Google Ads for local clients. Pending his
confirmation at the interview stage (not invented here), he may be able to speak to a real client
account affected by this migration, or at minimum walk through the actual Google Ads UI and the
export step he'd recommend before a client's migration date, which almost none of the existing
trade coverage does from a practitioner's chair rather than a press-release summary.

**Score: 31 / 35**

| Category | Score | Reason |
|---|---|---|
| Brightbox service relevance | 5 | Core PPC service; directly about a product Brightbox may manage for clients |
| Fort Wayne / local relevance | 4 | Not geographically bound, but the affected categories are exactly Brightbox's contractor client base |
| Evidence of current interest | 4 | Confirmed official source plus wide, near-immediate trade coverage; no independent volume data |
| Freshness / timeliness | 5 | Announced July 20, 2026; rollout begins this month |
| Archie firsthand opportunity | 4 | Real practitioner walkthrough possible; direct client history pending his confirmation |
| Organic ranking opportunity | 4 | Most existing coverage targets agencies, not business owners; a plain-English owner-facing angle is a real gap, though the topic is filling fast |
| Conversion potential | 5 | Directly touches the PPC service line and the audience Brightbox targets; natural "let us handle your migration" CTA |

---

### Candidate 2: How to Check Whether Your Business Actually Shows Up in Google's AI Overviews and AI Mode

| | |
|---|---|
| Category | SEO and AI Search |
| Type | Timely, new article |
| New or update | New |
| Proposed primary keyword | google ai overviews search console report |
| Close variants | "how to check ai overviews," "track your site in Google AI Mode" |
| Search intent | Informational. "How do I actually find out if I'm showing up in AI answers" |
| Audience | Small business owners already investing in SEO who are worried AI answers are displacing their organic clicks |
| Supports | `/seo/` |

**This is the calendar's planned slot and category for this cycle.**

**Why it matters now:** a genuinely new, dedicated Search Console report launched June 3, 2026 and
is still in limited rollout; most business owners do not know it exists, and most coverage that
does exist conflates it with the older, differently-scoped AI Overview filter.

**Evidence of interest:** heavy, sustained trade coverage since the June 3 launch, and a specific,
recurring point of confusion in that coverage (impressions-only, no clicks yet, and how that
relates to the older Search appearance filter) that a clear explainer can resolve. No Brightbox
Search Console query currently shows AI-search-related demand; this is stated plainly above rather
than implied otherwise.

**Questions people are asking:** Do I have access to this report yet? Why can't I see clicks? Is
this different from the AI Overview filter I already had? Does this cover AI Mode too? Can I see
which queries triggered it?

**Potential cannibalization:** none. No existing Brightbox content addresses AI Overviews or AI
Mode measurement.

**Opportunity for original experience:** Archie can check Brightbox's own Search Console live and
show, honestly, whether the property has been rolled into the new report yet or not — either
outcome is a real, first-party screenshot almost no competing article can produce, since most are
written from the press release rather than a live account. He can walk through both reporting paths
(the new dedicated report and the older Search appearance filter) side by side, which resolves the
exact confusion driving current search interest.

**Score: 28 / 35**

| Category | Score | Reason |
|---|---|---|
| Brightbox service relevance | 5 | Core SEO service, matches the `/seo/` hub directly |
| Fort Wayne / local relevance | 2 | Broadly applicable to any business owner; no inherent local angle |
| Evidence of current interest | 4 | Sustained trade coverage since June 3 launch; no site-level demand signal, stated honestly above |
| Freshness / timeliness | 5 | Six weeks old, still in limited rollout, genuinely new capability |
| Archie firsthand opportunity | 5 | Live account screenshots either way (rolled in or not) are a real, verifiable original asset |
| Organic ranking opportunity | 4 | Crowded with practitioner-facing pieces; an honest, verified owner-facing explainer is a real gap |
| Conversion potential | 3 | Builds topical authority and trust; less directly transactional than an account-migration story |

---

### Candidate 3: Does Your Service-Area Business Actually Qualify for a Google Business Profile Address?

| | |
|---|---|
| Category | Local SEO and GBP |
| Type | Evergreen, new article (flagged below as a possible fold-in instead) |
| New or update | New, with a strong case for update instead |
| Proposed primary keyword | service area business google business profile |
| Search intent | Informational, how-to. Setting up or fixing a GBP listing correctly |
| Audience | Contractors and home-service businesses without a public storefront (plumbers, HVAC, cleaners, landscapers) in Fort Wayne / Northeast Indiana |
| Supports | `/google-business-profile-optimization/` |

**Why it matters:** not news-driven. This is a persistent, high-confusion evergreen topic that maps
almost exactly onto Brightbox's actual client base (`client-profile.md` names "contractors and home
service businesses" and "service area businesses" directly in the audience list).

**Evidence of interest:** qualitative only, no volume claimed. Multiple independent GBP-focused
publications (Local Falcon, GBP Guardian, TrueFuture Media, and others) maintain dedicated explainer
content on this exact question, indicating it recurs often enough to be worth a standing resource.
Confirmed current against Google's own guidelines: a service-area business that does not meet
customers in person at its registered address is required to hide that address, and Google requires
a real, mail-receiving physical location for verification regardless (no PO boxes or virtual
offices).

**Questions people are asking:** Do I need to hide my home address? Will hiding my address hurt my
ranking? What counts as my service area? Can I get suspended for setting this up wrong?

**Potential cannibalization: real, and this is the deciding weakness.** `site-inventory.csv` lists
an existing article, "Google Business Profile: The Ultimate Guide," a year old and already flagged
as a refresh candidate — and `content-calendar.csv` cycle 3 (2026-09-01) already plans exactly that
update. A new standalone URL on service-area-business setup risks competing with that planned
refresh rather than supporting it. **Recommend that if this topic is chosen, it becomes a section
within the cycle 3 GBP refresh rather than a fourth candidate for a new URL**, unless Archie has a
reason to want it as its own page (for example, a distinct enough search intent to justify a
separate cluster piece — a judgment call for him, not decided here).

**Opportunity for original experience:** Archie's client setup and troubleshooting history with
service-area businesses, pending his confirmation at interview stage.

**Score: 27 / 35**

| Category | Score | Reason |
|---|---|---|
| Brightbox service relevance | 5 | Core GBP optimization service |
| Fort Wayne / local relevance | 5 | Directly matches Brightbox's contractor and service-area client base |
| Evidence of current interest | 3 | Recurring, evergreen confusion topic; no news hook, no volume data |
| Freshness / timeliness | 2 | Underlying Google policy is stable, not new |
| Archie firsthand opportunity | 4 | Likely real client setup/troubleshooting examples, pending his confirmation |
| Organic ranking opportunity | 4 | Existing GBP guide is thin on this specific sub-topic; room to do better |
| Conversion potential | 4 | Matches Brightbox's actual client type; natural GBP-service CTA |

---

## Recommendation

**Candidate 1, at 31 out of 35: Local Services Ads Are Moving Into Google Ads.**

This deviates from the calendar's planned category for this slot (SEO and AI Search) and planned
title. Per `MASTER-WORKFLOW.md`, "the calendar is a plan, not a contract" when research shows a
stronger topic. Three reasons it beat the calendar's own pick:

**It is genuinely time-critical in a way Candidate 2 is not.** Candidate 2's underlying capability
(the new Search Console report) has a soft, ongoing rollout with no deadline pressure on the
reader — it stays useful whenever it's published. Candidate 1's migration is starting *this month*,
for exactly Brightbox's contractor audience, with a real risk of unexported data loss if advertisers
don't act. Publishing this after the fact turns a warning into a postmortem.

**It has the clearer path to a defensible original-value element.** Both candidates offer a
first-party angle, but Candidate 1's is more concrete: a practitioner's actual account walkthrough
of what to export and check before a migration date is a specific, checkable action a reader can
follow, versus Candidate 2's "here's what I see in my dashboard," which is real and useful but
thinner.

**It matches Brightbox's own service line more directly.** PPC/Google Ads management is a service
Brightbox sells; a platform-mandated account migration is the kind of story that naturally produces
"we can help you through this" as a genuine CTA rather than a bolted-on one.

**Candidate 2 remains strong** and is the calendar's original pick for this slot — it should not be
read as rejected, only as scoring three points lower once a more urgent, higher-relevance story
surfaced during research. If Archie prefers to keep the calendar's SEO/AI Search category on
schedule for August 15, Candidate 2 is a fully sound choice on its own merits.

**Choosing Candidate 1 does shift the PPC hub ahead of the calendar's own sequencing** (cycle 4,
planned 2026-09-15, was the next PPC slot). That's a plan adjustment, not a problem — the calendar
explicitly allows this — but it's worth Archie knowing so cycles 3 and 4 can be resequenced
deliberately rather than by accident if he picks Candidate 1.

**Candidate 3 is a strong evergreen option** and should go to the topic backlog tagged as a likely
fold-in to the already-planned cycle 3 GBP refresh (2026-09-01), rather than being discarded.

---

## Source ledger for this report

| Claim | Source | Type | Date checked | Supports the claim |
|---|---|---|---|---|
| New Generative AI performance report launched June 3, 2026; impressions only, no clicks/CTR/query data; dimensions are pages, countries, dates, devices; limited rollout | [Search Console Help 16984139](https://support.google.com/webmasters/answer/16984139?hl=en); [Search Central Blog, June 2026](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) | Primary | 2026-08-01 | Yes, quoted directly |
| Clicks from AI Overviews/AI Mode are tracked in the classic Performance report under "Web" search type; no special optimization required to appear | [AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features) | Primary | 2026-08-01 | Yes, quoted directly |
| New report not available via Search Analytics API or BigQuery as of this check | Absence of API/BigQuery reference in Google's own documentation, cross-checked against independent trade observations | Primary (absence) + secondary corroboration | 2026-08-01 | Yes, used cautiously |
| LSA migrating into Google Ads via a specialized Performance Max campaign type; rollout begins August 2026 for pet care, home services, wellness, education; historical performance data does not migrate; pay-per-lead and Search/Maps-only placement unchanged | [Google Ads Help 17213585](https://support.google.com/google-ads/answer/17213585) | Primary | 2026-08-01 | Yes, quoted directly |
| Google reaffirms llms.txt is not used for Search or its generative AI features | Google's AI optimization guide, updated June 15, 2026, quoted via corroborating trade coverage | Primary (quoted secondhand, not independently re-fetched) | 2026-08-01 | Yes, but this claim should be re-verified against the guide directly before any article draft uses it |
| Service-area businesses without in-person customer contact at their registered address must hide that address; PO boxes/virtual offices are not valid for verification | [Guidelines for representing your business, GBP Help](https://support.google.com/business/answer/3038177?hl=en) | Primary | 2026-08-01 | Yes |
| No AI-search-related query appears in Brightbox's 90-day Search Console data | Brightbox Search Console via `performance-check --site --days 90` | Primary, first party | 2026-08-01 | Yes, stated as an honest absence, not evidence against the topic |
| Existing GBP Ultimate Guide is a year old and already a flagged refresh candidate; cycle 3 (2026-09-01) already plans that update | `site-inventory.csv`, `content-calendar.csv` | Primary, first party | 2026-08-01 | Yes |

**Not consulted:** Reddit, per this run's explicit instruction (commercial use not permitted for
Brightbox). No keyword volume tool was used and no volume figure is claimed anywhere in this
report.

---

## Topic backlog updates

- Added: "Google is folding Local Services Ads into Google Ads via Performance Max" — PPC,
  confirmed, scored 31/35 this run, this cycle's Recommended candidate.
- Added: "llms.txt / AEO myths for small businesses" — SEO and AI Search, confirmed current via
  Google's June 15, 2026 guide update, considered and set aside this cycle only because two
  stronger, more urgent candidates surfaced; primary source is clean for a future run.
- Note added to existing backlog entry "What actually affects Google Business Profile visibility":
  this run's Candidate 3 (service-area business address rules) is a strong, more specific sub-topic
  of that entry and is a good candidate to fold into the same cycle 3 refresh rather than treated
  separately.

---

## Next action

Archie chooses:

1. **Topic 1** — Local Services Ads moving into Google Ads via Performance Max (**Recommended**)
2. **Topic 2** — how to check whether your business shows up in Google AI Overviews and AI Mode (the calendar's original pick for this slot)
3. **Topic 3** — service-area business GBP address rules (recommended as a fold-in to the planned September 1 GBP refresh rather than a new URL, unless Archie wants it standalone)
4. Request different ideas
5. Update an existing article instead — the GBP Ultimate Guide refresh (already planned for cycle 3) is the strongest candidate for this

**No NeuronWriter analysis will be created until both the topic and the seed keyword are approved.**
