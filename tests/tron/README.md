# Tron: Light Bike Game

A minimal light bike game for testing the Aura workflow.

## Game Concept

Tron is a classic arcade game where players control light bikes that leave
trails behind them. The objective is to survive longer than opponents by
avoiding walls and trails.

## Current State

This is a stub project for testing Aura. It contains:
- Basic project structure
- No actual game implementation (yet!)

## Testing Aura

This project is used to validate the full Aura workflow:

1. Initialize Aura: `aura init`
2. Create an epic: `/aura.epic Add player movement`
3. Generate tickets: `/aura.tickets specs/epic-player-movement/`
4. Implement tickets: `/aura.implement <ticket-id>`

## Future Game Features (for testing)

Ideas for features to implement via Aura:
- Player movement (arrow keys)
- Trail rendering
- Collision detection
- Game over screen
- Score tracking
