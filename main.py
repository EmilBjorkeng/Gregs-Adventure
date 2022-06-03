import pygame
import game
import menus.main_menu as main_menu
import levels.map_editor as map_editor
import settings

window_size = (800, 600)

# Init Pygame
pygame.init()
# Set Icon
pygame_icon = pygame.image.load('./Assets/Icon.png')
pygame.display.set_icon(pygame_icon)
# make display
display = pygame.display.set_mode(window_size)
pygame.display.set_caption('Gregs Adventure')
# Get clock and activate fonts
clock = pygame.time.Clock()
pygame.font.get_init()

# -1 = Exit
# 0 = Main Menu
# 1 = The Game
# 2 = Map Editor
# 3 = Settings
switch_to = 0
came_from = 0

# Main Loop
running = True
while running:
    # Scene Manager/Switcher
    match switch_to:
        case -1:
            running = False
        case 0:
            go_next = main_menu.run(display, came_from)
            came_from = switch_to
            switch_to = go_next
        case 1:
            go_next = game.run(display, clock, came_from, window_size)
            came_from = switch_to
            switch_to = go_next
        case 2:
            go_next = map_editor.run(display, came_from, window_size)
            came_from = switch_to
            switch_to = go_next
        case 3:
            go_next = settings.run(display, came_from)
            came_from = switch_to
            switch_to = go_next
        case _:
            print(f'Error: "{switch_to}" is not a valid switch_to value')
            switch_to = 0
            came_from = 0

pygame.quit()
quit()
