import pygame
from player import Player

width = 1400
height = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spaceship")

BACKGROUND = pygame.image.load('assets/bg.jpg')  # load background

# create the player
player = Player(width, height)

keys_down = {}

running = True

while running:

    screen.blit(BACKGROUND, (0, 0))
    screen.blit(player.image, player.rect)

    # Player move
    if keys_down.get(pygame.K_LEFT):
        player.move_left()
    elif keys_down.get(pygame.K_RIGHT):
        player.move_right()
    elif keys_down.get(pygame.K_UP):
        player.move_up()
    elif keys_down.get(pygame.K_DOWN):
        player.move_down()

    # update window
    pygame.display.flip()

    # verify events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif event.type == pygame.KEYDOWN:
            keys_down[event.key] = True
        elif event.type == pygame.KEYUP:
            keys_down[event.key] = False
