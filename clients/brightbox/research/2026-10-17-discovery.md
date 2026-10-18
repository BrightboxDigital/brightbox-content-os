# Discovery Run — 2026-10-17

Manual end-to-end test of the scheduled discovery-and-monitoring routine. The automation remains
paused; this run tests the workflow without changing its schedule or activation state.

## Gate and monitoring sweep

No tracker row has an exact waiting status in a workflow status field, so discovery was allowed to
run. BBX-003 contains stale prose saying interview questions were awaiting Archie, but that article
was approved and published; the prose is not a waiting status and did not block the run.

The only due milestone was BBX-001's 90-day check. It completed and is documented in
`performance/BBX-001-90day-2026-10-17.md`. The article is healthy but low-volume: 12 Search Console
impressions, 0 clicks, average position 7.7, 19 GA4 sessions, and 0 key events. No content change is
recommended.

## Slot selection

The next open calendar slot is cycle 6 (target 2026-10-15), Local SEO and GBP. Its original messaging
idea had been placed on hold because the old in-dashboard Business Profile chat and call history were
retired in July 2024 and no source confirmed that feature had returned.

That conclusion needed refinement. Google's current primary documentation now explicitly says that
eligible, claimed and verified profiles can add an **SMS or WhatsApp contact option**. This is not the
old Google-hosted chat returning; it is a handoff to an external text or WhatsApp channel, and it is
available only for select regions/profiles. The accurate topic is therefore viable if that distinction
is the premise.

## Demand evidence

### Brightbox Search Console

A 90-day site snapshot (2026-07-17 to 2026-10-15) was recorded before conclusions were drawn:

- 47,666 impressions, 89 clicks, 0.19% CTR, average position 8.81.
- 1,231 GA4 sessions, 638 engaged sessions, 4,982 views, and 45 key events.
- Local-demand queries include `local seo fort wayne` (276 impressions, position 2.76),
  `fort wayne local seo` (229, position 3.15), and
  `local seo for home services companies fort wayne in` (41, position 7.46).
- No query containing `verification`, `qr code`, `whatsapp`, or `text messaging` appeared in the
  site's 90-day query set. That is an evidence gap, not a zero-volume claim.

### Semrush, used through the signed-in Chrome browser

| Keyword | U.S. volume | Intent | KD | CPC |
|---|---:|---|---:|---:|
| `google business profile verification` | 1,900 | Informational | 33 | $5.11 |
| `google review qr code` | 1,900 | Commercial | 43 | $2.61 |
| `how to get more google reviews` | 480 | Informational, commercial | 44 | $10.04 |
| `google business profile chat` | 30 | Not classified | n/a | $0.00 |
| `google business profile whatsapp` | 20 | Not classified | n/a | $0.00 |
| `google business profile messaging` | 10 | Not classified | n/a | $0.00 |

Semrush was read in the browser only. No Semrush API, plugin, or MCP path was used.

## NeuronWriter overlap check

Read-only `list_queries` checks were run through the official NeuronWriter MCP for both projects.
The Brightbox project has analyses for the five previously produced topics, including
`google business profile ranking factors`. The Clients project has broad `google business profile`,
`local seo`, and Fort Wayne service-page queries. Neither project has an analysis for Business
Profile verification, review QR codes, or Business Profile SMS/WhatsApp contact options. No new
analysis was created.

BBX-004 remains the main overlap boundary: it explains relevance, distance, prominence, category
accuracy, and review-policy risk. The candidates below must not become another general ranking or
visibility guide.

## Candidate 1 — Recommended

**Working title:** How to Verify a Google Business Profile: A Video Checklist for Service Businesses

- **Category:** Local SEO and GBP
- **Evergreen or timely:** Evergreen with a current procedural hook
- **New or update:** New
- **Proposed primary keyword:** `google business profile verification`
- **Search intent:** Informational with a strong problem-solving and service-hiring path
- **Audience:** Contractors, home-service companies, and other service-area businesses whose profile
  is not verified or whose verification video was rejected
- **Why it matters:** Google chooses the available verification methods; video is recommended when
  offered. Google's current instructions have separate evidence requirements for storefront,
  hybrid, and service-area businesses. Service-area businesses may need to show nearby location
  identifiers, work tools/equipment, and proof of management without publicly displaying a home
  address.
- **Original value:** Archie's real preparation checklist, the mistakes he has seen on client
  verification attempts, and a contractor-specific shot list. Those details must come from the
  interview; they must not be inferred.
- **Internal support:** `/google-business-profile-optimization/`, `/locations/fort-wayne/`, and a
  contextual link from BBX-004
- **Cannibalization:** Low if the article stays on verification evidence and rejected-video recovery.
  BBX-004 remains the ranking/visibility guide.

| Category | Score | Why |
|---|---:|---|
| Brightbox service relevance | 5 | Directly supports GBP setup and optimization work |
| Fort Wayne / local relevance | 4 | Strong fit for the local contractor audience, though the procedure is national |
| Evidence of current interest | 5 | Semrush: 1,900 U.S. searches/month |
| Freshness / timeliness | 3 | Current procedure, but not presented as a newly launched feature |
| Archie's firsthand contribution | 4 | Real client verification experience can make the checklist defensible |
| Organic ranking opportunity | 4 | KD 33 and a narrower service-business framing than generic help pages |
| Conversion potential | 4 | A rejected or stalled verification is a direct need for GBP help |
| **Total** | **29/35** | Pass |

**Primary sources:**
[Verify your business on Google](https://support.google.com/business/answer/7107242?hl=en-en) and
[Verify your business with a video recording](https://support.google.com/business/answer/14271705?hl=en).

---

## Candidate 2

**Working title:** Google Review QR Codes: A Safe Review-Request System for Service Businesses

- **Category:** Local SEO and GBP
- **Evergreen or timely:** Evergreen with a current native-feature hook
- **New or update:** New
- **Proposed primary keyword:** `google review qr code`
- **Search intent:** Commercial and how-to
- **Audience:** Local businesses and field-service teams that need a repeatable way to ask genuine
  customers for reviews
- **Why it matters:** Google now documents a native desktop-generated review QR code and suggests
  placing it in receipts, thank-you emails, and post-chat follow-ups. Incentives and selective
  positive-review solicitation remain prohibited.
- **Original value:** A practical request sequence for technicians and office staff, with Archie's
  real timing and follow-up recommendations. The article would show where the QR code belongs and
  where it creates policy or customer-experience risk.
- **Internal support:** `/google-business-profile-optimization/`, BBX-004's policy section, and the
  contact/CRM service path where relevant
- **Cannibalization:** Moderate but manageable. BBX-004 owns ranking factors and the policy summary;
  this article must own the operational review-request workflow and link back for deeper policy
  context.

| Category | Score | Why |
|---|---:|---|
| Brightbox service relevance | 4 | Strong GBP optimization and reputation workflow fit |
| Fort Wayne / local relevance | 4 | Directly useful to local and service-area businesses |
| Evidence of current interest | 5 | Semrush: 1,900 searches/month for the primary term; 480 for the broader review-acquisition term |
| Freshness / timeliness | 3 | Google's native QR-code workflow is current; no unsupported launch date claimed |
| Archie's firsthand contribution | 4 | Real request timing and technician/office workflows can differentiate it |
| Organic ranking opportunity | 3 | KD 43; useful but competitive |
| Conversion potential | 4 | Readers need an implemented review system, not just information |
| **Total** | **27/35** | Pass |

**Primary sources:**
[Create a Google link or QR code to request reviews](https://support.google.com/business/answer/16816815?hl=en)
and [Tips to get more reviews](https://support.google.com/business/answer/3474122?hl=en-en).

---

## Candidate 3

**Working title:** Google Business Profile Chat Did Not Come Back: How SMS and WhatsApp Contact Options Work

- **Category:** Local SEO and GBP
- **Evergreen or timely:** Timely clarification
- **New or update:** New; accurate reframe of calendar cycle 6
- **Proposed primary keyword:** `google business profile chat`
- **Search intent:** Informational and setup-oriented
- **Audience:** Local businesses that remember the retired Google chat feature or want customers to
  text them directly from Search or Maps
- **Why it matters:** Google-hosted chat and call history remain retired. Google's current help page
  separately allows eligible profiles in select regions to add an SMS number or WhatsApp click-to-chat
  URL. If both are added, Google says only the text-message option is shown.
- **Original value:** Confirm whether Brightbox's own profile currently has the option, document the
  real setup screen, and explain where those messages land operationally. This is a required
  pre-draft check, not an assumed fact.
- **Internal support:** `/google-business-profile-optimization/`, `/contact/`, and potentially a
  GHL workflow if Archie confirms how replies are handled
- **Cannibalization:** None with BBX-004 if this stays on contact-channel setup and workflow.

| Category | Score | Why |
|---|---:|---|
| Brightbox service relevance | 4 | Supports GBP management and lead-response setup |
| Fort Wayne / local relevance | 4 | Direct local lead-contact use case |
| Evidence of current interest | 2 | Exact Semrush demand is only 10–30 searches/month; no Brightbox GSC signal |
| Freshness / timeliness | 4 | Corrects a live product-availability misconception with current Google documentation |
| Archie's firsthand contribution | 5 | A real Brightbox-profile availability test and message-handling workflow are the article |
| Organic ranking opportunity | 4 | Low measured demand, but also little focused competition for the precise distinction |
| Conversion potential | 4 | Direct connection between discovery and a customer contacting the business |
| **Total** | **27/35** | Pass |

**Primary sources:**
[Chat with customers from your Business Profile](https://support.google.com/business/answer/15013580?hl=en-419)
and [Changes to Business Profile chat and call history](https://support.google.com/business/answer/14919056?hl=en).

## Considered and rejected this run

- `google business profile optimization checklist` (210 volume, KD 18): too close to BBX-004 and the
  GBP service page despite attractive metrics.
- `google business profile audit` (210 volume, KD 23): same overlap problem; it would repeat the
  ranking-factors article's practical audit framing.
- `why is my business not showing up on google maps` (140 volume, KD 28): BBX-004 already owns this
  intent explicitly.
- `google business profile categories` (140 volume, KD 31): BBX-004 already uses category accuracy
  and a real category-mistake example as a core section.
- Broad `local seo for service area businesses` (480 volume, KD 34): strong demand, but cycle 8 is
  already reserved to consolidate the two overlapping local-SEO articles before adding another
  broad local-SEO URL.

## Recommendation and stop point

**Recommend Candidate 1: the contractor-focused Business Profile video-verification guide.** It has
the best combination of measured demand, achievable difficulty, service fit, a real urgent problem,
and room for firsthand expertise without repeating BBX-004.

**Topic Approval Needed.** Choose Candidate 1, 2, or 3, ask for different ideas, or choose an update
instead. No NeuronWriter analysis, outline, interview, draft, WordPress action, or GHL action has been
started.

## Routine-test note

The test exposed and fixed a reporting bug in `scripts/performance_check.py`: site-wide GA4 totals
were being calculated by summing page-path rows, which double-counted sessions. The script now uses
a separate dimensionless totals request. Its 90-day output matches the baseline snapshot exactly:
1,231 sessions, 638 engaged sessions, 4,982 views, and 45 key events.
