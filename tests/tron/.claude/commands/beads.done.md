---
allowed-tools: Bash(bd:*), Bash(export:*)
description: Mark a task as complete
argument-hint: <task-id>
---

# Complete Task

Mark a Beads task as closed.

## Usage

```
/beads.done <task-id>
```

## Example

```
/beads.done proj-abc
```

## Instructions

### 1. Validate Task Exists

```bash
bd show $ARGUMENTS
```

If task not found, show error.

### 2. Close the Task

```bash
bd close $ARGUMENTS
```

### 3. Show What's Unblocked

```bash
bd ready
```

Display:

```
Completed: $ARGUMENTS

[Task Title] is now closed.

Tasks now unblocked:
  [task-id]: [Title]
  [task-id]: [Title]

Or if none: "No new tasks unblocked."
```

### 4. Suggest Next Steps

```
What's next?

  /beads.ready     - See all ready tasks
  /beads.status    - See project overview
  /beads.start <id> - Start the next task
```

## Notes

- Closing a task may unblock dependent tasks
- Use `/beads.status` to see overall progress
- Tasks can be reopened if needed with `bd update <id> --status open`
