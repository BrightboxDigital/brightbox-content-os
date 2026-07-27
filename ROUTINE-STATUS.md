# Scheduled Routines: active status

Set up July 20, 2026 as **local scheduled tasks** (they run on Archie's Mac when the app is open,
or on next launch if it was closed). Local, not cloud, because discovery and monitoring need the
Google service-account key at `~/.config/brightbox/service-account.json`, which a cloud routine
cannot reach.

## 1. Content discovery + monitoring sweep

- **Task id:** `brightbox-content-discovery`
- **Schedule:** 1st and 15th of each month, 9:00 AM (America/Indiana/Indianapolis)
- **Auto-runs** on that schedule. Also runnable any time via "Run now" in the Scheduled panel.
- **What it does each run:**
  1. Checks whether any article is waiting on Archie. If so, reports the exact next action and does
     not start new work.
  2. Monitoring sweep: for every published article, runs any 7 / 28 / 90 day check that is newly
     due, compared against its recorded baseline. Never prescribes adding words or keywords.
  3. If nothing is waiting, runs discovery: last 30 to 90 days of primary-source research plus the
     site's own Search Console demand, then three scored candidates.
  4. Saves the report, sets the tracker to `Topic Approval Needed`, commits and pushes to `main`.
  5. Stops at the topic-selection gate for Archie.
  6. **Sends Archie a push notification (added 2026-07-27)** summarizing what happened, every run,
     including runs where nothing was due. This is how he learns the sweep ran without checking the
     tracker manually. Set via a Step 6 in the task's own SKILL.md, not the scheduler's built-in
     `notifyOnCompletion` flag, because that flag can only be set from a regular interactive
     session, not from within a scheduled-task run.
- **Never** writes an article, creates a NeuronWriter analysis, or publishes anything.

**Timing caveat:** the 7/28/90 day checks are relative to each article's own publish date, but the
sweep only runs twice a month. A milestone can be "newly due" for up to roughly two weeks before the
next sweep catches it. Example: BBX-001 published 2026-07-19, so its 28-day mark is 2026-08-16. The
sweep on 2026-08-15 is one day too early to catch it; the next one is 2026-09-01, so the 28-day
check would actually run 16 days late. This is accepted as fine for now since these reviews are not
time-critical to the day. If tighter timing matters later, increase the cron frequency (e.g. weekly:
`0 9 * * 1`) rather than changing the due-date logic.

## 2. BBX-001 seven-day check

- **Task id:** `bbx-001-7day-check`
- **One-time:** July 26, 2026, 9:00 AM. Auto-disables after it runs.
- Superseded going forward by the monitoring sweep inside routine 1, which covers all articles.

## First-run note

The first time each task runs it may pause on a permission prompt for any tool not already on the
allowlist. To avoid that, open the Scheduled panel and click **Run now** once for
`brightbox-content-discovery`; approvals are stored and reused on later runs.

## If the app is closed at run time

The task runs on next launch instead of being skipped. For a twice-monthly job this is fine. If a
run is missed entirely, trigger it manually with Run now.

## Turning it off

Disable or delete either task from the Scheduled panel. Nothing else depends on them running.
