# Draft: PPC hub FAQ + Fort Wayne page link

**Status:** DRAFT, not approved, not published anywhere. For Archie's review.
**Purpose:** Give `/google-and-facebook-ads/` a small-budget FAQ that links to BBX-001, and add a
genuine local link into `/locations/fort-wayne/`, closing the internal-link gap flagged in the
[7-day check](performance/BBX-001-7day-2026-07-27.md).

All facts below are pulled from the already-approved BBX-001 article. Nothing new is claimed or
invented, per the brand's no-fabrication rule.

---

## 1. New FAQ block for /google-and-facebook-ads/

Both pages use Elementor with the ElementsKit accordion widget for their existing FAQ sections —
this isn't raw HTML you paste into a field, it's built through the Elementor editor. The content
below is written so you (or whoever has WP access) can either duplicate an existing accordion item
and swap the text, or hand it to whoever manages the page.

**Suggested placement:** a new accordion titled "Small Budget Google Ads: Quick Answers" placed
either right after the existing "10 FAQs About Google Ads" accordion, or above it if you want budget
questions to be the first thing a hesitant visitor sees. Your call — both work structurally.

1. **Does a small budget actually work for Google Ads?**
   It can, if the account is set up correctly. One Fort Wayne client runs a $15-a-day search
   campaign and generated 12 leads last month at $36.72 each. Whether that translates to your
   business depends on how competitive your service is locally, what a customer is worth to you,
   and what clicks cost in your category. We've written up [a full breakdown of that
   account](https://brightboxdigital.io/blog/does-a-small-google-ads-budget-work/), including the
   exact numbers.

2. **How much should I budget to start?**
   There's no universal number. A quick gut check: divide your monthly budget by your average cost
   per click. If that comes to fewer than 50 clicks a month, it's too thin a sample to learn from
   and adjust. Your category's competition and what a job is worth to you both matter more than any
   flat "$X a day" rule.

3. **Will the Google Ads change on August 17, 2026 affect my campaigns?**
   Only if two things are both true: your campaign is marked "Limited by budget" and it uses a
   target-based bid strategy like Target CPA or Target ROAS. If either isn't the case, this
   particular change doesn't apply to you. Worth checking either way before the date.

4. **Should I run Google Ads or Facebook ads on a small budget?**
   It depends on intent. Google Ads works because people are actively searching for what you offer
   right now. If your service is more of a "nice to have" that people wouldn't think to search for,
   Meta ads, where someone scrolling sees it and thinks "that would be nice," often perform better.

5. **What should I fix before increasing my ad spend?**
   Check your settings before you add money. In the accounts we've reviewed, the common issue isn't
   budget size, it's things like the Display Network and Search Partners left switched on, traffic
   sent to a homepage instead of a relevant page, or conversion tracking that's missing or broken.
   Fixing those usually recovers more than a bigger budget does.

Only one link (item 1) to avoid stuffing the same URL across every answer, matching the
`shared/internal-links.md` rule against repeating a link. All five are genuinely useful standalone
answers, not just link bait.

---

## 2. Suggested link from /locations/fort-wayne/

That page's own FAQ accordion currently has zero Google Ads questions (its 9 existing FAQs are all
about web design/SEO). Adding one keeps the pattern consistent and is a link the accordion widget
is already proven to support (it's the same widget type as the PPC page's FAQ).

**New FAQ item to add to the Fort Wayne page's existing "Frequently Asked Questions" accordion:**

> **How much does it cost to run Google Ads for a Fort Wayne business?**
> It depends on your service and local competition, but it doesn't have to be expensive to work.
> One of our Fort Wayne clients runs a $15-a-day Google Ads campaign and generates leads at $36.72
> each. See the full account breakdown in [Does a Small Google Ads Budget Actually
> Work?](https://brightboxdigital.io/blog/does-a-small-google-ads-budget-work/)

This is a genuine local reference (a real Fort Wayne client, real numbers already approved in the
article), not a city name bolted on for keyword reasons, so it satisfies `brand-voice.md`'s local
reference standard.

**Lighter-touch alternative**, if you'd rather not add a new FAQ item: the page's existing "Google &
Facebook Ads" service card currently reads:

> Reach customers in Fort Wayne and surrounding areas with targeted advertising campaigns focused
> on generating leads and measurable results. *Learn more →* (links to /google-and-facebook-ads/)

You could extend the sentence to: "...generating leads and measurable results. See what a $15-a-day
budget did for one local handyman client." with that last clause linked to the article. This is a
smaller edit but depends on whether that card's description field accepts a link — the FAQ accordion
definitely does, so that's the safer option if you want one clean answer.

---

## Not done here

- Nothing has been pasted into WordPress or Elementor. This is content only.
- No FAQPage schema — per `shared/editorial-standards.md`, FAQs never get schema markup.
- Didn't touch the PPC page's existing generic "10 FAQs" — left as is, this is additive.
- Internal link stays same-tab per the standing link-behaviour rule.
