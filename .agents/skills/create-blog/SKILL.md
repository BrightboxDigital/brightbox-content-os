---
name: create-blog
description: Run Brightbox's interactive approved-topic workflow through keyword approval, NEURONwriter analysis, interview, drafting, optimization, QA, and delivery. Never use unattended.
---

# Create Blog

Read `../../../.claude/skills/create-blog/SKILL.md` completely and follow it as the canonical
workflow. Also follow `../../../AGENTS.md`, `../../../CLAUDE.md`, `../../../MASTER-WORKFLOW.md`, and
the shared editorial and source-validation standards those files require.

This workflow is interactive. Preserve every approval stop. Use the connected official NeuronWriter
MCP tools directly. Do not run the legacy `../../../scripts/neuronwriter` REST client and do not
look for a local NeuronWriter API key. Creating an analysis with MCP `new_query` requires the user's
approved seed keyword in the current session. Evaluate clean semantic HTML with `evaluate_content`,
and call `import_content` exactly once after the article is final.
