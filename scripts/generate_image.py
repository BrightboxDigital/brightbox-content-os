#!/usr/bin/env python3
"""Generate a blog featured image with OpenAI, optimize it, and wire it into WordPress.

Stage order (matches the spec):
  1. Load the structured image brief.
  2. Generate one master image via the OpenAI Images API (gpt-image-2, medium, 1536x1024).
  3. Produce optimized derivatives (WP featured + social sizes) with focal-point aware crops.
  4. Upload derivatives to the WordPress media library.
  5. Set the WP draft's featured image and verify it.
  6. Write a manifest logging every URL, id, the prompt, and status.

GHL attachment is handled by push-social, which reads this manifest so each platform
draft gets its own correctly sized derivative. That keeps the HighLevel post creation
after the media exists, avoiding the edit-post endpoint.

Never publishes anything. Drafts only.

USAGE
  ./scripts/generate-image --brief clients/brightbox/drafts/BBX-001-image-brief.json --post-id 5555
  ./scripts/generate-image --brief ... --post-id ... --rerun     # force regeneration

SECRETS
  OPENAI_API_KEY from the environment, or ~/.config/brightbox/openai.json.
  WordPress creds reused from ~/.config/brightbox/wordpress.json.
  Never logged, never committed.
"""

import argparse
import base64
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

CFG = Path.home() / ".config" / "brightbox"
OPENAI_CFG = CFG / "openai.json"
WP_CFG = CFG / "wordpress.json"
OPENAI_URL = "https://api.openai.com/v1/images/generations"

# derivative specs: name -> (width, height, format, quality)
DERIVATIVES = {
    "wp_featured": (1200, 675, "webp", 82),
    "facebook":    (1200, 630, "webp", 82),
    "linkedin":    (1200, 630, "webp", 82),
    "instagram":   (1080, 1350, "jpg", 86),
    "square":      (1080, 1080, "jpg", 86),
}

# focal point keyword -> ImageMagick gravity
GRAVITY = {
    "center": "Center", "top": "North", "bottom": "South",
    "left": "West", "right": "East",
    "top-left": "NorthWest", "top-right": "NorthEast",
    "bottom-left": "SouthWest", "bottom-right": "SouthEast",
}


def log(msg):
    print(f"  {msg}")


def die(msg, stage=None, hint=None):
    if stage:
        print(f"\nFAILED at stage: {stage}", file=sys.stderr)
    print(f"ERROR: {msg}", file=sys.stderr)
    if hint:
        print(f"\n{hint}", file=sys.stderr)
    sys.exit(1)


def openai_key():
    k = os.environ.get("OPENAI_API_KEY")
    if k:
        return k
    if OPENAI_CFG.exists():
        d = json.loads(OPENAI_CFG.read_text())
        k = d.get("api_key")
        if k and "PASTE_" not in k:
            return k
    die("No OpenAI key found.",
        hint="Set OPENAI_API_KEY in the environment, or fill in ~/.config/brightbox/openai.json.")


def wp_creds():
    if not WP_CFG.exists():
        die(f"WordPress credentials not found at {WP_CFG}")
    d = json.loads(WP_CFG.read_text())
    d["site"] = d["site"].rstrip("/")
    return d


def wp_auth(c):
    raw = f"{c['username']}:{c['app_password']}".encode()
    return "Basic " + base64.b64encode(raw).decode()


# ---------------------------------------------------------------- OpenAI

def generate_master(prompt, out_path):
    """Call the Images API with retries and backoff. Returns the saved master path."""
    key = openai_key()
    body = json.dumps({
        "model": "gpt-image-2",
        "prompt": prompt,
        "size": "1536x1024",
        "quality": "medium",
        "output_format": "png",   # lossless master; derivatives set their own format
        "background": "opaque",
        "n": 1,
    }).encode()

    last_err = None
    for attempt in range(1, 4):  # 1 initial + up to 2 retries
        req = urllib.request.Request(OPENAI_URL, data=body, method="POST")
        req.add_header("Authorization", f"Bearer {key}")
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                resp = json.load(r)
            b64 = resp["data"][0]["b64_json"]
            raw = base64.b64decode(b64)
            out_path.write_bytes(raw)
            return out_path
        except urllib.error.HTTPError as e:
            code = e.code
            detail = e.read().decode(errors="replace")[:200]
            last_err = f"HTTP {code}: {detail}"
            if code == 429 or 500 <= code < 600:
                wait = 2 ** attempt
                log(f"OpenAI {code}, retry {attempt}/2 in {wait}s")
                time.sleep(wait)
                continue
            die(f"OpenAI image generation failed: {last_err}", stage="generate")
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = str(e)
            wait = 2 ** attempt
            log(f"OpenAI network error, retry {attempt}/2 in {wait}s")
            time.sleep(wait)
    die(f"OpenAI image generation failed after retries: {last_err}", stage="generate")


def validate_image(path, min_w=1024, min_h=512):
    """Confirm the file is a real image of the expected shape."""
    try:
        out = subprocess.run(
            ["magick", "identify", "-format", "%m %w %h", str(path)],
            capture_output=True, text=True, check=True).stdout.strip()
        fmt, w, h = out.split()
        w, h = int(w), int(h)
    except Exception as e:
        die(f"Returned file is not a valid image: {e}", stage="validate")
    if w < min_w or h < min_h:
        die(f"Master image too small: {w}x{h}", stage="validate")
    size = path.stat().st_size
    if size < 5000:
        die(f"Master image suspiciously small on disk: {size} bytes", stage="validate")
    log(f"master valid: {fmt} {w}x{h}, {size:,} bytes")
    return w, h


# ---------------------------------------------------------------- derivatives

def make_derivative(master, name, spec, gravity, out_dir, slug):
    w, h, fmt, q = spec
    fname = f"{slug}-{name.replace('_','-')}.{fmt}"
    out = out_dir / fname
    # resize to cover, then crop to exact size at the focal gravity; strip metadata
    cmd = ["magick", str(master),
           "-resize", f"{w}x{h}^",
           "-gravity", gravity,
           "-extent", f"{w}x{h}",
           "-strip"]
    if fmt in ("jpg", "jpeg"):
        cmd += ["-quality", str(q), "-interlace", "JPEG"]
    else:  # webp
        cmd += ["-quality", str(q), "-define", "webp:method=6"]
    cmd.append(str(out))
    subprocess.run(cmd, check=True, capture_output=True)
    return out, fname


# ---------------------------------------------------------------- WordPress

def wp_api(c, method, path, body=None, headers=None):
    url = f"{c['site']}/wp-json/wp/v2/{path.lstrip('/')}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", wp_auth(c))
    req.add_header("User-Agent", "BrightboxContentOS/1.0")
    if body is not None:
        req.add_header("Content-Type", "application/json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)


def wp_find_media(c, filename):
    """Idempotency: return existing media id/url if this filename is already uploaded."""
    slug = filename.rsplit(".", 1)[0]
    try:
        res = wp_api(c, "GET", f"media?search={urllib.parse.quote(slug)}&per_page=20")
    except Exception:
        return None
    for m in res:
        src = m.get("source_url", "")
        if src.rsplit("/", 1)[-1].rsplit(".", 1)[0] == slug:
            return {"id": m["id"], "url": src}
    return None


def wp_upload(c, path, filename, title, alt, caption=""):
    existing = wp_find_media(c, filename)
    if existing:
        log(f"reusing existing WP media {existing['id']} ({filename})")
        media_id = existing["id"]
    else:
        mime = "image/webp" if filename.endswith(".webp") else "image/jpeg"
        url = f"{c['site']}/wp-json/wp/v2/media"
        req = urllib.request.Request(url, data=Path(path).read_bytes(), method="POST")
        req.add_header("Authorization", wp_auth(c))
        req.add_header("Content-Type", mime)
        req.add_header("Content-Disposition", f'attachment; filename="{filename}"')
        req.add_header("User-Agent", "BrightboxContentOS/1.0")
        with urllib.request.urlopen(req, timeout=120) as r:
            m = json.load(r)
        media_id = m["id"]
        log(f"uploaded WP media {media_id} ({filename})")
    # set title / alt / caption
    meta = wp_api(c, "POST", f"media/{media_id}",
                  {"title": title, "alt_text": alt, "caption": caption})
    return {"id": media_id, "url": meta["source_url"]}


def main():
    ap = argparse.ArgumentParser(description="Generate + wire a blog featured image (drafts only)")
    ap.add_argument("--brief", required=True, help="path to the image brief JSON")
    ap.add_argument("--post-id", type=int, required=True, help="WordPress draft post ID")
    ap.add_argument("--rerun", action="store_true", help="regenerate even if a manifest exists")
    ap.add_argument("--outdir", default=None, help="where to write images and manifest")
    args = ap.parse_args()

    brief = json.loads(Path(args.brief).read_text())
    slug = brief.get("filename") or brief.get("slug") or f"post-{args.post_id}"
    slug = slug.lower().replace(" ", "-")
    outdir = Path(args.outdir) if args.outdir else Path(args.brief).parent / f"{slug}-images"
    outdir.mkdir(parents=True, exist_ok=True)
    manifest_path = outdir / "manifest.json"

    # Idempotency: if a manifest exists and featured is set, do nothing unless --rerun
    if manifest_path.exists() and not args.rerun:
        m = json.loads(manifest_path.read_text())
        if m.get("wp_featured_set"):
            log(f"manifest already complete at {manifest_path}. Use --rerun to regenerate.")
            print(json.dumps({"status": "already_done", "manifest": str(manifest_path)}))
            return

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "post_id": args.post_id,
        "slug": slug,
        "brief_title": brief.get("title"),
        "prompt": brief.get("prompt"),
        "master": None,
        "derivatives": {},
        "wp_featured_set": False,
        "stage": "start",
    }

    def save_manifest():
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

    prompt = brief.get("prompt")
    if not prompt:
        die("brief has no 'prompt' field", stage="brief")

    print(f"\nGenerating featured image for post {args.post_id} ({slug})\n")

    # 2. master
    manifest["stage"] = "generate"; save_manifest()
    master = outdir / f"{slug}-master.png"
    if master.exists() and not args.rerun:
        log(f"master already present: {master.name}")
    else:
        generate_master(prompt, master)
    validate_image(master)
    manifest["master"] = str(master)

    # 3. derivatives
    manifest["stage"] = "derivatives"; save_manifest()
    gravity = GRAVITY.get((brief.get("focal_point") or "center").lower(), "Center")
    deriv_files = {}
    for name, spec in DERIVATIVES.items():
        out, fname = make_derivative(master, name, spec, gravity, outdir, slug)
        deriv_files[name] = {"path": str(out), "filename": fname}
        log(f"derivative {name}: {fname}")
    manifest["derivatives"] = deriv_files

    # 4/5. upload to WP + set featured
    manifest["stage"] = "wordpress"; save_manifest()
    c = wp_creds()
    alt = brief.get("alt_text") or brief.get("title") or "Brightbox Digital blog featured image"
    title = brief.get("image_title") or brief.get("title") or slug
    caption = brief.get("caption", "")

    for name, info in deriv_files.items():
        up = wp_upload(c, info["path"], info["filename"], title, alt, caption if name == "wp_featured" else "")
        deriv_files[name]["wp_id"] = up["id"]
        deriv_files[name]["wp_url"] = up["url"]

    featured_id = deriv_files["wp_featured"]["wp_id"]
    wp_api(c, "POST", f"posts/{args.post_id}", {"featured_media": featured_id})
    # 5b. verify
    post = wp_api(c, "GET", f"posts/{args.post_id}?context=edit&_fields=featured_media")
    if post.get("featured_media") != featured_id:
        die(f"featured_media verification failed: expected {featured_id}, got {post.get('featured_media')}",
            stage="wordpress")
    manifest["wp_featured_set"] = True
    manifest["wp_featured_media_id"] = featured_id
    log(f"featured image set and verified (media {featured_id})")

    manifest["stage"] = "complete"; save_manifest()
    print(f"\nDone. Manifest: {manifest_path}")
    print("Featured image assigned to the WordPress draft. Nothing published.")
    print("Next: push-social will attach the platform derivatives to the GHL drafts.")


if __name__ == "__main__":
    main()
