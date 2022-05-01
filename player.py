import pygame
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.width = WIDTH
        self.height = HEIGHT
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width / 2
        self.rect.bottom = self.height - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > self.width:
            self.rect.right = self.width
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self,all_sprites, bullets):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()