import pygame
from pygame.locals import *
import sys

class Main:
    def __init__(self):
        self.window = pygame.display.set_mode((640, 360))
        self.display = pygame.Surface((320, 180))
        self.clock = pygame.Clock()
        self.dt = 0

    def run(self):
        while 1:
            self.dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.display.fill((0, 0, 0))

            self.window.blit(
                pygame.transform.scale(self.display, (640, 360)), (0, 0)
            )
            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()
