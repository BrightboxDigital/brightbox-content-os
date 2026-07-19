#!/usr/bin/env python3
"""Capture a dated performance baseline so change is measurable later.

The point of this script: the moment you observe a number, it becomes a
baseline. Without a recorded starting point, "did this work?" is unanswerable
six months later, and memory is not evidence.

Usage:
    ./scripts/snapshot-baseline --site --days 90 --label "before first PPC article"
    ./scripts/snapshot-baseline --page blog/should-i-redesign-my-website --days 28
    ./scripts/snapshot-baseline --queries "google ads,ppc,ads" --days 90 --label "PPC gap baseline"
    ./scripts/snapshot-baseline --show

Writes to clients/brightbox/performance/baselines.csv (site and page level) and
query-baselines.csv (per query). Appends, never overwrites. Rows are immutable
history: correct a mistake by adding a new row with a note, not by editing.

Every figure comes from the Search Console or GA4 API. Nothing is estimated.
"""

import argparse
import csv
import json
import sys
import warnings
from datetime import date, timedelta
from pathlib import Path

warnings.filterwarnings("ignore")

REPO = Path(__file__).resolve().parent.parent
CONFIG = REPO / "clients" / "brightbox" / "analytics-config.json"
KEY = Path.home() / ".config" / "brightbox" / "service-account.json"
PERF = REPO / "clients" / "brightbox" / "performance"
BASELINES = PERF / "baselines.csv"
QUERY_BASELINES = PERF / "query-baselines.csv"

SCOPES = [
    "https://www.googleapis.com/auth/webmasters.readonly",
    "https://www.googleapis.com/auth/analytics.readonly",
]

BASELINE_FIELDS = [
    "snapshot_date", "label", "scope", "target", "window_days",
    "window_start", "window_end",
    "gsc_impressions", "gsc_clicks", "gsc_ctr_pct", "gsc_avg_position",
    "ga4_sessions", "ga4_engaged_sessions", "ga4_engagement_rate_pct",
    "ga4_page_views", "ga4_key_events",
    "notes",
]

QUERY_FIELDS = [
    "snapshot_date", "label", "query", "window_days", "window_start", "window_end",
    "impressions", "clicks", "ctr_pct", "avg_position", "notes",
]


def die(msg, hint=None):
    print(f"\nERROR: {msg}", file=sys.stderr)
    if hint:
        print(f"\n{hint}", file=sys.stderr)
    sys.exit(1)


def load():
    if not CONFIG.exists():
        die(f"Config not found at {CONFIG}")
    if not KEY.exists():
        die(f"Service account key not found at {KEY}")
    from google.oauth2 import service_account
    cfg = json.loads(CONFIG.read_text())
    creds = service_account.Credentials.from_service_account_file(str(KEY), scopes=SCOPES)
    return cfg, creds


def append_row(path, fields, row):
    PERF.mkdir(parents=True, exist_ok=True)
    new = not path.exists()
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if new:
            w.writeheader()
        w.writerow(row)


# ------------------------------------------------------------------ fetchers


def gsc_totals(creds, cfg, start, end, page_filter=None):
    from googleapiclient.discovery import build
    svc = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    site = cfg.get("gsc_site_url") or cfg["site_url"]
    body = {"startDate": start.isoformat(), "endDate": end.isoformat(), "dimensions": []}
    if page_filter:
        body["dimensionFilterGroups"] = [
            {"filters": [{"dimension": "page", "operator": "contains", "expression": page_filter}]}
        ]
    rows = svc.searchanalytics().query(siteUrl=site, body=body).execute().get("rows", [])
    if not rows:
        return None
    r = rows[0]
    return {
        "impressions": int(r["impressions"]),
        "clicks": int(r["clicks"]),
        "ctr_pct": round(r["ctr"] * 100, 3),
        "position": round(r["position"], 2),
    }


def gsc_queries(creds, cfg, start, end, needles):
    from googleapiclient.discovery import build
    svc = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    site = cfg.get("gsc_site_url") or cfg["site_url"]
    rows = svc.searchanalytics().query(siteUrl=site, body={
        "startDate": start.isoformat(), "endDate": end.isoformat(),
        "dimensions": ["query"], "rowLimit": 1000,
    }).execute().get("rows", [])
    out = []
    for r in rows:
        q = r["keys"][0].lower()
        if any(n.strip().lower() in q for n in needles):
            out.append({
                "query": r["keys"][0],
                "impressions": int(r["impressions"]),
                "clicks": int(r["clicks"]),
                "ctr_pct": round(r["ctr"] * 100, 3),
                "position": round(r["position"], 2),
            })
    return sorted(out, key=lambda x: -x["impressions"])


def ga4_totals(creds, cfg, start, end, page_filter=None):
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        DateRange, Dimension, Filter, FilterExpression, Metric, RunReportRequest,
    )
    client = BetaAnalyticsDataClient(credentials=creds)
    for conv in ("keyEvents", "conversions"):
        req = RunReportRequest(
            property=f"properties/{cfg['ga4_property_id']}",
            date_ranges=[DateRange(start_date=start.isoformat(), end_date=end.isoformat())],
            metrics=[Metric(name="sessions"), Metric(name="engagedSessions"),
                     Metric(name="screenPageViews"), Metric(name=conv)],
            dimensions=[Dimension(name="pagePath")] if page_filter else [],
            limit=2000,
        )
        if page_filter:
            req.dimension_filter = FilterExpression(filter=Filter(
                field_name="pagePath",
                string_filter=Filter.StringFilter(
                    match_type=Filter.StringFilter.MatchType.CONTAINS, value=page_filter),
            ))
        try:
            resp = client.run_report(req)
            break
        except Exception as e:
            if conv == "keyEvents" and "keyEvents" in str(e):
                continue
            raise
    if not resp.rows:
        return None
    tot = [0.0] * 4
    for row in resp.rows:
        for i in range(4):
            tot[i] += float(row.metric_values[i].value)
    return {
        "sessions": int(tot[0]),
        "engaged": int(tot[1]),
        "engagement_rate_pct": round(tot[1] / tot[0] * 100, 2) if tot[0] else 0,
        "views": int(tot[2]),
        "key_events": int(tot[3]),
    }


# ------------------------------------------------------------------ main


def show():
    for path, name in ((BASELINES, "BASELINES"), (QUERY_BASELINES, "QUERY BASELINES")):
        print(f"\n{'=' * 78}\n{name}: {path.relative_to(REPO)}\n{'=' * 78}")
        if not path.exists():
            print("  none recorded yet")
            continue
        rows = list(csv.DictReader(open(path)))
        if not rows:
            print("  none recorded yet")
            continue
        for r in rows:
            if name == "BASELINES":
                print(f"\n  {r['snapshot_date']}  [{r['label']}]  {r['scope']}: {r['target']}  "
                      f"({r['window_days']}d)")
                print(f"    GSC: {r['gsc_impressions']} impr, {r['gsc_clicks']} clicks, "
                      f"{r['gsc_ctr_pct']}% CTR, pos {r['gsc_avg_position']}")
                print(f"    GA4: {r['ga4_sessions']} sessions, {r['ga4_engaged_sessions']} engaged "
                      f"({r['ga4_engagement_rate_pct']}%), {r['ga4_key_events']} key events")
            else:
                print(f"  {r['snapshot_date']}  {r['query'][:44]:<46} "
                      f"{r['impressions']:>6} impr {r['clicks']:>4} clicks  pos {r['avg_position']}")


def main():
    ap = argparse.ArgumentParser(description="Record a dated performance baseline")
    ap.add_argument("--site", action="store_true", help="whole site baseline")
    ap.add_argument("--page", help="single page path or slug")
    ap.add_argument("--queries", help="comma separated substrings to match queries, e.g. 'google ads,ppc'")
    ap.add_argument("--days", type=int, default=90)
    ap.add_argument("--label", default="", help="why this snapshot was taken")
    ap.add_argument("--notes", default="")
    ap.add_argument("--show", action="store_true", help="print everything recorded so far")
    args = ap.parse_args()

    if args.show:
        show()
        return
    if not (args.site or args.page or args.queries):
        ap.error("give --site, --page, or --queries (or --show)")

    cfg, creds = load()
    end = date.today() - timedelta(days=2)  # Search Console lags ~2 days
    start = end - timedelta(days=args.days)
    today = date.today().isoformat()

    print(f"Window: {start} to {end} ({args.days} days)")

    if args.site or args.page:
        target = args.page.strip("/") if args.page else "entire site"
        pf = target if args.page else None
        g = gsc_totals(creds, cfg, start, end, pf) or {}
        a = ga4_totals(creds, cfg, start, end, pf) or {}
        row = {
            "snapshot_date": today, "label": args.label,
            "scope": "page" if args.page else "site", "target": target,
            "window_days": args.days, "window_start": start.isoformat(),
            "window_end": end.isoformat(),
            "gsc_impressions": g.get("impressions", ""), "gsc_clicks": g.get("clicks", ""),
            "gsc_ctr_pct": g.get("ctr_pct", ""), "gsc_avg_position": g.get("position", ""),
            "ga4_sessions": a.get("sessions", ""), "ga4_engaged_sessions": a.get("engaged", ""),
            "ga4_engagement_rate_pct": a.get("engagement_rate_pct", ""),
            "ga4_page_views": a.get("views", ""), "ga4_key_events": a.get("key_events", ""),
            "notes": args.notes,
        }
        append_row(BASELINES, BASELINE_FIELDS, row)
        print(f"\nRecorded baseline: {row['scope']} = {target}")
        print(f"  GSC: {row['gsc_impressions']} impressions, {row['gsc_clicks']} clicks, "
              f"pos {row['gsc_avg_position']}")
        print(f"  GA4: {row['ga4_sessions']} sessions, {row['ga4_key_events']} key events")
        print(f"  -> {BASELINES.relative_to(REPO)}")

    if args.queries:
        needles = args.queries.split(",")
        qs = gsc_queries(creds, cfg, start, end, needles)
        for q in qs:
            append_row(QUERY_BASELINES, QUERY_FIELDS, {
                "snapshot_date": today, "label": args.label, "query": q["query"],
                "window_days": args.days, "window_start": start.isoformat(),
                "window_end": end.isoformat(),
                "impressions": q["impressions"], "clicks": q["clicks"],
                "ctr_pct": q["ctr_pct"], "avg_position": q["position"],
                "notes": args.notes,
            })
        ti = sum(q["impressions"] for q in qs)
        tc = sum(q["clicks"] for q in qs)
        print(f"\nRecorded {len(qs)} query baselines matching {needles}")
        print(f"  totals: {ti} impressions, {tc} clicks")
        if qs:
            worst = max(qs, key=lambda x: x["position"])
            best = min(qs, key=lambda x: x["position"])
            print(f"  best position:  {best['position']}  ({best['query']})")
            print(f"  worst position: {worst['position']}  ({worst['query']})")
        print(f"  -> {QUERY_BASELINES.relative_to(REPO)}")


if __name__ == "__main__":
    main()
