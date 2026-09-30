---
name: brainstorming
version: 0.3.0
description: Turn an idea into a bounded design before implementation; use for new features, behavior changes, and creative work.
---
# Brainstorming

Use this before implementation when intent, scope, or design is not already clear.

## Classify

- **Spike:** answer a feasibility question; build only throwaway probes.
- **Bounded:** a small change to an existing flow; present a short design and wait for approval.
- **Architectural:** a new project, subsystem, interface, or cross-cutting change; write a design artifact and implementation plan.

When uncertain, use the heavier path.

## Procedure

1. Inspect project instructions and enough code to understand the context.
2. Restate the outcome, audience, constraints, and success criteria. Separate facts from assumptions.
3. Ask only questions whose answers change scope, safety, or acceptance.
4. Offer the smallest viable design and note alternatives and trade-offs.
5. Stop at the required human approval gate before changing product code, scaffolding, installing dependencies, or creating external resources.
6. Preserve the approved intent in the next artifact.

## Output

Return classification, understanding, assumptions, acceptance criteria, non-goals, design, risks, approval needed, and next action. Do not silently turn approval of an idea into approval of implementation.
