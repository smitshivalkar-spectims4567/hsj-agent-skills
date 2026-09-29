# HSJ for Claude Code

Use `AGENTS.md` for shared project rules. Claude Code can discover skills from `.claude/skills/` or user skill directories.

```bash
mkdir -p .claude/skills
cp -R skills/repository-explorer skills/technical-planner skills/implementer skills/test-engineer .claude/skills/
```

Use `.claude-plugin/plugin.json` for plugin-aware installations. HSJ does not require a plugin or runtime to use the Markdown content.
