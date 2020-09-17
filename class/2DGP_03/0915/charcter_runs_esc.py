from pico2d import*

def handle_events():
    global running
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False

open_canvas()
grass = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\grass.png')
character = load_image('c:\\Users\\최현호\\Documents\\GitHub\\2DGP\\2DGP\\class\\run_animation.png')

        
running = True            
x = 0
frame = 0
while running and x < 800:
    clear_canvas()
    
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    
    update_canvas()

    x += 2
    frame = (frame + 1) % 8

    handle_events()
    
    delay(0.01)

close_canvas()
