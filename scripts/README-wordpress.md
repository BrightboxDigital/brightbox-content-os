# WordPress drafting: setup

`scripts/wp-draft` creates a WordPress **draft** from an approved article. It never publishes.
Publishing stays a separate manual step in wp-admin.

## One-time setup

1. In wp-admin: **Users, Profile**, scroll to **Application Passwords**.
2. Name it `Content OS`, click Add. **Copy the password immediately, it is shown once.**
3. Store it, keeping the spaces:

   ```
   cat > ~/.config/brightbox/wordpress.json <<'EOF'
   {"site": "https://brightboxdigital.io",
    "username": "YOUR_WP_USERNAME",
    "app_password": "xxxx xxxx xxxx xxxx xxxx xxxx"}
   EOF
   chmod 600 ~/.config/brightbox/wordpress.json
   ```

   **Do not paste the password into chat.** Never commit this file.

4. Verify:

   ```
   ./scripts/wp-draft --check
   ```

## Creating a draft

```
./scripts/wp-draft clients/brightbox/approved/BBX-001-styled.html \
  --title "Does a Small Google Ads Budget Actually Work?" \
  --slug does-a-small-google-ads-budget-work \
  --category "Google Ads" \
  --excerpt "12 leads at about 37 dollars each on a 15 dollar a day budget." \
  --featured ~/Desktop/handyman-screenshot.png \
  --alt-text "Google Ads campaign showing a 15 dollar daily budget and 12 conversions"
```

**`--category` must be the exact name of an existing WordPress category**, not the content
category label from `content-tracker.csv`. On BBX-002, passing "Google Ads and PPC" (the
tracker's label) instead of "Google Ads" (the site's actual category) created a real duplicate
category, splitting the two PPC articles across two different archive pages. Check the site's
existing categories first if unsure. The script now warns on any near-miss instead of silently
creating a sibling, but it still creates one unless you stop it.

**`--alt-text` is required whenever `--featured` is given.** The script refuses to run without
it, since a featured image uploaded without one ships with an empty `alt` attribute (found on
BBX-002). Write a real description of the image that naturally works in the article's primary
keyword.

It prints the wp-admin edit URL. Review it, set anything the script did not (Rank Math meta,
featured image position, the two in-body screenshots), then publish by hand.

## What it does and does not do

**Does:** creates a draft, sets title, body HTML, excerpt, slug, category, and optionally uploads and
attaches a featured image with alt text. Creates the category if no exact name match exists, after
warning about any similarly-named category found.

**Does not, by design:**

- **Publish.** status is always `draft`. There is no code path to publish and there will not be one.
- **Set the two in-body screenshots.** The article HTML still needs its `REPLACE_ME` image URLs
  swapped for real media library URLs before drafting. The script refuses to run while `REPLACE_ME`
  is present, so a draft never ships with broken images.
- **Set Rank Math SEO fields.** The SEO title and meta description from the article package still go
  in by hand, or through Rank Math's own fields. The REST API does not write them reliably.

## Security

- The application password is a credential. It lives only in `~/.config/brightbox/`, mode 600, never
  in this repository and never in chat.
- If it leaks, revoke it in wp-admin Application Passwords and generate a new one. Revoking is
  instant and does not affect the login password.
- The password grants whatever the WordPress user can do. Consider a dedicated user with an Editor
  role rather than an Administrator, so a leaked token cannot change site settings.

---

# Fixing the footer JavaScript (if it prints as text on every page)

**Symptom:** the script's code appears as visible text at the bottom of every page, under the footer.

**Cause:** the JS is being output without a `<script>` wrapper, so the browser prints it instead of
running it. This happens with some Header Footer Code Manager snippet configurations.

**Fix, the reliable way:**

1. Open the footer snippet in Header Footer Code Manager (the one in the Footer location).
2. Set its **Snippet Type to HTML**, not Javascript.
3. Replace its entire content with the contents of `shared/blog-template-footer-snippet.html`,
   which already includes the `<script>` and `</script>` tags.
4. Save. Clear any caching plugin. Hard refresh a page (Cmd+Shift+R).

The code should now run instead of showing, and the footer text disappears.

**Do not** mix the two. Either:
- Snippet Type HTML with the `<script>` tags included (use `blog-template-footer-snippet.html`), or
- Snippet Type Javascript with raw JS and no tags (use `blog-template.js`).

Using Javascript type WITH `<script>` tags double-wraps and breaks it. The HTML-type-with-tags path
is the more predictable of the two.

---

# Image automation: the one-command workflow

Replaces the manual Squoosh, upload, copy-URL, paste-placeholder loop, and the
ChatGPT featured-image back and forth.

## The full drafting command

```
# 1. optimize the raw screenshots (Squoosh replacement: resize + WebP + strip metadata)
./scripts/prep-images --outdir /tmp/prepped ~/Desktop/handyman.png ~/Desktop/conversion.png

# 2. generate a branded featured image from the title (no AI tool needed)
./scripts/make-featured --title "Does a Small Google Ads Budget Actually Work?" \
    --category "Google Ads and PPC" --out /tmp/featured.png

# 3. create the draft with everything uploaded and wired
./scripts/wp-draft clients/brightbox/approved/BBX-002-styled.html \
    --title "..." --slug "..." --category "Google Ads and PPC" --excerpt "..." \
    --body-image /tmp/prepped/handyman.webp \
    --body-image /tmp/prepped/conversion.webp \
    --featured /tmp/featured.png
```

`--body-image` uploads each image and drops it into the next `REPLACE_ME` placeholder in
document order. Pass one per placeholder. `--featured` uploads and sets the featured image.

## make-featured

Generates a consistent branded 1200x630 image: brand gradient, the article title auto-wrapped,
the category eyebrow, and the Brightbox logo. Same look every article, no AI generation, instant
and free. Requires ImageMagick.

Why this instead of an AI-generated image: a blog series is stronger with a consistent, recognisable
card than with one-off illustrations, and the editorial standard already prefers original brand
assets over decorative art. If a specific article genuinely needs a custom illustration, make one by
hand and pass it with `--featured` instead.

## prep-images

Resizes to a max width (default 1600), converts to WebP, strips EXIF and location metadata. That is
what Squoosh was doing. Uses cwebp, falls back to ImageMagick. Also cleans the filename into a tidy
slug for the URL.

## What still needs a human

- Cropping client identifiers out of a screenshot before prepping it. Do that first.
- The Rank Math SEO title and meta description, set in wp-admin.
- Reviewing and publishing the draft.
