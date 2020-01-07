import random
import time

import pygame
from pygame.locals import *

from utils.tank_fun import *
from utils.params import *


class PlayerTank(Display, Move, Block, Order):
    def get_order(self):
        return 50

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
        self.__move_time = 0
        self.width = self.images_player[0].get_width()
        self.height = self.images_player[0].get_height()

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
        x = self.x
        y = self.y
        if self.direct == Direction.UP:
            x = self.x + self.tank.get_width() / 2
        elif self.direct == Direction.DOWN:
            x = self.x + self.tank.get_width() / 2
            y = self.y + self.tank.get_height()
        elif self.direct == Direction.LEFT:
            y = self.y + self.tank.get_height() / 2
        elif self.direct == Direction.RIGHT:
            x = self.x + self.tank.get_width()
            y = self.y + self.tank.get_height() / 2

        bullet = Bullet(surface=self.surface, x=x, y=y, direct=self.direct)
        return bullet

    def move(self, direct):
        now = time.time()
        if now - self.__move_time < 0.05:
            return
        self.__move_time = now

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
            self.xx = self.x
            if self.yy < 0:
                self.bad_direct = self.direct
                return True
        elif self.direct == Direction.DOWN:
            self.yy = self.y + player_rare
            self.xx = self.x
            if self.yy + self.tank.get_height() > GAME_HEIGHT:
                self.bad_direct = self.direct
                return True
        elif self.direct == Direction.LEFT:
            self.xx = self.x - player_rare
            self.yy = self.y
            if self.xx < 0:
                self.bad_direct = self.direct
                return True
        elif self.direct == Direction.RIGHT:
            self.xx = self.x + player_rare
            self.yy = self.y
            if self.xx + self.tank.get_width() > GAME_WIDTH:
                self.bad_direct = self.direct
                return True
        rect_tank = pygame.Rect(self.xx, self.yy, self.width, self.height)

        rect_wall = pygame.Rect(wall.x, wall.y, wall.width, wall.height)
        print(wall.x, wall.y, wall.width, wall.height)
        if pygame.Rect.colliderect(rect_wall, rect_tank):
            self.bad_direct = self.direct

            return True
        self.bad_direct = Direction.NONE

        return False


class Bullet(Move, Display, Order):

    def get_order(self):
        return 50

    def __init__(self, **kwargs):

        self.img = pygame.image.load('pic/tankmissile.gif')
        self.surface = kwargs['surface']
        self.direct = kwargs['direct']
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.xx = 0
        self.yy = 0
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        if self.direct == Direction.UP:
            self.x = kwargs['x'] - self.img.get_width() / 2
            self.y = kwargs['y'] - self.img.get_height()
        elif self.direct == Direction.DOWN:
            self.x = kwargs['x'] - self.img.get_width() / 2
        elif self.direct == Direction.LEFT:
            self.x = kwargs['x'] - self.img.get_width()
            self.y = kwargs['y'] - self.img.get_height() / 2
        elif self.direct == Direction.RIGHT:
            self.y = kwargs['y'] - self.img.get_height() / 2

        self.xx = self.x
        self.yy = self.y

    def move(self, direct):
        if direct == Direction.UP:
            self.y -= bullet_rare
        elif direct == Direction.DOWN:
            self.y += bullet_rare
        elif direct == Direction.LEFT:
            self.x -= bullet_rare
        elif direct == Direction.RIGHT:
            self.x += bullet_rare

    def is_inflict_wall(self, wall):

        if self.xx < 0 or self.xx > GAME_WIDTH - self.img.get_width():
            return True
        elif self.yy < 0 or self.yy > GAME_WIDTH - self.img.get_height():
            return True

        rect_bullet = pygame.Rect(self.xx, self.yy, self.img.get_width(), self.img.get_height())
        rect_wall = pygame.Rect(wall.x, wall.y, wall.width, wall.height)
        if pygame.Rect.colliderect(rect_bullet, rect_wall):
            return True
        return False

    def show(self):
        self.move(self.direct)
        self.xx = self.x
        self.yy = self.y
        if self.direct == Direction.UP:
            self.yy = self.y - inflict_param
        elif self.direct == Direction.DOWN:
            self.yy = self.y + inflict_param
        elif self.direct == Direction.LEFT:
            self.xx = self.x - inflict_param
        elif self.direct == Direction.RIGHT:
            self.xx = self.x + inflict_param

        self.surface.blit(self.img, (self.x, self.y))

    def destroy(self, view):
        blast = Blast(surface=self.surface, x=self.xx + self.width / 2, y=self.yy + self.height, view=view)
        view.append(blast)


class Wall(Display, Block, Order):
    def get_order(self):
        return 40

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


class SteelWall(Display, Block, Order):

    def get_order(self):
        return 0

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


class Water(Display, Block, Order):

    def get_order(self):
        return 20

    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.images = pygame.image.load('pic/water.gif')
        self.surface = kwargs['surface']
        self.width = self.images.get_width()
        self.height = self.images.get_height()

    def show(self):
        self.surface.blit(self.images, (self.x, self.y))

    def destroy_wall(self):
        pass


class Grass(Display, Order):

    def get_order(self):
        return 100

    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.images = pygame.image.load('pic/grass.png')
        self.surface = kwargs['surface']
        self.width = self.images.get_width()
        self.height = self.images.get_height()

    def show(self):
        self.surface.blit(self.images, (self.x, self.y))

    def destroy_wall(self):
        pass


class Blast(Display):

    def get_order(self):
        return 90

    def __init__(self, **kwargs):
        self.surface = kwargs['surface']
        self.images = []
        self.view = kwargs['view']
        for i in range(1, 33):
            self.images.append(pygame.image.load('pic/blast_%d.png' % i))
        self.index = 0

        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()
        self.x = kwargs['x'] - self.width / 2
        self.y = kwargs['y'] - self.height / 2

    def show(self):
        img = self.images[self.index]
        self.surface.blit(img, (self.x, self.y))
        self.index += 1
        if self.index >= len(self.images):
            self.view.remove(self)
            self.index = 0


class Enemy(Display, AutoMove, Order, Block):
    def get_order(self):
        return 50

    def __init__(self, **kwargs):
        self.surface = kwargs['surface']
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.xx = 0
        self.yy = 0
        self.__move_time = 0

        self.images_player = [
            pygame.image.load('pic/enemy1U.gif'),
            pygame.image.load('pic/enemy1D.gif'),
            pygame.image.load('pic/enemy1L.gif'),
            pygame.image.load('pic/enemy1R.gif')
        ]
        self.direct = Direction.DOWN
        self.tank = None
        self.bad_direct = Direction.NONE

        self.width = self.images_player[0].get_width()
        self.height = self.images_player[0].get_height()

    def show(self):


        if self.direct == Direction.UP:
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

        self.move(self.direct)

    def move(self, direct=Direction.NONE):
        print(self.x, self.y, self.xx, self.yy)
        print("show")
        now = time.time()
        if now - self.__move_time > 2:
            self.direct = random.choices([Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT])[0]
            self.__move_time = now

        if self.bad_direct == self.direct:
            self.direct = random.choices([Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT])[0]
            self.bad_direct = Direction.NONE
        elif self.direct == Direction.UP and self.bad_direct != self.direct:
            self.y -= player_rare
        elif self.direct == Direction.DOWN and self.bad_direct != self.direct:
            self.y += player_rare
        elif self.direct == Direction.LEFT and self.bad_direct != self.direct:
            self.x -= player_rare
        elif self.direct == Direction.RIGHT and self.bad_direct != self.direct:
            self.x += player_rare

    def fire(self):

        if self.direct == Direction.UP:
            x = self.x + self.tank.get_width() / 2
        elif self.direct == Direction.DOWN:
            x = self.x + self.tank.get_width() / 2
            y = self.y + self.tank.get_height()
        elif self.direct == Direction.LEFT:
            y = self.y + self.tank.get_height() / 2
        elif self.direct == Direction.RIGHT:
            x = self.x + self.tank.get_width()
            y = self.y + self.tank.get_height() / 2

        bullet = Bullet(surface=self.surface, x=x, y=y, direct=self.direct)
        return bullet

    def is_inflict_wall(self, wall):

        if self.direct == Direction.UP:
            self.yy = self.y - player_rare
            self.xx = self.x
            if self.yy < 0:
                self.bad_direct = self.direct
                return True
        elif self.direct == Direction.DOWN:
            self.yy = self.y + player_rare
            self.xx = self.x
            if self.yy + self.tank.get_height() > GAME_HEIGHT:
                self.bad_direct = self.direct
                return True
        elif self.direct == Direction.LEFT:
            self.xx = self.x - player_rare
            self.yy = self.y
            if self.xx < 0:
                self.bad_direct = self.direct
                return True
        elif self.direct == Direction.RIGHT:
            self.xx = self.x + player_rare
            self.yy = self.y
            if self.xx + self.tank.get_width() > GAME_WIDTH:
                self.bad_direct = self.direct
                return True
        rect_tank = pygame.Rect(self.xx, self.yy, self.width, self.height)

        rect_wall = pygame.Rect(wall.x, wall.y, wall.width, wall.height)
        if pygame.Rect.colliderect(rect_wall, rect_tank):
            self.bad_direct = self.direct
            return True
        self.bad_direct = Direction.NONE

        return False