# Installation

HSJ is content-first. Choose the harness you use and install only the surfaces you need.

## Generic

Keep `AGENTS.md`, then reference or copy selected directories from `skills/`, `agents/`, and `workflows/`.

## Claude Code

Use the project `CLAUDE.md` and `.claude-plugin/plugin.json`. For a project-local setup:

```bash
mkdir -p .claude/skills
cp -R skills/brainstorming skills/writing-plans skills/verification-loop .claude/skills/
```

## Codex

Use `AGENTS.md` and `.codex-plugin/plugin.json`. Keep skill selection explicit.

## Cursor, Gemini, Hermes, OpenClaw, OpenCode

Use the adapter notes in `.cursor/`, `GEMINI.md`, `.hermes/`, `.openclaw/`, and `.opencode/`. These files document placement only. HSJ does not silently change global configuration, hooks, MCP servers, credentials, or permissions.

## Updating

Review changes before updating. Re-run `python3 scripts/validate.py` and the relevant project checks after installation.
