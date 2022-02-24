import pygame, sys

from scripts.tilesheet import Tilesheet
from pygame import *

pygame.init()

clock = pygame.time.Clock()

WINDOW_SIZE = (500,500)

pygame.display.set_caption("Game Window")
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window
display = pygame.Surface(WINDOW_SIZE)

font = pygame.font.Font("data/font/pixelM-10-reg.ttf", 50)

# images
tiles = Tilesheet("data/img/sprite_tiles.png", 16, 16, 2, 3)

player_img = pygame.image.load("data/img/player.png").convert()
player_img.set_colorkey((0,0,0))
player = pygame.transform.scale(player_img,(35,45))

ghost_img = pygame.image.load("data/img/ghost.png").convert()
ghost_img.set_colorkey((0,0,0))
ghost = pygame.transform.scale(ghost_img,(65,60))

# class
class Character:
    def __init__(self, x, y, health=3):
        self.x = x
        self.y = y
        self.health = health
        self.character_img = None
    
    def draw(self, screen):
        screen.blit(self.character_img,(self.x, self.y))

class Player(Character):
    def __init__(self, x, y, health=3):
        super().__init__(x, y, health)
        self.character_img = player

class Ghost(Character):
    def __init__(self, x, y, health=3):
        super().__init__(x, y, health)
        self.character_img = ghost

# function
def redraw_window():
    screen.blit(display,(0,0))
    
    player.draw(screen)
    
    ghost.draw(screen)
    
    #tiles.draw(screen)
    treasure = tiles.get_tile(0, 1)
    
    tile_wall = tiles.get_tile(0, 0)
    wall = pygame.transform.scale(tile_wall, (80, 80))
    tile_floor = tiles.get_tile(1, 0)
    floor = pygame.transform.scale(tile_floor, (80, 80))
    
    #screen.blit(treasure,(0, 0))
    screen.blit(wall,(100, 80))
    screen.blit(floor,(100, 160))
    
    
    pygame.display.update()

# game-loop variables
move_up = False
move_down = False
move_left = False
move_right = False

player_vel = 3 # velocity

player = Player(200,200)
ghost = Ghost(300,300)

# main - game loop
while True:
    display.fill((25,27,26))
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0,0))
    
    # key variable event
    if move_up == True and player.y - player_vel > 0:
        player.y -= player_vel
    if move_down == True and player.y + player_vel < WINDOW_SIZE[1]:
        player.y += player_vel
    if move_left == True and player.x - player_vel > 0:
        player.x -= player_vel
    if move_right == True and player.x + player_vel < WINDOW_SIZE[0]:
        player.x += player_vel
    
    # key event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_UP:
                move_up = True
            if event.key == K_DOWN:
                move_down = True
            if event.key == K_LEFT:
                move_left = True
            if event.key == K_RIGHT:
                move_right = True

        if event.type == KEYUP:
            if event.key == K_UP:
                move_up = False
            if event.key == K_DOWN:
                move_down = False
            if event.key == K_LEFT:
                move_left = False
            if event.key == K_RIGHT:
                move_right = False
    
    redraw_window()
    clock.tick(60)