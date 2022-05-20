import pygame
import math
from settings import *

class Player:
    def __init__(self, display, x: int, y: int):
        # Values
        self.dis = display
        self.pos = [x, y]
        self.vel = [0, 0]

        # Stats
        self.speed = 8
        self.crouch_speed_mult = 0.7
        self.jump_force = 30
        self.crouch_jump_mult = 0.8
        self.mass = 0.8

        # Hitbox
        self.hitbox_padding = 5
        self.crouch_hitbox_decrees = 16

        # Conditions
        self.facing_left = False
        self.is_walking = False
        self.onGround = False
        self.is_jumping = False
        self.is_crouching = False
        self.did_crouching = False

        # Sprites
        self.sprite_size = 50
        self.sprite = pygame.image.load(r'./Assets/Greg.png') # Idle
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite_size, self.sprite_size))
        self.crouch_sprite = pygame.image.load(r'./Assets/gregcrouch.png') # Crouch
        self.crouch_sprite = pygame.transform.scale(self.crouch_sprite, (self.sprite_size, self.sprite_size))

        # Animations
        self.animation_frame = 0
            # Walk Animation
        self.walk_animation_sprite = pygame.image.load(r'./Assets/gregwalk.png')
        self.walk_animation_sprite = pygame.transform.scale(self.walk_animation_sprite, (self.sprite_size * 5, self.sprite_size))
        self.walk_animation = [
            self.walk_animation_sprite.subsurface(0, 0, self.sprite_size, self.sprite_size),
            self.walk_animation_sprite.subsurface(self.sprite_size, 0, self.sprite_size, self.sprite_size),
            self.walk_animation_sprite.subsurface(self.sprite_size * 2, 0, self.sprite_size, self.sprite_size),
            self.walk_animation_sprite.subsurface(self.sprite_size * 3, 0, self.sprite_size, self.sprite_size),
            self.walk_animation_sprite.subsurface(self.sprite_size * 4, 0, self.sprite_size, self.sprite_size)
        ]
            # Crouch Walk Animation
        self.crouch_walk_animation_sprite = pygame.image.load(r'./Assets/gregcrouchwalk.png')
        self.crouch_walk_animation_sprite = pygame.transform.scale(self.crouch_walk_animation_sprite, (self.sprite_size * 5, self.sprite_size))
        self.crouch_walk_animation = [
            self.crouch_walk_animation_sprite.subsurface(0, 0, self.sprite_size, self.sprite_size),
            self.crouch_walk_animation_sprite.subsurface(self.sprite_size, 0, self.sprite_size, self.sprite_size),
            self.crouch_walk_animation_sprite.subsurface(self.sprite_size * 2, 0, self.sprite_size, self.sprite_size),
            self.crouch_walk_animation_sprite.subsurface(self.sprite_size * 3, 0, self.sprite_size, self.sprite_size),
            self.crouch_walk_animation_sprite.subsurface(self.sprite_size * 4, 0, self.sprite_size, self.sprite_size)
        ]

    def move(self, vel):
        mult = 1
        if self.is_crouching and self.onGround:
            mult = self.crouch_speed_mult
        self.vel[0] = vel * mult

    def jump(self):
        if self.onGround:
            mult = 1
            if self.is_crouching and self.onGround:
                mult = self.crouch_jump_mult
            self.vel[1] = -self.jump_force * mult
            self.is_jumping = True
    
    def draw(self):
        # Standing
        image = self.sprite
        # Walking
        if self.is_walking:
            # Animation timer
            self.animation_frame += 0.1
            if self.animation_frame > len(self.walk_animation):
                self.animation_frame = 0
            # Crouch walking
            if self.is_crouching:
               image = self.crouch_walk_animation[math.floor(self.animation_frame)]
            # Walking
            else:
                image = self.walk_animation[math.floor(self.animation_frame)]
        # Standing
        else:
            # Crouching
            if self.is_crouching:
                image = self.crouch_sprite
        # If facing left
        if self.facing_left:
            image = pygame.transform.flip(image, True, False)
        # Draw sprite
        self.dis.blit(image, self.pos)

    def hit_box_calculation(self):
        if self.is_crouching:
            move_down_by = self.crouch_hitbox_decrees
            self.did_crouching = True
        else:
            move_down_by = 0
            # Big Head after release
            if self.did_crouching:
                for b in boxes:
                    for h in range(0, self.sprite_size - 20, 1):
                        for w in range(0, self.sprite_size - self.hitbox_padding * 2, 1):
                            if self.pos[1] + move_down_by + h > b.y and self.pos[1] + move_down_by + h < b.y + b.sizeY:
                                if self.pos[0] + self.hitbox_padding + w > b.x and self.pos[0] + self.hitbox_padding + w < b.x + b.sizeX:
                                    self.pos[1] = b.y + b.sizeY - move_down_by
            self.did_crouching = False

        for b in boxes:
            # Hitting wall Hitbox
            for h in range(0, self.sprite_size - 24 - move_down_by, 1):
                for w in range(0, 15, 1):
                    if self.pos[1] + move_down_by + 15 + h > b.y and self.pos[1] + move_down_by + 15 + h < b.y + b.sizeY:
                        if self.pos[0] + self.hitbox_padding + w > b.x and self.pos[0] + self.hitbox_padding + w < b.x + b.sizeX:
                            self.pos[0] = b.x + b.sizeX - self.hitbox_padding
                        elif self.pos[0] + self.sprite_size - 15 - self.hitbox_padding + w > b.x and self.pos[0] + self.sprite_size - 15 - self.hitbox_padding + w < b.x + b.sizeX:
                            self.pos[0] = b.x - self.sprite_size + self.hitbox_padding

            # OnGround Hitbox
            for h in range(0, math.floor(self.sprite_size / 5) + 1, 1):
                for w in range(0, self.sprite_size - self.hitbox_padding * 2, 1):
                    if self.pos[1] + self.sprite_size - h + 1 > b.y and self.pos[1] + self.sprite_size - h < b.y + b.sizeY:
                        if self.pos[0] + 5 + w > b.x and self.pos[0] + 5 + w < b.x + b.sizeX:
                            self.pos[1] = b.y - self.sprite_size
                            self.onGround = True
            
            # Head
            for h in range(0, 15, 1):
                for w in range(0, self.sprite_size - self.hitbox_padding * 2, 1):
                    if self.pos[1] + move_down_by + h > b.y and self.pos[1] + move_down_by + h < b.y + b.sizeY:
                        if self.pos[0] + self.hitbox_padding + w > b.x and self.pos[0] + self.hitbox_padding + w < b.x + b.sizeX:
                            self.pos[1] = b.y + b.sizeY - move_down_by
    
    def update(self):
        # Gravity
        if not self.onGround:
            self.vel[1] += 2#world.gravity * self.mass

        resistence = world.friction

        # Velosity Calculations
        for i in range(0, 2, 1):
            # Positive velosity
            if self.vel[i] > 0:
                self.vel[i] += (resistence / self.mass) * (-self.vel[i] / 7)
                if self.vel[i] < 1:
                    self.vel[i] = 0
            # Negative velosity
            elif self.vel[i] < 0:
                self.vel[i] -= (resistence / self.mass) * (self.vel[i] / 7)
                if self.vel[i] > 0:
                    self.vel = 0

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.pos[0] < self.hitbox_padding + 2 - self.sprite_size:
            self.pos[0] = 800 - self.hitbox_padding - 2
        if self.pos[0] > 800 - self.hitbox_padding - 2:
            self.pos[0] = self.hitbox_padding + 2 - self.sprite_size

        self.onGround = False
        self.hit_box_calculation()

    def draw_hitboxes(self):
        move_down_by = 0
        if self.is_crouching:
            move_down_by = self.crouch_hitbox_decrees

        # OnGround Hitbox
        pygame.draw.rect(self.dis, (0, 255, 0), (self.pos[0] + 5, self.pos[1] + self.sprite_size - math.floor(self.sprite_size / 5) + 1, self.sprite_size - 10, math.floor(self.sprite_size / 5) + 1))
        # Head
        pygame.draw.rect(self.dis, (255, 0, 0), (self.pos[0] + self.hitbox_padding, self.pos[1] + move_down_by, self.sprite_size - self.hitbox_padding * 2, 15))
        # Hitting Wall Hitbox
        pygame.draw.rect(self.dis, (255, 255, 0), (self.pos[0] + self.hitbox_padding, self.pos[1] + 15 + move_down_by, 15, self.sprite_size - 24 - move_down_by))
        pygame.draw.rect(self.dis, (255, 255, 0), (self.pos[0] + self.sprite_size - 15 - self.hitbox_padding, self.pos[1] + 15 + move_down_by, 15, self.sprite_size - 24 - move_down_by))
