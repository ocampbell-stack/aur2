---
allowed-tools: Bash(bd:*), Bash(export:*)
description: Start working on a task
argument-hint: <task-id>
---

# Start Working on Task

Mark a Beads task as in_progress.

## Usage

```
/beads.start <task-id>
```

## Example

```
/beads.start proj-abc
```

## Instructions

### 1. Validate Task Exists

```bash
bd show $ARGUMENTS
```

If task not found, show error and suggest running `/beads.ready`.

### 2. Update Task Status

```bash
bd update $ARGUMENTS --status in_progress
```

### 3. Confirm and Show Details

Display:

```
Started task: $ARGUMENTS

[Task Title]

Description:
[Task description from bd show]

Spec file (if referenced):
[Path to spec file]

Ready to implement? Use:
  /aura.implement $ARGUMENTS
```

### 4. Show Context

If the task description references a spec file, read and summarize it:

```
Spec Summary:
- [Key requirements from spec]
- [Acceptance criteria highlights]
```

## Notes

- Only one task should typically be in_progress at a time
- Use `/beads.done <id>` when finished
- Use `/aura.implement <id>` to get guided implementation
