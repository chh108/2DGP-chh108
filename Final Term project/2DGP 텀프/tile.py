from pico2d import *
import gfw
import random
import player

MOVE_SPD = 150

class Tile:
    SIZE = 40
    def __init__(self, pos, delta):
        self.pos = pos
        self.prev_pos_y = player.pos[1]
        self.played = False
        self.delta = delta
        self.image = gfw.image.load('res/Platform_max.png')
        self.start = gfw.image.load('res/Platform_big.png')
        mag = random.uniform(0.1, 1.0)
        self.width = mag * self.image.w // 2

    def update(self):
        x, y = self.pos[0], self.pos[1] - max(0.0, player.pos[1] - self.prev_pos_y)
        dx, dy = self.delta
        x += dx * MOVE_SPD * gfw.delta_time
        #y += dy * MOVE_SPD * gfw.delta_time
        self.pos = x, y
        self.checking = x, y
        if not self.in_boundary():  # 바운더리 안에 있지 않으면 삭제
            gfw.world.remove(self)
        
        self.prev_pos_y = player.pos[1]

    def draw(self):
        w, h = 80, 20
        x, y = self.pos
        self.image.draw(x, y, w, h)
        if (player.pos[1] < 40):
            self.start.draw(250, 0, 500, 30)

    def in_boundary(self): # 발판 위치 확인 함수
        x, y = self.pos
        if x < -Tile.SIZE: return False
        if y < -Tile.SIZE: return False
        if x > get_canvas_width() + 10: return False
        if y > get_canvas_height() + 10: return False
        return True