import pygame

import data.config.config as conf

class Player:
    def __init__(self):
        self.pos = [100, 100]
        

    def rotation(self, dt, keys, theta):
        x_rot = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 35
        theta += x_rot * dt

        if theta < 0:
            theta = 360 - theta
        elif theta > 360:
            theta %= 360

        return theta

    def movement(self, dt, theta):
        keys = pygame.key.get_pressed()

        x = (keys[pygame.K_d] - keys[pygame.K_a]) * 35
        y = (keys[pygame.K_s] - keys[pygame.K_w]) * 35
        self.pos[0] += x * dt
        self.pos[1] += y * dt

        theta = self.rotation(dt, keys, theta)

        return theta

    def render(self, display):
        TS = conf.TILE_SIZE
        TS_2 = TS / 2
        pygame.draw.rect(display, (255, 255, 255), (self.pos[0] - TS_2, self.pos[1] - TS_2, TS / 2, TS / 2))
