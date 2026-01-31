# Git Workflow in Skills

## Vision
Skills automatically handle branching, committing, and PR creation. The user never manually runs git commands during aura workflows.

## Key Ideas
- `aura.scope` creates a branch (`scope/{bead-id}-{slug}`), commits the plan file
- `aura.execute` works on that branch, commits after each meaningful step, creates PR at the end
- Branch naming and commit messages use simple templates in the skill prompts — no need for separate Claude invocations (ADWS overengineered this)
- Claude Code already knows git and gh, just needs instructions in SKILL.md

## Implementation
- Add 5-10 lines to each SKILL.md with git instructions
- No new infrastructure needed
- Validate interactively before baking into automation

## Depends On
- Skills producing reliable output first
