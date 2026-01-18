---
allowed-tools: Bash(bd:*), Bash(export:*), Read, Write, Edit, Glob, Grep
description: Implement from a ticket or spec
argument-hint: <ticket-id or spec-path>
---

# Implement from Ticket

Execute implementation work based on a Beads ticket or spec file.

## Usage

```
/aura.implement <ticket-id>
/aura.implement specs/feature-name.md
```

## Instructions

### Step 0: Determine Input Type

If argument looks like a task ID (short alphanumeric):
```bash
bd show $ARGUMENTS
```

If argument looks like a file path:
```bash
cat $ARGUMENTS
```

### Step 1: Mark Task In Progress (if Beads task)

If working from a Beads task:
```bash
bd update $ARGUMENTS --status in_progress
```

### Step 2: Read the Spec/Task

Parse the task description or spec file to understand:

- **What needs to be built**: Core requirements
- **Files to modify**: Existing code to change
- **Files to create**: New files needed
- **Acceptance criteria**: How to verify completion

### Step 3: Create Implementation Plan

Before writing code, create a brief plan:

```
Implementation Plan for: [Title]

1. [First change - file and what to do]
2. [Second change - file and what to do]
3. [Validation step]
```

Present this plan and proceed.

### Step 4: Execute the Plan

- Follow the step-by-step tasks from the spec
- Make changes in order (foundational first)
- Write clean, simple code following project patterns
- Run validation commands after implementation

### Step 5: Verify Work

Run any validation commands from the spec:
- Tests
- Type checks
- Manual verification

### Step 6: Update Task Status (if Beads task)

After successful implementation:
```bash
bd close $ARGUMENTS
bd ready  # Show what's next
```

## Report

When complete, summarize:
- Files created or modified
- Brief description of changes
- Results of validation
- Beads task updated (if applicable)

## Notes

- If validation fails, fix issues before marking complete
- Keep implementations simple and focused
- Follow existing patterns in the codebase
