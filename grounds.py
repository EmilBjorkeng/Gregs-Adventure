import pygame

class Box:
    def __init__(self, display, rect:list, colour:list, friction: float):
        self.dis = display
        self.colour = (colour[0], colour[1], colour[2])
        self.x = rect[0]
        self.y = rect[1]
        self.sizeX = rect[2]
        self.sizeY = rect[3]
        self.friction = friction

    def draw(self):
        pygame.draw.rect(self.dis, self.colour, (self.x, self.y, self.sizeX, self.sizeY))

boxes = []