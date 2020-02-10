# 12-2. Game Character: Find a bitmap image of a game character you like or
# convert an image to a bitmap. Make a class that draws the character at the
# center of the screen and match the background color of the image to the
# background color of the screen, or vice versa.


import sys
import pygame


class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (230, 230, 230)
        self.character = pygame.image.load("exercise_12_2_ship.bmp")
        self.character_rect = self.character.get_rect()
        self.character_rect.center = self.screen.get_rect().center

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.screen.blit(self.character, self.character_rect)
            pygame.display.flip()


if __name__ == "__main__":
    screen = Screen()
    screen.run_game()
