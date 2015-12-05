import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE  = (0, 10, 255)

#Define screen size
WIDTH = 1000
HEIGHT = 700

class Level():

    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.p1spawn = 100
        self.p2spawn = width - 100
        self.screen.fill(BLACK)

    def draw(self):
        # This will draw the initial game space.
        print("Level being drawn")
        pygame.draw.rect(screen, BLUE, [0, 75, self.width, self.height])

    def getSpawn1(self):
        return self.p1spawn

    def getSpawn2(self):
        return self.p2spawn


class Building():

    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        print("Building being drawn")

class Powerup():

    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        print("Powerup being drawn")

class Player():
    PLAYER_LEFT = "L"
    PLAYER_RIGHT = "R"

    def __init__(self, screen, name, num):
        self.screen = screen
        self.name = name
        if num == 1:
            self.direction = PLAYER_LEFT
        else:
            self.direction = PLAYER_RIGHT

    def spwan(self):
        print("{} has spawned")

    def draw(self):
        print("{} is being drawn".format(self.name))

    def jump(self):
        print("{} jumped".format(self.name))

    def moveLeft(self):
        print("{} moved left".format(self.name))

    def moveRight(self):
        print("{} moved right".format(self.name))

pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("HiGH N00N")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

level = Level(screen, WIDTH, HEIGHT - 200);
level.draw()
pygame.display.flip()
 

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # screen.fill(WHITE)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()