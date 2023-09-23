import pygame as py
from settings import *

from pygame.sprite import Group
vec = py.math.Vector2

class Player(py.sprite.Sprite):
   
    def __init__(self, game):
        self.groups = self.game.all_sprites
        super().__init__(self.groups)
        self.game = game
    
    # Pallar
    class Platform(py.sprite.Sprite):
    # x,y -> efra vinstra horn, width -> breidd
        def __init__(self, game, x, y, width, height):
            self.groups = game.all_sprites, game.all_platforms
            super().__init__(self.groups)

            self.image = py.Surface((width, height)) #yfirborðið/rétthyrningur
            self.image.fill(RED)
            self.rect = self.image.get_rect()   # rammi
            self.rect.topleft = vec(x, y)