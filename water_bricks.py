import pygame

class WaterBricks(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("graphics/water_bricks.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
