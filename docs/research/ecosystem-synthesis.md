# HSJ ecosystem synthesis

HSJ is a portable operating layer for coding agents: reusable skills, focused agent roles, workflows, handoffs, adapter surfaces, and verification. It is not a model, IDE, or autonomous runtime.

## What the reference projects taught us

- **ECC:** the repository must have a real operating surface: rules, skills, agents, commands, adapters, hooks, MCP boundaries, tests, and install documentation. Skills are the durable source; commands are entry points.
- **Superpowers:** the agent should not jump from request to code. Brainstorming, design approval, planning, TDD, implementation, review, and verification are explicit gates. The process must be composable and usable across harnesses.
- **Agency Agents:** a large roster is easier to use when organized by divisions and each specialist has identity, mission, critical rules, deliverables, workflow, communication style, and success metrics. A catalog should lazy-load one specialist rather than preload everything.
- **Wshobson Agents:** packages and evaluations make a large collection maintainable. A specialist needs a narrow description, tool boundary, and a testable purpose.
- **Anthropic / Agent Skills:** `SKILL.md` plus frontmatter is the portable unit. Supporting references and scripts belong beside the skill. Discovery metadata should stay small.
- **Vercel Skills / OpenSkills:** installation and discovery are separate from skill content. Scope, source, target harness, and updates must be explicit.
- **Microsoft / OpenAI / OpenClaw:** native adapter surfaces and validation are part of the product, but compatibility claims need to be honest.

## HSJ product boundary

The HSJ repository combines the useful parts without copying a runtime:

```text
rules -> skills -> agents -> workflows -> handoffs -> verification
                    ^                         |
                    +------ adapters --------+
```

The user chooses the harness. HSJ supplies a focused operating method and specialist content. Human approval remains required for irreversible or externally consequential actions.

## Planned execution model

1. Discover the repository and task.
2. Classify the work as spike, bounded, or architectural.
3. Clarify intent and acceptance criteria.
4. Present the smallest design appropriate to the classification.
5. Stop for approval at the required gate.
6. Write a plan and assign bounded specialists.
7. Implement with tests.
8. Review from a fresh context.
9. Run security and release gates.
10. Return receipts, not confidence.

## Deliberate simplification

HSJ does not import third-party hooks, MCP servers, installers, or global configuration automatically. Those surfaces can execute code or change permissions. They will be added only as separately tested adapters.
