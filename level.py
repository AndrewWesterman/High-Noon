# Author:
# Andrew Westerman
# awesterman@csu.fullerton.edu
# CS 386: Final Project
# Module info:
# level.py: Object that contains the game game level.


import pygame
from constants import *
from platform import *

class Level():

    def __init__(self, players):
        self.player1 = players[0]
        self.player2 = players[1]
        self.platform_list = pygame.sprite.Group()  
        self.background = pygame.image.load(BACKGROUND)      

        level = [[193, 5, 0, 300, BLUE],
                 [175, 5, 205, 450, BLUE],
                 [210, 5, 805, 315, BLUE],
                 [65, 5, 145, 190, BLUE],
                 [55, 5, 805, 190, BLUE],
                 [70, 5, 385, 175, BROWN],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1], platform[4])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player1 = self.player1
            block.player2 = self.player2
            self.platform_list.add(block)

    def update(self):
        self.platform_list.update()

    def draw(self, screen): 
        screen.fill(BLACK)       
        screen.blit(self.background, [0,75])
        self.platform_list.draw(screen)