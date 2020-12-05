from pico2d import *
import gfw

MAX_LIFE = 3
MOVE_PPS = 300
FPS = 60
Draw_pixel = 0.5
Player_accel = 1.5
Player_friction = -0.2
Player_gravity = 0.8

def init():
    global image, pos, radius
    image = gfw.image.load('res/mario_run_left.png')
    radius = image.h // 2

    global run_left, run_right
    run_left = gfw.image.load('res/mario_run_left.png')
    run_right = gfw.image.load('res/mario_run_right.png')

    global heart_red, heart_white
    heart_red = gfw.image.load('res/heart_red.png')
    heart_white = gfw.image.load('res/heart_white.png')

    global wav_jump
    wav_jump = load_wav('res/jump.wav')

    global vel_x, vel_y
    vel_x, vel_y = 0, 0

    global draw_check
    draw_check = 1

    global fidx, time
    fidx = 0
    time = 0

    global dir
    dir = 0

    global jump, Key_down
    jump = False
    Key_down = False

    global speed_y
    speed_y = 0.0

    global col_box_w, col_box_h
    col_box_w = 32.0
    col_box_h = 32.0

    reset()

def reset():
    global pos
    pos = get_canvas_width() // 2, 30

    global delta_x, delta_y
    delta_x, delta_y = 0, 0

    global life
    life = MAX_LIFE

def decrease_life():
    global life
    life -= 1
    return life <= 0

def update():
    global fidx, time
    time += gfw.delta_time
    frame = time * 15
    fidx = int(frame) % 4

    global pos
    global speed_y
    global jump

    to_y = pos[1]
    speed_y -= gfw.delta_time * 15.0
    if speed_y != 0.0:
        to_y += speed_y

        if to_y < 30.0:
            to_y = 30.0
            speed_y = 0.0
            jump = False

    # to_y = pos[1] + speed_y
    # if to_y > 30.0:
    #     speed_y -= gfw.delta_time * 15.0

    global dir, draw_check

    acc_x, acc_y = 0.0, 0.0
    if dir == 1:
        acc_x = -Player_accel
        draw_check = 1
    elif dir == 2:
        acc_x = Player_accel
        draw_check = 2
    elif dir == 3:
        acc_x = 0

    global vel_x
    acc_x += vel_x * Player_friction
    vel_x += acc_x

    x, y = pos
    x += vel_x + 0.5 * acc_x

    hw, hh = image.w // 2 - 15, image.h // 2 + 25
    x = clamp(hw, x, get_canvas_width() - hw)
    pos = x, to_y

    # global acc_x, acc_y, dir, draw_check
    # acc_x, acc_y = 0, Player_gravity

    # if dir == 1:
    #     acc_x = -Player_accel
    #     draw_check = 1
    # elif dir == 2:
    #     acc_x = Player_accel
    #     draw_check = 2
    # elif dir == 3:
    #     acc_x = 0

    # global jump, pos, vel_x, vel_y
    # if jump == True:
    #     vel_y = 10
    # else:
    #     vel_y -= 3

    # acc_x += vel_x * Player_friction
    # vel_x += acc_x
    # vel_y -= acc_y

    # x, y = pos
    # x += vel_x + 0.5 * acc_x
    # y += vel_y - 0.5 * acc_y

    # hw, hh = image.w // 2 - 15, image.h // 2 + 25
    # x = clamp(hw, x, get_canvas_width() - hw)
    # y = clamp(hh, y, get_canvas_height() - hh)
    # pos = x, y

def draw():
    global image, pos, fidx, draw_check, run_left, run_right
    sx = fidx * 15 + fidx * 2
    if draw_check == 1:
        run_left.clip_draw(sx, 0, 15, 15, *pos, 40, 50)
    if draw_check == 2:
        run_right.clip_draw(sx, 0, 15, 15, *pos, 40, 50)

    x, y = get_canvas_width() - 30, get_canvas_height() - 30  # 하트를 오른쪽 위에서부터 그려준다.
    for i in range(MAX_LIFE):
        heart = heart_red if i < life else heart_white
        heart.draw(x, y)
        x -= heart.w

def handle_event(e):
    global dir, jump
    global speed_y
    global pos

    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_LEFT:
            dir = 1
        elif e.key == SDLK_RIGHT:
            dir = 2
        elif e.key == SDLK_UP:
            if jump == False:
                jump = True
                wav_jump.play()
                speed_y = 8.0

    elif e.type == SDL_KEYUP:
        if e.key == SDLK_LEFT:
            dir = 3
        elif e.key == SDLK_RIGHT:
            dir = 3
        elif e.key == SDLK_UP:
            pass
            #jump = False