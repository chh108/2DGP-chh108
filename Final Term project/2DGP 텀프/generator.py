from pico2d import *

import gfw
from missile import Missile
import random
from platform import Platform

MISSILE_COUNT = 4
PLATFORM_COUNT = 10

def update(score):
    max_count = MISSILE_COUNT + score / 10
    max_count2 = PLATFORM_COUNT
    if gfw.world.count_at(gfw.layer.missile) < max_count:
        generate_m(score)
    elif gfw.world.count_at(gfw.layer.platform) < max_count2:
        generate_p(score)

def generate_m(score):
    dx = random.random() # 이동속도 랜덤
    if dx < 0.5: dx -= 1.0 # 만들어진 방향에서 화면으로 오도록 하기 위함 ex) 위에서 만들어지면 아래로 이동

    dy = 0

    mag = 1 + score / 60 # 점수에 따른 속도 배율 60점 -> 속도 2배
    dx *= mag
    dy *= mag

    side = random.randint(1, 2) # 1 : left 2 : right
    if side == 1:
        x = 0
        y = random.uniform(0, get_canvas_height())
        if dx < 0: dx = -dx

    elif side == 2:
        x = get_canvas_width()
        y = random.uniform(0, get_canvas_height())
        if dx > 0: dx = - dx

    m = Missile((x,y), (dx,dy))
    gfw.world.add(gfw.layer.missile, m)

def generate_p(score):
    dx = random.random()
    if dx < 0.5: dx -= 1.0

    dy = 0

    x = random.uniform(0, get_canvas_width())
    y = random.uniform(50, get_canvas_height())

    p = Platform((x,y), (dx,dy))
    gfw.world.add(gfw.layer.platform, p)