import pygame

pygame.init()
clock = pygame.time.Clock()

SCREENWIDTH = 288
SCREENHEIGHT = 512
resolution = [SCREENWIDTH, SCREENHEIGHT]
surface = pygame.display.set_mode(resolution)

bird = pygame.image.load('assets/sprites/yellowbird-downflap.png').convert_alpha()
playerx = int(SCREENWIDTH * 0.2)
playery = int((SCREENHEIGHT - bird.get_height()) / 2)


while True:
    surface.fill([255, 255, 255])

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        pygame.quit()

    playery += 1/4
    player = surface.blit(bird,[playerx,playery])
    pygame.display.update()
    clock.tick(60)

