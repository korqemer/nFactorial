import pygame

class WaterBricks(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("Light Blue")
        self.rect = self.image.get_rect(topleft = pos)
