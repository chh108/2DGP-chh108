import gfw
from pico2d import *
import horz_state

def enter():
    global image
    image = load_image('C:/Users/최현호/Desktop/대학 파일들/2학년/2학기/2D게임프로그래밍/Final Term project/resource/title.png')

def update():
    pass

def draw():
    image.draw(400, 300)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(horz_state)
def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
