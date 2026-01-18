# Expected Beads Tasks

After running `/aura.tickets`, these tasks should exist:

## Task 1: Create Player Class
- ID: tron-001 (or similar)
- Description: Create a Player class with position and direction
- Status: open
- Dependencies: none
- Spec: specs/epic-player-movement/feature-player-class.md

## Task 2: Add Keyboard Input Handling
- ID: tron-002
- Description: Capture arrow key presses and update player direction
- Status: open
- Dependencies: tron-001
- Spec: specs/epic-player-movement/feature-keyboard-input.md

## Task 3: Implement Movement Loop
- ID: tron-003
- Description: Update player position based on direction each frame
- Status: open
- Dependencies: tron-002
- Spec: specs/epic-player-movement/feature-movement-loop.md

## Task 4: Create Trail Class
- ID: tron-004
- Description: Create a Trail class to store previous positions
- Status: open
- Dependencies: tron-003
- Spec: specs/epic-player-movement/feature-trail-class.md

## Task 5: Render Trail
- ID: tron-005
- Description: Draw trail segments on screen as bike moves
- Status: open
- Dependencies: tron-004
- Spec: specs/epic-player-movement/feature-trail-rendering.md

## Dependency Graph

```
tron-001 (Player Class)
    |
tron-002 (Keyboard Input)
    |
tron-003 (Movement Loop)
    |
tron-004 (Trail Class)
    |
tron-005 (Trail Rendering)
```

## Verification Commands

```bash
# List all tasks
bd list

# Show ready tasks (should show tron-001 initially)
bd ready

# Show task details
bd show tron-001

# Verify dependencies
bd show tron-002  # Should show blocked by tron-001
```
