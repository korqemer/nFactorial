import pygame
from tiles import Tile
from settings import tile_size, screen_width, screen_height
from fireboy import FireBoy
from watergirl import WaterGirl
from water_bricks import WaterBricks
from fire_bricks import FireBricks

class Level(pygame.sprite.Sprite):

    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.fireboy = pygame.sprite.GroupSingle()
        self.watergirl = pygame.sprite.GroupSingle()
        self.waterbricks = pygame.sprite.Group()
        self.firebricks = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                # ordinary bricks
                if cell == "X":
                    tile = Tile((x, y), tile_size)
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
                    waterBricksSprite = WaterBricks((x,y), tile_size)
                    self.waterbricks.add(waterBricksSprite)

                # fire bricks
                if cell == "A":
                    fireBricksSprite = FireBricks((x,y), tile_size)
                    self.firebricks.add(fireBricksSprite)



    def horizontal_movement_collision(self):
        fireboy = self.fireboy.sprite
        fireboy.rect.x += fireboy.direction.x * fireboy.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(fireboy.rect):
                if fireboy.direction.x < 0:
                    fireboy.rect.left = sprite.rect.right
                elif fireboy.direction.x > 0:
                    fireboy.rect.right = sprite.rect.left

        watergirl = self.watergirl.sprite
        watergirl.rect.x += watergirl.direction.x * watergirl.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(watergirl.rect):
                if watergirl.direction.x < 0:
                    watergirl.rect.left = sprite.rect.right
                elif watergirl.direction.x > 0:
                    watergirl.rect.right = sprite.rect.left

        for sprite in self.waterbricks.sprites():
            if fireboy.rect.colliderect(sprite.rect):
                print("water")


        for sprite in self.firebricks.sprites():
            if watergirl.rect.colliderect(sprite.rect):
                print("lava")
              

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


        watergirl = self.watergirl.sprite
        watergirl.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(watergirl.rect):
                if watergirl.direction.y > 0:
                    watergirl.rect.bottom = sprite.rect.top
                    watergirl.direction.y = 0
                elif watergirl.direction.y < 0:
                    watergirl.rect.top = sprite.rect.bottom
                    watergirl.direction.y = 0

        for sprite in self.waterbricks.sprites():
            if sprite.rect.colliderect(fireboy.rect):
                print("water")


        for sprite in self.firebricks.sprites():
            if sprite.rect.colliderect(watergirl.rect):
                print("lava")



    def run(self):
        self.tiles.draw(self.display_surface)

        self.fireboy.update()
        self.watergirl.update()

        self.fireboy.draw(self.display_surface)
        self.watergirl.draw(self.display_surface)

        self.waterbricks.draw(self.display_surface)
        self.firebricks.draw(self.display_surface)

        self.horizontal_movement_collision()
        self.vertical_movement_collision()





