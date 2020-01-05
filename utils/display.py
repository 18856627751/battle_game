from abc import *


class Display(metaclass=ABCMeta):

    @abstractmethod
    def show(self):
        pass
