---
name: discover-blog-topic
description: Research current Brightbox content opportunities, run due monitoring checks, produce three scored candidates, and stop for Archie's selection. This is the only Brightbox content workflow allowed to run unattended.
---

# Discover Blog Topic

Read `../../../.claude/skills/discover-blog-topic/SKILL.md` completely and follow it as the canonical
workflow. Also follow `../../../AGENTS.md`, `../../../CLAUDE.md`, and `../../../MASTER-WORKFLOW.md`.

The historical `.claude` path is intentional. Do not copy or reinterpret its rules here. For
NeuronWriter overlap checks, call the connected official MCP `list_queries` tool directly for
projects `eea0682a76fd76f0` and `0bdb5139dc86fbe7`. Do not run the legacy
`../../../scripts/neuronwriter` REST client and do not look for a local NeuronWriter API key.
Never call `new_query`, `evaluate_content`, or `import_content` from an unattended discovery task.
