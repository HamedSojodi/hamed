import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class Aline:
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.setting.heigh_screen=self.screen.get_rect().height
        self.setting.wigth_screen = self.screen.get_rect().width
        pygame.display.set_caption("Aline_invasion")

        self.bullets=pygame.sprite.Group()

        # make ship
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_event()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._cheack_keydown(event)

            if event.type == pygame.KEYUP:
                self._check_keyup(event)


    def _cheack_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            # self.ship.rect.x += 5
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_ESCAPE:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def fire_bullet(self):
        new_bullet =Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.ship.blitm()
        for bullet in self.bullets.sprites  ():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == "__main__":
    res = Aline()
    res.run_game()
