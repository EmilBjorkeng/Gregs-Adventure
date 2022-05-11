import pygame
import math

fps = 60

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Gregs Adventure')
clock = pygame.time.Clock()

class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3
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

    def move(self, x, y):
        self.x += x
        self.y += y
        if not x == 0:
            self.walking = True
    
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
        display.blit(image, (self.x * self.speed, self.y * self.speed))
        self.walking = False
    
    def update(self):
        self.move(0, 1)

greg = player(100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        greg.move(-1, 0)
        greg.facing_left = True
    if keys[pygame.K_d]:
        greg.move(1, 0)
        greg.facing_left = False

    greg.update()


    display.fill((255, 255, 255))

    greg.draw()

    pygame.display.update()
    clock.tick(fps)

# Game Over
pygame.quit()
quit()
