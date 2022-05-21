import pygame
import math
from grounds import *

class Player:
    def __init__(self, display, gravity: float, x: int, y: int):
        # Values
        self.dis = display
        self.gravity = gravity
        self.pos = [x, y]
        self.vel = [0, 0]

        # Stats
        self.speed = 8
        self.crouch_speed_mult = 0.7
        self.jump_force = 30
        self.crouch_jump_mult = 0.8
        self.mass = 0.8
        self.air_friction = 1

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

    def find_friction(self):
        for b in boxes:
            for h in range(0, math.floor(self.sprite_size / 5) + 1, 1):
                for w in range(0, self.sprite_size - self.hitbox_padding * 2, 1):
                    if self.pos[1] + self.sprite_size - h + 1 > b.y and self.pos[1] + self.sprite_size - h < b.y + b.sizeY:
                        if self.pos[0] + 5 + w > b.x and self.pos[0] + 5 + w < b.x + b.sizeX:
                            return b.friction
        return self.air_friction # in the air
    
    def update(self):
        # Gravity
        if not self.onGround:
            self.vel[1] += self.gravity * self.mass

        resistence = self.find_friction()

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

        # Did crouch
        if self.is_crouching:
            self.did_crouching = True
        if self.did_crouching and not self.is_crouching:
            # Check if you can stop crouching
            for b in boxes:
                for h in range(0, self.sprite_size, 1):
                    for w in range(0, self.sprite_size - self.hitbox_padding * 2, 1):
                        if self.pos[1] + h > b.y and self.pos[1] + h < b.y + b.sizeY:
                            if self.pos[0] + self.hitbox_padding + w > b.x and self.pos[0] + self.hitbox_padding + w < b.x + b.sizeX:
                                # If you can't
                                self.is_crouching = True
            # If you can
            if not self.is_crouching:
                self.did_crouching = False


        # Move hitbox down when crouchig
        move_down_by = 0
        if self.is_crouching:
            move_down_by = self.crouch_hitbox_decrees
        
        # X position
        self.pos[0] += self.vel[0]
        for b in boxes:
            is_colliding = True
            while is_colliding:
                is_colliding = False
                for h in range(0, self.sprite_size - move_down_by, 1):
                    for w in range(0, self.sprite_size - self.hitbox_padding * 2, 1):
                        if self.pos[1] + move_down_by + h > b.y and self.pos[1] + move_down_by + h < b.y + b.sizeY:
                            if self.pos[0] + self.hitbox_padding + w > b.x and self.pos[0] + self.hitbox_padding + w < b.x + b.sizeX:
                                is_colliding = True
                                if self.vel[0] > 0:
                                    self.pos[0] -= 1
                                else:
                                    self.pos[0] += 1
                                break
        
        # Y position
        self.pos[1] += self.vel[1]
        for b in boxes:
            is_colliding = True
            while is_colliding:
                is_colliding = False
                for h in range(0, self.sprite_size - move_down_by, 1):
                    for w in range(0, self.sprite_size - self.hitbox_padding * 2, 1):
                        if self.pos[1] + move_down_by + h > b.y and self.pos[1] + move_down_by + h < b.y + b.sizeY:
                            if self.pos[0] + self.hitbox_padding + w > b.x and self.pos[0] + self.hitbox_padding + w < b.x + b.sizeX:
                                is_colliding = True
                                if self.vel[1] > 0:
                                    self.pos[1] -= 1
                                else:
                                    self.pos[1] += 1
                                break
        
        # Check if on ground
        self.onGround = False
        for b in boxes:
            for h in range(0, math.floor(self.sprite_size / 6) + 1, 1):
                for w in range(0, self.sprite_size - self.hitbox_padding * 2 - 10, 1):
                    if self.pos[1] + self.sprite_size - math.floor(self.sprite_size / 6) + 1 + h > b.y and self.pos[1] + self.sprite_size - math.floor(self.sprite_size / 6) + 1 + h < b.y + b.sizeY:
                        if self.pos[0] + self.hitbox_padding + 5 + w > b.x and self.pos[0] + self.hitbox_padding + 5 + w < b.x + b.sizeX:
                            self.onGround = True

        if self.pos[0] < self.hitbox_padding + 2 - self.sprite_size:
            self.pos[0] = 800 - self.hitbox_padding - 2
        if self.pos[0] > 800 - self.hitbox_padding - 2:
            self.pos[0] = self.hitbox_padding + 2 - self.sprite_size

    def draw_hitboxes(self):
        move_down_by = 0
        if self.is_crouching:
            move_down_by = self.crouch_hitbox_decrees

        # Hitbox
        pygame.draw.rect(self.dis, (255, 255, 0), (
            self.pos[0] + self.hitbox_padding,
            self.pos[1] + move_down_by,
            self.sprite_size - self.hitbox_padding * 2,
            self.sprite_size - move_down_by), 2)

        # OnGround Hitbox
        pygame.draw.rect(self.dis, (0, 255, 0), (
            self.pos[0] + self.hitbox_padding + 5,
            self.pos[1] + self.sprite_size - math.floor(self.sprite_size / 6) + 1,
            self.sprite_size - self.hitbox_padding * 2 - 10,
            math.floor(self.sprite_size / 6) + 1))
