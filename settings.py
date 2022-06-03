import pygame

def run(display, go_back):
    stop_clicking = True

    button_font = pygame.font.SysFont('Areal', 50)
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1 # Exit

        # Mouse
        if pygame.mouse.get_pressed()[0]:
            if not stop_clicking:
                mousepos = pygame.mouse.get_pos()
                if mousepos[0] > 325 and mousepos[0] < 475:
                    if mousepos[1] > 260 and mousepos[1] < 310:
                        return go_back # Go Back
        elif stop_clicking:
            stop_clicking = False
        
        display.fill((255, 255, 255))
        # Buttons
        pygame.draw.rect(display, (0, 0, 0), (325, 260, 150, 50))

        # Hover
        mousepos = pygame.mouse.get_pos()
        if mousepos[0] > 325 and mousepos[0] < 475:
            if mousepos[1] > 260 and mousepos[1] < 310:
                pygame.draw.rect(display, (0, 0, 255), (325, 260, 150, 50))

        # Text
        text = button_font.render('Options', False, (0, 0, 0))
        display.blit(text, (250, 120))
        text = button_font.render('Back', False, (255, 255, 255))
        display.blit(text, (335, 270))
        pygame.display.update()