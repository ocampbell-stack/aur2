---
allowed-tools: Bash(bd:*), Bash(export:*), Read, Glob
description: Convert epic to beads tickets with dependencies
argument-hint: <epic-directory>
---

# Epic to Beads Tickets

Parse an epic README and create matching Beads tasks with proper dependencies.

## Usage

```
/aura.tickets <epic-directory>
```

## Example

```
/aura.tickets specs/epic-player-movement
```

## Instructions

### 1. Validate Prerequisites

Check that Beads is available:
```bash
bd --version
```

If `bd` command fails, inform the user they need to install Beads first.

Check the epic directory exists:
```bash
ls $ARGUMENTS/README.md
```

### 2. Parse Epic README

Read the epic README at `$ARGUMENTS/README.md`.

Extract:
- Epic title (from `# Epic:` heading)
- Phases (from `### Phase N:` sections under `## Execution Order`)
- For each phase:
  - Phase name and description
  - Specs listed (from numbered lists with `[Type: Title](./file.md)` links)
  - Execution order (sequential within phase)

### 3. Create Beads Tasks

For each spec found, create a Beads task:

```bash
bd create "Phase N: Spec Title" --description "Spec file: $ARGUMENTS/spec-file.md"
```

Track the task IDs returned for dependency setup.

### 4. Set Up Dependencies

**Within-phase dependencies** (sequential order):
- Task 2 in a phase depends on Task 1
- Task 3 depends on Task 2

**Cross-phase dependencies**:
- First task of Phase N depends on last task of Phase N-1

Use:
```bash
bd dep add <dependent-task-id> <blocking-task-id>
```

### 5. Output Summary

After creating all tasks:

```
Epic to Beads Complete

Epic: [Epic Title]
Source: $ARGUMENTS/README.md

Created Tasks:
  Phase 1: [Phase Name] (X tasks)
    [task-id]: [Title]
    [task-id]: [Title] (depends on [prev-id])

  Phase 2: [Phase Name] (Y tasks)
    [task-id]: [Title] (depends on [last-phase-1-id])

Total: N tasks with M dependencies

Next steps:
  - Run `/beads.ready` to see available tasks
  - Run `/beads.start <id>` to begin work
```

### 6. Verify

```bash
bd list
bd ready
```

## Error Handling

- Epic directory doesn't exist: Clear error message
- README.md missing: Clear error message
- No "Execution Order" section: Explain structure needed
- Beads not installed: Explain how to install
- `.beads/` not initialized: Suggest `bd init`
