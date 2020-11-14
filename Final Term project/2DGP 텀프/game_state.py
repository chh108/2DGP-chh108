import gfw
from pico2d import *
from gobj import *

def enter():
    global grass, Player
    grass = Grass()
    boy = Boy()

def update():
    boy.update()

def draw():
    grass.draw()
    boy.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LEFT):
        boy.dir = 1
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_RIGHT):
        boy.dir = 2
    elif (e.type, e.key) == (SDL_KEYUP, SDLK_LEFT):
        boy.dir = 3
    elif (e.type, e.key) == (SDL_KEYUP, SDLK_RIGHT):
        boy.dir = 3
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
