#!/usr/bin/env python3
"""Create a WordPress DRAFT from an approved Brightbox article. Never publishes.

This exists to save the manual paste. It creates a draft only. Publishing is a
separate human step in wp-admin, by design and by Archie's standing rule.

USAGE
    ./scripts/wp-draft --check
    ./scripts/wp-draft clients/brightbox/approved/BBX-001-styled.html \\
        --title "Does a Small Google Ads Budget Actually Work?" \\
        --slug does-a-small-google-ads-budget-work \\
        --category "Google Ads" \\
        --excerpt "12 leads at 36 dollars each on a 15 dollar a day budget." \\
        --featured /path/to/handyman-screenshot.png \\
        --alt-text "Google Ads campaign showing a 15 dollar daily budget and 12 conversions"

    --category must match an EXISTING WordPress category name exactly (check with
    --check or the site's category list first). This is not the content-tracker.csv
    "category" column verbatim; on BBX-002 those two things read the same to a human
    ("Google Ads and PPC" vs the site's actual "Google Ads" category) but were not the
    same string, and a real duplicate category got created because of it.

    Re-editing an existing draft after a text fix, same status guarantee:
    ./scripts/wp-draft clients/brightbox/approved/BBX-002-styled.html \\
        --update-id 5754

CREDENTIALS
    ~/.config/brightbox/wordpress.json, mode 600, never in this repository:

        {"site": "https://brightboxdigital.io",
         "username": "archie",
         "app_password": "xxxx xxxx xxxx xxxx xxxx xxxx"}

    Generate the application password in wp-admin, Users, Profile, Application
    Passwords. It is shown once. Paste it into that file, not into chat. The
    spaces in the password are fine, keep them.

HARD LIMIT
    status is always "draft". There is no publish path in this script and there
    will not be one. Publishing stays a separate explicit action in wp-admin.
"""

import argparse
import base64
import json
import mimetypes
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

CREDS = Path.home() / ".config" / "brightbox" / "wordpress.json"


def die(msg, hint=None):
    print(f"\nERROR: {msg}", file=sys.stderr)
    if hint:
        print(f"\n{hint}", file=sys.stderr)
    sys.exit(1)


def load_creds():
    if not CREDS.exists():
        die(
            f"WordPress credentials not found at {CREDS}",
            "In wp-admin: Users, Profile, Application Passwords. Create one named\n"
            "'Content OS', copy it, then:\n\n"
            f"  cat > {CREDS} <<'EOF'\n"
            '  {"site": "https://brightboxdigital.io", "username": "YOUR_WP_USERNAME",\n'
            '   "app_password": "xxxx xxxx xxxx xxxx xxxx xxxx"}\n'
            "  EOF\n"
            f"  chmod 600 {CREDS}\n\n"
            "Do not paste the password into chat.",
        )
    d = json.loads(CREDS.read_text())
    for k in ("site", "username", "app_password"):
        if not d.get(k):
            die(f"'{k}' missing from {CREDS}")
    d["site"] = d["site"].rstrip("/")
    return d


def auth_header(creds):
    raw = f"{creds['username']}:{creds['app_password']}".encode()
    return "Basic " + base64.b64encode(raw).decode()


def api(creds, method, path, body=None, headers=None):
    url = f"{creds['site']}/wp-json/wp/v2/{path.lstrip('/')}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", auth_header(creds))
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "BrightboxContentOS/1.0")
    if headers:
        for k, v in headers.items():
            req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:400]
        if e.code == 401:
            die("WordPress rejected the credentials (401).",
                "Check the username and application password. The app password is\n"
                "different from the login password. Regenerate it if unsure.")
        die(f"WordPress API error {e.code} on {method} {path}\n\n{detail}")


def resolve_category(creds, name):
    cats = api(creds, "GET", f"categories?search={urllib.parse.quote(name)}&per_page=100")
    for c in cats:
        if c["name"].lower() == name.lower():
            return c["id"]
    # No exact match. Found on BBX-002: "Google Ads and PPC" did not exactly match the
    # existing "Google Ads" category, so a duplicate got created and the site's two PPC
    # articles ended up split across two category archive pages. WordPress's own search
    # above is fuzzy, so anything it returned here is a real candidate worth a human's
    # eyes before we add a sibling category that reads the same to a reader.
    if cats:
        names = ", ".join(f"'{c['name']}' (id {c['id']})" for c in cats)
        print(f"  WARNING: no exact match for '{name}'. Similar existing categories found: "
              f"{names}. Creating '{name}' anyway; if one of those is actually the same "
              f"category, stop and re-run with --category set to its exact name instead.")
    made = api(creds, "POST", "categories", {"name": name})
    print(f"  created category '{name}' (id {made['id']})")
    return made["id"]


def upload_media(creds, path, alt_text=None):
    p = Path(path)
    if not p.exists():
        die(f"Featured image not found: {path}")
    mime = mimetypes.guess_type(str(p))[0] or "application/octet-stream"
    url = f"{creds['site']}/wp-json/wp/v2/media"
    req = urllib.request.Request(url, data=p.read_bytes(), method="POST")
    req.add_header("Authorization", auth_header(creds))
    req.add_header("Content-Type", mime)
    req.add_header("Content-Disposition", f'attachment; filename="{p.name}"')
    req.add_header("User-Agent", "BrightboxContentOS/1.0")
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            m = json.load(r)
            print(f"  uploaded {p.name} (media id {m['id']})")
    except urllib.error.HTTPError as e:
        die(f"Media upload failed {e.code}\n\n{e.read().decode(errors='replace')[:300]}")

    # Alt text is not writable in the same multipart upload above (WordPress needs it as
    # a separate JSON update on this install), so set it as a follow-up call. Every
    # featured image gets one: found on BBX-002, where an image uploaded without
    # --alt-text shipped with alt="" on the live page.
    if alt_text:
        body = json.dumps({"alt_text": alt_text}).encode()
        req2 = urllib.request.Request(f"{url}/{m['id']}", data=body, method="POST")
        req2.add_header("Authorization", auth_header(creds))
        req2.add_header("Content-Type", "application/json")
        req2.add_header("User-Agent", "BrightboxContentOS/1.0")
        with urllib.request.urlopen(req2, timeout=30) as r:
            json.load(r)
        print(f"  set alt text on media {m['id']}")
    else:
        print(f"  WARNING: no --alt-text given, media {m['id']} will have empty alt text")

    return {"id": m["id"], "url": m["source_url"]}


def main():
    ap = argparse.ArgumentParser(description="Create a WordPress draft. Never publishes.")
    ap.add_argument("html_file", nargs="?", help="path to the article HTML body")
    ap.add_argument("--title", help="post title (becomes the H1)")
    ap.add_argument("--slug")
    ap.add_argument("--category")
    ap.add_argument("--excerpt", default="")
    ap.add_argument("--featured", help="path to a featured image to upload")
    ap.add_argument("--alt-text",
                    help="alt text for the --featured image, required whenever --featured is "
                         "given. Write a real description of the image that naturally works "
                         "in the article's primary keyword, not a keyword-stuffed phrase.")
    ap.add_argument("--body-image", action="append", default=[], metavar="PATH",
                    help="image to upload and slot into the next REPLACE_ME placeholder, "
                         "in order. Repeat for multiple. Alt text for these comes from the "
                         "alt attribute already written into the article HTML, not this flag.")
    ap.add_argument("--update-id", type=int, metavar="POST_ID",
                    help="update this existing post's content instead of creating a new "
                         "one. Status is forced back to draft regardless of the post's "
                         "current status; this never publishes. --title/--slug/--category/"
                         "--excerpt/--featured are optional here and only touch the fields "
                         "given.")
    ap.add_argument("--check", action="store_true", help="verify credentials and exit")
    args = ap.parse_args()

    creds = load_creds()

    if args.check:
        me = api(creds, "GET", "users/me?context=edit")
        print(f"Site:     {creds['site']}")
        print(f"User:     {me.get('name')} (id {me.get('id')})")
        caps = me.get("capabilities", {}) or {}
        can_draft = caps.get("edit_posts", False)
        can_publish = caps.get("publish_posts", False)
        print(f"Can create drafts: {can_draft}")
        print(f"Can publish:       {can_publish}  (this script never will, regardless)")
        print("\nWordPress connection working.")
        return

    if args.update_id:
        if not args.html_file:
            ap.error("--update-id needs an html_file to read the new content from")
    elif not (args.html_file and args.title):
        ap.error("need an html_file and --title (or --check)")

    html = Path(args.html_file).read_text()

    # Strip any leading HTML comment block (build notes) so its REPLACE_ME prose
    # does not trip the guard below.
    html = re.sub(r"^\s*<!--.*?-->\s*", "", html, count=1, flags=re.S)

    # Upload body images and drop each into the next REPLACE_ME placeholder, in order.
    if args.body_image:
        placeholders = re.findall(r'src="(REPLACE_ME[^"]*)"', html)
        if len(args.body_image) != len(placeholders):
            die(f"{len(args.body_image)} body image(s) given but the article has "
                f"{len(placeholders)} REPLACE_ME placeholder(s).",
                "Pass one --body-image per placeholder, in the order they appear.")
        for img_path, placeholder in zip(args.body_image, placeholders):
            media = upload_media(creds, img_path)
            html = html.replace(placeholder, media["url"], 1)
            print(f"  slotted {Path(img_path).name} into {placeholder[:40]}...")

    if "REPLACE_ME" in html:
        die("The article still contains REPLACE_ME image placeholders.",
            "Pass --body-image for each one, or swap the URLs by hand first.")

    payload = {
        "status": "draft",          # hard limit. never anything else.
        "content": html,
    }
    if args.title:
        payload["title"] = args.title
    if args.excerpt:
        payload["excerpt"] = args.excerpt
    if args.slug:
        payload["slug"] = args.slug
    if args.category:
        payload["categories"] = [resolve_category(creds, args.category)]
    if args.featured:
        if not args.alt_text:
            die("--featured given without --alt-text.",
                "Write real alt text describing the image, incorporating the article's "
                "primary keyword naturally, and pass it with --alt-text. This is required "
                "so the image never ships with an empty alt attribute (see BBX-002).")
        payload["featured_media"] = upload_media(creds, args.featured, args.alt_text)["id"]

    if args.update_id:
        print(f"\nUpdating DRAFT {args.update_id} (status forced back to draft)")
        post = api(creds, "POST", f"posts/{args.update_id}", payload)
        print(f"\n  Draft updated. Status: {post['status']}")
    else:
        print(f"\nCreating DRAFT: {args.title}")
        post = api(creds, "POST", "posts", payload)
        print(f"\n  Draft created. Status: {post['status']}")

    edit_url = f"{creds['site']}/wp-admin/post.php?post={post['id']}&action=edit"
    preview_url = f"{creds['site']}/?p={post['id']}&preview=true"
    print(f"  Post ID:    {post['id']}")
    print(f"  Edit here:  {edit_url}")
    print(f"  Preview:    {preview_url}")
    print("\n  Nothing was published. Review in wp-admin, then publish manually.")


if __name__ == "__main__":
    main()
