import gfw
from pico2d import *
import title_state

canvas_width = 500
canvas_height = 800

def enter():
    global image, elapsed
    image = load_image('res/loading.png')
    elapsed = 0

def update():
    global elapsed
    elapsed += gfw.delta_time
    print(elapsed)
    if elapsed > 1.0:
        gfw.change(title_state)

def draw():
    image.clip_draw_to_origin(120, 0, 910, 512, 0, 0, 600, 900)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
