# Source Validation

A URL returning a successful response is not a validated source. It must support the exact wording
used in the article.

## Source priority

1. Primary documentation from the platform being discussed
2. Original research with accessible methodology
3. Official announcements
4. Government or educational sources
5. Reputable industry studies
6. High quality secondary analysis, only where nothing above exists

## Validation procedure

For every source, in order:

1. Open the page.
2. Confirm it loads.
3. Follow redirects to the end.
4. Use the final canonical URL.
5. Strip unnecessary tracking parameters.
6. Confirm the source supports the exact claim as worded in the draft.
7. Record its publication or updated date.
8. Determine whether it is still current for this subject.
9. Determine whether it is primary or secondary.
10. Recheck it immediately before final delivery.

Step 6 is the one that gets skipped. Do not skip it. If the source supports a weaker claim than the
draft makes, rewrite the draft to match the source, not the other way around.

## Automatic rejection

- 404 pages
- Soft 404 pages
- Redirects that land somewhere unrelated
- Sources that do not support the claim
- Scraper and content mill sites
- Unverifiable statistics
- AI generated summaries with no primary source
- Search snippets used as evidence
- Outdated product documentation presented as current
- Statistics with no accessible methodology
- Reddit comments used as factual proof

## Claim ledger

Build one per article. Save alongside the draft. Required columns:

| Field | Notes |
|---|---|
| Claim | The exact sentence as it appears in the draft |
| Draft location | Section and heading |
| Source title | As published |
| Publisher | Organization |
| Final URL | After redirects, tracking stripped |
| Published or updated | Date from the source |
| Date checked | Date you verified it |
| Primary or secondary | |
| Exact support found | Quote or paraphrase of the supporting passage |
| Qualification needed | Any hedge the draft must carry |
| Validation result | Pass, Rewrite Needed, or Reject |

Every claim must reach Pass before delivery.

## Claim classification

Label each claim internally. The draft's wording must match the label.

- **Fact** — verifiable and verified
- **Estimate** — a modeled or approximate figure, must be described as such
- **Opinion** — the author's judgment, must read as judgment
- **Personal experience** — first person, clearly attributed to the author
- **Correlation** — must not be worded as causation
- **Causation** — requires evidence that establishes it
- **Confirmed product feature** — documented by the platform
- **Limited test** — must be described as a test
- **Gradual rollout** — must be described as in progress
- **Rumor** — generally should not appear at all

Never let a limited test, a rollout in progress or an industry observation read as a confirmed update.

## Recheck before delivery

Sources go stale between drafting and delivery, especially platform documentation. Re-open every
external URL in the ledger immediately before presenting the article package and update the date
checked column.


## Reddit: permitted as signal, never as evidence

**Decision July 19, 2026, made by Archie.**

Reddit's Responsible Builder Policy was read in full. It requires express written approval for
commercial use of Reddit data. The policy is genuinely ambiguous about which framing governs this
case, and the two readings were weighed:

- **Claude's reading:** the Developers section scopes itself to "non-commercial applications," and
  research feeding a lead generating content program for a for profit business falls outside that.
- **Archie's reading, and the decision:** the specific prohibition is on selling, licensing, sharing
  or otherwise commercialising Reddit data. Reading public threads to decide what to write about
  redistributes nothing and resells nothing, so it is non-commercial research.

**Archie's decision governs.** It is his account and his agreement with Reddit. The disagreement is
recorded here rather than buried so that if Reddit ever clarifies its position against this use, the
reasoning is visible and the decision can be revisited rather than re-argued from scratch.

Enforcement risk, if the reading is wrong, is token revocation or app suspension. Reversible.

### Hard constraints on the implementation

`scripts/reddit-research` is built so that policy violations are structurally impossible rather than
merely discouraged:

- Read only. No posting, commenting, voting or messaging. The script uses application only OAuth and
  never holds a Reddit username or password, so it cannot act as a user.
- **Never collects usernames, author fields or comment bodies.** Only public post titles, dates,
  comment counts and permalinks.
- Never attempts to infer anything about any person. The policy's privacy section is absolute and
  the script collects nothing that would make inference possible.
- Rate limited well below the free tier ceiling.

### Editorial rules, unchanged

Reddit shows **what people are confused about**, never what is true.

- Never treat a Reddit post or comment as authoritative evidence.
- Never quote or paraphrase an individual post in an article.
- Never identify or characterise a user.
- Never use vote counts as data.
- Every factual claim sourced from a Reddit thread must be independently verified against a primary
  source before it appears anywhere.

Reddit output belongs in the interview stage, as a prompt for Archie: "this question keeps coming
up, what do you actually tell people who ask it?" His answer is the article content. The thread is
only what surfaced the question.
