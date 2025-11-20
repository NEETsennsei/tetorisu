import pygame

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
DARK_GRAY = (50, 50, 50)

# Tetromino colors
COLORS = [
    (0, 0, 0),       # 0: Empty
    CYAN,            # 1: I
    BLUE,            # 2: J
    ORANGE,          # 3: L
    YELLOW,          # 4: O
    GREEN,           # 5: S
    MAGENTA,         # 6: T
    RED              # 7: Z
]

# Game settings
FPS = 60
MOVE_DELAY = 100  # ms
