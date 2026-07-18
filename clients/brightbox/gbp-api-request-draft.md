# GBP API Access Request: Draft Justification

Draft for Archie's review. **Do not submit without reading it.** Every statement must be true of
what Brightbox will actually build, because Google evaluates the stated use case and vague or
overreaching requests get rejected.

Submit from the Google account that is an owner or manager on the Brightbox Business Profile.

**Project ID:** `brightbox-digita-1743176991871`

---

## Suggested response for the use case field

> Brightbox Digital is a one person web design and local marketing business in Fort Wayne, Indiana,
> operated by Archie Brady. We manage our own Google Business Profile at brightboxdigital.io.
>
> We are requesting API access to automate publishing Business Profile posts that link to articles
> we publish on our own website, and to read performance data for those posts.
>
> Specifically we intend to use:
>
> - My Business Account Management API and My Business Business Information API to identify our
>   account and location.
> - Google My Business API v4.9 localPosts to create a post when we publish a new article, and a
>   single follow up post seven to ten days later.
> - Business Profile Performance API to read views and CTA interactions on those posts so we can
>   evaluate whether the posts are useful.
>
> Expected volume is low. We publish roughly two articles per month, which means about four posts
> per month total across launch and follow up.
>
> We are not requesting access to modify business information. We will not change business name,
> categories, address, phone number, hours, service areas, managers or ownership through the API.
> We are not building a product for third parties and we are not managing other businesses'
> profiles through this integration. This is for our own single location only.

---

## Why it is worded this way

Three things make an application credible, and all three are true here, so none of this requires
stretching anything:

1. **A narrow, specific scope.** Naming the exact endpoints is stronger than asking for general
   access. It also matches what the system actually does.
2. **Low, honest volume.** Roughly four posts a month is small and easy to believe. Do not inflate it.
3. **An explicit statement of what will not be touched.** Business information write access is the
   sensitive part of this API. Ruling it out directly removes the main reason to reject.

## Before submitting, confirm these are still true

- [ ] Brightbox GBP profile is verified and active, and has been for 60 or more days
- [ ] brightboxdigital.io is listed on the profile
- [ ] Submitting from an owner or manager email on the profile
- [ ] The three read APIs are enabled in project `brightbox-digita-1743176991871`
- [ ] Publishing cadence stated matches reality, currently 1st and 15th
- [ ] Archie has read the text above and agrees it describes what he wants built

## After submitting

Record the submission date here so the wait is measurable rather than a vague feeling:

**Submitted:** _______________

Check quota at the Cloud console API quotas page. 0 QPM means still pending. 300 QPM means approved.

**Approved:** _______________

Until approved, GBP posting stays manual and `distribute-blog` produces ready to post packages only.
