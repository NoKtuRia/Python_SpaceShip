"""
    Define the class Game
"""

import pygame
from player import Player


class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}

    def update(self, screen):
        # display th player
        screen.blit(self.player.image, self.player.rect)

        for projectile in self.player.all_p_projectiles:
            projectile.move()

        self.player.all_p_projectiles.draw(screen)
