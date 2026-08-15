# Discovery run — 2026-08-15

Cycle 2 on the calendar (`content-calendar.csv`), target publication date 2026-08-15, category
SEO and AI Search. No tracker row exists for this cycle yet. This is the first article in that
category; the two published articles so far (BBX-001, BBX-002) are both Google Ads and PPC, so all
three candidates below stay inside the calendar's planned category for this slot rather than
extending the PPC lead further.

Reddit signal unavailable this run (`scripts/reddit-research` fails: no credentials at
`~/.config/brightbox/reddit.json`, same gap as prior runs). "Questions people are asking" below comes
from the framing of published secondary coverage and Google's own community-facing language
("to address questions from the community"), not from Reddit.

Site's own Search Console demand (`./scripts/performance-check --site --days 90`, window 2026-05-15
to 2026-08-13, baseline recorded): no query in the top impressions list references AI Overviews, AI
Mode, or AI answers directly. Demand is still dominated by web design and local SEO terms
(`web design fort wayne` 1,284 impressions, `website design` 182, `local seo services` 67,
`2025 local seo` 39). This is consistent with the 2026-08-01 baseline and is not treated as evidence
against these topics — it means the demand case rests on the industry-wide shift + Google's own new
tooling, not on existing Brightbox query data, and that is stated plainly rather than papered over.

NeuronWriter checked read-only (`list-queries`) in both project `eea0682a76fd76f0` (Brightbox, 2
queries: `local services ads performance max`, `google ads small budget`) and project
`0bdb5139dc86fbe7` (Clients, 47 queries, all unrelated client work — home builders, pools, HVAC,
insurance, etc., or Brightbox's own older `website design`/`google business profile`/`local seo`
queries). No overlap with any AI-search topic in either project. No new analysis created.

Checked `site-inventory.csv` for overlap: none of the 8 existing posts or 10 pages touch AI
Overviews, AI Mode, llms.txt, AEO/GEO, or the "leads despite AI answers" angle. No cannibalization
risk.

---

## Candidate 1 — How to Measure Whether Your Business Shows Up in Google AI Answers

- **Category:** SEO and AI Search
- **Evergreen or timely:** Timely, with an evergreen core (measurement fundamentals age well; the
  specific tool is new)
- **New or update:** New
- **Proposed primary keyword:** `google ai overviews search console` (alternatives: `measure ai
  overviews visibility`, `search console ai performance report`)
- **Search intent:** Informational / how-to. "Is my business showing up in AI Overviews, and how do I
  actually check?"
- **Intended audience:** Fort Wayne small business owners already running SEO with Brightbox or
  considering it, anxious about AI search but with no concrete way to check their own exposure
- **Why it matters now:** Google Search Console launched a dedicated Generative AI performance report
  on 2026-06-03, separating AI Overviews and AI Mode impressions from standard organic data in
  Search Console for the first time. This closes a real, specific measurement gap that business
  owners could not answer before. Google's own AI optimization guide (updated 2026-07-10) now points
  site owners at this report as the way to check AI visibility.
- **Evidence of interest:** At least 7 SEO-industry blogs (agencydashboard.io, neilpatel.com,
  csw.agency, superframeworks.com, pikaseo.com, zinc.digital, weblumino.com) published explainers on
  this report within about 10 weeks of launch, all citing the same underlying Google source. That is
  a fast, crowded response to a single feature launch, which cuts both ways: real demand, but real
  competition too, mostly restating the same GSC Help doc rather than giving a practical, business
  owner-level walkthrough. No search volume claimed.
- **Questions people are asking:** "Do I actually have this report yet?" "What can I see and what am I
  still blind to (no clicks, no CTR, no query-level data)?" "Does opting a page out of AI features
  hurt my regular rankings?" (Google has explicitly said no.)
- **Relevant Brightbox service:** SEO (`/seo/`)
- **Internal pages supported:** `/seo/`, possibly a new FAQ-style addition similar to the ones added
  for BBX-001
- **Potential cannibalization:** None found
- **Opportunity for original experience:** Open, not yet confirmed. The report is still "rolling out
  to a subset of website owners," per Google's own Help documentation, and it is not yet verified
  whether the Brightbox property itself has access. If it does, Archie can walk through his own real
  report with an original screenshot. If not, the article has to be honest about that limitation
  rather than staging a screenshot that doesn't reflect reality, and would lean more on interpreting
  the report's known dimensions and metrics (impressions only, no clicks/CTR/position) and what that
  practically means for a business owner deciding what to do next.

### Score: 25 / 35

| Category | Score | Why |
|---|---|---|
| Brightbox service relevance | 4 | Squarely an SEO measurement topic |
| Fort Wayne / local relevance | 3 | Not location-specific by nature; framed around local client anxiety |
| Evidence of current interest | 4 | Fast, multi-outlet coverage of a single dated Google feature launch |
| Freshness / timeliness | 5 | Feature launched 2026-06-03, guide updated 2026-07-10, both inside the 30-90 day window |
| Archie's firsthand contribution | 3 | Real, but conditional on confirming Brightbox's own GSC access to the report first |
| Organic ranking opportunity | 3 | Already 7+ competing explainers within 10 weeks, mostly interchangeable; a practical local-business angle can still differentiate |
| Conversion potential | 3 | Educational and trust-building, indirect lead generation |

---

## Candidate 2 — AEO, GEO, and llms.txt: What Google Actually Said

- **Category:** SEO and AI Search
- **Evergreen or timely:** Timely mythbusting, built on evergreen "don't chase hype" advice
- **New or update:** New
- **Proposed primary keyword:** `does llms.txt help seo` (alternatives: `llms.txt google search`,
  `aeo geo small business seo`)
- **Search intent:** Informational, myth-checking. "Do I need to do this AEO/GEO/llms.txt thing
  everyone is talking about?"
- **Intended audience:** Small business owners being pitched "AI SEO" services or hearing the terms
  AEO/GEO/llms.txt from vendors, marketing content, or well-meaning peers, unsure what is real
- **Why it matters now:** Google's Search Central AI optimization guide added a section in June 2026,
  "to address questions from the community," stating plainly that llms.txt files "will neither harm
  nor help your site's visibility or rankings in Google Search, as Google Search ignores them," and
  that no special AI markup or Markdown file is needed to appear in Google Search or its generative AI
  features. The guide was last updated 2026-07-10, both changes inside the 30-90 day window.
- **Evidence of interest:** Search results show at least 10 near-simultaneous articles on this exact
  clarification (techwyse.com, digitalapplied.com, baselinelabs.ai, searchenginejournal.com,
  almcorp.com, ecorpit.com, minneapolismade.com, organikpi.com, lbntechsolutions.com, booplex.com).
  Google explicitly framed its own update as a response to "questions from the community," which is
  itself evidence of real confusion at the ground level, not manufactured hype. One third-party
  adoption study cited across several of these pieces found llms.txt adoption at roughly 10% of a
  300,000-domain sample and concentrated among developer tools (Anthropic, Stripe, Cloudflare,
  Vercel, Supabase), not small local businesses; that figure is a third-party study, not verified
  first-hand, and would need its own methodology check before use in the draft.
- **Questions people are asking:** "Should I pay someone to build an llms.txt file for my site?"
  "What's the difference between SEO and this new AEO/GEO thing?" "Is my SEO agency doing this for
  me already?"
- **Relevant Brightbox service:** SEO (`/seo/`)
- **Internal pages supported:** `/seo/`
- **Potential cannibalization:** None found
- **Opportunity for original experience:** Depends on whether Archie has actually fielded this
  question from a client or seen it pitched by a competitor or vendor. If not, the piece leans more
  on explaining Google's own statement clearly than on a real client anecdote, which is a thinner
  originality case than the other two candidates.

### Score: 21 / 35

| Category | Score | Why |
|---|---|---|
| Brightbox service relevance | 4 | Directly an SEO advisory topic |
| Fort Wayne / local relevance | 2 | Genuinely general; llms.txt adoption skews toward developer tooling companies, a weak match for Brightbox's local service-business client base |
| Evidence of current interest | 4 | Google's own framing ("questions from the community") plus a wave of near-identical coverage |
| Freshness / timeliness | 4 | Guide update dated 2026-07-10, about 5 weeks old |
| Archie's firsthand contribution | 3 | Real only if he has actually fielded this question; unconfirmed |
| Organic ranking opportunity | 2 | Already saturated with 10+ nearly identical "Google says llms.txt does nothing" articles in the same short window |
| Conversion potential | 2 | Mythbusting builds trust but has the weakest direct commercial hook of the three |

Below the 24-point guideline. Kept in the set because the underlying news is genuinely fresh and
well-sourced, but it is honestly the weakest of the three on differentiation and commercial intent,
mainly because the SERP filled in so fast.

---

## Candidate 3 — Getting Leads When AI Answers Sit Above Your Listing (Recommended)

- **Category:** SEO and AI Search
- **Evergreen or timely:** Evergreen problem with a timely data hook
- **New or update:** New
- **Proposed primary keyword:** `leads when ai overviews replace clicks` (alternatives: `ai overviews
  lower click through rate`, `get leads despite ai search`)
- **Search intent:** Informational leaning commercial. "My traffic or leads look off and I suspect AI
  search is eating my clicks. What do I actually do about it?"
- **Intended audience:** Local service business owners already ranking reasonably well organically who
  are worried, correctly, that ranking is no longer enough
- **Why it matters now:** Independent tracking through early 2026 shows organic click-through drops
  sharply when an AI Overview is present. Pew Research (March 2025) found users click an organic
  result in 8% of visits when an AI summary is shown, versus 15% without one, and click a source cited
  inside the AI summary itself only 1% of the time. Seer Interactive's ongoing tracking put CTR on
  AI-Overview queries at 1.3% in December 2025, rising to 2.4% by February 2026, still well below the
  roughly 3.3% CTR on non-AI-Overview queries. Both are named studies with stated methodology (tracked
  panels), not uncredited statistics; both are third-party and would need a direct link check and a
  recheck for currency before the draft is delivered, per source-validation.md.
- **Evidence of interest:** This is the calendar's own cycle 7 rationale ("addresses the real business
  fear behind AI search... conversion angle rather than a ranking angle"), now supported by concrete,
  named, dated studies rather than the general framing the calendar had in mind. Coverage on the CTR
  impact itself (tynesidemarketing.co.uk, cognizo.ai, quickseo.ai, omnibound.ai, heroicrankings.com,
  almcorp.com) is broader industry-statistics coverage, not narrowly matched to this specific "what do
  I do about it" angle, meaning less direct duplication than candidates 1 and 2.
- **Questions people are asking:** "Is AI search the reason my calls slowed down?" "Should I be
  chasing an AI Overview citation or focusing somewhere else?" "What can I control if the click just
  isn't going to happen as often?"
- **Relevant Brightbox service:** SEO (`/seo/`) as the primary page, with a natural secondary tie to
  Google and Facebook Ads (`/google-and-facebook-ads/`) as the practical answer to "the organic click
  is less reliable, here's the other lever"
- **Internal pages supported:** `/seo/`, `/google-and-facebook-ads/`
- **Potential cannibalization:** None found. Distinct from both PPC articles (BBX-001 is budget
  thresholds, BBX-002 is a platform migration) and from the pending measurement/mythbusting SEO
  candidates above.
- **Opportunity for original experience:** Strong. This is a direct extension of what Brightbox
  already does for clients: SEO, PPC, and conversion-minded pages working together. Archie can speak
  to real account-level tradeoffs he makes when organic click volume looks softer than rankings would
  suggest, which is the same kind of grounded, account-level reasoning that made BBX-001 and BBX-002
  land well with him.

### Score: 28 / 35 — Recommended

| Category | Score | Why |
|---|---|---|
| Brightbox service relevance | 5 | Touches SEO, PPC, and conversion, the full breadth of what Brightbox sells |
| Fort Wayne / local relevance | 3 | Frames naturally around local service businesses even though the underlying data is national |
| Evidence of current interest | 4 | Two named, dated, methodology-stated studies (Pew, Seer Interactive), not vague statistics |
| Freshness / timeliness | 3 | The core problem isn't brand-new, but the specific CTR figures are current through February 2026 |
| Archie's firsthand contribution | 4 | Genuine account-level reasoning opportunity, the same pattern that worked well on BBX-001 and BBX-002 |
| Organic ranking opportunity | 4 | Less saturated than candidates 1 and 2; existing coverage is broad AI-Overview statistics roundups, not this specific practitioner angle |
| Conversion potential | 5 | Directly about lead generation despite reduced organic clicks, the strongest commercial hook of the three |

**Why this beat the other two:** it scores highest specifically because it ties to more of what
Brightbox actually sells (SEO and PPC together, not SEO alone), gives Archie the clearest firsthand,
account-level angle, and sits in a less crowded corner of an otherwise fast-filling SERP. Candidate 1
has the freshest single news hook and matches the calendar's original working title most literally,
so it is a strong second choice, especially if Archie can confirm Brightbox's own Search Console
property has access to the new report for a real screenshot. Candidate 2 is well-sourced but is the
weakest match to Brightbox's client base and already the most crowded SERP of the three.

---

## Note on the calendar

Cycle 2's planned working title, "How to Measure Whether Your Business Shows Up in Google AI
Answers," is Candidate 1 above, not the recommended candidate. All three candidates stay inside the
planned SEO and AI Search category, so choosing Candidate 3 would not disrupt category balance the
way BBX-002 disrupted PPC sequencing on 2026-08-01. It would mean the calendar's cycle 2 working title
gets used later, or folded into Candidate 3 as a secondary section, at Archie's discretion.
