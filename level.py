import pygame
from constants import *
from platform import *

class Level():

    def __init__(self, players):
        self.player1 = players[0]
        self.player2 = players[1]
        self.platform_list = pygame.sprite.Group()        

        level = [[210, 1, 500, 500],
                 [210, 1, 200, 400],
                 [210, 1, 600, 300],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player1 = self.player1
            block.player2 = self.player2
            self.platform_list.add(block)

    def update(self):
        self.platform_list.update()

    def draw(self, screen):
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, [0, 75, WIDTH, LEVEL_HEIGHT - 75])
        self.platform_list.draw(screen)