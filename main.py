import sys
import pygame

from ui.page import *
from utils.params import *

if __name__ == '__main__':
    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('坦克大战')

    game = Game(window)
    page = None

    while True:

        game.show()

        keys = pygame.key.get_pressed()
        game.press_key(keys)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYDOWN:
                pass

        pygame.display.flip()
