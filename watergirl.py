import pygame


class WaterGirl (pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("graphics/2.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        #movement
        self.jump_speed = -10
        self.gravity = 0.8
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_w]:
            self.jump()
        else:
            self.direction.x = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed


