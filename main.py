import sys
import pygame

from ui.page import *
from utils.params import *

if __name__ == '__main__':
    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('坦克大战')

    splash = Splash(window)
    game = Game(window)
    page = None

    while True:

        if get_status() == 0:
            page = splash
        elif get_status() == 1:
            page = game

        page.show()

        events = pygame.event.get()


        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYDOWN:
                print(event.key)
                page.press_key(event.key)
