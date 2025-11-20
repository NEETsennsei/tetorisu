import pygame
from settings import *
from grid import Grid
from tetromino import Tetromino

class Game:
    def __init__(self):
        self.grid = Grid()
        self.tetromino = Tetromino()
        self.next_tetromino = Tetromino()
        self.score = 0
        self.game_over = False
        self.last_move_time = pygame.time.get_ticks()
        self.fall_speed = 500  # ms

    def update(self):
        if self.game_over:
            return

        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time > self.fall_speed:
            if not self.grid.check_collision(self.tetromino, offset_y=1):
                self.tetromino.y += 1
            else:
                self.grid.lock_tetromino(self.tetromino)
                self.score += self.grid.clear_lines() * 100
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino()
                if self.grid.check_collision(self.tetromino):
                    self.game_over = True
            self.last_move_time = current_time

    def move(self, dx):
        if not self.game_over and not self.grid.check_collision(self.tetromino, offset_x=dx):
            self.tetromino.x += dx

    def rotate(self):
        if not self.game_over:
            original_shape = [row[:] for row in self.tetromino.shape]
            self.tetromino.rotate()
            if self.grid.check_collision(self.tetromino):
                self.tetromino.shape = original_shape

    def draw(self, surface):
        self.grid.draw(surface)
        self.tetromino.draw(surface)
