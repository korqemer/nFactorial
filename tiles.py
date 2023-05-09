import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        #self.image = pygame.image.load("graphics/brick-wall.png").convert_alpha()
        self.image = pygame.Surface((size, size))
        self.image.fill("Grey")
        self.rect = self.image.get_rect(topleft = pos)
