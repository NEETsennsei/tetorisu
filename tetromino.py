from settings import *
import random

class Tetromino:
    SHAPES = [
        [[1, 1, 1, 1]], # I
        [[2, 0, 0], [2, 2, 2]], # J
        [[0, 0, 3], [3, 3, 3]], # L
        [[4, 4], [4, 4]], # O
        [[0, 5, 5], [5, 5, 0]], # S
        [[0, 6, 0], [6, 6, 6]], # T
        [[7, 7, 0], [0, 7, 7]]  # Z
    ]

    def __init__(self):
        self.shape_index = random.randint(0, 6)
        self.shape = [row[:] for row in self.SHAPES[self.shape_index]]
        self.color_index = self.shape_index + 1
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        # Transpose and reverse rows for 90 degree clockwise rotation
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def draw(self, surface):
        for r, row in enumerate(self.shape):
            for c, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(surface, COLORS[self.color_index],
                                     ((self.x + c) * GRID_SIZE, (self.y + r) * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                    pygame.draw.rect(surface, WHITE,
                                     ((self.x + c) * GRID_SIZE, (self.y + r) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
