import pygame

x_tile_number = 10
tile_size = 64

screen_height = x_tile_number * tile_size
screen_width = 500

WIN_SIZE = ((screen_height+3), screen_width)
WIN_CAPTION = "Game Window"
WIN_FPS = pygame.time.Clock()