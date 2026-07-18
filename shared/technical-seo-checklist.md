# Technical SEO Checklist

Run after an article is live. Nothing here modifies the site. Findings go to the client's
`site-fix-backlog.md`.

## Pre-publication verification

- [ ] Title correct
- [ ] Slug correct, no year unless essential
- [ ] Author set to Archie Brady
- [ ] Category assigned
- [ ] Featured image set
- [ ] Alt text on every image
- [ ] Internal links resolve
- [ ] External links resolve
- [ ] CTA links resolve
- [ ] Mobile rendering acceptable
- [ ] Table of contents matches headings
- [ ] Article or BlogPosting schema present
- [ ] Canonical correct
- [ ] Index settings correct
- [ ] Site template share functionality displays as intended

## Post-publication indexing QA

- [ ] URL returns a successful response
- [ ] No noindex directive
- [ ] Not blocked in robots.txt
- [ ] Canonical is correct and self referencing where appropriate
- [ ] Canonical uses the preferred HTTPS URL
- [ ] Mobile version contains the complete article
- [ ] Title and H1 are unique across the site
- [ ] Linked from the blog archive
- [ ] Linked from its category page
- [ ] At least two relevant existing pages link to it
- [ ] XML sitemap contains the canonical URL
- [ ] Article structured data matches the visible page
- [ ] Structured data has no critical errors
- [ ] Featured image is crawlable
- [ ] Images have appropriate dimensions and alt text
- [ ] Usable on mobile
- [ ] Main content not obscured by interstitials or overlays
- [ ] No major layout or rendering issue
- [ ] Page experience reasonable

## Search Console

**Currently not connected.** Do not report inspection results you did not obtain.

When not connected, output these manual instructions and set status `Search Console Check Needed`:

1. Open Search Console for the brightboxdigital.io property.
2. Paste the article URL into the URL Inspection bar.
3. Record: coverage state, canonical Google selected, mobile usability, and any enhancements detected.
4. If the URL is not indexed and the page is ready, click Request Indexing once.
5. Record the request date in the tracker.

When connected: inspect the live URL, request indexing once where appropriate, record the request
date, and do not repeatedly request indexing.

**Never claim that submission guarantees indexing.**

## Brightbox site notes

The site runs WordPress with Rank Math. Sitemap index is at
`https://brightboxdigital.io/sitemap_index.xml` with post, page and category sitemaps.
