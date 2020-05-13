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
