import pygame

from .settings import *

# images ---------------------------------------------------------------------------- #
player_img = pygame.image.load("data/img/character/player.png")
player_img.set_colorkey((0, 0, 0))
player = pygame.transform.scale(player_img, (28, 36))

boss_img = pygame.image.load("data/img/entities/enemy/boss.png")
boss_img.set_colorkey((0, 0, 0))
boss = pygame.transform.scale(boss_img, (114, 114))

# classes --------------------------------------------------------------------------- #
class Entity:
    def __init__(self, x, y, health = 3) -> None:
        self.x = x
        self.y = y
        self.health = health
        self.character_img = None
        self.entity_vel = 0
        
    def draw(self, screen):
        screen.blit(self.character_img, (self.x, self.y))

class Player(Entity):
    def __init__(self, x, y, health=3):
        super().__init__(x, y, health)
        self.character_img = player
        self.entity_vel = 3
        
        # status
        self.on_ground = False
        self.on_wall = False
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
    
    def status(self, bool, string):
        if bool == True:
            key_pressed = bool
        else:
            key_pressed = bool
        
        if string == "up":
                self.moving_up = key_pressed
        if string == "down":
            self.moving_down = key_pressed
        if string == "right":
            self.moving_right = key_pressed
        if string == "left":
            self.moving_left = key_pressed

    def get_status(self):
        if self.moving_up == True and self.y - self.entity_vel - 100 > 0:
            self.y -= self.entity_vel
        if self.moving_down == True and self.y + self.entity_vel + 100 < WIN_SIZE[1]:
            self.y += self.entity_vel
        if self.moving_right == True and self.x + self.entity_vel + 100 < WIN_SIZE[0]:
            self.x += self.entity_vel
        if self.moving_left == True and self.x - self.entity_vel - 75 > 0:
            self.x -= self.entity_vel

class Boss(Entity):
    def __init__(self, x, y, health=3):
        super().__init__(x, y, health)
        self.character_img = boss
        self.entity_vel = 1