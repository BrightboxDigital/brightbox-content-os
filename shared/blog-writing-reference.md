# Blog Writing Reference (shared template)

The complete writing-and-NeuronWriter spec for one article, in one place, written to apply to **any
client** this system runs. It consolidates the universal rules from `editorial-standards.md`,
`source-validation.md`, and `MASTER-WORKFLOW.md`, and points to each client's own files for the
values that differ between clients.

**Scope** is strictly writing and NeuronWriter. Images, social, GBP, and publishing live in their own
files and are intentionally out of scope here.

**Tool-neutral.** This describes the method, not who performs it. Any assistant (Claude, Codex, or
another) follows the same steps and the same stops. Where it says "the assistant," read it as whatever
tool is doing the work.

**Precedence.** If anything here ever conflicts with the source files above, those win and this one
gets corrected. For anything marked per-client below, the client's own file is the authority.

---

## Per-client values

Nothing client-specific is hardcoded in this file. Each client defines the following in their own
`clients/<client>/` folder, and this reference points to them by role rather than naming one client.
Set these up once per client, and the rest of this document applies unchanged.

| Value | Where it lives | Notes |
|---|---|---|
| **Voice and banned words** | `clients/<client>/brand-voice.md` | The authority for tone, person, formatting habits, and the client's banned-word list. Do not duplicate it here or guess it. |
| **Author and approver** | `clients/<client>/client-profile.md` | The named human whose byline the article carries and who must approve each stop. Referred to below as "the author" and "the approver." |
| **Services and CTA options** | `clients/<client>/client-profile.md` | The real services a body CTA can point to, and the pages behind them. |
| **Local market** | `clients/<client>/client-profile.md` | The client's genuine geography for local references, if any. |
| **NeuronWriter project** | `clients/<client>/client-profile.md` or the client's connection notes | The project ID for new analyses, plus any legacy or historical project to search for overlap. |
| **NeuronWriter locale** | `clients/<client>/client-profile.md` | Engine, language, and country for analyses. Defaults below are a starting point, not a given. |
| **Cannibalization inventory** | `clients/<client>/site-inventory.csv` | Existing pages to check a new keyword and new internal links against. |
| **Working folders** | `clients/<client>/interviews/`, `/drafts/`, `/approved/` | Where interview notes, drafts, and approved HTML are saved. |

The rest of this file uses `<client>` and these role names in place of any one client's specifics.

---

## The writing pipeline (approved topic to approved article)

Four hard stops. Do not pass a stop without an explicit response from the approver.

1. **Keyword approval** *(Stop 1)* — recommend a seed keyword with close variants, search intent, a
   cannibalization check against the client's `site-inventory.csv`, and why it fits. Up to three
   alternatives if useful. **No NeuronWriter analysis is created until the approver approves** (it
   costs a credit). Tracker status `Keyword Approval Needed`, then wait.
2. **NeuronWriter analysis** — build the analysis and pull its data (see the NeuronWriter section),
   then build an editorial outline from it plus judgment.
3. **Outline review** *(Stop 2, only if material)* — if the outline differs materially from
   NeuronWriter's, show what changed, why, and the likely optimization effect, then wait. Minor
   differences do not trigger a stop.
4. **Originality gate** — in writing, answer: *what does this give a reader that the current top five
   results do not?* Name at least **three gaps** and commit to **at least two original value
   elements** (the author's firsthand observation, a real anonymized client situation the author
   supplied, a client checklist or decision framework, a real screenshot, an original diagram,
   original local context, a practical process, a meaningful tradeoff, a case where common advice
   fails, an experience-based recommendation, or legitimately available original data). If it cannot
   clear the gate, stop and propose a different angle, topic, or update.
5. **Interview the author** *(Stop 3)* — three to five numbered, topic-specific questions, bullet
   answers fine. Aim at a real client situation or repeated question, the author's process, a common
   mistake, the author's opinion, a tradeoff or exception, a local consideration, a substantiable
   result, or an asset the author can supply. Never ask "do you have anything to add." **Never draft
   until the author answers.** If a question is skipped, leave that material out, never invent it.
   Save to `clients/<client>/interviews/YYYY-MM-DD-slug.md`. Status `Interview Needed`.
6. **Source research** — build the full claim ledger before drafting conclusions (see Sourcing).
7. **Draft** — follow the structure below and the client's `brand-voice.md`. Save to
   `clients/<client>/drafts/`. Roughly 1,500 words as a default target, not a rule; intent and
   usefulness decide.
8. **Optimize** — score in NeuronWriter, then at most three passes (see NeuronWriter).
9. **Originality and editorial QA** — run the originality review and the full QA checklist, recheck
   every external source.
10. **Delivery** *(Stop 4)* — deliver the package, then the approver chooses: approve, request
    revisions, add more personal experience, change CTA, recheck a source, change images, or abandon.
    **Status never goes to `Approved` without the approver's explicit approval.** On revisions: make
    the change, fix related inconsistencies, rescore if substantial, revalidate affected sources,
    summarize what changed. Status `Review Needed`.

---

## NeuronWriter — how it is used

- **Project:** use the client's NeuronWriter project, recorded in the client profile. If the client
  has a separate legacy or historical project, search both when checking for prior-analysis overlap.
- **Reuse before spending.** Run `list-queries` first and reuse a suitable existing analysis rather
  than burning a credit. Create a new analysis only after the approver approves the keyword in the
  current session.
- **Settings:** set engine, language, and country from the client profile, plus geographic relevance
  for local queries. A common default is google.com, English, United States, but confirm it against
  the client's actual target market rather than assuming it.
- **What to pull:** competitors, recommended length, terms and usage ranges, H1/H2/H3
  recommendations, related questions, competitor structures, content-score guidance. Record the
  query ID in the tracker.
- **It is an input, not the authority.** Reject recommendations that are inaccurate, outdated,
  repetitive, irrelevant, unhelpful, inconsistent with intent, or likely to cause keyword stuffing.
  Consolidate if it suggests more than 25 headings. Never copy a competitor's outline.
- **Two tools, not interchangeable:**
  - `evaluate_content` scores the draft and saves nothing. Use it for every scoring pass.
  - `import_content` saves the content into the query editor as a revision. Call it **once, when the
    article is final**, with the clean semantic HTML (h1/h2/h3/p, not the client's styled template
    version), so the content lives in NeuronWriter and the author can open it. Import is the last
    NeuronWriter step on every article. If you only evaluate and never import, the query shows no
    content, which is wrong.
- **Optimization discipline:** record the initial score, then a maximum of **three passes**. Add a
  term only where it is a real content gap and reads naturally. Never exceed a usage range to raise a
  score, never add an irrelevant section, stop early when more optimization would cost quality.
  Record: initial score, final score, passes completed, terms added, terms intentionally omitted,
  recommendations rejected and why. Do not chase a perfect score.

---

## Required article structure

- **SEO metadata block:** SEO title (around 50 to 60 characters), meta description (around 140 to
  155), suggested slug (no year unless essential), primary keyword, secondary topics, search intent,
  content category, suggested excerpt, author, publication-date placeholder, updated-date
  placeholder, canonical placeholder. Never make a title awkward to hit a count.
- **H1:** exactly one, accurate, carries the primary topic naturally. **Never put an H1 in the
  article markup** when the CMS renders the post title as the H1, or the page gets two.
- **TL;DR:** directly after the H1. Three to five concise bullets or one short paragraph. Answers the
  central question, does not tease.
- **Introduction:** a real hook, the reader's problem or decision, at least one verified or defensible
  statistic where one exists (omit it and say so if none is defensible, never insert a weak number),
  a preview of what they will learn, and why it matters to this audience. No generic scene-setting.
- **Table of contents:** lists every H2, matches the final structure exactly. Check it last.
- **Body:** each section answers a real reader question, says why it matters, gives practical
  guidance, includes an example where possible, and carries the author's experience where
  appropriate. Descriptive headings, short paragraphs, lists or tables where they help. Use callouts
  rarely. Bold conclusions and warnings, never keywords. Avoid repetitive rhetorical questions.
- **Experience and trust:** weave in interview material — what the author commonly sees, how they
  evaluate the problem, mistakes businesses make, tradeoffs, exceptions, local considerations,
  anonymized client examples, a real process or checklist. **Never fabricate experience.**
- **Body CTAs:** two to three contextual, each tied to its section, never identical language. Point
  them at the client's real services and pages from the client profile.
- **Internal links:** three to five, every destination validated, natural descriptive anchor text,
  link to the most specific relevant page, do not repeat the same URL, **same tab**. Also check
  whether existing pages should link into the new article.
- **External links:** three to five authoritative, each passing claim-level validation, placed next
  to the claim it supports, primary sources preferred, **new tab** with `rel="noopener"`. Never imply
  a source supports more than it does. No `nofollow` on cited primary sources.
- **FAQ:** roughly four to seven, only where genuinely useful, concise but substantive. **No FAQPage
  schema.** No dumping unused keywords.
- **Conclusion:** answers the central question, reinforces the recommendation with nuance,
  transitions into the final CTA.
- **Key takeaways:** three to five specific ones. "SEO is important" is not a takeaway.
- **Main CTA:** ends the article, links to the most relevant service or contact page.

**HTML output rules:** one H1, logical H2/H3 hierarchy, semantic paragraphs, lists, tables, and
blockquotes where useful, accessible link text. No inline CSS, no scripts, no invented image URLs,
no schema in the body, no unnecessary wrappers, **no em dashes**.

**Link behaviour (house default, a client profile may override):**

| Link type | Behaviour | Markup |
|---|---|---|
| External | Opens in a new tab | `<a href="..." target="_blank" rel="noopener">` |
| Internal | Stays in the same tab | `<a href="...">` |

`rel="noopener"` is not optional. Do not add `target="_blank"` to internal links. Do not add
`nofollow` to primary sources cited as evidence.

---

## Voice and language

**Voice is per-client.** The authority is the client's `clients/<client>/brand-voice.md`: tone,
person (first person vs "we"), formatting habits to avoid, and the client's own banned-word list.
Read it before drafting and follow it exactly. Do not copy one client's voice rules into another, and
do not infer a banned-word list that a client has not written down.

The following are house defaults that apply across clients unless a client's `brand-voice.md` says
otherwise:

- Write like a human. Clear, direct, natural. Not a press release.
- **No em dashes** anywhere in body text.
- No generic AI phrasing, no fake urgency, no unsupported superlatives, no guaranteed ranking or lead
  claims, no keyword-stuffed headings, no excessive exclamation points, no long paragraphs, nothing
  that reads from a template.
- Do not make every list a bolded-lead-in plus colon plus explanation. It reads AI-generated when it
  appears in every section. Use it sparingly and vary structure.
- **Never invent** a client process, customer, project, quote, result, metric, case study, or
  opinion. An honest gap, flagged for the author, beats a fabricated claim.
- Local references must be genuine and add something real. Never insert a place name to hit a
  keyword. Never produce location-swapped versions of the same article.

---

## Sourcing and claims

- **A 200 response is not validation.** A source must support the exact claim as worded.
- **Source priority:** the platform's primary docs, then original research with accessible
  methodology, official announcements, government or educational sources, reputable industry studies,
  and high-quality secondary analysis only where nothing above exists.
- **Per-source procedure:** open it, confirm it loads, follow redirects to the end, use the final
  canonical URL, strip tracking params, **confirm it supports the exact claim** (the step that gets
  skipped, do not skip it), record its date, judge whether it is current, mark primary vs secondary,
  and **recheck immediately before delivery**. If the source supports a weaker claim than the draft,
  rewrite the draft to match the source.
- **Automatic rejection:** 404s and soft-404s, redirects landing somewhere unrelated, sources that do
  not support the claim, scraper and content-mill sites, unverifiable statistics, AI summaries with
  no primary source, search snippets used as evidence, outdated docs presented as current, statistics
  with no accessible methodology, forum or social comments used as proof.
- **Claim ledger (one per article, saved with the draft):** claim (exact sentence), draft location,
  source title, publisher, final URL (redirects followed, tracking stripped), published or updated
  date, date checked, primary or secondary, exact support found, qualification needed, validation
  result (Pass, Rewrite Needed, or Reject). **Every claim must reach Pass before delivery.**
- **Claim classification — the wording must match the label:** fact, estimate (described as such),
  opinion (reads as judgment), personal experience (first person, attributed to the author),
  correlation (never worded as causation), causation (requires evidence), confirmed product feature,
  limited test (described as a test), gradual rollout (described as in progress), rumor (generally
  should not appear). Never let a test, rollout, or observation read as a confirmed update.
- **Recheck before delivery:** sources go stale between drafting and delivery, especially platform
  docs. Re-open every external URL in the ledger right before presenting the package and update the
  date-checked column.
- **Forums and social (e.g. Reddit):** permitted as signal, never as evidence. They show what people
  are confused about, not what is true. Never quote or characterize a user, never use vote counts as
  data, verify every factual idea against a primary source. The real use is surfacing a question for
  the interview: "this keeps coming up, what do you actually tell people who ask it?" The author's
  answer is the content.

**Claims never permitted anywhere:** E-E-A-T as a score or single ranking factor; structured data
guaranteeing rankings or rich results; guaranteed indexing; any guaranteed ranking, traffic, or lead
outcome.

---

## The delivery package

Delivered in this exact order, then stop for the approver's decision. Items 5 and 10 belong to the
image and distribution workflows and are covered by their own files, not here.

1. Article summary
2. SEO metadata
3. Final article in semantic HTML
4. Human-readable preview
5. Image brief *(image workflow, out of scope for this reference)*
6. Claim and source verification ledger
7. Internal link report
8. NeuronWriter optimization report
9. Technical publishing checklist
10. Social and distribution preview *(distribution workflow, out of scope here)*
11. Items requiring the approver's review

---

## Editorial QA checklist (run before delivery)

- [ ] Topic approved by the approver
- [ ] Seed keyword approved by the approver
- [ ] Interview completed, answers accurately represented
- [ ] Search intent answered
- [ ] Originality gate satisfied, two or more original value elements present
- [ ] Exactly one H1
- [ ] TL;DR directly follows H1 and answers the central question
- [ ] Introduction carries a defensible statistic, or the omission is explained
- [ ] Table of contents matches final H2s
- [ ] Outline followed
- [ ] Two to three contextual CTAs
- [ ] Three to five internal links, all validated
- [ ] Three to five external links, all validated
- [ ] Claim ledger complete
- [ ] FAQs genuinely useful
- [ ] No FAQPage schema
- [ ] Conclusion present
- [ ] Three to five specific key takeaways
- [ ] Main CTA present
- [ ] No em dashes
- [ ] Client voice and banned-word rules from brand-voice.md followed
- [ ] No fabricated facts, customers, metrics or quotes
- [ ] No keyword stuffing
- [ ] No broken links
- [ ] Metadata complete
- [ ] Reads naturally start to finish
- [ ] Authorship consistent between byline and markup
- [ ] No unsupported ranking or lead promises
- [ ] No outdated platform claims presented as current

Never use an AI detector to judge quality.
