import pygame
from tiles import Tile
from settings import tile_size, screen_width, screen_height
from fireboy import FireBoy

class Level(pygame.sprite.Sprite):

    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.fireboy = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "X":
                    tile = Tile((x, y), tile_size, "grey")
                    self.tiles.add(tile)
                if cell == "F":
                    fireboySprite = FireBoy((x, y))
                    self.fireboy.add(fireboySprite)
                if cell == "A":
                    tile = Tile((x, y), tile_size, "red")
                    self.tiles.add(tile)

    def horizontal_movement_collision(self):
        fireboy = self.fireboy.sprite
        fireboy.rect.x += fireboy.direction.x * fireboy.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(fireboy.rect):
                if fireboy.direction.x < 0:
                    fireboy.rect.left = sprite.rect.right
                elif fireboy.direction.x > 0:
                    fireboy.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        fireboy = self.fireboy.sprite
        fireboy.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(fireboy.rect):
                if fireboy.direction.y > 0:
                    fireboy.rect.bottom = sprite.rect.top
                    fireboy.direction.y = 0
                elif fireboy.direction.y < 0:
                    fireboy.rect.top = sprite.rect.bottom
                    fireboy.direction.y = 0

    def run(self):
        self.tiles.draw(self.display_surface)

        self.fireboy.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.fireboy.draw(self.display_surface)




