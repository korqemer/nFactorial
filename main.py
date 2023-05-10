import pygame, sys
from settings import level_map
from tiles import Tile
from level import Level
from settings2 import level_map2

screen_width = 1152
screen_height = 786

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
tile_size = 64

clock = pygame.time.Clock()
level = Level(level_map, screen)
level2 = Level(level_map2, screen)

pygame.display.set_caption("Fireboy and Watergirl")

sound_effect = pygame.mixer.Sound("audio/audio.mp3")

sound_effect.play(loops =-1)

#intro screen
bigger_font = pygame.font.Font("font/open_sans.ttf", 48)
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

pause_messsage_main = smallest_font.render("to pause a game, click Escape", False, "Blue")
pause_messsage_main_rect = pause_messsage_main.get_rect(center = (560, 690))


# pause menu
pause_messsage = bigger_font.render("Pause", False, "White")
pause_messsage_rect = pause_messsage.get_rect(center = (560, 350))

pause_messsage2 = smallest_font.render("Don't forget to drink water and don't play with fire.", False, "White")
pause_messsage2_rect = pause_messsage2.get_rect(center = (560, 400))

return_buttom = font.render("To return, press Escape", False, "Red")
return_buttom_rect = return_buttom.get_rect(center = (560, 500))

menu_buttom = font.render("To go to Main Menu, press Q", False, "Red")
menu_rect = menu_buttom.get_rect(center = (560, 600))

state_dictionary = {
    1: "level1",
    2: "level2",
    3: "main menu",
    4: "pause",
    5: "game over",
    6: "next level"
}
prev_state = 3
state = 3
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if level1_buttom_rect.collidepoint(event.pos):
                state = 1
            elif level2_buttom_rect.collidepoint(event.pos):
                state = 2
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if state != 4:
                    prev_state = state
                    state = 4
                else:
                    state = prev_state
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            if state == 4:
                state = 3


    screen.fill((135, 206, 235))

    if state == 3:
        screen.fill(("white"))
        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(game_name, game_name_reck)
        screen.blit(level1_buttom, level1_buttom_rect)
        screen.blit(level2_buttom, level2_buttom_rect)
        screen.blit(game_messsage, game_messsage_rect)
        screen.blit(game_messsage2, game_messsage2_rect)
        screen.blit(pause_messsage_main, pause_messsage_main_rect)

    elif state == 1:
        level.run()
    elif state == 2:
        level2.run()
    # pause
    elif state == 4:
        screen.fill("Blue")
        screen.blit(pause_messsage, pause_messsage_rect)
        screen.blit(pause_messsage2, pause_messsage2_rect)
        screen.blit(return_buttom, return_buttom_rect)
        screen.blit(menu_buttom, menu_rect)

    pygame.display.update()
    clock.tick(60)
