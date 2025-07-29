# Tetris Game Configuration

# Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
GAME_AREA_WIDTH = 300  # Width of the tetris play area

# Grid
GRID_SIZE = 30
GRID_WIDTH = GAME_AREA_WIDTH // GRID_SIZE # 10 blocks wide
GRID_HEIGHT = 600 // GRID_SIZE # 20 blocks high

# Top-left corner of the grid on the screen
GRID_TOP_LEFT_X = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2
GRID_TOP_LEFT_Y = SCREEN_HEIGHT - (GRID_HEIGHT * GRID_SIZE) - 20

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Tetromino block colors
COLORS = [
    (0, 240, 240),    # I (Cyan)
    (240, 160, 0),    # L (Orange)
    (0, 0, 240),      # J (Blue)
    (240, 240, 0),    # O (Yellow)
    (160, 0, 240),    # T (Purple)
    (0, 240, 0),      # S (Green)
    (240, 0, 0),      # Z (Red)
]

# Tetromino Shapes
# The numbers correspond to the index in the COLORS list
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[2, 2, 2], [0, 0, 2]],  # L
    [[3, 3, 3], [3, 0, 0]],  # J
    [[4, 4], [4, 4]],  # O
    [[5, 5, 5], [0, 5, 0]],  # T
    [[0, 6, 6], [6, 6, 0]],  # S
    [[7, 7, 0], [0, 7, 7]],  # Z
]
