import pygame

pygame.init()

resolution = [288, 512]
surface = pygame.display.set_mode(resolution)

bird = pygame.image.load('assets/sprites/yellowbird-downflap.png').convert_alpha()

while True:
    surface.fill([255, 255, 255])

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        pygame.quit()

    player = surface.blit(bird,[0,0])
    pygame.display.update()