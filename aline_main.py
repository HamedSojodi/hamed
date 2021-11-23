                             import sys
import pygame
from settings import Settings


class Aline:
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.wigth_screen, self.setting.heigh_screen))
        pygame.display.set_caption("Aline_invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.setting.bg_color)
            pygame.display.flip()


if __name__ == "__main__":
    res = Aline()
    res.run_game()
