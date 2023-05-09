import pygame, sys
from settings import *
from tiles import Tile
from level import Level

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
level = Level(level_map, screen)


pygame.display.set_caption("Fireboy and Watergirl")
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('Black')
    level.run()

    pygame.display.update()
    clock.tick(60)
