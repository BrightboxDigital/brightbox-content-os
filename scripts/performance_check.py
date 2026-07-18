#!/usr/bin/env python3
"""Pull Search Console and GA4 data for a Brightbox article.

Usage:
    ./scripts/performance-check --check              # verify access, list properties
    ./scripts/performance-check <slug-or-path> [--days 28]
    ./scripts/performance-check should-i-redesign-my-website --days 90
    ./scripts/performance-check --site --days 28     # whole site, not one article

Design rule: this script reports what the APIs return and nothing else. If a call fails
or returns no rows, it says so. It never substitutes an estimate for missing data.
"""

import argparse
import json
import os
import sys
import warnings
from datetime import date, timedelta
from pathlib import Path

warnings.filterwarnings("ignore")  # Python 3.9 EOL notices from google libs

REPO = Path(__file__).resolve().parent.parent
CONFIG = REPO / "clients" / "brightbox" / "analytics-config.json"
KEY = Path.home() / ".config" / "brightbox" / "service-account.json"

SCOPES = [
    "https://www.googleapis.com/auth/webmasters.readonly",
    "https://www.googleapis.com/auth/analytics.readonly",
]


def die(msg, hint=None):
    print(f"\nERROR: {msg}", file=sys.stderr)
    if hint:
        print(f"\n{hint}", file=sys.stderr)
    sys.exit(1)


def load_config():
    if not CONFIG.exists():
        die(f"Config not found at {CONFIG}")
    return json.loads(CONFIG.read_text())


def save_config(cfg):
    CONFIG.write_text(json.dumps(cfg, indent=2) + "\n")


def credentials():
    if not KEY.exists():
        die(
            f"Service account key not found at {KEY}",
            "Download the JSON key from the Google Cloud console, then:\n"
            f"  mkdir -p {KEY.parent} && chmod 700 {KEY.parent}\n"
            f"  mv ~/Downloads/<key>.json {KEY} && chmod 600 {KEY}",
        )
    from google.oauth2 import service_account

    return service_account.Credentials.from_service_account_file(str(KEY), scopes=SCOPES)


# ---------------------------------------------------------------- Search Console


def gsc_client(creds):
    from googleapiclient.discovery import build

    return build("searchconsole", "v1", credentials=creds, cache_discovery=False)


def resolve_gsc_property(svc, cfg):
    """Find which Search Console property this service account can actually read."""
    if cfg.get("gsc_site_url"):
        return cfg["gsc_site_url"]

    try:
        sites = svc.sites().list().execute().get("siteEntry", [])
    except Exception as e:
        die(
            f"Could not list Search Console properties: {e}",
            "The service account probably has not been added to the property yet.\n"
            f"  Search Console > Settings > Users and permissions > Add user\n"
            f"  Email: {cfg['service_account_email']}\n"
            f"  Permission: Full",
        )

    if not sites:
        die(
            "The service account can authenticate but has access to zero Search Console properties.",
            "Add it in Search Console > Settings > Users and permissions:\n"
            f"  {cfg['service_account_email']}  (Full)",
        )

    domain = cfg["site_url"].replace("https://", "").replace("http://", "").rstrip("/")
    for entry in sites:
        url = entry["siteUrl"]
        if domain in url:
            cfg["gsc_site_url"] = url
            save_config(cfg)
            print(f"Detected Search Console property: {url}  (saved to config)")
            return url

    die(
        f"No Search Console property matches {domain}.",
        "Properties this service account can see:\n  "
        + "\n  ".join(f"{s['siteUrl']}  ({s.get('permissionLevel')})" for s in sites),
    )


def gsc_report(svc, site_url, start, end, page_filter=None):
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": ["query"],
        "rowLimit": 25,
    }
    if page_filter:
        body["dimensionFilterGroups"] = [
            {"filters": [{"dimension": "page", "operator": "contains", "expression": page_filter}]}
        ]

    rows = svc.searchanalytics().query(siteUrl=site_url, body=body).execute().get("rows", [])

    totals_body = {k: v for k, v in body.items() if k != "dimensions"}
    totals_body["dimensions"] = []
    totals = svc.searchanalytics().query(siteUrl=site_url, body=totals_body).execute().get("rows", [])

    return rows, (totals[0] if totals else None)


# ---------------------------------------------------------------- GA4


def ga4_report(creds, property_id, start, end, page_filter=None):
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        DateRange,
        Dimension,
        Filter,
        FilterExpression,
        Metric,
        RunReportRequest,
    )

    client = BetaAnalyticsDataClient(credentials=creds)

    # 'conversions' was renamed 'keyEvents'. Try the new name, fall back to the old.
    for conv_metric in ("keyEvents", "conversions"):
        req = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[DateRange(start_date=start.isoformat(), end_date=end.isoformat())],
            dimensions=[Dimension(name="pagePath")],
            metrics=[
                Metric(name="sessions"),
                Metric(name="engagedSessions"),
                Metric(name="screenPageViews"),
                Metric(name=conv_metric),
            ],
            limit=25,
        )
        if page_filter:
            req.dimension_filter = FilterExpression(
                filter=Filter(
                    field_name="pagePath",
                    string_filter=Filter.StringFilter(
                        match_type=Filter.StringFilter.MatchType.CONTAINS, value=page_filter
                    ),
                )
            )
        try:
            return client.run_report(req), conv_metric
        except Exception as e:
            if conv_metric == "keyEvents" and "keyEvents" in str(e):
                continue  # older property, retry with 'conversions'
            raise


def ga4_diagnosis(exc, cfg):
    """Translate a GA4 failure into the specific thing that is wrong.

    The two common failures look nothing alike but are easy to confuse:
    the API not being switched on in the Cloud project, versus the service
    account not having been granted access to the property.
    """
    msg = str(exc)

    if "has not been used in project" in msg or "is disabled" in msg:
        return (
            "The Google Analytics Data API is not enabled on the Cloud project.\n\n"
            "This is a different API from 'Google Analytics API'. The one you need is:\n\n"
            "    Google Analytics Data API   (analyticsdata.googleapis.com)\n\n"
            "Enable it here, then wait a couple of minutes for it to propagate:\n"
            f"    https://console.cloud.google.com/apis/library/analyticsdata.googleapis.com"
            f"?project={cfg['cloud_project_id']}\n\n"
            "Note this is not a permissions problem. Granting property access will not\n"
            "fix it until the API itself is switched on."
        )

    if "PERMISSION_DENIED" in msg or "does not have sufficient permissions" in msg:
        return (
            "The API is enabled but the service account cannot read this property.\n\n"
            "Grant it access:\n"
            "    GA4 > Admin > Property Access Management > add\n"
            f"    {cfg['service_account_email']}\n"
            "    Role: Viewer\n\n"
            f"Also confirm the property ID is right. Config says {cfg['ga4_property_id']}.\n"
            "It must be the numeric Property ID from Admin > Property Settings,\n"
            "not the G- measurement ID."
        )

    if "INVALID_ARGUMENT" in msg and "property" in msg.lower():
        return (
            f"Property {cfg['ga4_property_id']} was rejected as invalid.\n\n"
            "Check Admin > Property Settings for the numeric Property ID.\n"
            "It is a number like 393864986, not a G- measurement ID."
        )

    return f"Unrecognized error:\n\n{msg}"


# ---------------------------------------------------------------- output


def fmt_int(v):
    return f"{int(float(v)):,}"


def print_gsc(rows, totals, label):
    print(f"\n{'=' * 68}\nSEARCH CONSOLE: {label}\n{'=' * 68}")
    if not totals:
        print("\nNo data returned for this period.")
        print("For a new article this is normal. Search Console data lags 2 to 3 days,")
        print("and a page with no impressions returns no rows at all.")
        return
    print(
        f"\n  Impressions {fmt_int(totals['impressions'])}"
        f"   Clicks {fmt_int(totals['clicks'])}"
        f"   CTR {totals['ctr'] * 100:.2f}%"
        f"   Avg position {totals['position']:.1f}"
    )
    if not rows:
        print("\n  No individual queries returned.")
        return
    print(f"\n  {'QUERY':<44}{'IMPR':>7}{'CLICKS':>8}{'POS':>7}")
    print(f"  {'-' * 64}")
    for r in rows[:15]:
        q = r["keys"][0]
        q = q[:41] + "..." if len(q) > 44 else q
        print(f"  {q:<44}{fmt_int(r['impressions']):>7}{fmt_int(r['clicks']):>8}{r['position']:>7.1f}")


def print_ga4(resp, conv_metric, label):
    print(f"\n{'=' * 68}\nGA4: {label}\n{'=' * 68}")
    if not resp.rows:
        print("\nNo sessions recorded for this period.")
        return
    tot = [0.0] * 4
    for row in resp.rows:
        for i in range(4):
            tot[i] += float(row.metric_values[i].value)
    rate = (tot[1] / tot[0] * 100) if tot[0] else 0
    print(
        f"\n  Sessions {fmt_int(tot[0])}"
        f"   Engaged {fmt_int(tot[1])} ({rate:.1f}%)"
        f"   Views {fmt_int(tot[2])}"
        f"   {conv_metric} {fmt_int(tot[3])}"
    )
    if len(resp.rows) > 1:
        print(f"\n  {'PAGE PATH':<50}{'SESSIONS':>9}{'ENGAGED':>9}")
        print(f"  {'-' * 68}")
        for row in sorted(resp.rows, key=lambda r: -float(r.metric_values[0].value))[:15]:
            p = row.dimension_values[0].value
            p = "..." + p[-47:] if len(p) > 50 else p
            print(f"  {p:<50}{fmt_int(row.metric_values[0].value):>9}{fmt_int(row.metric_values[1].value):>9}")


# ---------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description="Search Console and GA4 report for a Brightbox article")
    ap.add_argument("target", nargs="?", help="article slug or URL path")
    ap.add_argument("--days", type=int, default=28, help="lookback window (default 28)")
    ap.add_argument("--site", action="store_true", help="whole site instead of one article")
    ap.add_argument("--check", action="store_true", help="verify access and exit")
    args = ap.parse_args()

    cfg = load_config()
    creds = credentials()

    if args.check:
        print(f"Key file:        {KEY}")
        print(f"Service account: {cfg['service_account_email']}\n")
        svc = gsc_client(creds)
        site = resolve_gsc_property(svc, cfg)
        print(f"Search Console:  OK  ({site})")
        try:
            resp, _ = ga4_report(creds, cfg["ga4_property_id"], date.today() - timedelta(days=7), date.today())
            print(f"GA4:             OK  (property {cfg['ga4_property_id']}, {len(resp.rows)} rows last 7 days)")
        except Exception as e:
            die("GA4 call failed.", ga4_diagnosis(e, cfg))
        print("\nBoth connections working.")
        return

    if not args.target and not args.site:
        ap.error("give an article slug, or --site for the whole site, or --check to test access")

    end = date.today() - timedelta(days=2)  # GSC lags ~2 days
    start = end - timedelta(days=args.days)

    if args.site:
        page_filter, label = None, f"entire site, {args.days} days"
    else:
        page_filter = args.target.strip("/").replace("blog/", "")
        label = f"{page_filter}, {args.days} days"

    print(f"\nWindow: {start} to {end}")

    svc = gsc_client(creds)
    site_url = resolve_gsc_property(svc, cfg)
    try:
        rows, totals = gsc_report(svc, site_url, start, end, page_filter)
        print_gsc(rows, totals, label)
    except Exception as e:
        print(f"\nSearch Console request failed: {e}", file=sys.stderr)

    try:
        resp, conv = ga4_report(creds, cfg["ga4_property_id"], start, end, page_filter)
        print_ga4(resp, conv, label)
    except Exception as e:
        print(f"\nGA4 request failed.\n\n{ga4_diagnosis(e, cfg)}", file=sys.stderr)

    print(f"\n{'=' * 68}")
    print("Reported figures come from the APIs above. Nothing here is estimated.")
    print("Diagnose before acting. See .claude/skills/monitor-blog/SKILL.md")
    print(f"{'=' * 68}\n")


if __name__ == "__main__":
    main()
