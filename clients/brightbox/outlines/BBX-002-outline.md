# BBX-002 Editorial Outline

**Keyword:** local services ads performance max
**NeuronWriter query:** `f4c1e6ac1d9ae07d`
**Target word count:** ~1,700-2,000. NeuronWriter's raw median/target is 1,026, but that figure is
pulled down by thin social posts in the competitor set (a 127-word Facebook caption, a 109-word
Instagram caption, a 714-word Reddit thread). Excluding those, real competing articles cluster
roughly 770-3,000 words, and the highest-scoring competitor (Google's own migration support page,
content score 87) runs 2,269 words. Targeting 1,700-2,000 sits mid-pack against the pieces actually
worth beating, consistent with how BBX-001 deviated from its own skewed NW median.
**Target readability:** 44
**Publication:** target 2026-08-15
**Status:** Outline built 2026-08-01. No material conflict with NeuronWriter's suggested subtopics
to flag as a Stop 2 item — see below.

---

## Why no Outline Review stop

NeuronWriter did not return a literal suggested H2/H3 outline for this query (no `suggested_headers`
data was present) — only a `topic_matrix` of ten importance-scored subtopic ideas, term-usage
percentages by field (title/description/H1/H2), and the actual headers competitors use. The
structure below incorporates all four of NeuronWriter's highest-importance ideas (importance 9:
what LSAs are, how LSAs differ from standard Google Ads/Performance Max, what Performance Max means
here, and what's changing in the migration) plus most of the remaining six at lower importance.
Since there's no NeuronWriter-authored outline to diverge from, this doesn't trigger `MASTER-WORKFLOW.md`
Stage 2's "material difference" stop — noted here for the record rather than skipped silently.

## SERP intent, confirmed

100% informational (NeuronWriter `serp_summary.top_intent`), 7% secondary transactional. Written as
an explainer/analysis piece, not a landing or sales page. Content-type mix is heavy blog-post/guide/
news (93% combined) — this is being treated by the market as a breaking-news topic right now, not
settled evergreen content, consistent with the "August 2026" and "2026-07-26" references appearing
directly in NeuronWriter's own scraped data.

---

## Originality gate — answered in writing, per MASTER-WORKFLOW Stage 4

**What will this article contribute that a reader cannot get from the current top five results?**

Top 5: (1) Google's own general LSA product page, (2) Google's official migration support page
(score 87, the strongest single source but written as reference documentation, not for a worried
business owner), (3) Search Engine Land, trade press aimed at marketers/agencies, (4) a Google exec's
LinkedIn Q&A thread, insider framing, (5) a Reddit thread, thin and unauthoritative.

**Three gaps identified:**

1. **None of the top 5 write for a home-service business owner as the reader.** They're written by
   and for PPC practitioners — Google's support doc is reference-style ("What's not changing,"
   "What's changing," jargon like "pay-per-lead goals" left undefined), Search Engine Land and the
   LinkedIn thread are agency-to-agency. A plumber or HVAC owner reading any of these has to
   translate "Performance Max campaign type with pay-per-lead goals" into "will my phone still ring
   and will it cost more" on their own.
2. **A real, recurring point of confusion in the current top results is unresolved.** NeuronWriter's
   own scraped questions include it twice, from two different sources: whether an existing standard
   Performance Max campaign and the new LSA-flavored Performance Max campaign interact, compete for
   budget, or run entirely separately. No competitor in the visible set answers this directly.
3. **No competitor offers a concrete, practitioner-grounded "what to actually do before your
   migration date" checklist.** Google's page says to export historical data; none of the agency
   articles walk through what that actually means for a lead-driven local business's own reporting
   or CRM setup, specifically.

**Two original value elements committed** (both pending Archie's interview answers below — not
invented in advance):

1. **A real client situation or Archie's direct account-management experience**, if he has managed
   or currently manages Local Services Ads for any client — or, if not, his practitioner's read on
   what he'd tell a client facing this migration, clearly labeled as professional judgment rather
   than a client case if that's what it is.
2. **A Brightbox pre-migration checklist** — grounded in what Archie actually checks or exports when
   any client's ad account structure changes, not a restatement of Google's own bullet list.

If Archie's interview answers can't substantiate at least one of these with something real (not
invented), the article should lean more heavily on original element 2 (the LSA-vs-standard-PMax
budget-interaction question) and be explicit that this is a genuinely open question rather than
inventing an answer.

---

## Proposed structure

### H1
**Local Services Ads Are Moving Into Google Ads. Here's What Changes for Contractors.**

Alternates considered: "...What Home Service Businesses Need to Know," "...What Actually Changes
When Your LSA Dashboard Disappears." NeuronWriter's H1 term data favors "local service(s)," "local
service ads," "performance max," and "google ads" appearing in the H1 — all four are present above.

### TL;DR
Three to four bullets: pay-per-lead stays, the dashboard goes away, rollout starts August 2026 for
home-service categories, and the one action item (export your data) before your migration date.

### Introduction
- Hook: named directly — Google is retiring the standalone LSA dashboard and folding it into
  Performance Max, starting this month, for exactly the contractor and home-service categories
  Brightbox serves.
- The reader's real question: is anything about how I pay, how I get leads, or what I show up for
  actually changing, or is this just a UI move?
- Primary-sourced date and category list, quoted from Google Ads Help.

### H2: What's staying the same
Answers the reassurance need first, before the changes. Pay-per-lead billing (quoted), Search- and
Maps-only placement, keywordless targeting by service category and area. Explicitly states this is
**not** a standard Performance Max campaign despite the name — won't expand to Display, YouTube, or
Gmail. Directly resolves NeuronWriter content-question #1 below.

### H2: What's actually changing
Standalone dashboard retired, manual bidding and industry-level Target CPA discontinued, weekly
budgets convert to daily average budgets, Better Business Bureau callouts no longer supported.

### H2: Who gets migrated first, and when
- August 2026: plumbing, HVAC, electrical, appliance repair, house cleaning, lawn care, roofing,
  pest control, moving (Google's own list, quoted)
- Late 2026: service-area businesses without a storefront, accounts with custom bidding/booking
- 2027: non-U.S. accounts, remaining categories
- Advance notice pattern: 14 days, then a 7-day reminder

### H2: The one thing to do before your migration date
Historical performance data — past impressions, clicks, spend, ad-level reports — does not migrate
automatically (quoted, primary sourced). Lead history does transfer. This is where Archie's
practitioner checklist lands (original value element 2).

### H2: If you already run a standard Performance Max campaign, does this affect it?
Directly answers the recurring, currently-unresolved question surfaced in NeuronWriter's own scraped
data. State plainly what's confirmed (this is a distinct, specialized PMax campaign type built for
pay-per-lead, not a merge into an existing standard PMax campaign) and flag anything Google's
documentation doesn't explicitly settle rather than guessing.

### H2: What Archie has seen / Archie's take
Original value element 1. Structure depends entirely on his interview answer — a real account
example if he has one, or his professional judgment if he doesn't, clearly labeled either way.

### H2: Frequently asked questions
Draft candidates, each to be checked against the primary source before use, none invented:
- Will my Google Guaranteed badge and reviews carry over?
- Do I have to do anything if I haven't been notified yet?
- Will this cost more per lead than before?
- What happens to my leads during the migration window?
- Can I opt out or delay migration?

**No FAQPage schema**, per standing site convention (matches BBX-001).

### Conclusion + key takeaways (3-5) + CTA
CTA: an account review offer, directly relevant since this is a mandatory platform change affecting
active ad spend.

---

## Terms to work in naturally

**Core terms, NeuronWriter suggested ranges:**
`local service ads` [1-14], `google ads` [1-10], `local service` [4-15], `performance max` [1-5],
`google business profile` [1-9], `service area` [1-2], `pay-per-lead` [1-3], `dashboard` [1-2],
`lsa` [1], `bidding` [1-3]

**Work in once, naturally, where relevant:** `home services`, `local services ads dashboard`,
`historical performance reports`, `pay-per-lead goals`, `google verified badge` /
`google guaranteed`, `service categories`, `august 2026`

**Do not force:** the long tail of near-duplicate phrase variants NeuronWriter lists (e.g. "campaign
with pay-per-lead," "max campaigns with pay-per-lead goals," "transition to performance max
campaigns") — these are the same idea fragmented by NeuronWriter's n-gram extraction, not distinct
concepts to hit individually. Natural coverage of the core terms above will cover them.

---

## Internal links, 3 to 5, all validated

- `/google-and-facebook-ads/` — primary service page, the hub this supports (currently has one
  supporting article, BBX-001; this becomes the second, distinct topic, no overlap)
- `/contact/` — account review CTA
- `/blog/does-a-small-google-ads-budget-work/` — natural tie for budget-limited advertisers reading
  about a platform change to their spend structure

**Never link `/fort-wayne-seo/`.** Not relevant here regardless.

## External links, 3 to 5, all primary

- Google Ads Help: Local Services Ads transition to Performance Max campaigns (support.google.com/google-ads/answer/17213585)
- Google's Local Service Ads product page, only if needed for the "what LSAs are" context
- A second Google Ads Help source if the FAQ section needs one (e.g. Google Guaranteed / Local Services Ads badge documentation) — to be located and validated at drafting time, not invented now

## Images, 2 to 3, at least one original if available

1. A screenshot of the actual Google Ads Help migration page or the in-product migration notice, if
   Archie can supply one from a client account (subject to his confirmation; anonymize any client
   identifiers).
2. A simple before/after diagram: standalone LSA dashboard versus the new in-Google-Ads campaign
   view.
3. Optional: a timeline graphic (August 2026 → late 2026 → 2027 phases).

---

## Statistics rule for this article

No invented statistics. Every date, category list, and quoted policy line comes from
support.google.com/google-ads/answer/17213585, checked and dated 2026-08-01, to be rechecked
immediately before delivery per `shared/source-validation.md`. No search volume or competitor
traffic figures appear anywhere.
