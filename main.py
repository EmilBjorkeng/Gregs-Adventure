import pygame
import main_menu
import pause_menu

fps = 60
gravity = 3.8
came_from_pause = False

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Gregs Adventure')
clock = pygame.time.Clock()
pygame.font.get_init()
main_menu.run(display)

# Boxes
from grounds import *
boxes.append(Box(display, [0, 580, 800, 10], [0, 0, 0], 1.2))
boxes.append(Box(display, [500, 550, 10, 30], [0, 0, 255], 1.2))
boxes.append(Box(display, [100, 470, 50, 10], [0, 0, 0], 1.2))
boxes.append(Box(display, [150, 450, 50, 10], [0, 0, 0], 1.2))
boxes.append(Box(display, [200, 420, 50, 10], [0, 0, 0], 1.2))
boxes.append(Box(display, [250, 530, 50, 10], [0, 0, 0], 1.2))

# Player
from player import *
greg = Player(display, gravity, 100, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    greg.is_walking = False
    keys = pygame.key.get_pressed()
    # Left
    if keys[pygame.K_a] and not keys[pygame.K_d]:
        greg.move(-1)
        greg.facing_left = True
        greg.is_walking = True
    # Right
    elif keys[pygame.K_d] and not keys[pygame.K_a]:
        greg.move(1)
        greg.facing_left = False
        greg.is_walking = True
    # Jump
    if keys[pygame.K_SPACE]:
        greg.jump()
    # Crouch
    greg.is_crouching = False
    if keys[pygame.K_LSHIFT]:
        greg.is_crouching = True

    # Pause
    if keys[pygame.K_ESCAPE]:
        if not came_from_pause:
            came_from_pause = True
            pause_menu.run(display)
    else:
        came_from_pause = False

    greg.update()

    # Draw
    display.fill((255, 255, 255))

    greg.draw()
    #greg.draw_hitboxes()

    for i in boxes:
        i.draw()

    pygame.display.update()
    clock.tick(fps)

# Game Over
pygame.quit()
quit()
