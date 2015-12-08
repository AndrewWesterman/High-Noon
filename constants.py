# Author:
# Andrew Westerman
# awesterman@csu.fullerton.edu
# CS 386: Final Project
# Module info:
# constants.py: holds all constants used by the game


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE  = (0, 10, 255)
BROWN = (171, 135, 89)

#Define screen size
WIDTH = 1000
HEIGHT = 700

#Define player directions
PLAYER_LEFT = "L"
PLAYER_RIGHT = "R"

#Define img file names
P1_LSPRITE = "assets/p1_L.png"
P1_RSPRITE = "assets/p1_R.png"
P2_LSPRITE = "assets/p2_L.png"
P2_RSPRITE = "assets/p2_R.png"
BACKGROUND = "assets/background.png"
LOGO = "assets/highnoon_logo.png"           #Logo Property of HighNoon Casino


#Define status bar size
STATUS_HEIGHT = 200

#Define level height
LEVEL_HEIGHT = HEIGHT - STATUS_HEIGHT + 75

#Define player spawns
P1_SPAWN = 100
P2_SPAWN = WIDTH - 100

#Define bullet speed
BULLET_SPEED = 15

#Define sound effects
SFX_BULLET = "assets/sfx_shoot.mp3"