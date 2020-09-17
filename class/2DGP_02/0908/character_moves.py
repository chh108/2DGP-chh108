from pico2d import *

open_canvas()

grass = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\grass.png')
character = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\character.png')

x = 0
while ( x < 800 ):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)

close_canvas()
