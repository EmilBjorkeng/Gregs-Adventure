import pygame

class Box:
    def __init__(self, display, rect:list, colour:list, friction: float):
        self.dis = display
        self.colour = (int(colour[0]), int(colour[1]), int(colour[2]))
        self.x = int(rect[0])
        self.y = int(rect[1])
        self.sizeX = int(rect[2])
        self.sizeY = int(rect[3])
        self.friction = float(friction)

    def draw(self):
        pygame.draw.rect(self.dis, self.colour, (self.x, self.y, self.sizeX, self.sizeY))

boxes = []