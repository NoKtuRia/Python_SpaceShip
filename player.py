"""
    Define the Player class
"""
import pygame
from p_projectile import PlayerProjectile

class Player(object):

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load('assets/transportation.png')
        self.width = width
        self.height = height
        self.speed = 15
        self.health = 1000
        self.max_health = 1000
        self.all_p_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 400

    def move_right(self):
        if self.rect.x + self.image.get_width() < self.width:
            self.rect.x += self.speed

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed

    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.y + self.image.get_height() < self.height:
            self.rect.y += self.speed

    def launch_projectile(self):
        self.all_p_projectiles.add(PlayerProjectile(self))
