from tanks.player_tank import *
from utils.tank_fun import *


class GameArea:
    def __init__(self, surface):
        self.surface = surface

        self.view = []

        file = open('map/tank.map', 'r', encoding='utf-8')
        for row, line in enumerate(file):
            line = line.strip()
            for column, item in enumerate(line):
                if item == '1':
                    wall = Wall(surface=self.surface, x=column * BLOCK, y=row * BLOCK)
                    self.view.append(wall)
                elif item == '2':
                    steel = SteelWall(surface=self.surface, x=column * BLOCK, y=row * BLOCK)
                    self.view.append(steel)
                elif item == '3':
                    water = Water(surface=self.surface, x=column * BLOCK, y=row * BLOCK)
                    self.view.append(water)
                elif item == '4':
                    grass = Grass(surface=self.surface, x=column * BLOCK, y=row * BLOCK)
                    self.view.append(grass)
                elif item == '8':
                    self.player = PlayerTank(surface=self.surface, x=column * BLOCK, y=row * BLOCK)
                    self.view.append(self.player)
                elif item == '9':
                    enemy = Enemy(surface=self.surface, x=column * BLOCK, y=row * BLOCK)
                    self.view.append(enemy)

        file.close()

    def graph(self):
        self.surface.fill((0, 0, 0))

        # 材料排序
        self.view.sort(key=lambda view: view.get_order() if isinstance(view, Order) else 0)

        for item in self.view:

            item.show()

        try:
            for block in list(self.view):
                if isinstance(block, Block):
                    if isinstance(block, Wall) or isinstance(block, SteelWall) or isinstance(block, Enemy):
                        for move in self.view:
                            if isinstance(move, Bullet):
                                inflict = move.is_inflict_wall(block)
                                if inflict:
                                    move.destroy(self.view)
                                    self.view.remove(move)
                                    if isinstance(block, Wall) or isinstance(block, Enemy):
                                        self.view.remove(block)
                                    raise Exception('break')
        except Exception as error:
            pass

        try:
            for block in self.view:
                if isinstance(block, Block):
                    for move in self.view:
                        if isinstance(move, PlayerTank) and not isinstance(block, PlayerTank):
                            if self.player.is_inflict_wall(block):
                                raise Exception('break')
        except Exception as e:
            pass


        try:
            for block in self.view:
                if isinstance(block, Block):
                    for move in self.view:
                        if isinstance(move, Enemy) and not isinstance(block, Enemy):

                            if move.is_inflict_wall(block):
                                raise Exception('break')
        except Exception as e:
            pass


    def press(self, keys):
        if keys[K_UP]:
            self.player.move(Direction.UP)
        elif keys[K_DOWN]:
            self.player.move(Direction.DOWN)
        elif keys[K_LEFT]:
            self.player.move(Direction.LEFT)
        elif keys[K_RIGHT]:
            self.player.move(Direction.RIGHT)
        elif keys[K_SPACE]:
            bullet = self.player.fire()
            self.view.append(bullet)


class GameInfo:
    def __init__(self, surface):
        self.surface = surface

    def graph(self):
        self.surface.fill((0x99, 0x99, 0x99))
