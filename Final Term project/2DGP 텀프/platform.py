from pico2d import *
import gfw
import random
import player

MOVE_SPD = 150

class Platform:
    SIZE = 40
    def __init__(self, pos, delta):
        self.pos = pos
        self.delta = delta
        self.image = gfw.image.load('res/Platform_max.png')
        self.start = gfw.image.load('res/Platform_big.png')
        mag = random.uniform(0.1, 1.0)
        self.width = mag * self.image.w // 2

    def update(self):
        x, y = self.pos
        dx, dy = self.delta
        x += dx * MOVE_SPD * gfw.delta_time
        #y += dy * MOVE_SPD * gfw.delta_time
        self.pos = x, y
        if not self.in_boundary():  # 바운더리 안에 있지 않으면 삭제
            gfw.world.remove(self)
    def draw(self):
        w, h = 80, 20
        x, y = self.pos
        self.image.draw(x, y, w, h)
        self.start.draw(250, 0, 500, 30)

    def in_boundary(self): # 발판 위치 확인 함수
        x, y = self.pos
        if x < -Platform.SIZE: return False
        if y < -Platform.SIZE: return False
        if x > get_canvas_width() + 10: return False
        if y > get_canvas_height() + 10: return False
        return True