import pygame
import menus.pause_menu as pause_menu
from classes.grounds import *
from classes.player import *

def run(display, clock, go_back):
    fps = 60
    gravity = 3.8

    # Clear out the boxes list
    while boxes:
        boxes.pop()

    # I hate that I can do this
    # I'm leaving it in just because of how cursed it is
    # It hurts to look at it
    # It does Load the level tho
    [boxes.append(Box(display, k[0], k[1], k[2][0])) for k in [[j.split(",") for j in i] for i in [i.split(":") for i in open(r"./levels/level1.level", "r").read().split(";")]]]

    # Player
    greg = Player(display, gravity, 100, 0)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1 # Exit

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
            pause_option = pause_menu.run(display)
            if not pause_option == 0:
                return pause_option

        greg.update()

        # Draw
        display.fill((255, 255, 255))

        greg.draw()
        #greg.draw_hitboxes()

        for i in boxes:
            i.draw()

        pygame.display.update()
        clock.tick(fps)