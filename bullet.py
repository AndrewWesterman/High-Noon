# Author:
# Andrew Westerman
# awesterman@csu.fullerton.edu
# CS 386: Final Project
# Module info:
# bullet.py: bullet object, handles bullet position and sound effects


import pygame
from constants import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        self.image = pygame.Surface([10,4])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y + 60
        self.direction = player.direction
        self.player = player

    def update(self):
        if self.direction == PLAYER_LEFT:
            self.rect.x -= BULLET_SPEED
        else:
            self.rect.x += BULLET_SPEED

    def sfx(self):
        pygame.mixer.music.load(SFX_BULLET)
        pygame.mixer.music.play()
