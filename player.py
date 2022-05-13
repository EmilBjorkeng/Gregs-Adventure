import pygame
import math
from main import display
from main import world
from main import boxes

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.speed = 2.4
        self.jump_force = 30
        self.terminal_vel = 10
        self.weight = 0.8
        self.size = 50
        self.sprite = pygame.image.load(r'./Greg.png')
        self.sprite = pygame.transform.scale(self.sprite, (self.size, self.size))
        self.walk_animation_sprite = pygame.image.load(r'./gregwalk.png')
        self.walk_animation_sprite = pygame.transform.scale(self.walk_animation_sprite, (self.size * 5, self.size))
        self.walk_animation = [
            self.walk_animation_sprite.subsurface(0, 0, self.size, self.size),
            self.walk_animation_sprite.subsurface(self.size, 0, self.size, self.size),
            self.walk_animation_sprite.subsurface(self.size * 2, 0, self.size, self.size),
            self.walk_animation_sprite.subsurface(self.size * 3, 0, self.size, self.size),
            self.walk_animation_sprite.subsurface(self.size * 4, 0, self.size, self.size)
        ]
        self.animation_frame = 0
        self.facing_left = False
        self.walking = False
        self.onGround = False

    def move(self, x, y):
        self.vx += x
        self.vy += y
        if not x == 0:
            self.walking = True

    def jump(self):
        if self.onGround:
            self.vy = -self.jump_force
    
    def draw(self):
        if self.walking:
            image = self.walk_animation[math.floor(self.animation_frame)]
            self.animation_frame += 0.1
            if self.animation_frame >= len(self.walk_animation):
                self.animation_frame = 0
        else:
            image = self.sprite
        if self.facing_left:
            image = pygame.transform.flip(image, True, False)
        display.blit(image, (self.x, self.y))
        self.walking = False

    def friction_calculation(self):
        # Check if on ground or in the air
        decreese_by = world.friction
        if not self.onGround:
            decreese_by = world.drag
        
        # Change X Velosity
        if self.vx > 0:
            if self.vx < decreese_by:
                self.vx = 0
            self.vx -= decreese_by
            if self.vx < 0:
                self.vx = 0
        elif self.vx < 0:
            if self.vx > -decreese_by:
                self.vx = 0
            self.vx -= -decreese_by
            if self.vx > 0:
                self.vx = 0

        # Change Y Velosity
        if self.vy > 0:
            if self.vy < decreese_by:
                self.vy = 0
            self.vy -= decreese_by
            if self.vy < 0:
                self.vy = 0
        elif self.vy < 0:
            if self.vy > -decreese_by:
                self.vy = 0
            self.vy -= -decreese_by
            if self.vy > 0:
                self.vy = 0
    
    def update(self):
        print(str(self.vx) + " : " + str(self.vy))
        self.x += self.vx
        self.y += self.vy
        self.friction_calculation()

        self.onGround = False
        for b in boxes:
            for h in range(0, math.floor(self.size / 5) + 1, 1):
                for w in range(0, self.size, 1):
                    if self.y + self.size - h + 1 > b.y and self.y + self.size - h < b.y + b.sizeY:
                        if self.x + w > b.x and self.x + w < b.x + b.sizeX:
                            self.y = b.y - self.size
                            self.onGround = True
        
        if not self.onGround and self.vy < self.terminal_vel:
            self.vy += world.gravity * self.weight