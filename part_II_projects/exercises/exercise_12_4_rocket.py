# 12-4. Rocket: Make a game that begins with a rocket in the center of the
# screen. Allow the player to move the rocket up, down, left, or right using the
# four arrow keys. Make sure the rocket never moves beyond any edge of the
# screen.

import sys
import pygame


class Screen:
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (235, 190, 71)
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.screen.fill(self.bg_color)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Exercise 12-4 Rocket")
        self.rocket_image = pygame.image.load("exercise_12_4_rocket.bmp")
        self.rocket_rect = self.rocket_image.get_rect()
        self.rocket_rect.center = self.screen_rect.center
        self.rocket_speed = 1.0
        self.rocket_x = float(self.rocket_rect.left)
        self.rocket_y = float(self.rocket_rect.top)
        self.rocket_moving_up = False
        self.rocket_moving_down = False
        self.rocket_moving_right = False
        self.rocket_moving_left = False

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.rocket_moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.rocket_moving_down = True
                    elif event.key == pygame.K_LEFT:
                        self.rocket_moving_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.rocket_moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.rocket_moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.rocket_moving_down = False
                    elif event.key == pygame.K_LEFT:
                        self.rocket_moving_left = False
                    elif event.key == pygame.K_RIGHT:
                        self.rocket_moving_right = False

            self.update_rocket()
            self.screen.blit(self.rocket_image, self.rocket_rect)
            pygame.display.flip()

    def update_rocket(self):
        if self.rocket_moving_up and self.rocket_y > 0:
            self.rocket_y -= self.rocket_speed

        if self.rocket_moving_down and \
                self.rocket_rect.bottom < self.screen_rect.bottom:
            self.rocket_y += self.rocket_speed

        if self.rocket_moving_right and \
                self.rocket_rect.right < self.screen_rect.right:
            self.rocket_x += self.rocket_speed

        if self.rocket_moving_left and self.rocket_x > 0:
            self.rocket_x -= self.rocket_speed

        self.rocket_rect.x = int(self.rocket_x)
        self.rocket_rect.y = int(self.rocket_y)


if __name__ == "__main__":
    screen = Screen()
    screen.run_game()
