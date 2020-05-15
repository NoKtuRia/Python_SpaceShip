import pygame
import os
import random
import time

pygame.init()

WIDTH = 750
HEIGHT = 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# LOAD IMAGE

# enemy ships
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green.png"))

# main ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green.png"))

# bullets
PIXEL_LASER_RED = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
PIXEL_LASER_BLUE = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
PIXEL_LASER_GREEN = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
PIXEL_LASER_YELLOW = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

