import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, type):
        super().__init__()
        self.type = type
        self.image = pygame.Surface((size, size))
        if type == "X":
            self.image = pygame.image.load("graphics/brick-wall.png").convert_alpha()
            self.rect = self.image.get_rect(topleft = pos)
        if type == "B":
            self.image = pygame.image.load("graphics/water.png").convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
        if type == "A":
            self.image = pygame.image.load("graphics/lava.png").convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
        if type == "Y":
            self.image = pygame.image.load("graphics/poison.png").convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
