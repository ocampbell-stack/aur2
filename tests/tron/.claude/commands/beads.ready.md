---
allowed-tools: Bash(bd:*), Bash(export:*)
description: Show tasks ready to work on
---

# Show Ready Tasks

Display Beads tasks that are ready to work on (no blocking dependencies).

## Usage

```
/beads.ready
```

## Instructions

### 1. Check Beads

```bash
if [ ! -d ".beads" ]; then
    echo "Beads not initialized. Run 'bd init' first."
    exit 0
fi
```

### 2. Get Ready Tasks

```bash
bd ready
```

### 3. Display Results

Format the output as:

```
Ready to Work On:

  [task-id]: [Title]
    Description: [brief description]

  [task-id]: [Title]
    Description: [brief description]
```

Or if none ready:

```
No tasks ready.

Possible reasons:
- All tasks are completed
- Remaining tasks are blocked by dependencies
- No tasks exist yet

Run `/beads.status` for a full overview.
```

### 4. Suggest Next Steps

```
To start working on a task:
  /beads.start <task-id>

To see task details:
  bd show <task-id>
```
