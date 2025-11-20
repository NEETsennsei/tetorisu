from settings import *

class Grid:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    def is_inside(self, r, c):
        return 0 <= r < GRID_HEIGHT and 0 <= c < GRID_WIDTH

    def is_empty(self, r, c):
        return self.grid[r][c] == 0

    def check_collision(self, tetromino, offset_x=0, offset_y=0):
        for r, row in enumerate(tetromino.shape):
            for c, cell in enumerate(row):
                if cell:
                    new_r = tetromino.y + r + offset_y
                    new_c = tetromino.x + c + offset_x
                    if not self.is_inside(new_r, new_c) or not self.is_empty(new_r, new_c):
                        return True
        return False

    def lock_tetromino(self, tetromino):
        for r, row in enumerate(tetromino.shape):
            for c, cell in enumerate(row):
                if cell:
                    self.grid[tetromino.y + r][tetromino.x + c] = tetromino.color_index

    def clear_lines(self):
        lines_cleared = 0
        for r in range(GRID_HEIGHT - 1, -1, -1):
            if 0 not in self.grid[r]:
                del self.grid[r]
                self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
                lines_cleared += 1
        return lines_cleared

    def draw(self, surface):
        for r in range(GRID_HEIGHT):
            for c in range(GRID_WIDTH):
                if self.grid[r][c]:
                    pygame.draw.rect(surface, COLORS[self.grid[r][c]],
                                     (c * GRID_SIZE, r * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                    pygame.draw.rect(surface, WHITE,
                                     (c * GRID_SIZE, r * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
                else:
                    pygame.draw.rect(surface, DARK_GRAY,
                                     (c * GRID_SIZE, r * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
