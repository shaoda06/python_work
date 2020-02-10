# 12-5. Keys: Make a Pygame file that creates an empty screen. In the event
# loop, print the event.key attribute whenever a pygame.KEYDOWN event is
# detected. Run the program and press various keys to see how Pygame responds.

import sys
import pygame


class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (230, 230, 230)
        self.screen.fill(self.bg_color)
        pygame.display.set_caption("Exercise 12-5 Keys")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)

            pygame.display.flip()


if __name__ == "__main__":
    screen = Screen()
    screen.run_game()
