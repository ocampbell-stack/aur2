---
allowed-tools: Bash(bd:*), Bash(export:*)
description: Show project status via Beads
---

# Beads Status: Project Overview

Show high-level project status via Beads task graph.

## Usage

```
/beads.status
```

## What This Shows

- Tasks by status (open, in_progress, closed)
- Progress metrics
- Currently active work
- Next available tasks
- Recently completed work

## Instructions

### 1. Check Beads Availability

```bash
if [ -d ".beads" ]; then
    bd --version
else
    echo "Beads not initialized in this project"
    echo "Run 'bd init' to set up Beads task tracking"
    exit 0
fi
```

### 2. Gather Status Information

```bash
# Count by status
TOTAL=$(bd list --all 2>/dev/null | wc -l || echo "0")
CLOSED=$(bd list --status closed 2>/dev/null | wc -l || echo "0")
IN_PROGRESS=$(bd list --status in_progress 2>/dev/null | wc -l || echo "0")
OPEN=$(bd list --status open 2>/dev/null | wc -l || echo "0")

echo "Total: $TOTAL | Closed: $CLOSED | In Progress: $IN_PROGRESS | Open: $OPEN"
```

### 3. Display Status Report

Output a formatted status report:

```
Beads Project Status

Progress: X of Y tasks complete (Z%)

Status Breakdown:
  Completed:    X tasks
  In Progress:  Y tasks
  Open:         Z tasks
```

### 4. Show Active Work

```bash
bd list --status in_progress
```

Display as:
```
Currently Active:
  [task-id]: [Title]
  [task-id]: [Title]
```

Or if none: "No tasks currently in progress"

### 5. Show Ready Work

```bash
bd ready
```

Display as:
```
Ready to Work On:
  [task-id]: [Title]
  [task-id]: [Title]
```

Or if none: "No tasks ready (all blocked or completed)"

### 6. Show Recent Completions

```bash
bd list --status closed --limit 5
```

Display as:
```
Recently Completed:
  [task-id]: [Title]
  [task-id]: [Title]
```

### 7. Summary Recommendations

Based on status, provide recommendations:

- If in_progress tasks exist: "Continue working on active tasks"
- If ready tasks exist but none active: "Start a ready task with `/beads.start <id>`"
- If all tasks complete: "All tasks complete!"
- If blocked tasks exist: "Some tasks are blocked - check dependencies with `bd show <id>`"

## Notes

- This is a read-only status check
- Use this to get oriented at the start of a session
- Gracefully handles missing Beads initialization
