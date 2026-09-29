# HSJ

> **Human judgment. Senior direction. Junior execution.**

[![Validate](https://github.com/smitshivalkar-spectims4567/hsj-agent-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/smitshivalkar-spectims4567/hsj-agent-skills/actions/workflows/validate.yml)

HSJ is a provider-neutral collection of skills, specialist agents, workflows, and quality gates for AI coding tools.

It helps an AI coding agent:

1. Understand an unfamiliar repository.
2. Clarify requirements.
3. Plan before editing.
4. Implement the smallest correct change.
5. Test and review the result.
6. Report what actually happened.

HSJ is intentionally Markdown-first. It does not replace Claude Code, Hermes, Cursor, Codex, or another agent runtime. It gives those tools a disciplined engineering team model.

## Why HSJ exists

Most AI coding agents can write code. The difficult part is making them work like a careful engineering team: understand first, plan before editing, use focused specialists, verify changes, and report uncertainty honestly. HSJ packages those habits as portable Markdown.

## Install

Clone the repository, then copy the skills, agents, or workflows into the AI coding tool you use. HSJ is Markdown-first so it can be adapted without a runtime or vendor lock-in.

```bash
git clone https://github.com/smitshivalkar-spectims4567/hsj-agent-skills.git
```

## MVP

- 10 reusable skills
- 4 specialist roles
- 4 workflows
- Human approval boundaries
- A lightweight validator

Start with the generic files in this repository. Provider adapters will be added only after they are tested.

## Roles

- **Human:** defines intent, approves risky actions, accepts the result.
- **Senior:** explores, clarifies, plans, coordinates, and reviews.
- **Junior:** executes the approved plan, tests changes, and reports results.

## Safety boundary

The agent must pause before destructive operations, production deployments, credential changes, billing changes, authentication changes, irreversible migrations, or external communications.

## Completion report

Every workflow ends with:

```text
Changed:
Tests run:
Tests passed:
Tests not run:
Known risks:
Human approval needed:
```

## Design principles

- **Progressive disclosure:** load only the skills relevant to the task.
- **Bounded specialists:** use a separate agent when focused context or permissions improve reliability.
- **Evidence over confidence:** never claim tests passed unless they ran.
- **Smallest correct change:** reuse existing project patterns before adding abstractions.
- **Human approval:** pause before destructive, irreversible, external, or production actions.

## Status

Early MVP. The system is intentionally small until real projects show which skills deserve expansion.
