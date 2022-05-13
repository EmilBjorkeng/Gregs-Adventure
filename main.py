import pygame

fps = 60

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Gregs Adventure')
clock = pygame.time.Clock()

# World
from world import *
world = World()

boxes = []
boxes.append(Box(0, 580, 500, 10))

# Player
from player import *
greg = Player(100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # Left
    if keys[pygame.K_a]:
        greg.move(-greg.speed, 0)
        greg.facing_left = True
    # Right
    if keys[pygame.K_d]:
        greg.move(greg.speed, 0)
        greg.facing_left = False
    # Jump
    if keys[pygame.K_SPACE]:
        greg.jump()

    greg.update()

    # Draw
    display.fill((255, 255, 255))

    greg.draw()

    for i in boxes:
        i.draw()

    pygame.display.update()
    clock.tick(fps)

# Game Over
pygame.quit()
quit()
