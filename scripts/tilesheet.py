import pygame

class Tilesheet:
    def __init__(self, file, w, h, row, col):
        raw_img = pygame.image.load(file).convert()
        raw_img.set_colorkey((155,173,183))
        self.tile_table = []
        for tile_x in range(0, col):
            line = []
            self.tile_table.append(line)
            for tile_y in range(0, row):
                rect = (tile_x * w, tile_y * h, w, h)
                line.append(raw_img.subsurface(rect))
    
    def draw(self, screen):
        for x, row in enumerate(self.tile_table):
            for y, tile in enumerate(row):
                screen.blit(tile, (x*16, y*16))
    
    def get_tile(self, x, y):
        return self.tile_table[x][y]