from tkinter import font
import pygame
from nanobot import WIDTH, Nanobot
from bacteria import HEIGHT, Bacteria
pygame.init()
bacteria_group = pygame.sprite.Group()
redlasergroup=pygame.sprite.Group()
clock = pygame.time.Clock()
gameover = False
game_win = False

font = pygame.font.Font(None, 36)


breach_sound = pygame.mixer.Sound("breach.wav")
gameover_sound = pygame.mixer.Sound("game_over.wav")
bacteria_hit_sound = pygame.mixer.Sound("bacteria_fire.wav")
nanobot_hit_sound = pygame.mixer.Sound("breach.wav")

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
FPS = 60
num_rows = 5
num_cols = 11
start_x = 100
start_y = 100
spacing_x = 60
spacing_y = 70
greenlasergroup = pygame.sprite.Group()
nanobot_group = pygame.sprite.Group()
bacteriagroup = pygame.sprite.Group()
redlasergroup = pygame.sprite.Group()
nanobot = Nanobot(greenlasergroup)
nanobot_group.add(nanobot)
for row in range(num_rows):
    for col in range(num_cols):
        x = start_x + col * spacing_x
        y = start_y + row * spacing_y
        bacteria = Bacteria(x, y, 2, redlasergroup, bacteriagroup)
        bacteriagroup.add(bacteria)






running = True
while running:
    screen.fill((0, 90, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                nanobot.fire()

    if pygame.sprite.groupcollide(greenlasergroup,  bacteriagroup, True, True,):
        nanobot.score += 100
        bacteria_hit_sound.play()
    if pygame.sprite.spritecollide(nanobot, redlasergroup, True):
        nanobot.lives -= 1
        nanobot_hit_sound.play()
    for bacteria in bacteriagroup:
        if bacteria.rect.bottom >= WINDOW_HEIGHT - 100 or nanobot.lives<=1:
            defeat_text = font.render("You lost! Game over!", True, "WHITE")
            defeat_text_rect = defeat_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            breach_sound.play()
            gameover=True
        if nanobot.score==4700:
            game_win=True
            gamewin_text=font.render("YOU WON!",True,"WHITE")
            gamewin_text_rect=gamewin_text.get_rect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

    if gameover:
        screen.fill("black")
        screen.blit(defeat_text, defeat_text_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    if game_win:
        screen.fill('black')
        screen.blit(gamewin_text, gamewin_text_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
    screen.fill((0, 0, 0))
    score_text = font.render(f"Score: {nanobot.score}", True, "WHITE")
    score_rect = score_text.get_rect(centerx=WINDOW_WIDTH // 2, top=60)

    lives_text = font.render(f"Lives: {nanobot.lives}", True, "WHITE")
    lives_rect = lives_text.get_rect(topright=(WINDOW_WIDTH - 20, 70))
    screen.blit(score_text, score_rect)
    screen.blit(lives_text, lives_rect)
    pygame.draw.line(screen, "WHITE", (0,50), (WINDOW_WIDTH, 50), 4)
    pygame.draw.line(screen, "WHITE", (0, WINDOW_HEIGHT - 100), (WINDOW_WIDTH, WINDOW_HEIGHT - 100), 4)


    nanobot_group.update(event)
    nanobot_group.draw(screen)
    bacteriagroup.update()
    bacteriagroup.draw(screen)
    redlasergroup.update()
    redlasergroup.draw(screen)
    greenlasergroup.update()
    greenlasergroup.draw(screen)
    clock.tick (FPS)
    pygame.display.flip()
pygame.quit()

        


