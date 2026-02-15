---
name: aur2.execute
description: Create beads from a scope file and implement them autonomously
argument-hint: <scope-or-plan-path>
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
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

3. **Create epic** - Create a parent epic for the scope:
   ```bash
   bd create "<Scope name>" -t epic -d "Scope: <scope-path>"
   ```
   Record the epic bead ID.

4. **Create child beads** - For each task, create a bead under the epic:
   ```bash
   bd create "<Task title>" -t task -d "<Description>" --parent <epic-id>
   ```
   Record the bead ID returned.

5. **Build ID mapping** - Track task number -> bead ID

6. **Set dependencies** - For each task with dependencies:
   ```bash
   bd dep add <task-bead-id> <blocker-bead-id>
   ```

7. **Visualize graph** - Confirm the dependency DAG is correct:
   ```bash
   bd graph --all --compact
   ```
   Review the output: Layer 0 tasks have no blockers and start first. Higher layers depend on lower layers. Tasks in the same layer can run in parallel.

8. **Output summary** - Show the epic ID, created beads, and dependency graph. The user can check progress at any time with `bd epic status` or `bd swarm status <epic-id>`.

### Parsing Rules

- Task numbers are sequential across all phases
- Dependencies reference task numbers, not bead IDs
- Phase headers are informational only
- Tasks without "(depends on ...)" have no blockers

## Phase 2: Implement Graph

1. **Read scope** - Understand the overall goal and context
2. **Find ready beads** - Run `bd ready --parent <epic-id>` to find unblocked tasks in this scope
3. **Implement loop** - For each ready bead:
   - Show bead details: `bd show <id>`
   - Mark in progress: `bd update <id> --status in_progress`
   - Implement the work described
   - Record context: `bd comments add <id> "Done: <what was implemented>. Decisions: <key choices made>. Files: <created or modified>"`
   - Close when done: `bd close <id> --reason "<what was done>" --suggest-next`
4. **Repeat** - Run `bd ready --parent <epic-id>` again after each close for newly unblocked tasks
5. **Complete** - When no more ready tasks under the epic, close the epic: `bd epic close-eligible`

## Autonomous Mode

If working in an agent worktree (agent-alpha, agent-beta, etc.), read and follow `protocols/autonomous-workflow.md`. Create ONE feature branch for the entire scope execution — do not create separate branches per bead.

## Implementation Guidelines

These apply to the work done in each bead during the implement loop:

- Read relevant files before making changes
- Make minimal, focused changes per bead

**In a codebase** (source code, application logic):
- Follow existing code patterns and conventions
- Test changes when possible
- Verify builds still pass

**In a knowledge base** (markdown repos, hive-mind instances):
- Follow KB conventions: YAML frontmatter on all files (source, ingested, confidence, last_verified, tags)
- Update `knowledge-base/INDEX.md` when adding or modifying KB files
- Run compound deliverable verification where applicable (fidelity, coherence, privacy, professionalism)
- Respect privacy standards — team models are internal only

**In mixed contexts**: Apply both sets of guidelines as appropriate.

## Error Handling

- If bd create fails, report and continue with remaining tasks
- If implementation fails, leave a comment (`bd comments add <id> "<what failed>"`) and do not close the bead
