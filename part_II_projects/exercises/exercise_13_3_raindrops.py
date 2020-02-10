# 13-3. Raindrops: Find an image of a raindrop and create a grid of raindrops.
# Make the raindrops fall toward the bottom of the screen until they disappear.

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

        self.raindrops = pygame.sprite.Group()
        self._create_raindrop()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.screen_color)

            self.raindrops.draw(self.screen)
            pygame.display.flip()

    def _create_raindrop(self):
        raindrop = Raindrop()
        raindrop_width, raindrop_height = raindrop.rect.size

        number_x = self.screen_width // raindrop_width
        number_y = self.screen_height // raindrop_height

        space_x = self.screen_width % raindrop_width // (number_x + 1)
        space_y = self.screen_height % raindrop_height // (number_y + 1)

        for number_row in range(number_y):
            for number_column in range(number_x):
                raindrop = Raindrop()
                raindrop.rect.x = raindrop_width * \
                    number_column + space_x * (number_column + 1)
                raindrop.rect.y = raindrop_height * \
                    number_row + space_y * (number_row + 1)
                self.raindrops.add(raindrop)


class Raindrop(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("exercise_13_3_raindrop.bmp")
        self.rect = self.image.get_rect()


if __name__ == "__main__":
    screen = Screen()
    screen.run_game()
