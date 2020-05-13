"""
    Define the Player class
"""
import pygame


class Player(object):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/transportation.png')
        self.speed = 10
        self.health = 1000
        self.max_health = 1000
        self.attack = 150
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 400

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed
