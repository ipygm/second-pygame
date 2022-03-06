import pygame

from .settings import tile_size

# images ---------------------------------------------------------------------------- #
lives_img = pygame.image.load("data/img/gui/lives.png")
lives_img.set_colorkey((0, 0, 0))
lives = pygame.transform.scale(lives_img, (145, 40))

# classes --------------------------------------------------------------------------- #
class Interface:
    def __init__(self, pos):
        self.pos = pos
        self.interface_img = None

class Health(Interface):
    def __init__(self, pos):
        super().__init__(pos)
        self.interface_img = lives_img
    
    def draw(self, screen):
        for i in range(3):
            lives_rect = lives.get_rect()
            lives_rect.topleft = self.pos
            screen.blit(lives, lives_rect)