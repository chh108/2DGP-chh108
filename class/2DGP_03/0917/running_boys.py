from pico2d import *

import gobj

import random

def handle_events():
    global running, boy
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_LEFT:
                boy.dx -= 5
            elif e.key == SDLK_RIGHT:
                boy.dx += 5
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                boy.dx = 0
            elif e.key == SDLK_RIGHT:
                boy.dx = 0
        elif e.type == SDL_MOUSEMOTION:
            boy.x, boy.y = e.x, get_canvas_height() - e.y - 1

open_canvas()

team = [ gobj.Boy() for i in range(11) ]

boy = team[0]
grass = gobj.Grass()

running = True            

while running:
    clear_canvas()
    grass.draw()
    for b in team: b.draw()
    update_canvas()
    
    handle_events()
    
    for b in team: b.update()

    delay(0.01)

close_canvas() 
