import pygame, sys
from settings import *
from tiles import Tile
from level import Level


pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
level = Level(level_map, screen)

pygame.display.set_caption("Fireboy and Watergirl")

sound_effect = pygame.mixer.Sound("audio/audio.mp3")

sound_effect.play(loops =- 1)
#intro screen

font = pygame.font.Font(None, 36)
game_name = font.render("Fireboy and Watergirl", False, "Black")
game_name_reck = game_name.get_rect(center = (550, 130))

player_stand = pygame.image.load("graphics/fireboy-and-watergirl-removebg-preview.png").convert_alpha()
player_stand_scaled = pygame.transform.scale(player_stand, (250, 245))
player_stand_rect = player_stand_scaled.get_rect(center = (550, 260))

game_message = font.render("Click Space to start a game", False, "Black")
game_message_reck = game_message.get_rect(center = (550, 400))

screen_dictionary = {
    1, "menu",
    2, "game over",
    3, "pause",
    4, "level 1"
}

state = 4
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((135, 206, 235))

    if state == 4:
        level.run()
    elif state == 1:
        screen.fill((135, 206, 235))
        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(game_name, game_name_reck)
        screen.blit(game_message, game_message_reck)


    pygame.display.update()
    clock.tick(60)
