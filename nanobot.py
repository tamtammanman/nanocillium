WIDTH,HEIGHT = 1200,700
import pygame
from greenlaser import Greenlaser
class Nanobot(pygame.sprite.Sprite):
    def __init__(self, lasergroup):
        super().__init__()
        self.image = pygame.image.load("nanobot1.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH // 2)
        self.rect.bottom = HEIGHT - 100
        self.velocity = 5
        self.lasergroup = lasergroup
        self.lives = 5
        self.score = 0
    def update(self,event):
        """Update the player movement based on key press"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x -= self.velocity
            if event.key == pygame.K_RIGHT:
                self.rect.x += self.velocity
    def fire(self):
        if len(self.lasergroup)<2:
            Greenlaser(self.rect.centerx, self.rect.top, self.lasergroup)



