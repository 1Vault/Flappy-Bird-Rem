import pygame
from sys import exit
from random import randint

def bird_animation():
    global bird_velo, bird_grav, bird_State, bird_surf

    if bird_velo > 0:
        bird_surf = bird_State[2]
    else:
        bird_surf = bird_State[0]
def Bg_change():
    global game_active, bg_surf, bg_rect, bg_surf, Bgs
    if game_active:
        bg_surf = Bgs[0]
    else:
        bg_surf = Bgs[1]

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Flaps of BIRDS')
clock = pygame.time.Clock()

bird_state_1 = pygame.image.load('bird_1.png').convert_alpha()
bird_state_2 = pygame.image.load('bird_2.png').convert_alpha()
bird_state_3 = pygame.image.load('bird_3.png').convert_alpha()
bird_State = [bird_state_1, bird_state_2, bird_state_3]

bird_surf = pygame.image.load('bird_1.png').convert_alpha()
bird_rect = bird_surf.get_rect(center = (200, 200))
bird_velo = 0
bird_grav = -0.1

pillerU_surf = pygame.image.load('pillerU.png').convert_alpha()
pillerU_rect = pillerU_surf.get_rect(center = (850, 200))

pillerD_surf = pygame.image.load('pillerD.png').convert_alpha()
pillerD_rect = pillerD_surf.get_rect(center = (850, 200))
obspeed = 4

bgT_surf = pygame.image.load('bg.png').convert_alpha()
bgF_surf = pygame.image.load('BgF.png').convert_alpha()
Bgs = [bgT_surf, bgF_surf]
bg_surf = pygame.image.load('bg.png').convert_alpha()
bg_rect = bg_surf.get_rect(center = (400, 200))

z = 3
font = pygame.font.Font('Pixeltype.ttf', 50)
deffont = pygame.font.Font(None, 50)

score = 0
Hscore = 0
game_active = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                bird_velo = 0
                bird_velo += 4
        else:
            if event.type == pygame.KEYDOWN:
                game_active = True
                Bg_change()
    if game_active:
        while bird_rect.x != 200:
            bird_rect.x -= 2
            screen.blit(bgF_surf, bg_rect)
            screen.blit(bird_surf, bird_rect)
            pygame.display.update()
            clock.tick(60)
        if pillerD_rect.x <= -100:
            z = randint(1, 5)
            pillerD_rect.x = 850
            pillerU_rect.x = 850
            obspeed += 0.5
            score += 1
        if z == 1:
            pillerD_rect.top = -50
            pillerU_rect.top = 400
        if z == 2:
            pillerD_rect.top = -150
            pillerU_rect.top = 300
        if z == 3:
            pillerD_rect.top = -175
            pillerU_rect.top = 275
        if z == 4:
            pillerD_rect.top = -225
            pillerU_rect.top = 325
        if z == 5:
            pillerD_rect.top = -400
            pillerU_rect.bottom = 425

        screen.blit(bg_surf, bg_rect)
        screen.blit(pillerU_surf, pillerU_rect)
        pillerU_rect.x -= obspeed

        screen.blit(pillerD_surf, pillerD_rect)
        pillerD_rect.x -= obspeed

        screen.blit(bird_surf, bird_rect)
        bird_rect.y -= bird_velo
        bird_velo += bird_grav

        score_text = font.render(f'Score: {score}', False, 'White')
        score_text_rect = score_text.get_rect(midbottom=(400, 100))
        screen.blit(score_text, score_text_rect)

        if bird_rect.colliderect(pillerD_rect or pillerU_rect):
            game_active = False
        pygame.display.update()
        clock.tick(60)
        bird_animation()
        if bird_rect.collidepoint(200, 450):
            game_active = False
    elif game_active == False:
        if score > Hscore:
            Hscore = score
        Bg_change()
        screen.blit(bg_surf, bg_rect)
        pillerD_rect.x = 850
        pillerU_rect.x = 850

        score_text = font.render('Press any key to start', False, 'gold')
        score_text_rect = score_text.get_rect(midbottom=(400, 100))
        screen.blit(score_text, score_text_rect)
        if Hscore == 0:
            score2_text = deffont.render('Welcome To Flap Of Bird', True, 'gold')
            score2_text_rect = score_text.get_rect(midbottom=(375, 350))
            screen.blit(score2_text, score2_text_rect)
        else:
            score2_text = deffont.render(f'High Score: {Hscore}', True, 'black')
            score2_text_rect = score_text.get_rect(midbottom=(475, 300))
            screen.blit(score2_text, score2_text_rect)

        screen.blit(bird_surf, bird_rect)
        bird_rect.center = 400, 200

        pygame.display.update()
        clock.tick(60)
