from pico2d import *

import gfw
from missile import Missile
import random

MISSILE_COUNT = 10

def update(score):
    max_count = MISSILE_COUNT + score / 10
    if gfw.world.count_at(gfw.layer.missile) < max_count:
        generate(score)

def generate(score):
    dx = random.random() # 이동속도 랜덤
    if dx < 0.5: dx -= 1.0 # 만들어진 방향에서 화면으로 오도록 하기 위함 ex) 위에서 만들어지면 아래로 이동

    dy = random.random()
    if dy < 0.5: dy -= 1.0

    mag = 1 + score / 60 # 점수에 따른 속도 배율 60점 -> 속도 2배
    dx *= mag
    dy *= mag

    side = random.randint(1, 4) # 1 : left 2 : down 3 : right 4 : up 각 모서리에서만 생성되도록 적용
    if side == 1:
        x = 0
        y = random.uniform(0, get_canvas_height())
        if dx < 0: dx = -dx

    elif side == 2:
        x =  random.uniform(0, get_canvas_width())
        y = 0
        if dy < 0 : dy = -dy

    elif side == 3:
        x = get_canvas_width()
        y = random.uniform(0, get_canvas_height())
        if dx > 0: dx = - dx

    elif side == 4:
        x = random.uniform(0, get_canvas_width())
        y = get_canvas_height()
        if dy > 0: dy = -dx

    m = Missile((x,y), (dx,dy))
    gfw.world.add(gfw.layer.missile, m)