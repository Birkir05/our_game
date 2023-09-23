import pygame as py
from settings import *
from sprites import *


# ****** Leikjavélin *****
class Game:

    def __init__(self):
        py.init()                    # Ræsum pygame
        self.clock = py.time.Clock() # Klukka

        py.display.set_caption(TITLE)   # Titill glugga / leiks
        self.screen = py.display.set_mode((WIDTH, HEIGTH), py.FULLSCREEN|py.SCALED) #Gluggin
        self.running = True

    def new(self):
        # ****** upphafsstillum leik ******
        # Búum til tóm kvikasöfn 
        self.all_sprites = py.sprite.Group()    # Allt sem á að teikna
        self.all_platforms = py.sprite.Group()  # Allir pallar

        # Búum til kvika sem er til í upphafi
        self.player = Player(self) # senda inn allt í klasanum Game - föll og breytur
                                   # inn í Player klasan í sprites skjali

        # Búum til palla
        


    # Skoðar atburði 
    def events(self):
        for e in py.event.get():
            if e.type == py.QUIT:
                self.running = False
            if e.type == py.KEYDOWN and e.key == py.K_q:
                self.running = False
            if e.type == py.KEYDOWN and e.key == py.K_SPACE:
                self.player.jump()

    # uppfærir kvika/fígúrur
    def update(self):
        self.all_sprites.update()


    # Teiknum allt
    def draw(self):
        self.screen.fill(BLACK)            # Bakgrunnur
        self.all_sprites.draw(self.screen) # Fígúrur teiknaðar í glugga

        py.display.flip()                  # Sýnum sem hefur verið teiknað
        

# ***** Leikjalykkja ****

game = Game() # Búum til leik
game.new() # Upphafsstillum leik

while game.running:

    game.events() # Vinnum úr atburðum
    game.update() # Uppfærum sýndarheim
    game.draw()   # Teiknum allt
    game.clock.tick(FPS) # Svæfum lykkjuna ef þess þarf 

py.quit()