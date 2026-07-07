import pygame
WIDTH,HEIGHT = 1000,500
class Redlaser(pygame.sprite.Sprite):
    def __init__(self, x, y, redlasergroup):
        super().__init__()
        self.image = pygame.image.load("red_laser.png")
        self.image = pygame.transform.scale(self.image,(10,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = (x)
        self.rect.bottom = (y)
        self.velocity = 15
        redlasergroup.add(self)


    def update(self):
        self.rect.y += self.velocity 
        if self.rect.top >HEIGHT:
            self.kill()