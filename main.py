import pygame

pygame.init()
clock = pygame.time.Clock()

SCREENWIDTH = 288
SCREENHEIGHT = 512
BASEY        = SCREENHEIGHT * 0.79
resolution = [SCREENWIDTH, SCREENHEIGHT]
surface = pygame.display.set_mode(resolution)

background = pygame.image.load('assets/sprites/background-day.png').convert()
base =  pygame.image.load('assets/sprites/base.png').convert_alpha()
basex = 0
baseShift = base.get_width() - background.get_width()

bird = pygame.image.load('assets/sprites/yellowbird-downflap.png').convert_alpha()
playerx = int(SCREENWIDTH * 0.2)
playery = int((SCREENHEIGHT - bird.get_height()) / 2)


while True:
    surface.fill([255, 255, 255])
    bg = surface.blit(background,[0,0])

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        pygame.quit()
    elif keystate[pygame.K_UP]:
        playery -= 6

    playery += 1
    player = surface.blit(bird,[playerx,playery])
    basex = -((-basex + 4) % baseShift)
    surface.blit(base, (basex, BASEY))
    pygame.display.update()
    clock.tick(30)

