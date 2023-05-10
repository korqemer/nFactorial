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

font = pygame.font.Font("font/open_sans.ttf", 36)
smaller_font = pygame.font.Font("font/open_sans.ttf", 24)
smallest_font = pygame.font.Font("font/open_sans.ttf", 18)


game_name = font.render("Fireboy and Watergirl", False, "Black")
game_name_reck = game_name.get_rect(center = (550, 130))

player_stand = pygame.image.load("graphics/fireboy-and-watergirl-removebg-preview.png").convert_alpha()
player_stand_scaled = pygame.transform.scale(player_stand, (150, 145))
player_stand_rect = player_stand_scaled.get_rect(center = (560, 260))

level1_buttom = font.render("Level 1", False, "Black")
level1_buttom_rect = level1_buttom.get_rect(center = (400, 450))
level2_buttom = font.render("Level 2", False, "Black")
level2_buttom_rect = level2_buttom.get_rect(center = (700, 450))

game_messsage = smaller_font.render("this game was created for nFactorial entrace exam", False, "Blue")
game_messsage_rect = game_messsage.get_rect(center = (560, 550))

game_messsage2 = smallest_font.render("by Miras N.", False, "Blue")
game_messsage2_rect = game_messsage.get_rect(center = (775, 590))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if level1_buttom_rect.collidepoint(event.pos):
                print("Level 1 clicked!")
            if level2_buttom_rect.collidepoint(event.pos):
                print("Level 2 clicked!")

    screen.fill((135, 206, 235))

    if not True:
        level.run()
    else:
        screen.fill(("white"))
        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(game_name, game_name_reck)
        screen.blit(level1_buttom, level1_buttom_rect)
        screen.blit(level2_buttom, level2_buttom_rect)
        screen.blit(game_messsage, game_messsage_rect)
        screen.blit(game_messsage2, game_messsage2_rect)



    pygame.display.update()
    clock.tick(60)
