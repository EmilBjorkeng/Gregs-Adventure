import pygame

class World:
    def __init__(self):
        self.gravity = 3.8
        self.friction = 0.8

world = World()

class Box:
    def __init__(self, display, x, y, sizeX, sizeY):
        self.dis = display
        self.colour = (0, 0, 0)
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY

    def draw(self):
        pygame.draw.rect(self.dis, self.colour, (self.x, self.y, self.sizeX, self.sizeY))

boxes = []