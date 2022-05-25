import pygame
import menus.main_menu as main_menu
import menus.pause_menu as pause_menu
from grounds import *
from player import *

fps = 60
gravity = 3.8

pygame.init()
pygame_icon = pygame.image.load('./Assets/Icon.png')
pygame.display.set_icon(pygame_icon)
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Gregs Adventure')
clock = pygame.time.Clock()
pygame.font.get_init()

came_from_pause = False
back_to_menu = True
while True:
    back_to_menu = False
    main_menu.run(display)

    # Clear out the boxes list
    while boxes:
        boxes.pop()

    # I hate that I can do this
    # I'm leaving it in just because of how cursed it is
    # It hurts to look at it
    [boxes.append(Box(display, k[0], k[1], k[2][0])) for k in [[j.split(",") for j in i] for i in [i.split(":") for i in open(r"./levels/level1.level", "r").read().split(";")]]]

    # Player
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
                pause_bool = pause_menu.run(display)
                back_to_menu = pause_bool
                running = not pause_bool
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

    if not back_to_menu:
        pygame.quit()
        quit()
