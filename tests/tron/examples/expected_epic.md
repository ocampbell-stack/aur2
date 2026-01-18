# Epic: Player Movement

## Overview

Add arrow key controls and trail rendering to the tron light bike.

The player needs to be able to control their bike using the keyboard arrow keys.
As the bike moves, it should leave a visible trail behind it that remains on screen.

This epic is scoped to movement and visuals only - collision detection and game
over logic are explicitly out of scope.

## Specs in This Epic

### Phase 1: Basic Movement
- [ ] [Feature: Player Class](./feature-player-class.md) - Create Player with position and direction
- [ ] [Feature: Keyboard Input](./feature-keyboard-input.md) - Capture arrow key presses
- [ ] [Feature: Movement Loop](./feature-movement-loop.md) - Update position each frame

### Phase 2: Trail Rendering
- [ ] [Feature: Trail Class](./feature-trail-class.md) - Store previous positions
- [ ] [Feature: Trail Rendering](./feature-trail-rendering.md) - Draw trail segments

## Execution Order

### Phase 1: Basic Movement
**Goal**: Player can control bike with arrow keys

Execute in order:
1. [Feature: Player Class](./feature-player-class.md) - Need entity before input
2. [Feature: Keyboard Input](./feature-keyboard-input.md) - Capture user input
3. [Feature: Movement Loop](./feature-movement-loop.md) - Apply input to movement

**Success Criteria**:
- Player class exists with x, y position and direction
- Arrow keys change player direction
- Player moves in the current direction each frame

---

### Phase 2: Trail Rendering
**Goal**: Bike leaves visible trail as it moves

Execute in order:
1. [Feature: Trail Class](./feature-trail-class.md) - Store position history
2. [Feature: Trail Rendering](./feature-trail-rendering.md) - Render the trail

**Success Criteria**:
- Trail stores all previous positions
- Trail renders as connected line segments
- Trail color is distinct from bike

---

## Path Dependencies Diagram

```
Phase 1
    |-- Player Class
    |-- Keyboard Input (depends on Player)
    +-- Movement Loop (depends on Input)
    |
Phase 2
    |-- Trail Class (depends on Movement)
    +-- Trail Rendering (depends on Trail Class)

Critical Path: Player -> Input -> Movement -> Trail -> Render
```

## Out of Scope

- Collision detection
- Game over logic
- Multiple players
- AI opponents

## Success Metrics

- [ ] Arrow keys control bike direction
- [ ] Bike moves smoothly in current direction
- [ ] Trail appears behind bike as it moves
- [ ] Trail is visually distinct from bike

## Future Enhancements

1. Collision detection with trails and walls
2. Game over screen when collision occurs
3. Score tracking and display
4. Multiple players / AI opponents
