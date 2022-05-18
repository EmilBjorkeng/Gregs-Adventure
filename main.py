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
boxes.append(Box(display, 500, 550, 10, 30))
boxes.append(Box(display, 100, 470, 50, 10))
boxes.append(Box(display, 150, 450, 50, 10))

# Player
from player import *
greg = Player(display, 100, 500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # Left
    if keys[pygame.K_a]:
        greg.move(-1)
        greg.facing_left = True
    # Right
    if keys[pygame.K_d]:
        greg.move(1)
        greg.facing_left = False
    # Jump
    if keys[pygame.K_SPACE]:
        greg.jump(held_space)
        if held_space < 20:
            held_space += 1
    elif held_space > 0:
        held_space -= 0.5
    # Crouch
    greg.is_crouching = False
    if keys[pygame.K_LSHIFT]:
        greg.is_crouching = True

    greg.update()

    # Draw
    display.fill((255, 255, 255))

    greg.draw()

    for i in boxes:
        i.draw()

    move_down_by = 0
    if greg.is_crouching:
        move_down_by = greg.crouch_decrees

    # OnGround Hitbox
    #pygame.draw.rect(display, (0, 255, 0), (greg.x + 5, greg.y + greg.size - math.floor(greg.size / 5) + 1, greg.size - 10, math.floor(greg.size / 5) + 1))
    # Head
    #pygame.draw.rect(display, (255, 0, 0), (greg.x + greg.padding, greg.y + move_down_by, greg.size - greg.padding * 2, 15))
    # Hitting Wall Hitbox
    #pygame.draw.rect(display, (255, 255, 0), (greg.x + greg.padding, greg.y + 15 + move_down_by, 15, greg.size - 24 - move_down_by))
    #pygame.draw.rect(display, (255, 255, 0), (greg.x + greg.size - 15 - greg.padding, greg.y + 15 + move_down_by, 15, greg.size - 24 - move_down_by))

    pygame.display.update()
    clock.tick(fps)

# Game Over
pygame.quit()
quit()
