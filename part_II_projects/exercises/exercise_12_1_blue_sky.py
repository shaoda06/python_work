# 12-1. Blue Sky: Make a Pygame window with a blue background.
import sys
import pygame


class Screen:
    """Make a Pygame window with a blue background"""

    def __init__(self):
        pygame.init()
        self.bg_color = (0, 0, 255)
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Exercise 12-1 Blue Sky")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == "__main__":
    screen = Screen()
    screen.run_game()
