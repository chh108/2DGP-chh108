from pico2d import *

import copy
import helper

class Boy:
    def __init__(self):
        self.image = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\run_animation.png')
        self.fidx = 1

        self.speed = 1
        self.delta = 0, 0
        self.target = None
        self.target_list = []
        self.pos = 0, 90

    def draw(self):
        self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.pos[0], self.pos[1])

    def update(self):
        self.fidx = (self.fidx + 1) % 8
        if self.target == None:
            self.speed = 1
            if len(self.target_list) != 0:
                self.target = copy.copy(self.target_list[0])
                self.target_list.pop(0)
                self.delta = helper.delta(self.pos, self.target, self.speed)
        helper.move_toward_obj(boy)


def handle_events():
    global running, boy
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            boy.speed += 1
            if boy.target == None:
                boy.target = e.x, HEIGHT - 1 - e.y
                boy.delta = helper.delta(boy.pos, boy.target, boy.speed)
            else:
                boy.delta = helper.delta(boy.pos, boy.target, boy.speed)
                boy.target_list.append((e.x, HEIGHT - 1 - e.y))
                print(boy.target_list)


open_canvas()
grass = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\grass.png')
character = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\run_animation.png')

boy = Boy()

done = False

running = True

WIDTH, HEIGHT = 800, 600


frame = 0

while running:
    clear_canvas()

    grass.draw(400, 30)
    
    boy.draw()

    update_canvas()

    handle_events()

    boy.update()

    delay(0.01)

close_canvas()
