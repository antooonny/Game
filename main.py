import pygame
from sys import exit
import random

def display_score():
    curr_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = score.render(f'Score: {curr_time}', False, (64, 64, 64)).convert_alpha()
    score_rec = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rec)
    return curr_time

def obstacle_movement(o_list):
    if o_list:
        for obstacle_rect in o_list:
            obstacle_rect.x -= 5
            screen.blit(snail_surface, obstacle_rect)

        o_list = [obstacle for obstacle in o_list if obstacle.x > 0]
        return o_list

    else:
        return []

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Experimental Game!')
clock = pygame.time.Clock()
game_active = False
start_time = 0
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

score = pygame.font.Font('font/Pixeltype.ttf', 50)
title = pygame.font.Font('font/Pixeltype.ttf', 50)
title_surf = title.render("This is my game!", False, 'black').convert_alpha()
title_rec = title_surf.get_rect(center = (400, 50))

start = pygame.font.Font('font/Pixeltype.ttf', 50)
start_surf = start.render("Press spacebar to start !", False, 'black').convert_alpha()
start_rec = start_surf.get_rect(center = (400, 350))

sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()


snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (40, 300))
obstacle_list = []

player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player.get_rect(midbottom = (300, 300))
player_gravity = 0

player_dupe = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_dupe = pygame.transform.scale2x(player_dupe)
player_dupe_rect = player_dupe.get_rect(center = (400, 200))
snail_x = 0
score2 = 0

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == obstacle_timer and game_active:
            print('test')
            obstacle_list.append(snail_surface.get_rect(bottomright = (random.randint(1100,1500), 300)))

    if game_active:



        screen.blit(sky, (0,0))
        screen.blit(ground, (0,300))
        screen.blit(snail_surface, snail_rectangle)
        score2 = display_score()

        mouse_pos = pygame.mouse.get_pos()
        if player_rectangle.collidepoint(mouse_pos):
            player_rectangle.x = 800

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] == 1 and player_rectangle.bottom == 300:
            player_gravity = -20

        player_gravity+=1
        player_rectangle.y += player_gravity

        obstacle_list = obstacle_movement(obstacle_list)

        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player, player_rectangle)

        if snail_rectangle.colliderect(player_rectangle):
            game_active = False

    else:

        screen.fill((94,129,162))
        screen.blit(player_dupe, player_dupe_rect)
        screen.blit(start_surf, start_rec)
        score_mes = test_font.render(f'Your score: {score2}', False, 'black')
        score_mes_rec = score_mes.get_rect(center = (400, 320))
        if score2 == 0:
            screen.blit(title_surf, title_rec)

        else:
            screen.blit(score_mes, score_mes_rec)

        if pygame.key.get_pressed()[pygame.K_SPACE] == 1:
            game_active = True
            snail_rectangle.left = 0
            start_time = int(pygame.time.get_ticks()/1000)
    pygame.display.update()
    clock.tick(60)