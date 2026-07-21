#!/usr/bin/env python3
"""Push a blog article's social posts into the GoHighLevel Social Planner as DRAFTS.

Creates draft posts (never auto-publishes) in GHL so Archie reviews and schedules
them in the Social Planner. Targets whatever accounts are connected: Facebook,
Instagram, LinkedIn, and Google Business Profile.

USAGE
    ./scripts/push-social --check
    ./scripts/push-social --list-accounts
    ./scripts/push-social --from clients/brightbox/distribution/<folder>/posts.json

CREDENTIALS
    ~/.config/brightbox/ghl.json, mode 600, never in this repository:
        {"location_id": "...", "private_token": "..."}
    Create the token in GHL: Settings, Private Integrations, with the Social
    Planner scopes. Do not paste it into chat.

HARD LIMIT
    Every post is created with status "draft". There is no publish path here.
    Archie schedules and publishes inside GHL.
"""

import argparse
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

CREDS = Path.home() / ".config" / "brightbox" / "ghl.json"
BASE = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"  # required GHL version header


def upload_media_to_ghl(creds, file_path):
    """Upload a local image to GHL Media Storage and return its hosted URL.

    Uses curl, not urllib: GHL's media endpoint sits behind Cloudflare bot
    protection that blocks Python's TLS signature but allows curl. Needs the
    token to carry the medias.write scope.
    """
    p = Path(file_path)
    ct = "image/jpeg" if p.suffix.lower() in (".jpg", ".jpeg") else "image/webp"
    cmd = [
        "curl", "-s", "--max-time", "90", "-X", "POST",
        f"{BASE}/medias/upload-file",
        "-H", f"Authorization: Bearer {creds['private_token']}",
        "-H", f"Version: {API_VERSION}",
        "-H", "Accept: application/json",
        "-F", f"file=@{p};type={ct}",
        "-F", f"locationId={creds['location_id']}",
    ]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout
    try:
        d = json.loads(out)
    except json.JSONDecodeError:
        die(f"GHL media upload returned non-JSON for {p.name}", out[:200])
    url = d.get("url") or d.get("fileUrl") or (d.get("file") or {}).get("url")
    if not url:
        if "not authorized for this scope" in out:
            die("The GHL token lacks the medias.write scope.",
                "In GHL: Settings, Private Integrations, edit the Content OS integration,\n"
                "add the 'Medias / Write' scope (and Medias / Read), save, and update the\n"
                "token in ~/.config/brightbox/ghl.json if it regenerates.")
        die(f"GHL media upload failed for {p.name}", out[:300])
    return url


def die(msg, hint=None):
    print(f"\nERROR: {msg}", file=sys.stderr)
    if hint:
        print(f"\n{hint}", file=sys.stderr)
    sys.exit(1)


def load_creds():
    if not CREDS.exists():
        die(f"GHL credentials not found at {CREDS}",
            "Create it with your Location ID and Private Integration token:\n"
            f'  {{"location_id": "...", "private_token": "..."}}\n'
            "Do not paste the token into chat.")
    d = json.loads(CREDS.read_text())
    for k in ("location_id", "private_token"):
        if not d.get(k) or "PASTE_" in str(d.get(k)):
            die(f"'{k}' is not filled in yet in {CREDS}")
    return d


def require_user_id(creds):
    if not creds.get("user_id") or "PASTE_" in str(creds.get("user_id")):
        die("user_id is not filled in yet in " + str(CREDS),
            "GHL requires the posting user's ID. Find it in GHL: Settings, then\n"
            "My Staff, click your user, and copy the ID from the page URL (the long\n"
            "string after /team/ or /staff/). Paste it into ghl.json as \"user_id\".")
    return creds["user_id"]


def api(creds, method, path, body=None):
    url = f"{BASE}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {creds['private_token']}")
    req.add_header("Version", API_VERSION)
    req.add_header("Accept", "application/json")
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:500]
        if e.code in (401, 403):
            die(f"GHL rejected the token ({e.code}).",
                "Check the Private Integration token and that it has the Social\n"
                "Planner scopes. Regenerate it in GHL if unsure.\n\n" + detail)
        die(f"GHL API error {e.code} on {method} {path}\n\n{detail}")


def get_accounts(creds):
    """Return the live social accounts connected in this location's Social Planner.

    GHL nests them under results.accounts. Each has id, name, platform, plus
    deleted/isExpired flags we filter on so we never target a dead account.
    """
    res = api(creds, "GET", f"/social-media-posting/{creds['location_id']}/accounts")
    accts = (res.get("results") or {}).get("accounts") or []
    out = []
    for a in accts:
        if a.get("deleted") or a.get("isExpired"):
            continue
        out.append({
            "id": a.get("id"),
            "platform": (a.get("platform") or a.get("type") or "").lower(),
            "name": a.get("name", ""),
        })
    return out


PLATFORM_ALIASES = {
    "facebook": {"facebook", "fb"},
    "instagram": {"instagram", "ig"},
    "linkedin": {"linkedin"},
    "google": {"google", "gbp", "gmb", "googlemybusiness", "google_business"},
    "tiktok": {"tiktok"},
    "youtube": {"youtube"},
    "twitter": {"twitter", "x"},
}


def match_platform(account_platform, wanted):
    aliases = PLATFORM_ALIASES.get(wanted, {wanted})
    return account_platform in aliases


def create_draft(creds, account_ids, summary, media_url=None):
    body = {
        "accountIds": account_ids,
        "summary": summary,
        "status": "draft",       # HARD LIMIT: draft only, never published
        "type": "post",
        "userId": creds["user_id"],
    }
    if media_url:
        body["media"] = [{"url": media_url}]
    return api(creds, "POST", f"/social-media-posting/{creds['location_id']}/posts", body)


def main():
    ap = argparse.ArgumentParser(description="Push article social posts to GHL Social Planner as drafts")
    ap.add_argument("--check", action="store_true", help="verify token and list connected accounts")
    ap.add_argument("--list-accounts", action="store_true", help="show connected social accounts and IDs")
    ap.add_argument("--from", dest="posts_file", help="posts.json describing the posts to create")
    ap.add_argument("--media", help="optional public image URL to attach to every post")
    ap.add_argument("--media-manifest", help="manifest.json from generate-image; attaches the "
                    "correct platform derivative URL to each draft")
    args = ap.parse_args()

    # platform -> which derivative to use. All social platforms get a JPG (never the
    # WebP featured), since some networks do not render WebP. GBP uses the landscape JPG.
    PLATFORM_DERIVATIVE = {
        "facebook": "facebook", "linkedin": "linkedin",
        "instagram": "instagram", "google": "facebook", "pinterest": "square",
    }
    # manifest gives us LOCAL derivative files; we upload each to GHL Media Storage
    # (not WordPress) so the social sizes never clutter the WP library.
    manifest_local = {}
    if args.media_manifest:
        man = json.loads(Path(args.media_manifest).read_text())
        for name, info in (man.get("derivatives") or {}).items():
            if info.get("path") and Path(info["path"]).exists():
                manifest_local[name] = info["path"]
    ghl_media_cache = {}  # derivative name -> uploaded GHL url, upload once each

    creds = load_creds()

    if args.check or args.list_accounts:
        accts = get_accounts(creds)
        print(f"Location: {creds['location_id']}")
        print(f"Connected accounts: {len(accts)}\n")
        for a in accts:
            print(f"  {a['platform']:<12} {a['name']:<28} id={a['id']}")
        if args.check:
            print("\nGHL connection working. Nothing was posted.")
        return

    if not args.posts_file:
        ap.error("give --from posts.json, or --check")

    require_user_id(creds)
    posts = json.loads(Path(args.posts_file).read_text())
    accts = get_accounts(creds)
    by_platform = {}
    for a in accts:
        by_platform.setdefault(a["platform"], a["id"])

    print(f"Creating DRAFT posts in GHL for location {creds['location_id']}\n")
    created, skipped = 0, []
    for p in posts:
        platform = p["platform"].lower()
        # find the connected account id for this platform
        acct_id = None
        for ap_platform, aid in by_platform.items():
            if match_platform(ap_platform, platform):
                acct_id = aid
                break
        if not acct_id:
            skipped.append(platform)
            print(f"  SKIP {platform}: not connected in GHL Social Planner")
            continue
        # pick media: explicit per-post > this platform's derivative uploaded to GHL > global --media
        media_url = p.get("media")
        if not media_url and manifest_local:
            deriv = PLATFORM_DERIVATIVE.get(platform, "wp_featured")
            local = manifest_local.get(deriv) or manifest_local.get("wp_featured")
            if local:
                if deriv not in ghl_media_cache:
                    ghl_media_cache[deriv] = upload_media_to_ghl(creds, local)
                    print(f"  uploaded {Path(local).name} to GHL media storage")
                media_url = ghl_media_cache[deriv]
        media_url = media_url or args.media
        res = create_draft(creds, [acct_id], p["caption"], media_url)
        post = (res.get("results") or {}).get("post") or res.get("post") or {}
        pid = post.get("_id") or post.get("id") or "?"
        created += 1
        print(f"  draft created for {platform}  (id {pid})")

    print(f"\n{created} draft(s) created. {'Skipped: ' + ', '.join(skipped) if skipped else ''}")
    print("Nothing was published. Open GHL Social Planner to review and schedule.")


if __name__ == "__main__":
    main()
