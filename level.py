import pygame
from tiles import Tile
from settings import tile_size, screen_width, screen_height
from fireboy import FireBoy
from watergirl import WaterGirl



class Level(pygame.sprite.Sprite):

    def __init__(self, level_data, surface):
        super().__init__()
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.fireboy = pygame.sprite.GroupSingle()
        self.watergirl = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                # ordinary bricks
                if cell == "X":
                    tile = Tile((x, y), tile_size, cell)
                    self.tiles.add(tile)
                # fireboy
                if cell == "F":
                    fireboySprite = FireBoy((x, y))
                    self.fireboy.add(fireboySprite)
                # watergirl
                if cell == "W":
                    waterGirlSprite = WaterGirl((x, y))
                    self.watergirl.add(waterGirlSprite)
                # water bricks
                if cell == "B":
                    tile = Tile((x, y), tile_size, cell)
                    self.tiles.add(tile)
                # fire bricks
                if cell == "A":
                    tile = Tile((x, y), tile_size, cell)
                    self.tiles.add(tile)

                #poison bricks
                if cell == "Y":
                    tile = Tile((x, y), tile_size, cell)
                    self.tiles.add(tile)


    def horizontal_movement_collision(self):
        fireboy = self.fireboy.sprite
        fireboy.rect.x += fireboy.direction.x * fireboy.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(fireboy.rect):
                if sprite.type == "X":
                    if fireboy.direction.x < 0:
                        fireboy.rect.left = sprite.rect.right
                    elif fireboy.direction.x > 0:
                        fireboy.rect.right = sprite.rect.left
                elif sprite.type == "B" or sprite.type == "Y":
                    self.game_ender()

        watergirl = self.watergirl.sprite
        watergirl.rect.x += watergirl.direction.x * watergirl.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(watergirl.rect):
                if sprite.type == "X":
                    if watergirl.direction.x < 0:
                        watergirl.rect.left = sprite.rect.right
                    elif watergirl.direction.x > 0:
                        watergirl.rect.right = sprite.rect.left

                elif sprite.type == "A" or sprite.type == "Y":
                    self.game_ender()


    def vertical_movement_collision(self):
        fireboy = self.fireboy.sprite
        fireboy.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(fireboy.rect):
                if sprite.type == "X":
                    if fireboy.direction.y > 0:
                        fireboy.rect.bottom = sprite.rect.top
                        fireboy.direction.y = 0
                    elif fireboy.direction.y < 0:
                        fireboy.rect.top = sprite.rect.bottom
                        fireboy.direction.y = 0
                elif sprite.type == "B" or sprite.type == "Y":
                    self.game_ender()

        watergirl = self.watergirl.sprite
        watergirl.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(watergirl.rect):
                if sprite.type == "X":
                    if watergirl.direction.y > 0:
                        watergirl.rect.bottom = sprite.rect.top
                        watergirl.direction.y = 0
                    elif watergirl.direction.y < 0:
                        watergirl.rect.top = sprite.rect.bottom
                        watergirl.direction.y = 0
                elif sprite.type == "A" or sprite.type == "Y":
                    self.game_ender()

    def game_ender(self):
        # problem with returning to menu
        pygame.quit()
        exit()

    def run(self):
        self.tiles.draw(self.display_surface)
        self.fireboy.update()
        self.watergirl.update()

        self.fireboy.draw(self.display_surface)
        self.watergirl.draw(self.display_surface)

        self.horizontal_movement_collision()
        self.vertical_movement_collision()







