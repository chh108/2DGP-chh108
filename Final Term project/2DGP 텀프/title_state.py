import gfw
from pico2d import *
import main_state
from gobj import *


canvas_width = 500
canvas_height = 800
def enter():
    global image
    image = load_image(RES_DIR + 'title.png')

def update():
    pass

def draw():
    image.clip_draw_to_origin(0, 0, 800, 600, 0, 0, 500, 800)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(main_state)
def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
