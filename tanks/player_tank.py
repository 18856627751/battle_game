import pygame
from pygame.locals import *

from utils.display import Display
from utils.params import *


class PlayerTank(Display):
    def __init__(self, **kwargs):
        self.surface = kwargs['surface']
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.xx = 0
        self.yy = 0

        self.images_player = [
            pygame.image.load('pic/p1tankU.gif'),
            pygame.image.load('pic/p1tankD.gif'),
            pygame.image.load('pic/p1tankL.gif'),
            pygame.image.load('pic/p1tankR.gif')
        ]
        self.direct = Direction.UP
        self.tank = None
        self.bad_direct = Direction.NONE

    def show(self):
        if self.direct == Direction.NONE:
            self.surface.blit(self.tank, (self.x, self.y))
        elif self.direct == Direction.UP:
            self.tank = self.images_player[0]
            self.surface.blit(self.tank, (self.x, self.y))
        elif self.direct == Direction.DOWN:
            self.tank = self.images_player[1]
            self.surface.blit(self.tank, (self.x, self.y))
        elif self.direct == Direction.LEFT:
            self.tank = self.images_player[2]
            self.surface.blit(self.tank, (self.x, self.y))
        elif self.direct == Direction.RIGHT:
            self.tank = self.images_player[3]
            self.surface.blit(self.tank, (self.x, self.y))

    def fire(self):
        pass

    def move(self, direct):
        print(self.bad_direct)
        if self.direct != direct:
            self.direct = direct
            self.bad_direct = Direction.NONE
        elif direct == Direction.UP and self.bad_direct != direct:
            self.y -= player_rare
        elif direct == Direction.DOWN and self.bad_direct != direct:
            self.y += player_rare
        elif direct == Direction.LEFT and self.bad_direct != direct:
            self.x -= player_rare
        elif direct == Direction.RIGHT and self.bad_direct != direct:
            self.x += player_rare

    def is_inflict_wall(self, wall):

        if self.direct == Direction.UP:
            self.yy = self.y - player_rare
            self.xx=self.x
        elif self.direct == Direction.DOWN:
            self.yy = self.y + player_rare
            self.xx = self.x
        elif self.direct == Direction.LEFT:
            self.xx = self.x - player_rare
            self.yy = self.y
        elif self.direct == Direction.RIGHT:
            self.xx = self.x + player_rare
            self.yy = self.y

        rect_tank = pygame.Rect(self.xx, self.yy, self.tank.get_width(), self.tank.get_height())

        rect_wall = pygame.Rect(wall.x, wall.y, wall.width, wall.height)
        if pygame.Rect.colliderect(rect_wall, rect_tank):
            self.bad_direct = self.direct
            return True
        self.bad_direct = Direction.NONE
        return False


class Wall(Display):
    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.images = pygame.image.load('pic/walls.gif')
        self.surface = kwargs['surface']

        self.width = self.images.get_width()
        self.height = self.images.get_height()

    def show(self):
        self.surface.blit(self.images, (self.x, self.y))

    def destroy_wall(self):
        pass


class SteelWall(Display):

    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.images = pygame.image.load('pic/steels.gif')
        self.surface = kwargs['surface']
        self.width = self.images.get_width()
        self.height = self.images.get_height()

    def show(self):
        self.surface.blit(self.images, (self.x, self.y))

    def destroy_wall(self):
        pass
