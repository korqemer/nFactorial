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
        self.game_over = False

        self.fireboy_x
        self.fireboy_y
        self.watergirl_x
        self.watergirl_y

        self.watergirl_success = False
        self.fireboy_success = False
        self.total_success = False

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

                    self.fireboy_x = x
                    self.fireboy_y = y


                # watergirl
                if cell == "W":
                    waterGirlSprite = WaterGirl((x, y))
                    self.watergirl.add(waterGirlSprite)
                    self.watergirl_x = x
                    self.watergirl_y = y

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
                if cell == "U":
                    tile = Tile((x,y), tile_size, cell)
                    self.tiles.add(tile)
                if cell == "O":
                    tile = Tile((x,y), tile_size, cell)
                    self.tiles.add(tile)


    def game_ender(self):
        self.game_over = True

        self.fireboy.sprite.rect.x = self.fireboy_x
        self.fireboy.sprite.rect.y = self.fireboy_y

        self.watergirl.sprite.rect.x = self.watergirl_x
        self.watergirl.sprite.rect.y = self.watergirl_y


    def horizontal_movement_collision(self):
        fireboy = self.fireboy.sprite
        fireboy.rect.x += fireboy.direction.x * fireboy.speed

        # boundaries
        if fireboy.rect.x <= 0:
            fireboy.rect.x = 0
        elif fireboy.rect.right - 5 >= screen_width:
            fireboy.rect.right = screen_width

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(fireboy.rect):
                if sprite.type == "X":
                    if fireboy.direction.x < 0:
                        fireboy.rect.left = sprite.rect.right
                    elif fireboy.direction.x > 0:
                        fireboy.rect.right = sprite.rect.left
                elif sprite.type == "B" or sprite.type == "Y":
                    self.game_ender()
                elif sprite.type == "U":
                    self.fireboy_success = True



        watergirl = self.watergirl.sprite
        watergirl.rect.x += watergirl.direction.x * watergirl.speed

        # boundaries
        if watergirl.rect.x <= 0:
            watergirl.rect.x = 0
        elif watergirl.rect.right - 5 >= screen_width:
            watergirl.rect.right = screen_width

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(watergirl.rect):
                if sprite.type == "X":
                    if watergirl.direction.x < 0:
                        watergirl.rect.left = sprite.rect.right
                    elif watergirl.direction.x > 0:
                        watergirl.rect.right = sprite.rect.left
                elif sprite.type == "A" or sprite.type == "Y":
                    self.game_ender()
                elif sprite.type == "O":
                    self.watergirl_success = True

    def is_success(self):
        self.total_success = self.watergirl_success and self.fireboy_success
        self.fireboy.sprite.rect.x = self.fireboy_x
        self.fireboy.sprite.rect.y = self.fireboy_y

        self.watergirl.sprite.rect.x = self.watergirl_x
        self.watergirl.sprite.rect.y = self.watergirl_y


    def vertical_movement_collision(self):
        fireboy = self.fireboy.sprite
        fireboy.apply_gravity()
        # boundaries
        if fireboy.rect.top <= 0:
            fireboy.rect.top = 0
        elif fireboy.rect.top >= screen_height:
            fireboy.rect.top = screen_height

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

        #boundaries

        if watergirl.rect.top <= 0:
            watergirl.rect.top = 0
        elif watergirl.rect.top >= screen_height:
            watergirl.rect.top = screen_height

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


    def run(self):
        self.tiles.draw(self.display_surface)
        self.fireboy.update()
        self.watergirl.update()

        self.fireboy.draw(self.display_surface)
        self.watergirl.draw(self.display_surface)

        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.is_success()








