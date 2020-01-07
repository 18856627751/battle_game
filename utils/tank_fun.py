from abc import *

from utils.params import Direction


class Display(metaclass=ABCMeta):

    @abstractmethod
    def show(self):
        pass


class Move(metaclass=ABCMeta):

    @abstractmethod
    def move(self, direct):
        pass

    @abstractmethod
    def is_inflict_wall(self, block):
        pass


class Block(metaclass=ABCMeta):
    pass


class Order(metaclass=ABCMeta):
    @abstractmethod
    def get_order(self):
        pass


class AutoMove(Move, ABC):
    @abstractmethod
    def is_inflict_wall(self, block):
        pass

    @abstractmethod
    def move(self,direct=Direction.NONE):
        pass
