import pygame as py
from settings import *

from pygame.sprite import Group


class Player(py.sprite.Sprite):
   
    def __init__(self, game):
        self.groups = self.game.all_sprites
        super().__init__(self.groups)
        self.game = game