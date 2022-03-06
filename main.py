import pygame, sys

from pygame import *
from scripts.settings import *
from scripts.tile_map import *
from scripts.game_data import *
from scripts.entity import Boss, Player
from scripts.gui import *

from random import randint

pygame.display.set_caption(WIN_CAPTION)
screen = pygame.display.set_mode(WIN_SIZE, 0, 32)
display = pygame.Surface(WIN_SIZE)

orb_img = pygame.image.load("data/img/healing_orb/health/red_orb.png")
orb_img.set_colorkey((0, 0, 0))
orb_sprite = pygame.transform.scale(orb_img, (22, 22))

# classes --------------------------------------------------------------------------- #
class Orb(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = orb_sprite
        self.rect = self.image.get_rect(topleft = pos)

# variables ------------------------------------------------------------------------- #
map = TileMap(stage, screen)

player = Player(200, 200)
boss = Boss(250, 100)

gui_health = Health((15, 15))

orb_group = pygame.sprite.Group()

# randomization of obj/s ------------------------------------------------------------ #
for i in range(1):
    random_x = randint(100,480)
    random_y = randint(120,380)
    Orb((random_x, random_y), orb_group)

# functions ------------------------------------------------------------------------- #
def redraw_win():
    screen.blit(display, (0, 0))
    
    map.run()
    
    gui_health.draw(screen)
    
    orb_group.update()
    orb_group.draw(screen)
    
    player.draw(screen)
    boss.draw(screen)
    
    pygame.display.update()

# game loop ------------------------------------------------------------------------- #
while True:
    display.fill((0, 0, 0,)) # background
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0)) # scale bg
    
    player.get_status()
    
    # key event --------------------------------------------------------------------- #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_UP:
                player.status(True, "up")
            if event.key == K_DOWN:
                player.status(True, "down")
            if event.key == K_RIGHT:
                player.status(True, "right")
            if event.key == K_LEFT:
                player.status(True, "left")
                
        if event.type == KEYUP:
            if event.key == K_UP:
                player.status(False, "up")
            if event.key == K_DOWN:
                player.status(False, "down")
            if event.key == K_RIGHT:
                player.status(False, "right")
            if event.key == K_LEFT:
                player.status(False, "left")
    
    redraw_win()
    WIN_FPS.tick(60)    