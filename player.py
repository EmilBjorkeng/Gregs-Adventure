import pygame
import math
from settings import *

class Player:
    def __init__(self, display, x, y):
        self.dis = display
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.speed = 2.7
        self.jump_force = 20
        self.jump_cooldown = 0
        self.mass_while_jumping = 0.001
        self.terminal_vel = 10
        self.mass = 0.8
        self.size = 50
        self.padding = 5
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
        self.is_jumping = False

    def move(self, value):
        self.vx += value
        self.walking = True

    def jump(self, held_space):
        if self.onGround:
            if self.jump_cooldown <= 0 or held_space < 5:
                self.vy = -self.jump_force
                self.is_jumping = True
                self.jump_cooldown = 5
            else:
                self.jump_cooldown -= 1
    
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
        self.dis.blit(image, (self.x, self.y))
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

    def hit_box_calculation(self):
        for b in boxes:
            # Hitting wall Hitbox
            for h in range(0, self.size - 10, 1):
                for w in range(0, 15, 1):
                    if self.y + h > b.y and self.y + h < b.y + b.sizeY:
                        if self.x + self.padding + w > b.x and self.x + self.padding + w < b.x + b.sizeX:
                            self.x = b.x + b.sizeX - self.padding
                        elif self.x + self.size - 15 - self.padding + w > b.x and self.x + self.size - 15 - self.padding + w < b.x + b.sizeX:
                            self.x = b.x - self.size + self.padding

            # OnGround Hitbox
            for h in range(0, math.floor(self.size / 5) + 1, 1):
                for w in range(0, self.size - self.padding * 2, 1):
                    if self.y + self.size - h + 1 > b.y and self.y + self.size - h < b.y + b.sizeY:
                        if self.x + 5 + w > b.x and self.x + 5 + w < b.x + b.sizeX:
                            self.y = b.y - self.size
                            self.onGround = True
    
    def update(self):
        #print(str(self.vx) + " : " + str(self.vy))
        self.x += self.vx
        self.y += self.vy
        self.friction_calculation()

        if self.x < self.padding + 2 - self.size:
            self.x = 800 - self.padding - 2
        if self.x > 800 - self.padding - 2:
            self.x = self.padding + 2 - self.size

        self.onGround = False
        self.hit_box_calculation()
        
        # Gravity
        if not self.onGround and self.vy < self.terminal_vel:
            # Gravity while jumping
            if (self.is_jumping):
                self.vy += world.gravity * self.mass_while_jumping
                if self.vy > 0:
                    self.is_jumping = False
            # Gravity while falling
            else:
                self.vy += world.gravity * self.mass