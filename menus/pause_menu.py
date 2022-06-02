import pygame

def run(display):
    title_font = pygame.font.SysFont('Areal', 75)
    button_font = pygame.font.SysFont('Areal', 50)
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

        # Mouse
        if pygame.mouse.get_pressed()[0]:
            mousepos = pygame.mouse.get_pos()
            if mousepos[0] > 325 and mousepos[0] < 475:
                if mousepos[1] > 260 and mousepos[1] < 310:
                    running = False
                if mousepos[1] > 320 and mousepos[1] < 370:
                    temp = 0
                if mousepos[1] > 380 and mousepos[1] < 430:
                    return True

        pygame.draw.rect(display, (255, 255, 255), (100, 100, 600, 400))   
        pygame.draw.rect(display, (0, 0, 0), (100, 100, 600, 400), 3)

        # Buttons
        pygame.draw.rect(display, (0, 0, 0), (325, 260, 150, 50))
        pygame.draw.rect(display, (0, 0, 0), (325, 320, 150, 50))
        pygame.draw.rect(display, (255, 0, 0), (325, 380, 150, 50))

        # Hover
        mousepos = pygame.mouse.get_pos()
        if mousepos[0] > 325 and mousepos[0] < 475:
            if mousepos[1] > 260 and mousepos[1] < 310:
                pygame.draw.rect(display, (0, 0, 255), (325, 260, 150, 50))
            if mousepos[1] > 320 and mousepos[1] < 370:
                pygame.draw.rect(display, (0, 0, 255), (325, 320, 150, 50))
            if mousepos[1] > 380 and mousepos[1] < 430:
                pygame.draw.rect(display, (0, 0, 255), (325, 380, 150, 50))

        # Text
        text = title_font.render('Pause Menu', False, (0, 0, 0))
        display.blit(text, (250, 120))
        text = button_font.render('Resume', False, (255, 255, 255))
        display.blit(text, (335, 270))
        text = button_font.render('Options', False, (255, 255, 255))
        display.blit(text, (335, 330))
        text = button_font.render('Quit', False, (255, 255, 255))
        display.blit(text, (365, 390))
        pygame.display.update()

    return False