import gfw
from pico2d import *
from player import Player
from score import Score
import gobj
from background import *


canvas_width = 500
canvas_height = 800

def enter():
    gfw.world.init(['bg', 'enemy', 'bullet', 'player', 'ui'])

    global background_city
    background_city = FixedBackground('bg_city.png')
    gfw.world.add(gfw.layer.bg, background_city)

    global background_cloud
    background_cloud = FixedBackground('clouds.png')
    gfw.world.add(gfw.layer.ui, background_cloud)

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global score
    score = Score(canvas_width - 20, canvas_height - 50)
    gfw.world.add(gfw.layer.ui, score)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/segoeprb.ttf', 40)

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()


def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
