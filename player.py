import pygame
from constants import *

class Player(pygame.sprite.Sprite):

    def __init__(self, screen, name, num):
        super().__init__()
        height = 60
        width = 40
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0
        self.name = name
        self.num = num
        if num == 1:
            self.direction = PLAYER_LEFT
        else:
            self.direction = PLAYER_RIGHT
        self.x = None
        self.y = None
        self.level = None
        
    def update(self):
        self.grav()

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
            self.x = P1_SPAWN
        else:
            self.x = P2_SPAWN

        self.y = LEVEL_HEIGHT - self.rect.height        
        print("{} has spawned".format(self.name))

    def draw(self, screen):
        print("{} is being drawn".format(self.name))

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= LEVEL_HEIGHT:
            self.change_y = -10

    def moveLeft(self):
        self.change_x = -6
        print("{} moved left".format(self.name))

    def moveRight(self):
        self.change_x = 6
        print("{} moved right".format(self.name))

    def stop(self):
        self.change_x = 0