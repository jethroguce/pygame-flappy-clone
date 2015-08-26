import pygame

pygame.init()

resolution = [288, 512]
surface = pygame.display.set_mode(resolution)

while True:
    surface.fill([255, 255, 255])

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        pygame.quit()