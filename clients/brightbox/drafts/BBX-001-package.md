# BBX-001 Article Package

**Status:** Archie Review Needed
**Draft:** `clients/brightbox/drafts/BBX-001-draft-v1.html`
**NeuronWriter query:** `9072fc816ea7d1c1`

---

## 1. Article summary

Answers the question people actually search when they type "google ads small budget": can this work
at my budget, and how low is too low. Answered with a real Fort Wayne handyman account at $15 a day
producing 12 leads at $36.72 each, then Archie's audit findings from his last 10 accounts explaining
why most small budgets underperform, then the confirmed August 17, 2026 bidding change and exactly
which campaigns it reaches.

**Word count:** 1,849. **Content score:** 66, up from 63 after one optimization pass.

---

## 2. SEO metadata

| Field | Value |
|---|---|
| SEO title | Does a Small Google Ads Budget Actually Work? (45 characters) |
| Meta description | A real Fort Wayne account running $15 a day brought in 12 leads at $36.72 each. What a small Google Ads budget can do, and what usually goes wrong. (146 characters) |
| Suggested slug | `does-a-small-google-ads-budget-work` |
| Primary keyword | google ads small budget |
| Secondary topics | limited by budget, cost per lead, Target CPA, negative keywords, conversion tracking, Local Services Ads |
| Search intent | Informational threshold question with commercial investigation |
| Content category | Google Ads and PPC |
| Suggested excerpt | One of my handyman clients runs $15 a day and got 12 leads last month at $36.72 each. Here is what a small budget can realistically do, and the settings that usually waste it. |
| Author | Archie Brady |
| Published | 2026-08-01 (placeholder) |
| Updated | none, new article |
| Canonical | `https://brightboxdigital.io/blog/does-a-small-google-ads-budget-work/` |

**No year in the slug.** The August 17 section will be revised in place after the date rather than
the URL going stale.

---

## 3. Claim and source verification ledger

| # | Claim | Source | Type | Checked | Supports exact wording? |
|---|---|---|---|---|---|
| 1 | "If your campaign's Target CPA is $10, but your recent actual CPA performance is $5, your campaign will deliver more closely to a $10 actual CPA starting August 17, 2026." | [Google Ads Help 17061251](https://support.google.com/google-ads/answer/17061251) | Primary | 2026-07-19 | Yes, quoted verbatim |
| 2 | Change affects budget-limited campaigns using target based bid strategies | Same | Primary | 2026-07-19 | Yes |
| 3 | Bid Target Adjustment Tool available July 6, 2026 | Same | Primary | 2026-07-19 | Yes |
| 4 | "Limited by budget" means daily budget is below the recommended amount to capture available impressions and clicks | [Google Ads Help 2616012](https://support.google.com/google-ads/answer/2616012) | Primary | 2026-07-19 | Yes |
| 5 | Local Services Ads is pay per lead | [Local Services Help 6224841](https://support.google.com/localservices/answer/6224841) | Primary | 2026-07-19 | Yes, "Pay only for leads" |
| 6 | Handyman account: $15/day, $440.53 spent, 110 clicks, $4.00 CPC, 11.02% CTR, 12 conversions, $36.72 cost per conversion | Archie's Google Ads screenshot | Primary, first party | 2026-07-19 | Yes. All figures reconcile internally |
| 7 | Of last 10 accounts: 8 Display/Search Partners on, 7 homepage traffic, 7 no conversion tracking, 6 limited by budget, 2 no negatives | Archie, interview 2026-07-19 | Primary, first party | 2026-07-19 | Yes. Sample size stated in article |
| 8 | One account had a Primary conversion action Inactive and misconfigured with zero conversions | Archie's screenshot | Primary, first party | 2026-07-19 | Yes |

### Claims deliberately excluded

| Rejected claim | Why |
|---|---|
| "Typical waste is 25 to 40% of ad spend" | Circulates across agency blogs citing each other. No traceable methodology |
| "Broad match wastes 30 to 50% of budget" | Same |
| "Homepage landing pages reduce conversions 50 to 70%" | Same |
| "75% of Google's revenue comes from Google Ads" | Appears in a competitor. No accessible primary source |
| Any figure for how much CPA will rise after August 17 | Google has not published it. The article says so explicitly |

### Claim classification

- **Fact, primary sourced:** the August 17 change, its conditions, the tool date, the LSA model
- **First party observation:** the handyman account figures, the 10 account audit counts
- **Opinion, labelled as such:** when Meta beats Google, when not to run ads at all
- **Explicitly uncertain:** how much any account's CPA moves after August 17

**Note on link checking:** `support.google.com` returns 404 to curl and to browser user agents, but
the pages load and serve full content through the standard fetcher. Do not treat a curl 404 on
Google support URLs as a broken link. All five were verified by retrieving actual page content.

---

## 4. Internal link report

| Anchor | Destination | Status | Hops |
|---|---|---|---|
| Get in touch | `/contact/` | 200 | 0 |
| Google and Facebook Ads | `/google-and-facebook-ads/` | 200 | 0 |
| This article on website redesigns | `/blog/should-i-redesign-my-website/` | 200 | 0 |
| SEO services | `/seo/` | 200 | 0 |

Four internal links, within the 3 to 5 requirement. All validated 2026-07-19. `/fort-wayne-seo/`
deliberately not used, it 301s.

**Inbound links needed after publication.** At least two existing pages should link to this article.
Recommended: `/google-and-facebook-ads/` and `/locations/fort-wayne/`.

---

## 5. Image brief

### Image 1: the handyman campaign screenshot (required, original)

- **Placement:** in "What a real small budget account looks like", directly after the metrics list
- **Purpose:** proves the numbers are real rather than illustrative
- **Source:** Archie's Google Ads account, already captured
- **Privacy:** the campaign name "Handyman Services" is generic and safe. **Confirm no client
  business name, account name or customer ID is visible anywhere in the frame before publishing.**
- **Alt text:** "Google Ads campaign showing a $15 daily budget, 110 clicks, 12 conversions and a
  $36.72 cost per conversion"
- **Caption:** "A real Fort Wayne handyman campaign. $440.53 spent, 12 leads, $36.72 each."
- **Filename:** `small-google-ads-budget-real-account-results.png`
- **Aspect ratio:** wide, roughly 16:5 as captured

### Image 2: the misconfigured conversion tracking screenshot (required, original)

- **Placement:** in "Conversion tracking is missing or broken", after the paragraph about checking
- **Purpose:** shows what a broken setup actually looks like in the interface
- **Source:** Archie's account, already captured. No client identifiers visible
- **Alt text:** "Google Ads conversion action marked Primary but showing Inactive and Misconfigured
  with zero conversions"
- **Caption:** "A Primary conversion action, inactive and misconfigured, while the campaign kept spending."
- **Filename:** `google-ads-conversion-tracking-misconfigured.png`

### Image 3: optional

A simple diagram for the "divide your budget by your cost per click" rule. Only if Archie wants it.
Two original screenshots already satisfy the requirement.

**Do not use stock photography.** Both originals are more useful than anything stock would add.

---

## 6. NeuronWriter optimization report

| | |
|---|---|
| Query ID | `9072fc816ea7d1c1` |
| Initial score | 63 |
| Final score | **66** |
| Passes | 1 of a permitted 3 |
| Competitor median score | 53 |
| Competitor mean | 52 |
| Competitor max | 82 |
| Beats | 25 of 31 scored competitors |

**Terms added in pass 1, all genuine content gaps:** `conversion rate`, `keyword planner`,
`search volume`, `target location`, `exact match`, `ad groups`.

**Terms deliberately rejected:**

| Term | Reason |
|---|---|
| `e-commerce` | Irrelevant to a local service audience |
| `much you spend`, `willing to spend`, `single click`, `get clicks` | Phrase fragments, not concepts. Adding them is stuffing |
| `google ads on a small`, `ads on a small budget` | Truncated fragments |
| `advertise on google`, `running google ads`, `better results from google ads` | Generic filler |

**Terms slightly over their suggested range:** `click` (16 vs 9), `small budget` (8 vs 7),
`daily budget` (3 vs 1), `bid strategy` (3 vs 1). All are the actual subject of the article.
Forcing them down would damage readability for a marginal score gain. **Deliberately not corrected.**

**Word count note.** NeuronWriter targets 1,182. The draft is 1,849. That target is depressed by
non-article results in the competitor set: a 280 word YouTube page, a 220 word YouTube page, a 339
word Shopify thread and a 50 word blocked Quora page. Median across the 18 real written articles is
1,552 and the mean is 1,971. The draft sits between them. **Deliberate deviation, documented.**

---

## 7. Technical publishing checklist

- [ ] Slug set to `does-a-small-google-ads-budget-work`, no year
- [ ] Author set to Archie Brady, matching the byline
- [ ] Category: Google Ads and PPC
- [ ] Both screenshots uploaded with the alt text above, metadata stripped
- [ ] Featured image set
- [ ] Canonical self referencing, HTTPS, trailing slash
- [ ] Not noindex
- [ ] Article or BlogPosting schema present, author matches visible byline
- [ ] **No FAQPage schema**
- [ ] Appears in `post-sitemap.xml`
- [ ] Linked from `/blog/` archive and its category
- [ ] At least two existing pages link to it
- [ ] Mobile rendering checked, full article present
- [ ] All four internal and three external links clicked and verified live
- [ ] Share buttons render via the template

---

## 8. Distribution preview

**Recommended format: Archie recorded Reel.** This article rests on real account data and a personal
opinion, which is exactly the case where his face and voice add something a carousel cannot.

Hook options, all built on the real number:
1. "One of my clients spends fifteen dollars a day on Google Ads. Last month that brought in twelve leads."
2. "Everyone says you need a big budget for Google Ads. Here is a real account that says otherwise."
3. "If your Google Ads campaign says limited by budget, there is a change coming on August 17 you should know about."

**GBP launch post:** hold. Not approved for the API and the first four posts need Archie's approval
regardless. Draft on publication.

Full package produced by `distribute-blog` after approval. Not built yet, deliberately.

---

## 9. Items requiring Archie's review

1. **Confirm the handyman figures are current** and that the screenshot's period matches. The article
   says "last month".
2. **Confirm the screenshot has no client identifiers** anywhere in the frame.
3. **The "one in four leads closes" example** in the "what a job is worth" section is illustrative
   arithmetic, not a claim about this client's close rate. Confirm that reads clearly, or supply his
   real close rate if he wants it stated.
4. **The Local Services Ads paragraph** says "a few clients" per his correction from one to three.
   Confirm the framing is honest.
5. **Confirm the Fort Wayne comparison** to Indianapolis and Chicago is a fair characterisation of
   relative competition, since it is stated as fact.
6. **Decide on image 3.** Two originals already meet the requirement.

---

## Approval options

1. Approve the article
2. Request revisions
3. Add more personal experience
4. Change the CTA
5. Recheck a source
6. Change images
7. Abandon the topic
