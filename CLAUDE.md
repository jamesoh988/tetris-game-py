# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Setup and Installation
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install pygame
```

### Running the Game
```bash
# Activate virtual environment first
source venv/bin/activate

# Run the main game
python main.py
```

Note: This is a GUI application that requires a display. On headless systems or remote environments, you may encounter X11/OpenGL errors.

## Code Architecture

### File Structure
- `main.py`: Main game logic with `Game` and `Block` classes, game loop, and event handling
- `config.py`: Game configuration constants (screen dimensions, colors, tetromino shapes)
- `plan_tetris_python.md`: Korean language project specification and requirements document

### Key Classes and Components

#### Game Class (`main.py:23-87`)
- Manages game state, pygame initialization, and main game loop
- Contains fall timing logic (`fall_time`, `fall_speed`)
- Handles events, updates, and rendering

#### Block Class (`main.py:6-21`) 
- Represents tetromino pieces with shape, color, and position
- Uses shape matrices from `config.SHAPES` and colors from `config.COLORS`
- Handles block rendering on the game grid

#### Configuration (`config.py`)
- `SHAPES`: 7 tetromino piece definitions as 2D arrays
- `COLORS`: RGB color values for each tetromino type  
- Grid and screen dimension constants
- Currently supports basic I, L, J, O, T, S, Z pieces

### Current Implementation Status
This is a basic tetris implementation with:
- Block spawning and falling mechanics
- Grid-based rendering system
- Basic pygame event handling

Missing advanced features mentioned in the plan:
- Collision detection and line clearing
- Block rotation and movement controls
- Score system and levels
- Next piece preview and ghost blocks
- Sound effects and music
- Leaderboard system

### Game Controls (Planned)
- Arrow keys: Move and rotate blocks
- Space: Hard drop
- P: Pause
- R: Restart
- ESC: Exit