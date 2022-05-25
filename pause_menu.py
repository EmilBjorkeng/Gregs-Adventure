import pygame

def run(display):
    came_from_gameplay = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if not came_from_gameplay:
                running = False
        else:
            came_from_gameplay = False

        pygame.draw.rect(display, (255, 255, 255), (100, 100, 600, 400))       
        pygame.draw.rect(display, (0, 0, 0), (100, 100, 600, 400), 3)
        pygame.display.update()