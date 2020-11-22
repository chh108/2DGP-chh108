from pico2d import *
import gfw
import player

def init():
    global start, clouds
    start = gfw.image.load('res/bg.png')
    doing = gfw.image.load('res/bg_b.png')

def draw():
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    px, py = player.pos
    dx, dy = x - px, y - py
    start.clip_draw(0, 50, 640, 500, x + dx * 0.02, y + dy * 0.02, 600, 900) # 플레이어가 중앙으로 부터 떨어진 거리의 2%만큼 이동

def update():
    pass