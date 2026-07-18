---
name: monitor-blog
description: Run the 7, 28 and 90 day post-publication reviews for an article, diagnose weak performance, and recommend action. Also runs the quarterly content refresh review. Use when a review is due or when asked how an article is performing.
---

# Monitor Blog

Reviews at roughly 7, 28 and 90 days after publication.

**Search Console and GA4 are not connected.** Where a check needs data from a system that is not
connected, create a manual review task with exact instructions. **Never invent a metric.** Never
report a number you did not retrieve.

## Seven day check

Everything here can be verified without a connector.

- Live page status
- Indexing status where available, otherwise manual inspection instructions
- Canonical correct and self referencing
- Included in the XML sitemap
- Internal links resolve, and at least two existing pages link into the article
- No broken links
- Renders correctly, including mobile
- GBP launch post status
- Social distribution status

Update the tracker. Set `Search Console Check Needed` if indexing could not be confirmed.

## Twenty-eight day check

Review whatever is genuinely available:

Search impressions, search clicks, queries, average position, CTR, article sessions, engaged
sessions, conversions, GBP post views, GBP CTA interactions, social reach and engagement, and
generative AI visibility reporting where it exists.

Without GSC and GA4, output a manual pull list telling Archie exactly which reports to open, which
date range to set, and which figures to paste back. Then analyze what he provides.

## Ninety day check

Evaluate:

- Is the intended query producing impressions
- Do unexpected queries reveal a better angle
- Does CTR suggest a title or description problem
- Is another Brightbox page competing
- Has the article earned conversions
- Are additional internal links justified
- Do sources need updating
- Should it be expanded, consolidated, or left alone

### Diagnose before acting

**Never respond to weak performance by adding words or keywords.** Identify which problem it is:

indexing, search intent, topic demand, competition, cannibalization, weak title, weak
differentiation, insufficient authority, poor internal linking, outdated information, conversion
design, or page experience.

Each has a different fix. An intent mismatch is not solved by more content. A cannibalization
problem is not solved by optimization.

## Success measures

Success is not only rankings. Track indexing, qualified impressions, organic clicks, relevant
queries, engagement, leads, assisted conversions, CTA clicks, GBP interactions, social engagement,
sales conversations influenced by content, and whether clients find the article useful.

That last one matters and only Archie can report it. Ask him.

## Quarterly refresh review

At least quarterly, review all published content for broken external links, outdated statistics,
platform changes, old screenshots, expired product information, declining traffic, high impressions
with weak CTR, cannibalization, missing internal links, and substantial improvement opportunities.

Mark candidates `Refresh Candidate` or `Consolidation Candidate` in the tracker.

**Only change dateModified or a visible updated date after a substantive update.** Never change a
publication date to make content appear fresh.

## Promotion recommendations

Where an article deserves more reach: internal links, GBP posts, social video, carousel, email
mention, direct sharing with clients who asked the question, legitimate local or partner outreach,
or inclusion on a relevant service page.

Do not perform outreach, send email or message third parties without explicit approval. Never seek
fake mentions or low quality backlinks.
