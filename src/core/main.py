import pygame
from pygame.locals import *
import sys

import data.config.config as conf
from src.engine.raycaster import RaycastEngine
from src.entities.player import Player

def draw_grid():
    surf = pygame.Surface((360, 180))

    for x in range(int(360 / conf.TILE_SIZE) + 1):
        for y in range(int(180 / conf.TILE_SIZE) + 1):
            pygame.draw.rect(
                surf, (255, 255, 255), (x * conf.TILE_SIZE, y * conf.TILE_SIZE, conf.TILE_SIZE, conf.TILE_SIZE), 1
            )

    return surf

class Main:
    def __init__(self):
        self.window = pygame.display.set_mode(conf.WIN_SIZE)
        self.display = pygame.Surface((320, 180))
        self.clock = pygame.Clock()
        self.dt = 0

        self.player = Player()
        self.raycast = RaycastEngine(self)

        self.grid = draw_grid()

    def run(self):
        while 1:
            self.dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.raycast.theta = self.player.movement(self.dt, self.raycast.theta)
                   

            self.display.fill((0, 0, 0))
            self.display.blit(
                self.grid, (0, 0)
            )

            self.raycast.cast(self.player.pos, self.display)
            self.player.render(self.display)

            self.window.blit(
                pygame.transform.scale(self.display, (640, 360)), (0, 0)
            )
            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()
