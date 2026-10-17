#!/usr/bin/env python3
"""Safe command-line client for the NEURONwriter Content Writer API.

Read-only commands are available without extra confirmation. Operations that
consume an analysis credit or save a revision require explicit confirmation
flags so an unattended discovery run cannot trigger them accidentally.
"""

import argparse
import json
import os
import stat
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


API_ROOT = "https://app.neuronwriter.com/neuron-api/0.5/writer"
CONFIG = Path.home() / ".config" / "brightbox" / "neuronwriter.json"
KNOWN_PROJECTS = {
    "brightbox": "eea0682a76fd76f0",
    "clients": "0bdb5139dc86fbe7",
}


def die(message, *, code=1):
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(code)


def load_api_key():
    if not CONFIG.is_file():
        die(
            f"NEURONwriter credentials not found at {CONFIG}. "
            "Create the file with mode 600 and JSON: {\"api_key\":\"...\"}. "
            "Never paste the key into chat or commit it."
        )
    try:
        config = json.loads(CONFIG.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        die(f"Cannot read {CONFIG}: {exc}")
    key = config.get("api_key", "").strip()
    if not key:
        die(f"'api_key' is missing from {CONFIG}")
    if os.name != "nt":
        mode = stat.S_IMODE(CONFIG.stat().st_mode)
        if mode & 0o077:
            die(f"{CONFIG} must not be group/world readable; run chmod 600 '{CONFIG}'")
    return key


def request(method, payload=None):
    body = json.dumps(payload or {}).encode("utf-8")
    req = urllib.request.Request(
        f"{API_ROOT}/{method}",
        data=body,
        method="POST",
        headers={
            "X-API-KEY": load_api_key(),
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "BrightboxContentOS/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:800]
        if exc.code in (401, 403):
            die("NEURONwriter rejected the API key or plan access. Check the Neuron API access tab.")
        die(f"NEURONwriter API returned HTTP {exc.code}: {detail}")
    except urllib.error.URLError as exc:
        die(f"Cannot reach NEURONwriter: {exc.reason}")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        die("NEURONwriter returned a non-JSON response")


def print_json(value):
    print(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True))


def project_id(value):
    return KNOWN_PROJECTS.get(value.lower(), value)


def html_payload(args):
    path = Path(args.html_file)
    if not path.is_file():
        die(f"HTML file not found: {path}")
    payload = {"query": args.query, "html": path.read_text(encoding="utf-8")}
    if args.title:
        payload["title"] = args.title
    if args.description:
        payload["description"] = args.description
    return payload


def cmd_check(_args):
    projects = request("list-projects")
    seen = {item.get("project") for item in projects if isinstance(item, dict)}
    print("NEURONwriter: OK")
    for name, identifier in KNOWN_PROJECTS.items():
        state = "available" if identifier in seen else "not visible"
        print(f"  {name}: {identifier} ({state})")


def cmd_list_projects(_args):
    print_json(request("list-projects"))


def cmd_list_queries(args):
    payload = {"project": project_id(args.project)}
    for name in ("status", "keyword", "language", "engine", "source"):
        value = getattr(args, name)
        if value:
            payload[name] = value
    if args.tag:
        payload["tags"] = args.tag
    print_json(request("list-queries", payload))


def cmd_new_query(args):
    if not args.confirm_credit:
        die("new-query consumes one analysis credit; rerun with --confirm-credit after Archie approves the keyword")
    payload = {
        "project": project_id(args.project),
        "keyword": args.keyword,
        "engine": args.engine,
        "language": args.language,
        "competitors_mode": args.competitors_mode,
    }
    print_json(request("new-query", payload))


def cmd_get_query(args):
    print_json(request("get-query", {"query": args.query}))


def cmd_wait_query(args):
    deadline = time.monotonic() + args.timeout
    while True:
        result = request("get-query", {"query": args.query})
        status_value = result.get("status") if isinstance(result, dict) else None
        if status_value in ("ready", "not found"):
            print_json(result)
            return
        if time.monotonic() >= deadline:
            print_json(result)
            die(f"query was not ready after {args.timeout} seconds", code=2)
        time.sleep(args.interval)


def cmd_get_content(args):
    print_json(request("get-content", {"query": args.query}))


def cmd_evaluate(args):
    print_json(request("evaluate-content", html_payload(args)))


def cmd_import(args):
    if not args.confirm_write:
        die("import-content saves a revision; rerun with --confirm-write only after the article is final")
    print_json(request("import-content", html_payload(args)))


def add_html_arguments(parser):
    parser.add_argument("--query", required=True, help="NEURONwriter query ID")
    parser.add_argument("--html-file", required=True, help="Path to clean semantic article HTML")
    parser.add_argument("--title")
    parser.add_argument("--description")


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    check = commands.add_parser("check", help="Verify API access and expected projects")
    check.set_defaults(func=cmd_check)

    list_projects = commands.add_parser("list-projects", help="List projects")
    list_projects.set_defaults(func=cmd_list_projects)

    list_queries = commands.add_parser("list-queries", help="List queries in a project")
    list_queries.add_argument("--project", required=True, help="Project ID, 'brightbox', or 'clients'")
    list_queries.add_argument("--status", choices=("waiting", "in progress", "ready"))
    list_queries.add_argument("--keyword")
    list_queries.add_argument("--language")
    list_queries.add_argument("--engine")
    list_queries.add_argument("--source", choices=("neuron", "neuron-api"))
    list_queries.add_argument("--tag", action="append")
    list_queries.set_defaults(func=cmd_list_queries)

    new_query = commands.add_parser("new-query", help="Create an approved analysis (uses one credit)")
    new_query.add_argument("--project", required=True, help="Project ID, 'brightbox', or 'clients'")
    new_query.add_argument("--keyword", required=True)
    new_query.add_argument("--engine", default="google.com")
    new_query.add_argument("--language", default="English")
    new_query.add_argument("--competitors-mode", choices=("top10", "top30", "top-intent"), default="top-intent")
    new_query.add_argument("--confirm-credit", action="store_true")
    new_query.set_defaults(func=cmd_new_query)

    get_query = commands.add_parser("get-query", help="Retrieve recommendations and status")
    get_query.add_argument("--query", required=True)
    get_query.set_defaults(func=cmd_get_query)

    wait_query = commands.add_parser("wait-query", help="Wait until recommendations are ready")
    wait_query.add_argument("--query", required=True)
    wait_query.add_argument("--interval", type=int, default=10)
    wait_query.add_argument("--timeout", type=int, default=240)
    wait_query.set_defaults(func=cmd_wait_query)

    get_content = commands.add_parser("get-content", help="Retrieve the most recent saved revision")
    get_content.add_argument("--query", required=True)
    get_content.set_defaults(func=cmd_get_content)

    evaluate = commands.add_parser("evaluate-content", help="Score HTML without saving it")
    add_html_arguments(evaluate)
    evaluate.set_defaults(func=cmd_evaluate)

    import_content = commands.add_parser("import-content", help="Save final HTML as a revision")
    add_html_arguments(import_content)
    import_content.add_argument("--confirm-write", action="store_true")
    import_content.set_defaults(func=cmd_import)
    return parser


def main():
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
