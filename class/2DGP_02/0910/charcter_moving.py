from pico2d import*

open_canvas()

grass = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\grass.png')
character = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\character.png')

x = 0
while ( x < 800 ):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    x = x + 2
    update_canvas()
    delay(0.01)
    get_events()

close_canvas()
