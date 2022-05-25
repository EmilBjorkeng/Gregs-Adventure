import pygame

def run(display):
    banner = pygame.image.load(r'./Assets/Banner.png')
    button_font = pygame.font.SysFont('Areal', 50)
    running = True
    click_cooldown = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Mouse
        if pygame.mouse.get_pressed()[0]:
            if not click_cooldown:
                mousepos = pygame.mouse.get_pos()
                if mousepos[0] > 325 and mousepos[0] < 475:
                    if mousepos[1] > 260 and mousepos[1] < 310:
                        running = False
                    if mousepos[1] > 320 and mousepos[1] < 370:
                        temp = 0
                    if mousepos[1] > 380 and mousepos[1] < 430:
                        pygame.quit()
                        quit()
        else:
            click_cooldown = False

        display.fill((255, 255, 255))

        # Banner
        display.blit(banner, (0, 0))

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
        text = button_font.render('Start', False, (255, 255, 255))
        display.blit(text, (360, 270))
        text = button_font.render('Options', False, (255, 255, 255))
        display.blit(text, (335, 330))
        text = button_font.render('Quit', False, (255, 255, 255))
        display.blit(text, (365, 390))

        pygame.display.update()