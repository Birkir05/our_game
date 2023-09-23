import pygame as py
from settings import *

from pygame.sprite import Group
vec = py.math.Vector2

class Player(py.sprite.Sprite):
   
    def __init__(self, game):
        self.groups = self.game.all_sprites
        super().__init__(self.groups)
        self.game = game

    def update(self): # Kallað á update fallið fyrir hvern ramma sem líður
        self.acc = vec(0, GRAVITY)

        keys = py.key.get_pressed()
        if keys[py.K_d]:
            self.acc.x = ACC
        if keys[py.K_a]:
            self.acc.x = -ACC

        # Loftmótstaðan, hefur áhrif á hröðun, meiri hraði =>  meiri mótstaða
        self.acc.x -= self.vel.x * DRAG

        # Geymum gömlu staðsetninguna
        old_pos = self.pos

        # Uppærum staðsetningu
        # x = 1/2*a*t^2 +v_0t +x_0 (t = 1 rammi)
        self.pos = 0.5*self.acc + self.vel + self.po
        

    def jump(self):
        self.vel.y = -13 # Látum hann fá hraða upp
    

    
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



