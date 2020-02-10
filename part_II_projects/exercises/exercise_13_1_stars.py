# 13-1. Stars: Find an image of a star. Make a grid of stars appear on the
# screen.

import sys
import pygame
from pygame.sprite import Sprite


class Screen:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (255, 255, 255)
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.screen_color)
            self.stars.draw(self.screen)
            pygame.display.flip()

    def _create_stars(self):
        star = Star(self.screen)

        number_x = self.screen_width // star.star_width
        number_y = self.screen_height // star.star_height

        space_x = (self.screen_width % star.star_width) // (number_x + 1)
        space_y = (self.screen_height % star.star_height) // (number_y + 1)

        for number_row in range(number_y):
            for number_column in range(number_x):
                star = Star(self.screen)
                star.rect.x = space_x * \
                    (number_column + 1) + star.star_width * number_column
                star.rect.y = space_y * \
                    (number_row + 1) + star.star_height * number_row
                self.stars.add(star)


class Star(Sprite):
    def __init__(self, sc):
        super().__init__()
        self.screen = sc

        self.image = pygame.image.load("exercise_13_1_star.bmp")
        self.rect = self.image.get_rect()
        self.star_width, self.star_height = self.rect.size


if __name__ == "__main__":
    screen = Screen()
    screen.run_game()
