import pygame
WIDTH,HEIGHT = 1000,500
class Redlaser(pygame.sprite.Sprite):
    def __init__(self, x, y, redlasergroup):
        super().__init__()
        self.image = pygame.image.load("red_laser.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH // 2)
        self.rect.bottom = HEIGHT
        self.velocity = 15
        redlasergroup.add(self)


    def update(self):
        self.rect.y += self.velocity 
        if self.rect.top < 0:
            self.kill()