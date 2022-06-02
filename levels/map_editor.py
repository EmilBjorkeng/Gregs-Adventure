import pygame

def run(display):
    button_font = pygame.font.SysFont('Areal', 50)
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        display.fill((255, 255, 255))
        pygame.draw.rect(display, (0, 0, 0), (10, 10, 100, 100))
        pygame.display.update()