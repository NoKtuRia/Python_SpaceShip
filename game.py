"""
    Define the class Game
"""

import pygame
from player import Player


class Game:

    def __init__(self):
        self.is_playing = True
        # generate the player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

    def start(self):
        self.is_playing = True

    def game_over(self):
        print("Partie perdue\nRemise a neuf du jeu...")
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # display th player
        screen.blit(self.player.image, self.player.rect)

        for projectile in self.player.all_p_projectiles:
            projectile.move()

        self.player.all_p_projectiles.draw(screen)
