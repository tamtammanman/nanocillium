WIDTH,HEIGHT = 1200,700
import random

import pygame
from redlaser import Redlaser
class Bacteria(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, redlasergroup, bacteriagroup):
        super().__init__()
        self.image = pygame.image.load("bacteria.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.velocity = velocity
        self.lasergroup = redlasergroup
        self.direction = 1
        self.bacteriagroup = bacteriagroup

    def update(self):
        self.rect.x += self.direction*self.velocity
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            for bacteria in self.bacteriagroup: 
                bacteria.direction *= -1
                bacteria.rect.y += 20


        if random.randint(0, 1000) > 999 and len(self.lasergroup) < 3:

            self.fire()

    def fire(self):
        Redlaser(self.rect.centerx, self.rect.bottom, self.lasergroup)
