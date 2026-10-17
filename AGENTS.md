# Agent instructions (Codex and other agents)

This repository runs Brightbox Digital's human-and-AI content system. The rules are the same for
every agent. They live in files written originally for Claude Code. The file names are historical.
The rules apply to you.

Read before doing anything:

1. `CLAUDE.md`: the non-negotiable rules, connection status and verified URLs. **Master rules file.**
2. `MASTER-WORKFLOW.md`: the full process and every hard stop where Archie must respond.
3. `.claude/skills/<workflow>/SKILL.md`: the four workflows (`discover-blog-topic`, `create-blog`,
   `distribute-blog`, `monitor-blog`).
4. `CODEX-HANDOFF.md`: how the scheduled discovery routine runs, access requirements, the routine
   prompt, and lessons learned.

Codex-native entry points for the four workflows live in `.agents/skills/`. They intentionally route
to the historical `.claude/skills/` files above, which remain the canonical workflow instructions.

The short version:

- Only `discover-blog-topic` (plus the monitoring sweep) may run unattended. Everything else needs
  Archie live.
- Never publish, never create a NeuronWriter analysis before Archie approves topic and keyword, and
  never invent data, clients, quotes or opinions.
- Record baselines with `./scripts/snapshot-baseline` the moment you see a number. Append-only.
- Never put secrets in this repo. Credentials live in `~/.config/brightbox/`.
- Run scripts through their bash wrappers in `./scripts`. They use `.venv/`.
- Use `./scripts/neuronwriter` for NEURONwriter. The unattended routine is read-only; `new-query`
  requires an approved keyword and `--confirm-credit` in an interactive session.
- Commit as `Archie Brady <bradaj01@gmail.com>` and push to `main`.
