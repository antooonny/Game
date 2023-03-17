import pygame
from sys import exit

def display_score():
    curr_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = score.render(f'Score: {curr_time}', False, (64, 64, 64)).convert_alpha()
    score_rec = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rec)
    print(curr_time)
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Experimental Game!')
clock = pygame.time.Clock()
game_active = True
start_time = 0
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

score = pygame.font.Font('font/Pixeltype.ttf', 50)


sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (40, 300))

player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player.get_rect(midbottom = (300, 300))
player_gravity = 0

snail_x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game_active:
        screen.blit(sky, (0,0))
        screen.blit(ground, (0,300))
        screen.blit(snail_surface, snail_rectangle)
        display_score()
        snail_rectangle.left+=1

        mouse_pos = pygame.mouse.get_pos()
        if player_rectangle.collidepoint(mouse_pos):
            player_rectangle.x = 800

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] == 1 and player_rectangle.bottom == 300:
            player_gravity = -20

        player_gravity+=1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player, player_rectangle)

        if snail_rectangle.colliderect(player_rectangle):
            game_active = False

    else:

        screen.fill("black")
        if pygame.key.get_pressed()[pygame.K_SPACE] == 1:
            game_active = True
            snail_rectangle.left = 0
            start_time = int(pygame.time.get_ticks()/1000)
    pygame.display.update()
    clock.tick(60)