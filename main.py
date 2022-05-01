import pygame
from player import Player
from mob import Mob

WIDTH = 500
HEIGHT = 600
WHITE = (255, 255, 255)

display = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_text(surf, text, size, x, y):
    font = pygame.font.SysFont('arial', 25)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
def show_go_screen():
    draw_text(screen, "Game-over", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Fleches gauche et droites pour bouger, ", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Espace pour tirer", 22,
    WIDTH / 2, HEIGHT / 2.5)
    draw_text(screen,  'Meilleur score:'+str(bestScore), 22,
    WIDTH / 2, HEIGHT / 3)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
def newmob():
    m = Mob(WIDTH, HEIGHT)
    all_sprites.add(m)
    mobs.add(m)

picture = pygame.image.load("bg.jpeg")
picture = pygame.transform.scale(picture, (500, 600))
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player(WIDTH, HEIGHT)
all_sprites.add(player)
score = 0
bestScore = 0
gameOver = False

for i in range(8):
    m = Mob(WIDTH, HEIGHT)
    all_sprites.add(m)
    mobs.add(m)

running = True

while running:
    clock.tick(60)
    display.blit(picture,(0,0))
    if gameOver: 
        show_go_screen()
        gameOver = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        player = Player(WIDTH, HEIGHT)
        all_sprites.add(player)
        for i in range(8):
            newmob()
        score = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(all_sprites, bullets)

    all_sprites.update()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)

    for hit in hits:
        newmob()
        score += 1
    hits = pygame.sprite.spritecollide(player, mobs, False)
    draw_text(screen, 'score: '+str(score), 64,  50, 10)

    if hits:
        if score > bestScore: 
            bestScore = score
        gameOver = True
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

