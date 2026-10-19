---
name: distribute-blog
description: Build the social video or carousel package, platform specific captions, and the Google Business Profile launch post for a published article. Use after an article is approved, live and technically validated. Interactive only.
---

# Distribute Blog

Read `shared/social-content-standards.md` before starting. It holds the full requirements.

## Preconditions

The article must be approved, live, and past the technical indexing QA in
`shared/technical-seo-checklist.md`. Do not build distribution for an article that is not live, and
never for one Archie has not approved.

The publishing workflow must initiate this handoff proactively. Once live QA and inbound linking
are complete, ask Archie whether he is ready to start social content creation and present the format
choice below. Do not wait for him to raise GHL or distribution in a later message.

## Step 1. Pick the format

Choose from: Archie recorded face to camera Reel, screen recording, branded motion graphic, four to
six slide carousel, or single image post. Prefer the Reel when personal explanation, opinion or
experience improves the subject. Say why you chose it.

Ask Archie whether he is willing to record before building a video package. If not, build the
carousel package instead.

## Step 2. Build the package

Video: 30 to 45 seconds, with all sixteen elements listed in the standards file. The script must be
built from his actual interview answers, sound conversational, cover one problem and no more than
three points, contain no invented examples, contain no em dashes, and fit the duration read at a
normal pace.

Carousel: cover headline, slide by slide copy, visual direction, CTA slide, caption, alt text,
dimensions, safe zones.

## Step 3. Platform versions

Distinct versions for Instagram, Facebook, TikTok, LinkedIn and YouTube Shorts. Each with caption,
title where applicable, CTA, link instructions, hashtags, suggested posting date, and a follow up
engagement action. Do not reuse one caption everywhere.

## Step 4. GBP launch post

GBP routes through GoHighLevel Social Planner. Generate the complete ready-to-post package and,
after Archie approves it in the current session, use `scripts/push-social` to create a draft only.
Never claim that a GHL draft was scheduled or published.

Contents: concise hook, one useful takeaway, natural local relevance where appropriate, Learn More
CTA, live article URL, UTM parameters, publicly accessible image. No phone number in the copy. No
unsupported promises. No keyword stuffing.

```
utm_source=google&utm_medium=organic&utm_campaign=gbp_blog&utm_content=[article-slug]-launch
```

Validate the article URL, canonical destination, image URL, CTA, UTM parameters and current GBP
content policies before presenting it.

## Step 5. Approval

The first four launch posts require Archie's approval. Show copy, image, CTA, destination URL and
proposed date. Ask him to approve the GHL draft push, request revisions, change image, change CTA,
or skip.

Set status `GBP Approval Needed`. Wait.

After four successful posts, ask whether future launch posts may publish automatically. Never enable
automatic external publishing without explicit approval.

## Step 6. Record

Save everything to `clients/brightbox/distribution/YYYY-MM-DD-slug/`. Update the tracker with reel
format, script status, recording status, social distribution status, GBP launch status and ID, and
the UTM campaign. GBP follow-up posts are not part of the workflow.

Since nothing can auto-publish yet, this becomes a queue for Archie to work through manually.

## If a GBP post is rejected

Do not resubmit repeatedly. Record the rejection, identify the likely policy issue, notify Archie,
prepare a corrected version, and wait for his decision.
