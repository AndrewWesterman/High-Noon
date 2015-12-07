import pygame
from constants import *
from level import *
from player import *
from powerup import *


def main():

    pygame.init()
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("HiGH N00N")
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    player1 = Player(screen, "Player 1", 1)
    player2 = Player(screen, "Player 2", 2)


    level = Level([player1, player2]);
    player1.level = level
    player2.level = level

    player1.spawn()
    player2.spawn()
 
    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(player1)
    active_sprite_list.add(player2)

     # Loop until the user clicks the close button.
    done = False     

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player1.moveLeft()
                if event.key == pygame.K_d:
                    player1.moveRight()
                if event.key == pygame.K_w:
                    player1.jump()
                if event.key == pygame.K_LEFT:
                    player2.moveLeft()
                if event.key == pygame.K_RIGHT:
                    player2.moveRight()
                if event.key == pygame.K_UP:
                    player2.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player1.change_x < 0:
                    player1.stop()
                if event.key == pygame.K_d and player1.change_x > 0:
                    player1.stop()
                if event.key == pygame.K_LEFT and player2.change_x < 0:
                    player2.stop()
                if event.key == pygame.K_RIGHT and player2.change_x > 0:
                    player2.stop()

        active_sprite_list.update()
        level.update()
     
        # --- Game logic should go here
        if player1.rect.right > WIDTH:
            player1.rect.right = WIDTH
        if player2.rect.right > WIDTH:
            player2.rect.right = WIDTH

        if player1.rect.left < 0:
            player1.rect.left = 0
        if player2.rect.left < 0:
            player2.rect.left = 0

        # --- Drawing code should go here
        level.draw(screen)
        active_sprite_list.draw(screen)

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        # screen.fill(WHITE)
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()