import sys

import pygame

pygame.init()

window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('坦克大战')

while True:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
