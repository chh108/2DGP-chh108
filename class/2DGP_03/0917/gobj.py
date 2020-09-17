from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\grass.png')
        self.x, self.y = 400, 30
    def draw(self):
        self.image.draw(self.x, self.y)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(100, 500)
        self.image = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\run_animation.png')
        self.dx = random.random()
        self.fidx = random.randint(0,7)
    def draw(self):
        self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.x += self.dx * 5
        self.fidx = (self.fidx + 1) % 8

print(" Hello, this is gobj.py !")
print("My name is:", __name__)
if __name__ == '__main__':
    print("not imported")
