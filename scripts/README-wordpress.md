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
  --category "Google Ads and PPC" \
  --excerpt "12 leads at about 37 dollars each on a 15 dollar a day budget." \
  --featured ~/Desktop/handyman-screenshot.png
```

It prints the wp-admin edit URL. Review it, set anything the script did not (Yoast/Rank Math meta,
featured image position, the two in-body screenshots), then publish by hand.

## What it does and does not do

**Does:** creates a draft, sets title, body HTML, excerpt, slug, category, and optionally uploads and
attaches a featured image. Creates the category if it does not exist.

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
