---
name: create-blog
description: Take an approved topic through keyword approval, NeuronWriter analysis, the originality gate, an interview with Archie, source research, drafting, optimization and delivery. Use after Archie has selected a topic. Interactive only, never unattended.
---

# Create Blog

Runs from an approved topic to a delivered article package. It contains four hard stops. Do not pass
a stop without an explicit response from Archie.

Read `MASTER-WORKFLOW.md` stages 2 through 10 and `shared/editorial-standards.md` before starting.

## Stop 1. Keyword approval

Recommend a seed keyword. Give close variants, search intent, a cannibalization check against
`site-inventory.csv`, and why this keyword matches the article. Offer up to three alternatives if
useful.

**Do not create a NeuronWriter analysis before Archie approves the keyword.** It costs a credit.

Set tracker status `Keyword Approval Needed`. Wait.

## NeuronWriter

Project `eea0682a76fd76f0`. Run `list-queries` first and reuse a suitable existing analysis rather
than burning a credit. Engine google.com, English, United States, plus geographic relevance for
local queries.

Retrieve competitors, recommended length, terms and usage ranges, heading recommendations, related
questions, competitor structures, and content score guidance. Record the query ID in the tracker.

Build the editorial outline from this plus your own judgment. NeuronWriter is an input, not the
authority. Reject recommendations that are inaccurate, outdated, repetitive, irrelevant, unhelpful,
inconsistent with intent, or likely to cause keyword stuffing. Consolidate if it suggests more than
25 headings. Never copy a competitor's outline.

## Stop 2. Outline review, only if material

If your outline differs materially from the NeuronWriter outline, show what changed, why, and the
likely optimization effect, then set status `Outline Review` and wait. Minor differences do not
require a stop.

## Originality gate

Answer in writing: what will this article contribute that a reader cannot get from the current top
five results? Identify at least three gaps. Commit to at least two original value elements from the
list in `shared/editorial-standards.md`.

If it cannot clear the gate, stop and recommend a different angle, a different topic, an update, or
more input from Archie. Do not draft a piece that has nothing to add.

## Stop 3. Interview Archie

Three to five numbered, topic-specific questions. Tell him bullet answers are fine. Never ask
"do you have anything to add."

Aim at: a real client situation or repeated question, his process, a common mistake, his opinion, a
tradeoff or exception, a Fort Wayne consideration, a substantiable result, an asset he can supply.

Set status `Interview Needed`. **Do not draft until he responds.** If he skips a question, leave
that material out. Never invent an answer.

Save to `clients/brightbox/interviews/YYYY-MM-DD-slug.md`.

## Source research

Follow `shared/source-validation.md` completely. Build the claim ledger. Every claim reaches Pass
before delivery. A 200 response is not validation.

If no defensible statistic exists for the introduction, tell Archie rather than inserting a weak one.

## Draft

Follow `shared/editorial-standards.md` for structure and `clients/brightbox/brand-voice.md` for
voice. Roughly 1,500 words as a target, not a rule. No em dashes. No fabricated experience.

Save to `clients/brightbox/drafts/`.

## Optimize

Score in NeuronWriter, record the initial score, then at most three passes. Add terms only where
they represent a real gap and read naturally. Never exceed a range to raise a score. Stop early when
further optimization would cost quality.

Record initial score, final score, passes, terms added, terms intentionally omitted, and rejected
recommendations with reasons.

**Two different NeuronWriter tools, do not confuse them.** `evaluate-content` scores the draft but
saves nothing. `import-content` saves the content into the query editor as a revision. Use
`evaluate-content` for the scoring passes, then **once the article is final, call `import-content`
with the clean semantic HTML (h1/h2/h3/p, not the bbx-post styled version) so the content is stored
in NeuronWriter and Archie can open it in the editor.** If you only evaluate and never import, the
query shows no content, which is wrong. Import is the last NeuronWriter step, every article.

## QA

Run the originality review and the full editorial QA checklist. Recheck every external source.

## Stop 4. Delivery

Deliver the eleven part package in the order given in `MASTER-WORKFLOW.md` Stage 10.

Set status `Archie Review Needed`. Ask him to choose: approve, request revisions, add more personal
experience, change CTA, recheck a source, change images, or abandon the topic.

**Do not set status `Approved` until he explicitly approves.**

On revisions: make the change, fix related inconsistencies, rescore if substantial, revalidate
affected sources, and summarize what changed.

## After approval

Save the final HTML to `clients/brightbox/approved/`. WordPress is not connected, so output HTML
only and hand off to Archie. Do not publish. Then run `distribute-blog` once the article is live.
