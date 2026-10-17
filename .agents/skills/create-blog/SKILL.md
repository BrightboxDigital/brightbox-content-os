---
name: create-blog
description: Run Brightbox's interactive approved-topic workflow through keyword approval, NEURONwriter analysis, interview, drafting, optimization, QA, and delivery. Never use unattended.
---

# Create Blog

Read `../../../.claude/skills/create-blog/SKILL.md` completely and follow it as the canonical
workflow. Also follow `../../../AGENTS.md`, `../../../CLAUDE.md`, `../../../MASTER-WORKFLOW.md`, and
the shared editorial and source-validation standards those files require.

This workflow is interactive. Preserve every approval stop. Use `../../../scripts/neuronwriter` for
NEURONwriter operations and read `../../../scripts/README-neuronwriter.md` before the first API call.
Creating an analysis requires the user's approved seed keyword and `--confirm-credit`. Evaluate with
clean semantic HTML, and use `import-content --confirm-write` exactly once after the article is final.
