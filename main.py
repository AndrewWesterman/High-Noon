
class Level():

    def __init__(self, screen):
        self.screen = screen

    def draw():
        # This will draw the initial game space.
        print("Level being drawn")

class Building():

    def __init__(self, screen):
        self.screen = screen

    def draw():
        print("Building being drawn")

class Powerup():

    def __init__(self, screen):
        self.screen = screen

    def draw():
        print("Powerup being drawn")

class Player():

    def __init__(self, screen, name):
        self.screen = screen
        self.name = name

    def draw():
        print("{} is being drawn".format(self.name))

    def jump():
        print("{} jumped".format(self.name))

    def moveLeft(self):
        print("{} moved left".format(self.name))

    def moveRight(self):
        print("{} moved right".format(self.name))

pygame.init()


pygame.quit()