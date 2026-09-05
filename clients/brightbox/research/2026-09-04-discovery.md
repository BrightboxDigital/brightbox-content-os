# Discovery Run — 2026-09-04

Cycle 3 (`content-calendar.csv`, target 2026-09-01 — already 3 days past its target date). Category:
Local SEO and GBP, Update, planned working title "What Actually Affects Google Business Profile
Visibility," supporting `/google-business-profile-optimization/`.

## Why this slot

Cycles 1 (PPC, BBX-001) and 2's SEO/AI Search slot (BBX-003) are both produced. BBX-002 was an extra
PPC piece inserted ahead of its originally planned slot (cycle 4, 2026-09-15), per its own tracker
notes. Category balance right now: PPC 2, SEO and AI Search 1, Local SEO and GBP 0, Web Design 0.
Local SEO and GBP is furthest behind and cycle 3 is already overdue, so this run stays inside the
calendar's own plan rather than deviating.

## Overlap check

- `site-inventory.csv`: one existing GBP article, `google-business-profile-the-ultimate-guide`
  (published July 2025, "Brightbox Digital Team" byline — see site-fix-backlog.md #1 authorship
  issue, not this run's problem to fix but worth Archie's awareness when this page is touched).
  Already flagged in site-fix-backlog.md #8 as a refresh candidate ("both subjects have moved
  substantially in twelve months").
- NeuronWriter: no query in the Brightbox project (`eea0682a76fd76f0`) for this topic. The `Clients`
  project (`0bdb5139dc86fbe7`) has one prior query, `google business profile` (id `e15ef003bb0c82d1`,
  created 2025-07-04) — read-only, matches the same topic as the existing guide, no new query
  created this run.
- No cannibalization risk found: this is a straightforward update to the one existing GBP guide, not
  a new URL competing with it.

## Demand evidence

Site-wide 90-day Search Console pull (`./scripts/performance-check --site --days 90`, window
2026-06-04 to 2026-09-02, recorded to `performance/baselines.csv`): 40,139 impressions, 87 clicks
site-wide. No GBP-specific or local-SEO-specific query appears in the top 15 by impressions — demand
is dominated by web design and Fort Wayne-branded terms (`web design fort wayne` 2,619 impr,
`website design fort wayne` 972 impr, `advertising agencies fort wayne` 581 impr). **This is a real
gap in existing evidence, stated plainly, not disqualifying** — GBP content supports a core Brightbox
service and a real audience segment (contractors, service-area businesses) regardless of what the
site currently ranks for, since the site has never had strong GBP content to rank with.

The existing GBP guide itself gets modest but real traffic: 90-day pull (baseline recorded) shows 8
Search Console impressions (avg. position 12.0) and 29 GA4 sessions, 23 engaged. That's more 90-day
GA4 traffic than any of the three articles published so far by this system, so an update compounds on
an already-indexed, already-ranking page rather than starting a new URL from zero.

No search volume is invented anywhere in this report. Where a number appears, it is from the site's
own Search Console/GA4 pull or an official Google source, both cited.

## Research

Prioritized primary sources. Two genuinely new, verifiable developments found in the last several
months:

**1. Google tightened its review-solicitation policy.** Confirmed directly against the live policy
page, [Prohibited and restricted content – Google Business Profile Help](https://support.google.com/business/answer/7400114?hl=en)
(fetched 2026-09-04). Current policy text explicitly prohibits: incentivizing reviews; discouraging
negative reviews or selectively soliciting positive ones; "merchants requesting that staff solicit a
certain number of reviews"; "merchants requesting that staff solicit reviews that include specific
content," including content that identifies a staff member by name; and pressuring or requiring
customers to leave reviews while on the business premises. Secondary trade coverage (ppc.land,
Birdeye, several local-SEO agency blogs) dates the specific staff-name and quota language to an
April 17, 2026 policy rewrite, with the on-premises-pressure language tightened around February 20,
2026 per Search Engine Roundtable's reporting. **Those two specific dates come from secondary
sources and were not independently verified against a dated Google changelog** — the policy page
itself carries no visible revision date — so the report treats "confirmed current policy" as the
verified fact and the April/February dates as reported-but-unconfirmed context, not as a fact the
article should assert on its own authority.

This is squarely relevant to Brightbox's stated contractor and home-service audience
(`client-profile.md`), where "ask the customer for a 5-star review before you leave the job" and
review kiosks in service vehicles are common practices that this policy now puts at risk.

**2. Q&A feature and "Ask Maps" — investigated, not used as a claim.** Multiple secondary sources
report Google discontinued the public Q&A section on Business Profiles (dated variously to
November 2025 or a gradual removal into early 2026) and introduced "Ask Maps," a Gemini-powered
conversational feature, publicly on March 12, 2026. **This could not be confirmed against a primary
Google source in this run** — the relevant support.google.com Q&A pages returned either 404 or
content with no mention of discontinuation, and no blog.google or Search Central page was found
confirming it directly. Per source-validation.md, this fails validation and is not used as a claim
anywhere in the candidates below. If Archie has seen this in his own dashboard or client accounts,
that firsthand observation would be usable in a future article; the secondary reporting alone is not.

**3. Service-area business address and boundary rules — confirmed, evergreen not timely.** Confirmed
directly against [Manage your service areas – Google Business Profile Help](https://support.google.com/business/answer/9157481?hl=en)
(fetched 2026-09-04): service-area businesses must not display a business address; up to 20 service
areas specified by city or postal code (not radius); boundaries should stay within roughly 2 hours'
drive of the business; service area edits can take up to 48 hours to appear. No recent change date
found — this reads as stable, ongoing policy rather than news, which is reflected in Candidate 3's
freshness score below.

## Candidates

### Candidate 1 — Recommended: Update the GBP Ultimate Guide with what's actually changed

**Category:** Local SEO and GBP · **Evergreen or timely:** Evergreen with a timely update hook ·
**New or update:** Update to `google-business-profile-the-ultimate-guide` · **Proposed primary
keyword:** `google business profile ranking factors` (alternates: `what affects google business
profile ranking`, `google business profile visibility`) · **Search intent:** Informational — "why
isn't my GBP showing up / what should I actually be doing" · **Audience:** Local business owners and
service-area/contractor businesses managing their own GBP, or evaluating whether Brightbox should
manage it for them.

**Why it matters now:** the existing guide is 14 months old on a profile system Google visibly keeps
changing, and it predates the confirmed review-solicitation policy tightening above — a genuine gap
in current content, not a manufactured reason to touch the page. **Evidence of interest:** the page
already earns real if modest traffic (8 impressions/29 sessions in 90 days, recorded baseline above)
and B2B interest in "2026 GBP ranking factors" is visibly high across the industry (numerous
competitor and agency posts on the exact phrase this run searched), though none of those secondary
sources' specific ranking-weight percentages are usable per source-validation.md — Google has never
published a numeric weighting for GBP ranking factors, and none of the industry reports found show
an accessible methodology for the figures they cite. The article should describe Google's own
documented framework (relevance, distance, prominence — the three factors Google names directly in
its own Search/Maps ranking documentation) and specific documented signals (primary category
accuracy, complete profile fields, photos, and now review-solicitation compliance) rather than
borrow anyone's invented percentage.

**Questions people are asking:** why did my ranking drop / why does a nearby competitor outrank me;
does posting on GBP actually help; is asking my customers for reviews the way I've always done it
still safe; do I need a physical address if I only do service calls (this last one is Candidate 3's
territory — worth a short pointer between the two rather than duplicating content, see
cannibalization note below).

**Relevant Brightbox service:** Google Business Profile optimization. **Internal pages supported:**
`/google-business-profile-optimization/` (service page), `/locations/fort-wayne/`. **Potential
cannibalization:** low risk against Candidate 3 if scoped as "what affects your overall visibility"
versus Candidate 3's narrower "service-area business setup" — but the two should cross-link rather
than both trying to cover service-area address rules in full. **Opportunity for original
experience:** real — Archie manages GBP for multiple current clients and can speak to which
categories/signals he's actually seen move the needle, and to whether any of his clients used
review-solicitation practices (staff-name asks, on-site pressure, kiosks) that the tightened policy
now puts at risk. That is exactly the kind of concrete, current, firsthand-grounded update this
system is built to produce.

**Score: 28/35**

| Category | Score | Why |
|---|---|---|
| Brightbox service relevance | 5 | Directly supports the GBP optimization service page |
| Fort Wayne / local relevance | 4 | GBP is inherently a local-business topic; not Fort Wayne-specific in itself |
| Evidence of current interest | 3 | No site GSC query evidence yet, but the page already earns real traffic and industry attention is visibly high (qualitative, not a number) |
| Freshness / timeliness | 4 | Anchored by a confirmed, current policy change the existing guide doesn't cover; page itself is 14 months stale |
| Archie's firsthand contribution | 4 | Real client GBP management and a real opinion on review-solicitation risk |
| Organic ranking opportunity | 4 | Updating an already-indexed page beats starting a new URL from zero |
| Conversion potential | 4 | Direct path to a paid Brightbox service |

**Validated sources:** support.google.com/business/answer/7400114 (fetched 2026-09-04, primary);
support.google.com/business/answer/3038177 (Business representation guidelines, primary); site's own
Search Console/GA4 pulls (primary, this session).

---

### Candidate 2 — The tightened review-solicitation policy, as its own article

**Category:** Local SEO and GBP · **Evergreen or timely:** Timely, evergreen underneath · **New or
update:** New · **Proposed primary keyword:** `google review policy staff names` (alternates:
`can you ask customers for reviews google`, `google business profile review rules 2026`) · **Search
intent:** Informational/compliance — "am I breaking a rule with how I currently ask for reviews" ·
**Audience:** Home-service and contractor businesses whose front-line staff currently solicit
reviews in person.

**Why it matters now:** the confirmed policy language (staff names, quotas, on-premises pressure) is
a direct, practical compliance question for exactly the audience `client-profile.md` names as core —
contractors and home-service businesses, many of whom train techs to ask for reviews on-site.
**Evidence of interest:** moderate secondary trade coverage (ppc.land, Birdeye, several agency blogs
covering the April 2026 change), no direct GSC signal since this is new ground for the site.
**Questions people are asking:** can I still ask my customers for a review before I leave the job; is
a review kiosk in the van now against the rules; what happens if a review gets flagged. **Relevant
Brightbox service:** GBP optimization / reputation management angle. **Internal pages supported:**
`/google-business-profile-optimization/`. **Potential cannibalization:** meaningful overlap with
Candidate 1 if both are produced — the review-solicitation material would need to live in one place,
not both. **Opportunity for original experience:** depends entirely on whether Archie has clients
who currently use exactly these now-restricted practices; if not, the article risks being generic
compliance explainer rather than something only Brightbox could write.

**Score: 23/35**

| Category | Score | Why |
|---|---|---|
| Brightbox service relevance | 4 | Relevant to GBP/reputation management, one step removed from the core optimization service |
| Fort Wayne / local relevance | 3 | Applies to any business anywhere, not Fort Wayne-specific |
| Evidence of current interest | 3 | Real secondary coverage, no site-level signal |
| Freshness / timeliness | 3 | The underlying policy change is ~5 months old, at the edge of the research window |
| Archie's firsthand contribution | 4 | Strong if he has real client examples, unverified until interview |
| Organic ranking opportunity | 3 | Several established local-SEO publishers (Birdeye, ppc.land) already cover this well |
| Conversion potential | 3 | Useful, but a softer commercial angle than GBP optimization broadly |

**Validated sources:** support.google.com/business/answer/7400114 (fetched 2026-09-04, primary).
Secondary coverage (ppc.land, ppc.land's Amy Toman/LinkedIn citation, Search Engine Roundtable via
secondary report) used only to date the change, not as evidence for any claim in the article itself.

---

### Candidate 3 — Google Business Profile setup for service-area and no-storefront contractors

**Category:** Local SEO and GBP · **Evergreen or timely:** Evergreen · **New or update:** New ·
**Proposed primary keyword:** `google business profile service area business` (alternates: `gbp no
address contractor`, `service area business google setup`) · **Search intent:** Informational/
how-to — "how do I set up my GBP correctly if I don't have a public storefront." · **Audience:**
Plumbers, HVAC, electrical, roofing, cleaning and similar contractors operating from a home base or
non-public location — explicitly named in `client-profile.md`'s audience and already the framing
used in BBX-002.

**Why it matters now:** not a news hook — this is a persistent, recurring setup mistake, evidenced by
an active Google Business Profile Community thread ("Address for Service Area Business") found
during research, which is signal of confusion, not evidence, per source-validation.md's Reddit/forum
rules. The real case for this topic is audience fit, not timeliness. **Evidence of interest:**
qualitative only (recurring community confusion); no site GSC signal. **Questions people are
asking:** do I need to show an address if customers never visit me; can I use a PO box; how many
service areas can I list; why did my listing get suspended after I added a service area. **Relevant
Brightbox service:** GBP optimization. **Internal pages supported:**
`/google-business-profile-optimization/`, and could reasonably link from BBX-002 (Local Services
Ads), since LSA and GBP setup are adjacent concerns for the same contractor audience. **Potential
cannibalization:** low against the existing GBP guide if scoped narrowly to service-area setup
specifically rather than general visibility. **Opportunity for original experience:** real — Archie's
client base is contractor-heavy per his own interview answers on BBX-002, so he likely has direct
experience with service-area setup mistakes and can speak to them concretely.

**Score: 25/35**

| Category | Score | Why |
|---|---|---|
| Brightbox service relevance | 4 | Supports the GBP optimization service page |
| Fort Wayne / local relevance | 5 | Directly matches Brightbox's stated contractor/service-area audience |
| Evidence of current interest | 3 | Recurring community confusion (signal only), no GSC data |
| Freshness / timeliness | 2 | No recent change found; stable ongoing policy, weak timely hook |
| Archie's firsthand contribution | 4 | Strong fit with his known contractor client base |
| Organic ranking opportunity | 3 | Moderate competition, less saturated than general GBP ranking-factor content |
| Conversion potential | 4 | Targets Brightbox's highest-value client type directly |

**Validated sources:** support.google.com/business/answer/9157481 (fetched 2026-09-04, primary).

---

## Recommendation

**Candidate 1** (update the GBP ultimate guide) is recommended. It scores highest, it is the
calendar's own planned move for this slot, it compounds on a page that already ranks rather than
starting from zero, and it has a genuine new-information hook (the review-solicitation policy
change) rather than a cosmetic refresh. Candidate 2's material is strong enough that, if chosen
instead or in addition, it should not be built as a second full article competing with Candidate 1 —
either fold it into the Candidate 1 update as a section, or pick one and hold the other back for a
later cycle. Candidate 3 remains a strong standing option for a future Local SEO/GBP slot given how
well it matches Brightbox's actual client base, and needs no further revalidation before being run
again next time this category comes up.

## Also noted this run, not acted on

- `client-profile.md` still states "PPC is the current content gap. Zero of the seven published
  articles cover Google Ads or PPC." That's now stale — two PPC articles (BBX-001, BBX-002) are
  published. Not fixed this run since it's a documentation-accuracy item outside this workflow's
  scope, flagged for whoever next edits that file.
- GA4 key events are now recording data site-wide (16 in the last 90 days, up from 0 at launch) —
  see the site-wide baseline note. Worth Archie confirming what was configured and when, since
  site-fix-backlog.md #0b previously recorded this as unresolved.
