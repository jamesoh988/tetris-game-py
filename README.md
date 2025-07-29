# Python Tetris Game

A classic Tetris game implemented in Python using pygame. Enjoy the timeless puzzle game with smooth controls, scoring system, and increasing difficulty levels.

## Features

- **Classic Tetris Gameplay**: Traditional tetromino pieces (I, L, J, O, T, S, Z)
- **Scoring System**: Earn points by clearing lines
- **Level Progression**: Game speed increases as you advance
- **Line Clearing**: Complete horizontal lines disappear automatically
- **Smooth Controls**: Responsive piece movement and rotation
- **Game Over Detection**: Game ends when pieces reach the top

## Screenshots

![Tetris Game](screenshot.png)
*Classic Tetris gameplay with colorful tetromino pieces*

## Installation

### Prerequisites

- Python 3.6 or higher
- pygame library

### Setup

1. Clone the repository:
```bash
git clone https://github.com/jamesoh988/tetris-game-py.git
cd tetris-game-py
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install pygame:
```bash
pip install pygame
```

## How to Play

### Running the Game

```bash
python main.py
```

### Controls

| Key | Action |
|-----|--------|
| ← Left Arrow | Move piece left |
| → Right Arrow | Move piece right |
| ↓ Down Arrow | Soft drop (move piece down faster) |
| ↑ Up Arrow | Rotate piece clockwise |
| Space | Hard drop (instantly drop piece to bottom) |
| Esc | Quit game |

### Game Rules

1. **Objective**: Clear horizontal lines by filling them completely with tetromino pieces
2. **Piece Movement**: Tetrominoes fall from the top of the screen
3. **Line Clearing**: When a horizontal line is completely filled, it disappears and you earn points
4. **Game Over**: The game ends when pieces stack up to the top of the playing field
5. **Scoring**: Points are awarded for clearing lines, with bonus points for clearing multiple lines simultaneously

### Tetromino Pieces

- **I-piece** (Cyan): Long straight piece (4 blocks)
- **L-piece** (Orange): L-shaped piece
- **J-piece** (Blue): Reverse L-shaped piece
- **O-piece** (Yellow): Square piece (2x2)
- **T-piece** (Purple): T-shaped piece
- **S-piece** (Green): S-shaped piece
- **Z-piece** (Red): Z-shaped piece

## Game Configuration

The game settings can be modified in `config.py`:

- **Screen dimensions**: Adjust window size
- **Grid size**: Change block size and play area dimensions
- **Colors**: Customize tetromino piece colors
- **Shapes**: Modify tetromino piece patterns

## Code Structure

```
tetris-game-py/
│
├── main.py          # Main game logic and classes
├── config.py        # Game configuration and constants
├── README.md        # This file
├── .gitignore       # Git ignore file
└── venv/           # Virtual environment (not tracked)
```

### Main Components

- **Block class**: Represents individual tetromino pieces
- **Game class**: Handles game logic, rendering, and user input
- **Configuration**: Centralized settings for easy customization

## Development

### Adding New Features

1. **Sound Effects**: Add pygame.mixer for audio feedback
2. **High Scores**: Implement persistent score tracking
3. **Different Game Modes**: Add variations like time attack or endless mode
4. **Enhanced Graphics**: Improve visual effects and animations

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Technical Details

- **Language**: Python 3.6+
- **Framework**: pygame
- **Architecture**: Object-oriented design with separate classes for game logic and pieces
- **Rendering**: 60 FPS game loop with efficient drawing
- **Input Handling**: Real-time keyboard input processing

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Inspired by the classic Tetris game created by Alexey Pajitnov
- Built with Python and pygame
- Developed as a learning project for game development concepts

---

**Enjoy playing Tetris!** 🎮

For questions or suggestions, please open an issue on GitHub.