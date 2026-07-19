#!/usr/bin/env python3
"""Search Reddit for the questions people actually ask about a topic.

COMPLIANCE NOTE, READ BEFORE USING
    Reddit's Responsible Builder Policy requires express written approval for
    commercial use of Reddit data. Archie's position, recorded July 19, 2026, is
    that Brightbox's use is non-commercial research: reading public threads to
    decide what to write about, never redistributing or reselling data.

    Claude's reading differed and is recorded in shared/source-validation.md so
    the disagreement is visible rather than buried. This is Archie's decision and
    Archie's account. If Reddit's position is ever clarified against this use,
    stop using this script.

    Enforcement risk is token revocation or app suspension.

WHAT THIS DOES NOT DO
    No posting. No commenting. No voting. No messaging. No user profiling.
    Read only, public listings only. It never stores comment bodies, never
    records usernames, and never attempts to infer anything about any person.
    The policy's privacy section is absolute on that point and this script is
    built so that violating it is not possible.

USAGE
    ./scripts/reddit-research "google ads budget" --subs PPC,smallbusiness --days 180
    ./scripts/reddit-research "call only ads" --subs PPC --limit 50
    ./scripts/reddit-research --check

CREDENTIALS
    ~/.config/brightbox/reddit.json, mode 600, never in this repository:

        {"client_id": "...", "client_secret": "..."}

    Uses the application-only OAuth flow, so no Reddit username or password is
    needed or accepted. The script cannot act as a user because it never holds
    user credentials.
"""

import argparse
import base64
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CREDS = Path.home() / ".config" / "brightbox" / "reddit.json"
RESEARCH = REPO / "clients" / "brightbox" / "research"

# Reddit asks for a descriptive, identifying User-Agent. Do not make this generic.
USER_AGENT = "macos:io.brightboxdigital.contentos:v1.0 (content research, contact archie@brightboxdigital.io)"

TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
API = "https://oauth.reddit.com"

# Free tier is 100 queries per minute per client id. Stay well under it.
SECONDS_BETWEEN_CALLS = 1.2

QUESTION_RE = re.compile(
    r"^(how|what|why|when|where|which|who|is|are|do|does|did|can|could|should|would|will|any|anyone|has|have|am|if)\b"
    r"|\?",
    re.I,
)


def die(msg, hint=None):
    print(f"\nERROR: {msg}", file=sys.stderr)
    if hint:
        print(f"\n{hint}", file=sys.stderr)
    sys.exit(1)


def load_creds():
    if not CREDS.exists():
        die(
            f"Reddit credentials not found at {CREDS}",
            "Create a script app at https://www.reddit.com/prefs/apps then:\n\n"
            f"  cat > {CREDS} <<'EOF'\n"
            '  {"client_id": "YOUR_ID", "client_secret": "YOUR_SECRET"}\n'
            "  EOF\n"
            f"  chmod 600 {CREDS}\n\n"
            "Do not paste these values into chat.",
        )
    d = json.loads(CREDS.read_text())
    for k in ("client_id", "client_secret"):
        if not d.get(k):
            die(f"'{k}' missing from {CREDS}")
    return d


def get_token(creds):
    basic = base64.b64encode(
        f"{creds['client_id']}:{creds['client_secret']}".encode()
    ).decode()
    data = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode()
    req = urllib.request.Request(TOKEN_URL, data=data, method="POST")
    req.add_header("Authorization", f"Basic {basic}")
    req.add_header("User-Agent", USER_AGENT)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)["access_token"]
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:300]
        die(
            f"Reddit token request failed: HTTP {e.code}",
            "401 usually means the client id or secret is wrong, or the app type\n"
            "is not 'script'. Check https://www.reddit.com/prefs/apps\n\n"
            f"Response: {body}",
        )


def api_get(token, path, params):
    url = f"{API}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("User-Agent", USER_AGENT)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            remaining = r.headers.get("x-ratelimit-remaining")
            return json.load(r), remaining
    except urllib.error.HTTPError as e:
        if e.code == 429:
            die("Rate limited by Reddit (429). Wait a few minutes before retrying.")
        if e.code in (403, 404):
            return None, None  # private, banned, or nonexistent subreddit
        raise


def search(token, sub, query, limit, days):
    """Search one subreddit. Returns public post metadata only."""
    cutoff = time.time() - days * 86400
    out = []
    data, remaining = api_get(token, f"/r/{sub}/search", {
        "q": query, "restrict_sr": "true", "sort": "relevance",
        "t": "year" if days > 90 else "month", "limit": min(limit, 100),
    })
    if data is None:
        return None, remaining
    for child in data.get("data", {}).get("children", []):
        p = child.get("data", {})
        created = p.get("created_utc", 0)
        if created < cutoff:
            continue
        # Deliberately NOT collected: author, comment bodies, any user field.
        out.append({
            "title": (p.get("title") or "").strip(),
            "subreddit": p.get("subreddit", sub),
            "created": datetime.fromtimestamp(created, timezone.utc).date().isoformat(),
            "num_comments": p.get("num_comments", 0),
            "score": p.get("score", 0),
            "permalink": "https://www.reddit.com" + p.get("permalink", ""),
            "is_question": bool(QUESTION_RE.search((p.get("title") or "").strip())),
        })
    return out, remaining


def main():
    ap = argparse.ArgumentParser(description="Read-only Reddit topic research")
    ap.add_argument("query", nargs="?", help="topic to search for")
    ap.add_argument("--subs", default="PPC,smallbusiness,SEO,localseo,web_design",
                    help="comma separated subreddits")
    ap.add_argument("--days", type=int, default=180, help="only posts newer than this")
    ap.add_argument("--limit", type=int, default=100, help="max posts per subreddit")
    ap.add_argument("--questions-only", action="store_true")
    ap.add_argument("--save", help="write markdown to research/ with this slug")
    ap.add_argument("--check", action="store_true", help="verify credentials and exit")
    args = ap.parse_args()

    creds = load_creds()
    token = get_token(creds)

    if args.check:
        data, remaining = api_get(token, "/r/PPC/search",
                                  {"q": "test", "restrict_sr": "true", "limit": 1})
        print(f"Credentials file: {CREDS}")
        print(f"User-Agent:       {USER_AGENT}")
        print("Auth:             OK (application-only, no user credentials held)")
        print(f"Rate limit remaining: {remaining}")
        print("\nReddit connection working.")
        return

    if not args.query:
        ap.error("give a search query, or --check")

    subs = [s.strip() for s in args.subs.split(",") if s.strip()]
    all_posts, skipped = [], []

    print(f'Searching {len(subs)} subreddits for "{args.query}", last {args.days} days\n')
    for sub in subs:
        posts, remaining = search(token, sub, args.query, args.limit, args.days)
        if posts is None:
            skipped.append(sub)
            print(f"  r/{sub:<18} unavailable (private, banned, or does not exist)")
        else:
            qs = sum(1 for p in posts if p["is_question"])
            print(f"  r/{sub:<18} {len(posts):>3} posts, {qs} phrased as questions")
            all_posts.extend(posts)
        time.sleep(SECONDS_BETWEEN_CALLS)

    if args.questions_only:
        all_posts = [p for p in all_posts if p["is_question"]]

    all_posts.sort(key=lambda p: -p["num_comments"])

    print(f"\n{'=' * 78}")
    print(f"{len(all_posts)} posts, sorted by comment count")
    print(f"{'=' * 78}\n")
    for p in all_posts[:40]:
        mark = "Q" if p["is_question"] else " "
        print(f"[{mark}] {p['title'][:88]}")
        print(f"    r/{p['subreddit']}  {p['created']}  {p['num_comments']} comments  "
              f"score {p['score']}")
        print(f"    {p['permalink']}\n")

    if skipped:
        print(f"Skipped (unavailable): {', '.join(skipped)}\n")

    print("REMINDER: Reddit shows what people are confused about, never what is true.")
    print("Every factual claim still needs a primary source. Do not quote or paraphrase")
    print("any individual post in an article, and never identify a user.")

    if args.save:
        RESEARCH.mkdir(parents=True, exist_ok=True)
        path = RESEARCH / f"{datetime.now().date().isoformat()}-reddit-{args.save}.md"
        with open(path, "w") as f:
            f.write(f"# Reddit signal: {args.query}\n\n")
            f.write(f"Collected {datetime.now().date().isoformat()}. "
                    f"Subreddits: {', '.join(subs)}. Window: {args.days} days.\n\n")
            f.write("**This is signal, not evidence.** It shows which questions recur. "
                    "It proves nothing about the answers. Do not quote individual posts "
                    "or identify users in any article.\n\n")
            f.write("| Question or title | Subreddit | Date | Comments |\n")
            f.write("|---|---|---|---|\n")
            for p in all_posts[:60]:
                t = p["title"].replace("|", "\\|")[:110]
                f.write(f"| {t} | r/{p['subreddit']} | {p['created']} | {p['num_comments']} |\n")
        print(f"\nSaved to {path.relative_to(REPO)}")


if __name__ == "__main__":
    main()
