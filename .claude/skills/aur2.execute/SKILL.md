---
name: aur2.execute
description: Create beads from a scope file and implement them autonomously
argument-hint: <scope-or-plan-path>
disable-model-invocation: true
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

# Execute Scope

Create beads from a scope/plan file and implement them in dependency order.

## Input

Path to a scope or plan file, e.g., `.aur2/plans/queue/my-feature/scope.md`

## Phase 1: Create Bead Graph

1. **Read scope** - Parse the scope markdown file

2. **Extract tasks** - Find all tasks in format:
   ```
   N. [ ] <Task title> (depends on X, Y) - <Description>
   ```
   or without dependencies:
   ```
   N. [ ] <Task title> - <Description>
   ```

3. **Create beads** - For each task, create a bead:
   ```bash
   bd create --title "<Task title>" --description "<Description>. Epic: <scope-path>"
   ```
   Record the bead ID returned

4. **Build ID mapping** - Track task number -> bead ID

5. **Set dependencies** - For each task with dependencies:
   ```bash
   bd dep add <task-bead-id> <blocker-bead-id>
   ```

6. **Visualize graph** - Confirm the dependency DAG is correct:
   ```bash
   bd graph --all --compact
   ```
   Review the output: Layer 0 tasks have no blockers and start first. Higher layers depend on lower layers. Tasks in the same layer can run in parallel.

7. **Output summary** - Show created beads and dependency graph

### Parsing Rules

- Task numbers are sequential across all phases
- Dependencies reference task numbers, not bead IDs
- Phase headers are informational only
- Tasks without "(depends on ...)" have no blockers

## Phase 2: Implement Graph

1. **Read scope** - Understand the overall goal and context
2. **Find ready beads** - Run `bd ready` to find unblocked tasks
3. **Implement loop** - For each ready bead:
   - Show bead details: `bd show <id>`
   - Mark in progress: `bd update <id> --status in_progress`
   - Implement the work described
   - Record context: `bd comments add <id> "Done: <what was implemented>. Decisions: <key choices made>"`
   - Close when done: `bd close <id> --reason "<what was done>" --suggest-next`
4. **Repeat** - Check for newly unblocked tasks after each close
5. **Complete** - When no more ready tasks, scope is done

## Autonomous Mode

If working in an agent worktree (agent-alpha, agent-beta, etc.), read and follow `protocols/autonomous-workflow.md`. Create ONE feature branch for the entire scope execution — do not create separate branches per bead. In a hive-mind context, "implementation" often means producing markdown deliverables and KB updates, not just code changes.

## Implementation Guidelines

- Read relevant files before making changes
- Follow existing patterns in the codebase
- Make minimal, focused changes
- Test changes when possible

## Error Handling

- If bd create fails, report and continue with remaining tasks
- If implementation fails, leave a comment (`bd comments add <id> "<what failed>"`) and do not close the bead
