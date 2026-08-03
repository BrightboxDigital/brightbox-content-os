# BBX-002 Distribution Package

**Article:** Local Services Ads Move to Google Ads: What Changes
**Live URL:** https://brightboxdigital.io/blog/local-services-ads-moving-to-google-ads/
**Format:** Carousel (Archie's choice, 2026-08-03, no recording this time)
**Built:** 2026-08-03. **Revised same day** after Archie's design feedback on v1 (see below).

---

## Design history

**v1** used the already-approved square featured image as slide 1, then 5 more slides that
alternated light and dark backgrounds, kept the Brightbox logo on every slide, numbered slides
(2/6 through 6/6), and closed with a graphic styled to look like a clickable button.

**Archie's feedback:** inconsistent colors read as unpolished, the logo looked small and rough at
that size, drop the slide numbers, and don't draw something that looks like a button on a static
image since nobody can tap it. He also flagged that Instagram has newer carousel size options
worth checking before finalizing.

**v2 (current, approved):**
- One consistent theme on all 6 slides: the same navy-to-purple gradient used on
  brightboxdigital.io's own homepage hero (`#0A1530` to `#3B1568` to `#5C2599`), white headline
  text, a short amber (`#FFC163`) accent bar under each headline. No light-background slides.
- No logo anywhere on any slide.
- No slide numbers.
- Slide 6's closing line is plain text ("Get in touch"), not a drawn button shape.
- Content vertically centered on each slide rather than top-anchored, since the original
  top-anchored layout left a lot of dead space at the bottom on the taller format.
- Built at **two sizes** instead of one, after checking current platform specs (below).

## Current carousel sizes, checked 2026-08-03

- **Instagram:** 1080x1350 (4:5 portrait) is the current recommended default for carousels, more
  feed real estate than square. Instagram also just added a 1080x1440 (3:4) option. Whatever ratio
  slide 1 uses locks the format for the whole carousel, so consistency across slides matters.
- **LinkedIn:** accepts 1080x1080 or 1080x1350, portrait now recommended for mobile attention. Uses
  the same 1080x1350 set as Instagram.
- **Facebook:** 1080x1080 (1:1) is standard. Facebook crops non-square images to 1:1 in feed
  regardless of what's uploaded, so a native square set avoids an unpredictable crop.

Two image sets were built from the same source content: `instagram-linkedin-1080x1350/` and
`facebook-1080x1080/`.

## Slide by slide

Every fact on every slide is a direct restatement of the published article. Slides were rendered
as HTML/CSS and screenshotted at native resolution via headless Chrome, not AI-generated,
specifically to avoid the fabrication risk found earlier when a Canva AI-generated timeline
diagram invented two migration phases that don't exist. Nothing on these slides was invented.

| Slide | Headline | Content |
|---|---|---|
| 1 (cover) | Local Services Ads Move to Google Ads / What Changes | Archie's original graphic (also the article's featured image), re-cropped left-focal for each carousel size |
| 2 | What's Staying the Same | Pay per lead, Search/Maps only, keywordless |
| 3 | What's Changing | Dashboard gone, manual bidding gone, weekly to daily budgets, BBB callouts gone |
| 4 | When It's Happening | Aug 2026 / Late 2026 / 2027 phases, exact categories per phase |
| 5 | Do This Before Your Migration Date | Export your performance reports, they won't transfer automatically |
| 6 (CTA) | Managing Local Services Ads? | Offer to help, plain text "Get in touch" (no button graphic) |

Files: `carousel-slides/instagram-linkedin-1080x1350/ig_s1.png` through `ig_s6.png`, and
`carousel-slides/facebook-1080x1080/fb_s1.png` through `fb_s6.png`.

## Alt text

- Slide 1: "Local Services Ads listing transitioning into a Google Ads Performance Max campaign for pay-per-lead, with icons for plumbing, HVAC, electrical, roofing, and cleaning" (matches the live featured image alt text)
- Slide 2: "What's staying the same: pay per lead, Search and Maps only, keywordless targeting"
- Slide 3: "What's changing: the dashboard goes away, manual bidding is gone, weekly budgets become daily, BBB callouts are removed"
- Slide 4: "Migration timeline: August 2026, late 2026, and 2027 phases with affected categories"
- Slide 5: "Reminder to export Local Services Ads performance reports before your migration date, since Google says they will not transfer automatically"
- Slide 6: "Managing Local Services Ads? Get in touch for help preparing for the migration."

---

## Platform posts, pushed as GHL drafts 2026-08-03 (v3, current)

**v3 change:** Archie asked for slide 1 to be his original ChatGPT-designed graphic (the one
already used as the article's featured image) rather than a plain text cover, so people can see
what the carousel is about immediately. Re-cropped that image at both carousel sizes (left-focal,
same technique used for the featured image derivatives) and swapped it in as slide 1. Slides 2-6
unchanged from v2.

Each redesign deleted the prior version's GHL drafts before pushing new ones, so there's no
duplicate content sitting in GHL. All four created with `status: draft`. **Nothing published.**

| Platform | GHL account targeted | Draft post ID | Images |
|---|---|---|---|
| Instagram | brightboxdigital | `6a710aa22926bb08c8f0bab4` | All 6 slides, 1080x1350 set |
| Facebook | Brightbox Digital (page) | `6a710aa6dba7e3fc35831b14` | All 6 slides, 1080x1080 set |
| LinkedIn | **Archie Brady (personal profile)**, not the Brightbox Digital page | `6a710aa6036e65b5d9cd4bfc` | All 6 slides, 1080x1350 set |
| Google (GBP) | Brightbox Digital - Fort Wayne | `6a710aa77ed5b0c7d6527429` | Slide 1 only (1080x1080), single image per GBP convention |

**LinkedIn still flagged, unanswered:** two LinkedIn accounts are connected (personal profile and
the Brightbox Digital page). The script takes the first match returned by GHL's API, which is the
personal profile. Confirm that's what you want, or ask for a second draft on the page.

**Technical note for future runs:** `scripts/push_social.py` now accepts a `media_files` list per
post, confirmed working against GHL's live API (all images in the list save to the post). This is
what makes a true swipeable carousel possible.

### Captions

Unchanged from v1, same wording, only the attached images changed. Full text in the original
delivery in chat, and reproduced below for the record.

**Instagram:**
> Local Services Ads is getting folded into Google Ads. If you run these for a home service
> business (or you're thinking about it), here's the short version: Pay per lead stays the same.
> Search and Maps only stays the same. Keywordless stays the same. What changes: the dashboard
> goes away, manual bidding stops working, budgets go from weekly to daily, and the BBB callout is
> gone. Rollout starts this month for plumbing, HVAC, electrical, roofing, cleaning, and more. One
> real thing to do now: export your performance reports before your migration date. Google says
> they will not transfer automatically. Full breakdown at the link in bio.
> #LocalServicesAds #GoogleAds #PPC #HomeServiceMarketing #FortWayneBusiness #ContractorMarketing

**Facebook:** longer version ending with the article link directly in the caption.

**LinkedIn:** longest version, business-owner framing, explicitly raises the Performance Max
open-question angle.

**GBP launch post:**
> Local Services Ads is moving into Google Ads this month. If you're a Fort Wayne area plumber,
> electrician, HVAC company, or other home service business running LSA, here's what's changing,
> and what's staying the same. One thing to do before your migration date: export your performance
> reports, they won't carry over automatically. Learn more: [live article URL with UTM]

UTM: `utm_source=google&utm_medium=organic&utm_campaign=gbp_blog&utm_content=local-services-ads-moving-to-google-ads-launch`

**This is one of Archie's first four launch posts and needs his explicit approval before
scheduling**, per the standing rule in `shared/social-content-standards.md`.

### TikTok and YouTube: not pushed, flagged honestly

Neither is connected in GHL's Social Planner. Beyond the connection gap, a static image carousel
isn't the right format for either anyway (TikTok's photo/slideshow mode isn't wired into this
pipeline, YouTube has no static-carousel format at all). Not built for this article.

### GBP follow-up post, prepared but not yet pushed

Scheduled for roughly **2026-08-10 to 2026-08-13** (7 to 10 days after launch). Not created as a
GHL draft yet, held to build fresh closer to the date.

> Quick follow-up on the Local Services Ads changes: if you're also running a standard Performance
> Max campaign, does the new LSA campaign compete with it for budget? Google hasn't confirmed
> either way yet. Here's what we do know, and why it's worth treating as an open question rather
> than a settled one: [live article URL with UTM]

UTM: `utm_source=google&utm_medium=organic&utm_campaign=gbp_blog&utm_content=local-services-ads-moving-to-google-ads-followup`

---

## Approval needed

1. **LinkedIn account** — personal profile or the Brightbox Digital page (or both)? Still open.
2. **GBP launch post** — review copy, image, CTA, destination URL, and proposed date, then
   approve, request revisions, change image, change CTA, or skip. Required per the first-four rule.
3. Instagram and Facebook carousels are approved (v2 design signed off) and ready to schedule
   directly in GHL Social Planner whenever convenient.
