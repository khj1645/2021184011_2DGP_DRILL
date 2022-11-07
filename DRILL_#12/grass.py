from pico2d import *

class Grass:
    image = None
    def __init__(self, x, y):
        if Grass.image == None:
            self.image = load_image('grass.png')
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


