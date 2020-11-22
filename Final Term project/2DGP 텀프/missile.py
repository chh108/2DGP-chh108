from pico2d import *
import gfw
import random
import player

MOVE_PPS = 200

class Missile:
    SIZE = 60
    def __init__(self, pos, delta):
        self.pos = pos  # 차이
        self.delta = delta
        self.image = gfw.image.load('res/missile.png')
        mag = random.uniform(0.3, 1.0)
        self.radius = mag * self.image.h // 2

    def update(self):
        x, y = self.pos
        dx, dy = self.delta
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS * gfw.delta_time
        self.pos = x, y
        if not self.in_boundary():  # 바운더리 안에 있지 않으면 삭제
            gfw.world.remove(self)
    def draw(self):
        x, y = self.pos
        w, h = self.radius * 2, self.radius * 2
        diameter = 2 * self.radius
        self.image.draw(x, y, diameter, diameter)

    def in_boundary(self): # 미사일 위치 확인 함수
        x, y = self.pos
        if x < -Missile.SIZE: return False
        if y < -Missile.SIZE: return False
        if x > get_canvas_width() + Missile.SIZE: return False
        if y > get_canvas_height() + Missile.SIZE: return False
        return True