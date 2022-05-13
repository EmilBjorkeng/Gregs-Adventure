import pygame
from main import display

class World:
    def __init__(self):
        self.gravity = 3.8
        self.drag = 2.5
        self.friction = 4

class Box:
    def __init__(self, x, y, sizeX, sizeY):
        self.colour = (0, 0, 0)
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY

    def draw(self):
        pygame.draw.rect(display, self.colour, (self.x, self.y, self.sizeX, self.sizeY))