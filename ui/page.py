from pygame.locals import *

status = 0


def get_status():
    return status


def set_status(sta):
    global status
    status = sta


class Splash:
    def __init__(self, surface):
        self.surface = surface

    def graph(self):
        pass

    def show(self):
        pass

    def press_key(self,key):
        print(key)

        try:
            if key == K_SPACE:
                set_status(1)
        except Exception as error:
            print(error)
        finally:
            pass



class Game:
    def __init__(self, surface):
        self.surface = surface

    def graph(self):
        pass

    def show(self):
        pass

    def press_key(self,key):
        print(key,'game')
