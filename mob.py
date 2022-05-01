import pygame
import random

RED = (255, 0, 0)

class Mob(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.width = WIDTH
        self.heigth = HEIGHT
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self,):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > self.heigth + 10 or self.rect.left < -25 or self.rect.right >  self.width  + 20:
            self.rect.x = random.randrange( self.width  - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)