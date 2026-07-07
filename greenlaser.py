import pygame
WIDTH,HEIGHT = 1000,500
class Greenlaser(pygame.sprite.Sprite):
    def __init__(self, x, y, lasergroup):
        super().__init__()
        self.image = pygame.image.load("green_laser.png")
        self.image = pygame.transform.scale(self.image,(10,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = 15
        lasergroup.add(self)


    def update(self):
        self.rect.y -= self.velocity 
        if self.rect.bottom < 0:
            self.kill()