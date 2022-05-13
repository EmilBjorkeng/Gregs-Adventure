import pygame

fps = 60
held_space = 0

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Gregs Adventure')
clock = pygame.time.Clock()

# Settings
from settings import *
boxes.append(Box(display, 0, 580, 800, 10))

# Player
from player import *
greg = Player(display, 100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # Left
    if keys[pygame.K_a]:
        greg.move(-greg.speed)
        greg.facing_left = True
    # Right
    if keys[pygame.K_d]:
        greg.move(greg.speed)
        greg.facing_left = False
    # Jump
    if keys[pygame.K_SPACE]:
        greg.jump(held_space)
        if held_space < 20:
            held_space += 1
    elif held_space > 0:
        held_space -= 0.5

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
