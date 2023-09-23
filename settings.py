# ******* Almennar stillingar ******

TITLE = "Platformer"
WIDTH, HEIGTH = 640, 360
FPS = 60
BOUNDARYx = 256
BOUNDARYy = 72

# **** Pallar****
PLATFORMS = [[0, HEIGTH-20, WIDTH, 20],
             [80, 50, 200, 20], 
             [516, 154, 90, 20],
             [300, 250, 100, 20]]


# ***** Litir *****

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
YELLOW = (226, 232, 21)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


# ******* Eiginleikar sýndarheims ****

GRAVITY = 0.5 # Þyngdarhröðun [dílar/ramma^2]
DRAG = 0.05 #  Loftmótstaða

# Loftmótsaða

# ******* Eiginliekar hetju ******
ACC = 0.25 # Hröðun hetjunnar (acceleration)


# ****** Eiginleikar óvina *****
MOB_ACC = 0.15 # Hröðun óvina (mobile units)
BOSS_ACC = 0.30 
