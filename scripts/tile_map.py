import pygame
from scripts.tile import *
from scripts.settings import *
from csv import reader

# image paths
tile_wall = "data/img/platform/wall.png"
tile_floor = "data/img/platform/floor.png"

class TileMap:
    def __init__(self, lvl, screen):
        self.screen = screen
        self.world_shift = 0
        self.current_x = None
        
        wall_lyt = load_map(lvl['wall'])
        self.wall_sprites = self.group_tiles(wall_lyt, 'wall')
        
        floor_lyt = load_map(lvl['floor'])
        self.floor_sprites = self.group_tiles(floor_lyt, 'floor')
    
    def group_tiles(self, lyt, type):
        sprite_group = pygame.sprite.Group()
        
        for row_i, row in enumerate(lyt):
            for col_i, v in enumerate(row):
                if v == "0":
                    x = col_i * tile_size
                    y = row_i * tile_size
                    
                    #print(row)
                    
                    items = ['wall', 'floor']
                    
                    if type == items[0]:
                        wall_tile_l = load_sprites(tile_wall)
                        tile_screen = wall_tile_l[int(v)]
                        sprite = StaticTile(tile_size, x, y, tile_screen)
                    
                    if type == items[1]:
                        floor_tile_l = load_sprites(tile_floor)
                        tile_screen = floor_tile_l[int(v)]
                        sprite = StaticTile(tile_size, x, y, tile_screen)
                    
                    sprite_group.add(sprite)
        
        return sprite_group
    
    def run(self):
        self.wall_sprites.update(self.world_shift)
        self.wall_sprites.draw(self.screen)
        
        self.floor_sprites.update(self.world_shift)
        self.floor_sprites.draw(self.screen)

# support functions for TileMap class
def load_map(path):
    platform_map = []
    with open(path) as map:
        level = reader(map, delimiter =",")
        for row in level:
            platform_map.append(list(row))
        return platform_map

def load_sprites(path):
    screen = pygame.image.load(path).convert_alpha()
    tile_num_x = int(screen.get_size()[0] / tile_size)
    tile_num_y = int(screen.get_size()[1] / tile_size)
    
    tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_screen = pygame.Surface((tile_size, tile_size))
            new_screen.blit(screen, (0,0), pygame.Rect(x, y, tile_size, tile_size))
            tiles.append(new_screen)
        
    return tiles
