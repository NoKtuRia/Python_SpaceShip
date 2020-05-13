import pygame
from player import Player

WIDTH, HEIGHT = 1400, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship")

BACKGROUND = pygame.image.load('assets/bg.jpg')  # load background
player = Player()

running = True

while running:

    screen.blit(BACKGROUND, (0, 0))
    screen.blit(player.image, (player.rect))

    # update window
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
