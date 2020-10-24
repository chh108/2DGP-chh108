import random
from pico2d import *

RES_DIR = 'C:/Users/최현호/Desktop/대학 파일들/2학년/2학기/2D게임프로그래밍/Final Term project/resource'

class Grass:
	def __init__(self):
		self.image = load_image(RES_DIR + '/grass.png')
	def draw(self):
		self.image.draw(400, 30)
	def update(self):
		pass

class Ball:
    def __init__(self, x, y, dx, dy):
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.image = load_image(RES_DIR + '/ball21x21.png')
    def update(self):
        self.x += self.dx
        self.y += self.dy
    def draw(self):
        self.image.draw(self.x, self.y)

balls = []

class Boy:
    #constructor
    # def __init__(self, pos, delta):
    #   self.x, self.y = pos
    #   self.dx, self.dy = delta
    def __init__(self):
        self.x = 0
        self.y = 60
        self.dx, self.dy = 0, 0
        self.fidx = random.randint(0, 7)
        self.image = load_image(RES_DIR + '/yoshi_run.png')
    def fire(self):
        ball = Ball(self.x, self.y, 2 * self.dx, 2 * self.dy)
        balls.append(ball)
        print("now ball count = %d" % len(balls))
    def draw(self):
        self.image.clip_draw( 42 + self.fidx * 27, 0, 27, 40, self.x, self.y)
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.fidx = (self.fidx + 1) % 10

if __name__ == "__main__":
	print("Running test code ^_^")
