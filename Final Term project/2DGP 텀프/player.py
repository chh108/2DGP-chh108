import random
from pico2d import *
import gfw
from gobj import *

WIDTH = 500
HEIGHT = 800
FPS = 60

Draw_pixel = 0.5
Player_accel = 1.5
Player_friction = -0.2
Player_gravity = 0.8

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  1,
        (SDL_KEYDOWN, SDLK_RIGHT): 2,
        (SDL_KEYUP, SDLK_LEFT):    3,
        (SDL_KEYUP, SDLK_RIGHT):   3,
    }

    #constructor
    def __init__(self):
        # self.game = game
        self.image = load_image(RES_DIR + '/mario_run_left.png')
        self.image2 = load_image(RES_DIR + '/mario_run_right.png')
        self.fidx = 0
        self.time = 0
        self.draw_check = 1
        self.pos_x, self.pos_y = WIDTH / 2, HEIGHT / 2
        self.vel_x, self.vel_y = 0, 0
        self.acc_x, self.acc_y = 0, 0
        self.dir = 0

    def draw(self):
        width = 15
        sx = self.fidx * width + self.fidx * 2
        if self.draw_check == 1:
            self.image.clip_draw(sx, 0, width, 15, self.pos_x, self.pos_y, 30, 40)
        if self.draw_check == 2:
            self.image2.clip_draw(sx, 0, width, 15, self.pos_x, self.pos_y, 30, 40)

    def jump(self):
        self.y -= 0.1
        landed = False
        self.y += 0.1
        if landed:
            self.vel_y = +15

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.dir = Player.KEY_MAP[pair]

    def update(self):
        self.time += gfw.delta_time
        frame = self.time * 15
        self.fidx = int(frame) % 4
        self.acc_x, self.acc_y = 0, Player_gravity

        if self.dir == 1:
            self.acc_x = -Player_accel
            self.draw_check = 1
        elif self.dir == 2:
            self.acc_x = Player_accel
            self.draw_check = 2
        elif self.dir == 3:
            self.acc_x = 0

        self.acc_x += self.vel_x * Player_friction
        self.vel_x += self.acc_x
        #self.vel_y -= self.acc_y
        self.pos_x += self.vel_x + 0.5 * self.acc_x
        self.pos_y += self.vel_y - 0.5 * self.acc_y

        if self.pos_x > WIDTH - 15:
            self.pos_x = WIDTH - 15
        elif self.pos_x < 15:
            self.pos_x = 15
        if self.pos_y < 20:
            self.pos_y = 20

if __name__ == "__main__":
    for (l,t,r,b) in Player.IMAGE_RECTS:
        l *= 2
        t *= 2
        r *= 2
        b *= 2
        l -= 1
        r += 2
        print('(%3d, %d, %d, %d),' % (l,t,r,b))