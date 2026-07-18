# Social and GBP Content Standards

Every approved and published article produces a distribution package.

## Format selection

Pick the format that actually serves the subject:

1. **Archie recorded face to camera Reel** — preferred when personal explanation, opinion or
   experience improves the subject
2. **Screen recording** — when the subject is a tool, dashboard or interface
3. **Branded motion graphic video** — when no footage is needed
4. **Four to six slide carousel** — when the subject is a list, comparison or framework
5. **Single image post** — when one idea carries it

The system writes what Archie needs to say. It never fabricates his presence, his voice or his image.

## Video package

Target 30 to 45 seconds. Deliver:

- Video objective
- Intended audience
- Primary hook
- Three alternative hooks
- Teleprompter ready script
- On screen headline
- On screen takeaway highlights
- Shot list
- B-roll suggestions
- Screen recording suggestions
- Reel cover headline
- Safe zone instructions
- CTA
- Caption
- Accessible transcript
- Recommended article link placement

Script rules: use Archie's interview answers, sound conversational, address one primary problem,
no more than three main points, no formal blog introduction, no invented examples, no em dashes,
natural CTA at the end, and it must fit the duration when read at a normal pace.

## Carousel package

If Archie does not want to record:

- Cover headline
- Slide by slide copy
- Visual direction per slide
- Final CTA slide
- Caption
- Alt text
- Recommended dimensions
- Safe zones

## Platform versions

Produce distinct versions for Instagram, Facebook, TikTok, LinkedIn and YouTube Shorts.

Each needs: caption, title where applicable, CTA, link instructions, relevant hashtags, suggested
posting date, and a suggested follow up engagement action.

Do not reuse an identical caption across platforms where behavior differs. LinkedIn tolerates
longer context. TikTok and Shorts need front loaded hooks. Instagram link handling differs from
Facebook.

## Publishing

No social connector is currently configured. Build a distribution queue in
`clients/brightbox/distribution/` and stop there.

Auto-publishing requires all three: the connection exists, Archie explicitly authorized publishing,
and the content is approved.

## Google Business Profile

GBP posting runs through the official API when available. Required capabilities are limited to:
list accounts, list locations, create local post, get local post, list posts, retrieve post
insights, and delete a post when explicitly authorized.

**Do not grant or use tools that change business name, categories, address, phone, hours, service
areas, managers or ownership.**

GBP is not currently connected. Generate the complete ready to post package, mark status
`Connection Needed`, and never claim it was published.

### Launch post

Created after the article is approved, published and validated. Contains:

- Concise hook
- One useful takeaway
- Natural local relevance where appropriate
- Learn More CTA
- Live article URL
- UTM parameters
- Publicly accessible image

No phone number in the copy. No unsupported promises. No keyword stuffing.

UTM format:

```
utm_source=google
utm_medium=organic
utm_campaign=gbp_blog
utm_content=[article-slug]-launch
```

Validate before posting: article URL, canonical destination, image URL, CTA, UTM parameters, and
current GBP content policies.

### Follow-up post

Seven to ten days after launch. Built from one of: an FAQ, a quick tip, a common mistake, a local
consideration, or an important takeaway. It must stand alone. It must not duplicate the launch post.

```
utm_content=[article-slug]-followup
```

### Approval

The first four launch posts and the first four follow-up posts each require Archie's approval.
Show copy, image, CTA, destination URL and proposed date, then ask him to approve and publish,
request revisions, change image, change CTA, or skip.

After four successful posts, ask whether future launch posts may publish automatically. Do not
enable automatic external publishing without explicit approval.

### Recording

After publishing, record: account, location, local post ID, search URL, creation date, post state,
CTA, destination URL, UTM campaign, media URL.

### Rejection

Do not resubmit repeatedly. Record the rejection, identify the likely policy issue, notify Archie,
prepare a corrected version, and wait.

**Never claim GBP posts directly improved rankings without defensible evidence.**

## Promotion

Recommended channels: internal links, GBP posts, social video, carousel, email mention, direct
sharing with clients who asked the question, legitimate local or partner outreach, and inclusion on
a relevant service page.

Do not perform outreach, send email or message third parties without explicit approval.
Never seek fake mentions or low quality backlinks.
