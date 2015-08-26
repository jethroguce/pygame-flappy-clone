import pygame

pygame.init()

SCREENWIDTH = 288
SCREENHEIGHT = 512
resolution = [SCREENWIDTH, SCREENHEIGHT]
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

    playerx = int(SCREENWIDTH * 0.2)
    playery = int((SCREENHEIGHT - bird.get_height()) / 2)

    player = surface.blit(bird,[playerx,playery])
    pygame.display.update()