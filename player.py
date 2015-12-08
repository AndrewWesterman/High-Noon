# Author:
# Andrew Westerman
# awesterman@csu.fullerton.edu
# CS 386: Final Project
# Module info:
# player.py: the player object, in charge of maintatining player positions and sprite handling


import pygame
from constants import *

class Player(pygame.sprite.Sprite):

    def __init__(self, screen, name, num):
        super().__init__()

        self.image = pygame.image.load(P1_LSPRITE).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0
        self.name = name
        self.num = num
        self.lives = 3
        if num == 1:
            self.direction = PLAYER_LEFT
            self.image = pygame.image.load(P1_LSPRITE).convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
        else:
            self.direction = PLAYER_RIGHT
            self.image = pygame.image.load(P2_RSPRITE).convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
        self.x = None
        self.y = None
        self.level = None
        
    def update(self):
        self.grav()

        self.updateImage()

        self.rect.x += self.change_x
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.change_y = 0

    def grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= LEVEL_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = LEVEL_HEIGHT - self.rect.height

    def spawn(self):
        if self.num == 1:
            self.rect.x = P1_SPAWN
        else:
            self.rect.x = P2_SPAWN

        self.rect.y = LEVEL_HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= LEVEL_HEIGHT:
            self.change_y = -10

    def moveLeft(self):
        self.change_x = -6
        self.direction = PLAYER_LEFT

    def moveRight(self):
        self.change_x = 6
        self.direction = PLAYER_RIGHT
    def stop(self):
        self.change_x = 0

    def updateImage(self):
        if self.direction == PLAYER_RIGHT:
            if self.num == 1:
                self.image = pygame.image.load(P1_RSPRITE).convert()
                self.image.set_colorkey(WHITE)
            else:
                self.image = pygame.image.load(P2_RSPRITE).convert()
                self.image.set_colorkey(WHITE)
        else:
            if self.num == 1:
                self.image = pygame.image.load(P1_LSPRITE).convert()
                self.image.set_colorkey(WHITE)
            else:
                self.image = pygame.image.load(P2_LSPRITE).convert()
                self.image.set_colorkey(WHITE)