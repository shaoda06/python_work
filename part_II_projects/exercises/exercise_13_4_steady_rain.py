# 13-4. Steady Rain: Modify your code in Exercise 13-3 so when a row of
# raindrops disappears off the bottom of the screen, a new row appears at the
# top of the screen and begins to fall.


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
            self.raindrops.update()
            self._create_new_drop()
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

    def _create_new_drop(self):
        for raindrop in self.raindrops:
            if raindrop.rect.y >= self.screen_height:
                self.raindrops.remove(raindrop)

                new_drop_x = raindrop.rect.x

                new_drop_height = raindrop.rect.height
                number_y = self.screen_height // new_drop_height
                space_y = self.screen_height % new_drop_height // (number_y + 1)

                new_drop = Raindrop()
                new_drop.rect.x = new_drop_x
                new_drop.rect.y = space_y
                self.raindrops.add(new_drop)

class Raindrop(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("exercise_13_3_raindrop.bmp")
        self.rect = self.image.get_rect()
        self.drop_speed = 10

    def update(self):
        self.rect.y += self.drop_speed


if __name__ == "__main__":
    screen = Screen()
    screen.run_game()
