from platform import platform
import pygame

from csv import *
from .game_data import stage
from .settings import tile_size
from .tile import StaticTile

# game_data (map) -------------------------------------------------------------------- #
tile_wall = "data/img/platform/wall.png"
tile_floor = "data/img/platform/floor.png"
tile_lc_ceiling = "data/img/lc_ceiling.png"
tile_rc_ceiling = "data/img/rc_ceiling.png"
tile_ll_ceiling = "data/img/ll_ceiling.png"
tile_rl_ceiling = "data/img/rl_ceiling.png"

# classes --------------------------------------------------------------------------- #
class Map:
    def __init__(self, lvl, screen):
        self.screen = screen
        self.world_shift = 0
        layout = []
        items = []
        self.sprites = []
        for item in stage:
            items.append(item)
            
            obj = load_map(lvl[item]) # store dictionary to a variable
            layout.append(list(obj)) # list all variables
            
            map_sprite = self.group_tiles(obj, item)
            self.sprites.append(map_sprite)

    def group_tiles(self, lyt, type):
        sprite_group = pygame.sprite.Group()
        
        for row_i, row in enumerate(lyt):
            for col_i, v in enumerate(row):
                if v == "0":
                    x = col_i * tile_size
                    y = row_i * tile_size

                    print(row)
                    
                    items = ["wall", "floor"]
                    
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

    def draw(self):
        for sprite in self.sprites:
            sprite.update(self.world_shift)
            sprite.draw(self.screen)

# support --------------------------------------------------------------------------- #
def load_map(path):
    platform_map = []
    with open(path) as map:
        level = reader(map, delimiter = ",")
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

