# BBX-004 Outline — What Actually Affects Google Business Profile Visibility

Update to `google-business-profile-the-ultimate-guide` (post 3715, live). Primary keyword: `google
business profile ranking factors`. NeuronWriter query `50626179a9e8a271`.

## No literal NW outline returned

NeuronWriter gave a `topic_matrix` (subtopic ideas with importance scores) rather than a literal
H1-H3 outline, same pattern as BBX-002 and BBX-003. Outline below is built from that topic_matrix,
competitor structural patterns (see NW competitor list), and editorial judgment. No material-
difference Outline Review stop triggered for that reason. What *is* material, and worth flagging
directly: the keyword shift from the existing article's "how to set up a GBP from scratch" angle to
"what affects ranking" means this update is closer to a full rewrite than an edit. See the current-
article audit below.

## Audit of the current live article

Read in full (`https://brightboxdigital.io/blog/google-business-profile-the-ultimate-guide/`,
post ID 3715). Findings:

- **Voice violates `brand-voice.md` throughout.** Heavy repetition of "find your business on
  Google" (appears roughly 15+ times), generic filler sentences, no firsthand voice, no Archie
  quote or byline person (visible_author issue already flagged in `site-inventory.csv`).
- **Zero coverage of the new primary keyword's actual topic.** The current guide is a setup
  walkthrough (create a Google account, verify your business, step-by-step signup). It does not
  address ranking factors, relevance/distance/prominence, or reviews-as-a-ranking-signal at all.
- **Two sections carry accuracy risk and need verification before reuse, not blind carry-forward:**
  "Accepting Food Orders through Your Profile" (Google's in-listing food ordering links are widely
  reported as discontinued; needs a primary-source check before this section is kept, cut, or
  corrected) and the Q&A feature is mentioned implicitly via "messaging, Q&A sections" (the
  2026-09-04 discovery run could not confirm Q&A's status against a primary source either way, so
  this needs its own check, not an assumption in either direction).
- **Genuinely reusable material:** the "Common Mistakes to Avoid" section's three mistakes
  (incomplete information, ignoring reviews, underusing features) are still directionally correct
  and can be rewritten in brand voice rather than discarded.

**Conclusion: this will read as a new article, structured around ranking factors, published under
the same URL/slug.** Flagging this plainly rather than quietly doing a partial edit, since it's a
bigger scope than "update" might imply.

## Proposed outline

1. **TL;DR** (standard template block)
2. **H2 — The three factors Google names directly: relevance, distance, prominence.** Grounded in
   Google's own local-ranking documentation (to be validated at Stage 6, source research). This
   replaces guesswork/invented percentage weightings that competitors use without methodology (per
   `source-validation.md`, not usable).
3. **H2 — What actually moves each factor**
   - H3 Relevance: category accuracy, complete profile fields, business description
   - H3 Distance: service area setup, address accuracy (links to the Candidate 3 backlog topic —
     service-area businesses without a public address — as a "read more" pointer rather than
     duplicating that content here)
   - H3 Prominence: reviews (volume, recency, response), general web presence/citations, GBP posts
4. **H2 — Google's review-solicitation rules just got stricter.** The confirmed policy change (no
   staff-name-specific asks, no quotas, no on-premises pressure) — this is the timely hook. What's
   still fine versus what to stop doing. Directly relevant to the contractor/service-business
   audience who train techs to ask for reviews on the job.
5. **H2 — Does posting on your profile actually help ranking?** Topic-backlog explicitly warns:
   "Only proceed with defensible evidence. Do not assert a ranking effect." Framed honestly: posts
   are an engagement/freshness signal Google itself describes loosely, not a documented ranking
   lever. Say what's known versus what's marketing claim.
6. **H2 — Common mistakes that actually hurt visibility.** Rewritten version of the existing
   section's three points, in brand voice, replacing the generic filler.
7. **H2 — Getting your profile set up right** (condensed). Keeps essential setup guidance
   (category selection, verification, complete fields) in brief since it still has search value,
   but cut from a multi-step walkthrough down to a tight checklist-style section, no longer the
   article's main focus.
8. **FAQ** — candidates from NW's `people_also_ask` and `content_questions`: "How do I get my GBP
   to rank higher?", "Can service-area businesses rank without a physical address?" (ties to
   Candidate 3), "Does posting on GBP help my ranking?" (reinforces section 5's honest framing
   rather than contradicting it).
9. **Key Takeaways**
10. **CTA**

10 H2-level sections, well under the 25-heading ceiling.

## Term coverage plan

Backbone terms confirmed across ~all competitors: "ranking" (6-54x), "google business profile"
(3-10x), "business profiles" (6-11x), "ranking factor" (1-6x). These will occur naturally across
sections 2-3 without forcing. Longer-tail terms (local pack, prominence, relevance, category
accuracy) map directly onto section 3's subsections. No term will be padded past what the content
needs; NW's own data shows word count and score are not the same thing (backlinko scored 32-38 at
6,500-12,000 words; onthemap scored 77 at 2,318 words).

## Word count target

NW's raw target/median (1,862) is skewed low by thin YouTube/LinkedIn/Facebook results in the SERP.
Real top-scoring articles run 2,300-8,000+ words (median of top 5 by score: 3,817). Target
**2,500-3,500 words** — enough to cover all three ranking factors plus the policy update properly,
without padding to chase the raw NW number, same deviation pattern used on BBX-001/002/003.
