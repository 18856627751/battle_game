from tanks.player_tank import *


class GameArea:
    def __init__(self, surface):
        self.surface = surface

        self.walls = []

        file = open('map/tank.map', 'r', encoding='utf-8')
        for row, line in enumerate(file):
            line = line.strip()
            for column, item in enumerate(line):
                if item == '1':
                    wall = Wall(surface=self.surface, x=column * BLOCK, y=row * BLOCK)
                    self.walls.append(wall)
                elif item == '2':
                    steel = SteelWall(surface=self.surface, x=column * BLOCK, y=row * BLOCK)
                    self.walls.append(steel)
                elif item == '8':
                    self.player = PlayerTank(surface=self.surface, x=column * BLOCK, y=row * BLOCK)

        file.close()

    def graph(self):
        self.surface.fill((0, 0, 0))

        for wall in self.walls:
            wall.show()

        self.player.show()

        for wall in self.walls:

            if self.player.is_inflict_wall(wall):
                break




    def press(self, keys):
        if keys[K_UP]:
            self.player.move(Direction.UP)
        elif keys[K_DOWN]:
            self.player.move(Direction.DOWN)
        elif keys[K_LEFT]:
            self.player.move(Direction.LEFT)
        elif keys[K_RIGHT]:
            self.player.move(Direction.RIGHT)


class GameInfo:
    def __init__(self, surface):
        self.surface = surface

    def graph(self):
        self.surface.fill((0x99, 0x99, 0x99))
