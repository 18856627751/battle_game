import pygame
from utils.params import *

from pygame.locals import *
from ui.game_part import *



class Game:
    def __init__(self, surface):
        self.surface = surface

        self.game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.info_surface = pygame.Surface((INFO_WIDTH, INFO_HEIGHT))
        #
        self.game_area = GameArea(self.game_surface)
        self.game_info = GameInfo(self.info_surface)

    def show(self):
        self.surface.fill((0x77, 0x77, 0x77))

        self.surface.blit(self.game_surface, (WINDOW_PADDING, WINDOW_PADDING))
        self.surface.blit(self.info_surface, (2*WINDOW_PADDING+GAME_WIDTH, WINDOW_PADDING))

        self.game_area.graph()
        self.game_info.graph()

    def press_key(self, key):
        self.game_area.press(key)
