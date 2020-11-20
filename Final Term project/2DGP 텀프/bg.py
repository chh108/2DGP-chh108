from pico2d import *
import gfw
import player

def init():
    global city, clouds
    city = gfw.image.load('res/bg_city.png')
    clouds = gfw.image.load('res/clouds.png')

def draw():
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    px, py = player.pos
    dx, dy = x - px, y - py
    city.draw(x + dx * 0.02, y + dy * 0.02, 600, 900) # 플레이어가 중앙으로 부터 떨어진 거리의 2%만큼 이동
    clouds.draw(x + dx * 0.05, y + dy * 0.05, 600, 900)

def update():
    pass