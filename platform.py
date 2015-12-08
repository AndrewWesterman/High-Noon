# Author:
# Andrew Westerman
# awesterman@csu.fullerton.edu
# CS 386: Final Project
# Module info:
# platform.py: the platform object


import pygame
from constants import *

class Platform(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
