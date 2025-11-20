import asyncio
import pygame
import sys
from settings import *
from game import Game

async def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1)
                elif event.key == pygame.K_RIGHT:
                    game.move(1)
                elif event.key == pygame.K_DOWN:
                    game.update() # Soft drop
                elif event.key == pygame.K_UP:
                    game.rotate()

        game.update()
        screen.fill(BLACK)
        game.draw(screen)
        
        # Draw Score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {game.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Draw Next Piece Preview
        next_text = font.render("Next:", True, WHITE)
        screen.blit(next_text, (SCREEN_WIDTH - 100, 10))
        
        # Draw the next tetromino shape (simplified drawing for preview)
        # We need to offset it to the preview area
        preview_x = SCREEN_WIDTH - 80
        preview_y = 50
        for r, row in enumerate(game.next_tetromino.shape):
            for c, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, COLORS[game.next_tetromino.color_index],
                                     (preview_x + c * GRID_SIZE, preview_y + r * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                    pygame.draw.rect(screen, WHITE,
                                     (preview_x + c * GRID_SIZE, preview_y + r * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
        
        if game.game_over:
             # Simple Game Over text
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over", True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
