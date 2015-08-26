import pygame

pygame.init()

resolution = [288, 512]
surface = pygame.display.set_mode(resolution)

while True:
	surface.fill([255, 255, 255])