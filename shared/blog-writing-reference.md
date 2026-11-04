# Blog Writing Reference

The complete writing-and-NeuronWriter spec for a Brightbox article, in one place. This consolidates
the authoritative rules from `editorial-standards.md`, `source-validation.md`,
`clients/brightbox/brand-voice.md`, the `create-blog` skill, and `MASTER-WORKFLOW.md`.

Scope is **strictly writing and NeuronWriter**. Images, social, GBP, and publishing live in their own
files (`social-content-standards.md`, `scripts/README-images.md`, `scripts/README-wordpress.md`) and
are intentionally out of scope here. Where those stages touch the delivery package, they are marked
and left to their own docs. If any rule here ever conflicts with the source files, the source files
win and this one gets corrected.

---

## The writing pipeline (approved topic to approved article)

Four hard stops. Do not pass a stop without an explicit response from Archie.

1. **Keyword approval** *(Stop 1)* — recommend a seed keyword with close variants, search intent, a
   cannibalization check against `site-inventory.csv`, and why it fits. Up to three alternatives if
   useful. **No NeuronWriter analysis is created until Archie approves** (it costs a credit). Tracker
   status `Keyword Approval Needed`, then wait.
2. **NeuronWriter analysis** — build the analysis and pull its data (see the NeuronWriter section),
   then build an editorial outline from it plus judgment.
3. **Outline review** *(Stop 2, only if material)* — if the outline differs materially from
   NeuronWriter's, show what changed, why, and the likely optimization effect, then wait. Minor
   differences do not trigger a stop.
4. **Originality gate** — in writing, answer: *what does this give a reader that the current top five
   results do not?* Name at least **three gaps** and commit to **at least two original value
   elements** (Archie's firsthand observation, a real anonymized client situation he supplied, a
   Brightbox checklist or decision framework, a real screenshot, an original diagram, original local
   context, a practical process, a meaningful tradeoff, a case where common advice fails, an
   experience-based recommendation, or legitimately available original data). If it cannot clear the
   gate, stop and propose a different angle, topic, or update.
5. **Interview Archie** *(Stop 3)* — three to five numbered, topic-specific questions, bullet answers
   fine. Aim at a real client situation or repeated question, his process, a common mistake, his
   opinion, a tradeoff or exception, a Fort Wayne consideration, a substantiable result, or an asset
   he can supply. Never ask "do you have anything to add." **Never draft until he answers.** If he
   skips a question, leave that material out, never invent it. Save to
   `clients/brightbox/interviews/YYYY-MM-DD-slug.md`. Status `Interview Needed`.
6. **Source research** — build the full claim ledger before drafting conclusions (see Sourcing).
7. **Draft** — follow the structure and voice rules below. Save to `clients/brightbox/drafts/`.
   Roughly 1,500 words as a target, not a rule.
8. **Optimize** — score in NeuronWriter, then at most three passes (see NeuronWriter).
9. **Originality and editorial QA** — run the originality review and the full QA checklist, recheck
   every external source.
10. **Delivery** *(Stop 4)* — deliver the package, then Archie chooses: approve, request revisions,
    add more personal experience, change CTA, recheck a source, change images, or abandon.
    **Status never goes to `Approved` without his explicit approval.** On revisions: make the change,
    fix related inconsistencies, rescore if substantial, revalidate affected sources, summarize what
    changed. Status `Archie Review Needed`.

---

## NeuronWriter — how it is used

- **Project:** `eea0682a76fd76f0` (the live Brightbox project). Historical queries live in the
  **`Clients`** project `0bdb5139dc86fbe7`. Search both when checking for prior-analysis overlap.
- **Reuse before spending.** Run `list-queries` first and reuse a suitable existing analysis rather
  than burning a credit. Create a new analysis only after Archie approves the keyword in the current
  session.
- **Settings:** engine google.com, language English, country United States, plus geographic
  relevance for local queries.
- **What to pull:** competitors, recommended length, terms and usage ranges, H1/H2/H3
  recommendations, related questions, competitor structures, content-score guidance. Record the
  query ID in the tracker.
- **It is an input, not the authority.** Reject recommendations that are inaccurate, outdated,
  repetitive, irrelevant, unhelpful, inconsistent with intent, or likely to cause keyword stuffing.
  Consolidate if it suggests more than 25 headings. Never copy a competitor's outline.
- **Two tools, not interchangeable:**
  - `evaluate_content` scores the draft and saves nothing. Use it for every scoring pass.
  - `import_content` saves the content into the query editor as a revision. Call it **once, when the
    article is final**, with the clean semantic HTML (h1/h2/h3/p, not the styled `bbx-post` version),
    so the content lives in NeuronWriter and Archie can open it. Import is the last NeuronWriter step
    on every article. If you only evaluate and never import, the query shows no content, which is wrong.
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
  article markup** — WordPress renders the post title as the H1, so a second one duplicates it.
- **TL;DR:** directly after the H1. Three to five concise bullets or one short paragraph. Answers the
  central question, does not tease.
- **Introduction:** a real hook, the reader's problem or decision, at least one verified or defensible
  statistic where one exists (omit it and say so if none is defensible, never insert a weak number),
  a preview of what they will learn, and why it matters to this audience. No generic scene-setting.
- **Table of contents:** lists every H2, matches the final structure exactly. Check it last.
- **Body:** each section answers a real reader question, says why it matters, gives practical
  guidance, includes an example where possible, and carries the author's experience where
  appropriate. Descriptive headings, short paragraphs, lists or tables where they help. Callouts
  available (Quick Tip, Important, Example, Local Consideration, Watch Out, Brightbox Perspective),
  used rarely. Bold conclusions and warnings, never keywords. Avoid repetitive rhetorical questions.
- **Experience and trust:** weave in interview material — what the author commonly sees, how he
  evaluates the problem, mistakes businesses make, tradeoffs, exceptions, local considerations,
  anonymized client examples, a real process or checklist. **Never fabricate experience.**
- **Body CTAs:** two to three contextual, each tied to its section, never identical language.
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

**Link behaviour, standing rule (Archie, July 19, 2026):**

| Link type | Behaviour | Markup |
|---|---|---|
| External | Opens in a new tab | `<a href="..." target="_blank" rel="noopener">` |
| Internal | Stays in the same tab | `<a href="...">` |

`rel="noopener"` is not optional. Do not add `target="_blank"` to internal links. Do not add
`nofollow` to primary sources cited as evidence.

---

## Voice and language

Write like a human. Professional but conversational, clear, direct, and natural, like writing to a
smart friend. Not a press release.

**Sound like:** calm, clear, practical, experienced, direct, helpful, honest about tradeoffs,
understandable to business owners, confident without exaggeration.

**Person:** first person for Archie's genuine experience or opinion — this is the voice that
differentiates the content, so use it where he actually has something to say. Use "we" for Brightbox
processes only when backed by information Archie has provided. Never invent a Brightbox process,
client, project, quote, result, metric, case study, or opinion. An honest gap, flagged, beats a
fabricated claim.

**Never use:** em dashes, the word "actually," generic AI phrasing, "in today's digital landscape,"
"game-changing," "unlock the power of," "revolutionize," "secret hack," fake urgency, unsupported
superlatives, guaranteed ranking or lead claims, overly formal agency language, keyword-stuffed
headings, repetitive rhetorical questions, excessive exclamation points, long paragraphs, anything
that reads from a template.

**Banned words (any form, including plural, past tense, and -ing):** adapt, adhere, amplify,
characterized, cognizant, complementary, complexity, comprehensive, conceptualize, critique, crucial,
cultivate, deep understanding, delve, discern, elevate, elucidate, embarked, emphasize, empower,
encompass, endeavour, enhance, enlightening, esteemed, expertise, explore, facilitate, folks, foster,
groundbreaking, holistic, implications, inherent, insights, integral, intricate, invaluable,
landscape, leverage, multifaceted, nuanced, offerings, paramount, perspectives, peril, pertinent,
pivotal, profound, promote, recognize, relentless, resonate, shed light, significant, synergy,
systemic, tapestry, testament, treasure trove, underpinnings, underscores, unleash, unlock, unravel,
valuable. If a sentence naturally wants one, rewrite the sentence rather than reaching for a synonym
that still reads as filler.

**Formatting:** do not make every list a bolded-lead-in plus colon plus explanation. It reads
AI-generated when it appears in every section. Use it sparingly and vary structure elsewhere: plain
paragraphs, a short list without bold lead-ins, a table, or straight prose.

**Local references:** Fort Wayne and Northeast Indiana mentions must be genuine and add something
real, a real local consideration, market observation, or client situation. Never insert a city name
to hit a keyword. Never produce city-swapped versions of the same article.

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
  with no accessible methodology, Reddit comments used as proof.
- **Claim ledger (one per article, saved with the draft):** claim (exact sentence), draft location,
  source title, publisher, final URL (redirects followed, tracking stripped), published or updated
  date, date checked, primary or secondary, exact support found, qualification needed, validation
  result (Pass, Rewrite Needed, or Reject). **Every claim must reach Pass before delivery.**
- **Claim classification — the wording must match the label:** fact, estimate (described as such),
  opinion (reads as judgment), personal experience (first person, attributed to Archie), correlation
  (never worded as causation), causation (requires evidence), confirmed product feature, limited test
  (described as a test), gradual rollout (described as in progress), rumor (generally should not
  appear). Never let a test, rollout, or observation read as a confirmed update.
- **Recheck before delivery:** sources go stale between drafting and delivery, especially platform
  docs. Re-open every external URL in the ledger right before presenting the package and update the
  date-checked column.
- **Reddit:** permitted as signal, never as evidence. It shows what people are confused about, not
  what is true. Never quote or characterize a user, never use vote counts as data, verify every
  factual idea against a primary source. Its real use is surfacing a question for the interview:
  "this keeps coming up, what do you actually tell people who ask it?" Archie's answer is the content.

**Claims never permitted anywhere:** E-E-A-T as a score or single ranking factor; structured data
guaranteeing rankings or rich results; guaranteed indexing; any guaranteed ranking, traffic, or lead
outcome.

---

## The delivery package

Delivered in this exact order, then stop for Archie's decision. Items 5 and 10 belong to the image
and distribution flows and are covered by their own files, not here.

1. Article summary
2. SEO metadata
3. Final article in semantic HTML
4. Human-readable preview
5. Image brief *(see `scripts/README-images.md`, out of scope for this reference)*
6. Claim and source verification ledger
7. Internal link report
8. NeuronWriter optimization report
9. Technical publishing checklist
10. Social and GBP distribution preview *(see `social-content-standards.md`, out of scope here)*
11. Items requiring Archie's review

---

## Editorial QA checklist (run before delivery)

- [ ] Topic approved by Archie
- [ ] Seed keyword approved by Archie
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
- [ ] No fabricated facts, clients, metrics or quotes
- [ ] No keyword stuffing
- [ ] No broken links
- [ ] Metadata complete
- [ ] Reads naturally start to finish
- [ ] Authorship consistent between byline and markup
- [ ] No unsupported ranking or lead promises
- [ ] No outdated platform claims presented as current

Never use an AI detector to judge quality.
