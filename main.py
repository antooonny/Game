import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Experimental Game!')
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
score = pygame.font.Font('font/Pixeltype.ttf', 50)
score_surface = score.render('Score', False, 'black').convert_alpha()
score_rec = score_surface.get_rect(center = (400, 200))

sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('Testing', False, 'black').convert()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (40, 300))

player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player.get_rect(midbottom = (300, 300))
snail_x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky, (0,0))
    screen.blit(ground, (0,300))
    screen.blit(text_surface, (350, 0))
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player, player_rectangle)
    screen.blit(score_surface, score_rec)
    snail_rectangle.left+=1
    # if player_rectangle.colliderect(snail_rectangle):
    #     player_rectangle.x = 800
    mouse_pos = pygame.mouse.get_pos()
    if player_rectangle.collidepoint(mouse_pos):
        player_rectangle.x = 800

    pygame.display.update()
    clock.tick(60)