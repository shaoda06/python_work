# 13-5. Sideways Shooter Part 2: We’ve come a long way since Exercise 12-6,
# Sideways Shooter. For this exercise, try to develop Sideways Shooter to the
# same point we’ve brought Alien Invasion to. Add a fleet of aliens, and make
# them move sideways toward the ship. Or, write code that places aliens at
# random positions along the right side of the screen and then sends them
# toward the ship. Also, write code that makes the aliens disappear when
# they’re hit.

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

        self.ship_image = pygame.image.load("exercise_13_5_ship.bmp")
        self.ship_rect = self.ship_image.get_rect()
        self.ship_rect.midleft = self.screen_rect.midleft
        self.ship_speed = 1
        self.ship_move_up = False
        self.ship_move_down = False

        self.bullets = pygame.sprite.Group()

        self.alien_move_vertical_speed = 1
        self.alien_move_horizontal_speed = 5
        self.alien_move_direction = 1
        self.aliens = pygame.sprite.Group()
        self._create_alien_fleet()

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
            self.aliens.update()
            self._check_bullet_alien_collision()
            self._check_fleet_edges()
            self.aliens.draw(self.screen)
            pygame.display.flip()

    def ship_update(self):
        if self.ship_move_up and self.ship_rect.y > 0:
            self.ship_rect.y -= self.ship_speed
        if self.ship_move_down \
                and self.ship_rect.bottom < self.screen_rect.bottom:
            self.ship_rect.y += self.ship_speed

    def _create_alien_fleet(self):
        alien = Alien(self)
        number_x = 4
        number_y = (self.screen_rect.height - 2 *
                    alien.rect.height) // (2 * alien.rect.height)

        for number_column in range(number_x):
            for number_row in range(number_y):
                alien = Alien(self)
                alien.rect.y = alien.rect.height * (number_row + 1) + \
                    alien.rect.height * number_row
                alien.rect.x = self.screen_rect.width - 2 * \
                    (number_column + 1) * alien.rect.width
                self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens:
            if alien.rect.top <= 0 \
                    or alien.rect.bottom >= self.screen_rect.bottom:
                self.alien_move_direction *= -1
                self._move_fleet_left()
                break

    def _move_fleet_left(self):
        for alien in self.aliens:
            alien.rect.x -= self.alien_move_horizontal_speed

    def _check_bullet_alien_collision(self):
        collision = pygame.sprite.groupcollide(
            self.aliens, self.bullets, True, True)


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


class Alien(Sprite):
    def __init__(self, screen):
        self.screen = screen
        super().__init__()
        self.image = pygame.image.load("exercise_13_5_alien.bmp")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.screen.alien_move_direction * \
            self.screen.alien_move_vertical_speed


if __name__ == "__main__":
    screen = Screen()
    screen.run_game()
