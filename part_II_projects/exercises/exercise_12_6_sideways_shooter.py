# 12-6. Sideways Shooter: Write a game that places a ship on the left side of
# the screen and allows the player to move the ship up and down. Make the
# ship fire a bullet that travels right across the screen when the player
# presses the spacebar. Make sure bullets are deleted once they disappear off
# the screen.

import sys
import pygame
from pygame.sprite import Sprite


class Screen:
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230)
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()

        self.ship_image = pygame.image.load("exercise_12_2_ship.bmp")
        self.ship_rect = self.ship_image.get_rect()
        self.ship_rect.midleft = self.screen_rect.midleft
        self.ship_speed = 1
        self.ship_move_up = False
        self.ship_move_down = False
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.ship_move_up = True
                    elif event.key == pygame.K_DOWN:
                        self.ship_move_down = True
                    elif event.key == pygame.K_SPACE:
                        new_bullet = Bullet(self)
                        self.bullets.add(new_bullet)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.ship_move_up = False
                    elif event.key == pygame.K_DOWN:
                        self.ship_move_down = False

            self.ship_update()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.left > self.screen_rect.right:
                    self.bullets.remove(bullet)
            self.screen.fill(self.screen_color)
            self.screen.blit(self.ship_image, self.ship_rect)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            pygame.display.flip()

    def ship_update(self):
        if self.ship_move_up and self.ship_rect.y > 0:
            self.ship_rect.y -= self.ship_speed
        if self.ship_move_down \
                and self.ship_rect.bottom < self.screen_rect.bottom:
            self.ship_rect.y += self.ship_speed


class Bullet(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = self.screen.ship_rect.midright

    def update(self):
        self.rect.x += int(self.bullet_speed)

    def draw_bullet(self):
        pygame.draw.rect(self.screen.screen, self.bullet_color, self.rect)


if __name__ == "__main__":
    screen = Screen()
    screen.run_game()
