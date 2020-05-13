"""
    Define the class of the player's projectile
"""
import pygame


class PlayerProjectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.attack = 150
        self.image = pygame.image.load('assets/shot6_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 20
        self.velocity = 20

    def remove(self):
        self.player.all_p_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.velocity

        if self.rect.y > 800:
            self.remove()
