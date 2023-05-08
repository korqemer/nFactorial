import pygame


class Player (pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.image.load()
        self.rect = self.image.get_rect(topleft = pos)
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            pass
        elif keys[pygame.K_LEFT]:
            pass
        else:
            pass
