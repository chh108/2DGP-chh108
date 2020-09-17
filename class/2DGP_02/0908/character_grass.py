from pico2d import *

open_canvas()

grass = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\grass.png')
character = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

delay(5)

close_canvas()
