# HSJ operating model

## Surfaces

| Surface | Job |
|---|---|
| `AGENTS.md` | shared repository contract |
| `rules/` | always-on safety and quality rules |
| `skills/` | reusable procedures and domain guidance |
| `agents/` | focused roles that select skills and tools |
| `agency/` | optional large specialist roster, lazy-loaded |
| `workflows/` | ordered phases and stop conditions |
| `commands/` | short entry points into workflows |
| `templates/` | bounded handoffs and reports |
| `adapters/` | harness placement and compatibility notes |
| `scripts/` | validation and safe local catalog tools |

## Handoff contract

A handoff must name the sender, receiver, task, current state, relevant files, constraints, acceptance criteria, evidence required, and the next action. Do not pass an entire transcript when a short artifact will do.

## Quality gates

- **Design gate:** intent, scope, acceptance criteria, and risks are visible.
- **Implementation gate:** the diff follows existing patterns and stays within scope.
- **Verification gate:** tests and reviews have exact evidence.
- **Release gate:** unresolved risk and human approval are explicit.

## Specialist selection

Search by capability, inspect the specialist, then load only the minimum needed. Specialist personality is a communication aid, not authority or evidence.
