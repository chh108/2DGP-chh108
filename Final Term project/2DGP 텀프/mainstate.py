from pico2d import *
import player
import gfw
import generator
import bg
import highscore
from tile import Tile

STATE_IN_GAME, STATE_GAME_OVER = range(2) # STATE_IN_GAME = 0, STATE_GAME_OVER = 1

def collides_distance(a, b):
    ax, ay = a.pos
    bx, by = b.pos
    radius_sum = a.radius + b.radius
    distance_sq = (ax-bx)**2 + (ay-by)**2
    return distance_sq < radius_sum**2 # 계산을 편하게 하기 위함

def check_collision(): # 충돌 체크 함수
    for m in gfw.world.objects_at(gfw.layer.missile):
        if collides_distance(player, m):
            wav_explosion.play()
            gfw.world.remove(m)
            dead = player.decrease_life()
            if dead:
                end_game()

def start_game():
    global state
    if state != STATE_GAME_OVER:
        return

    player.reset() # player가 리셋하도록 설정함.
    gfw.world.clear_at(gfw.layer.missile) # 기존의 미사일 객체들을 전부 삭제
    gfw.world.remove(highscore)

    state = STATE_IN_GAME

    global score
    score = 0

    music_bg.repeat_play()

def end_game():
    global state
    print('Dead')
    state = STATE_GAME_OVER
    music_bg.stop()

    highscore.add(score)
    gfw.world.add(gfw.layer.ui, highscore)

def enter(): # GAME_STATE의 사이클
    gfw.world.init(['bg', 'missile', 'player', 'ui', 'tile'])
    player.init()
    gfw.world.add(gfw.layer.player, player)
    bg.init()
    gfw.world.add(gfw.layer.bg, bg)

    global game_over_image
    game_over_image = gfw.image.load('res/game_over.png')

    global font
    font = gfw.font.load('res/ConsolaMalgun.ttf', 30)

    global music_bg, wav_item, wav_explosion, wav_jump
    music_bg = load_music('res/bgm.mp3')
    wav_item = load_wav('res/item.wav')
    wav_explosion = load_wav('res/explosion.wav')

    highscore.load()

    global state
    state = STATE_GAME_OVER
    start_game()

def exit():
    global music_bg, wav_item, wav_explosion
    del music_bg
    del wav_item
    del wav_explosion
    pass

def update():
    if state != STATE_IN_GAME: # 게임 오버 구현
        return

    global score
    score += gfw.delta_time # delta 타임 값을 계속 더해줌
    gfw.world.update() # 월드 업데이트
    generator.update(score) # 점수에 따른 미사일 생성
    check_collision() # 충돌 체크

    # 플레이어가 떨어질 때 타일과 충돌하는지 검사합니다.
    if player.speed_y < 0.0:
        player_half_w = player.col_box_w * 0.5
        player_half_h = player.col_box_h * 0.5
        player_left = player.pos[0] - player_half_w
        player_right = player.pos[0] + player_half_w
        player_bottom = player.pos[1] - player_half_h
        player_top = player.pos[1] + player_half_h

        for i in gfw.world.objects_at(gfw.layer.tile):
            x, y = i.pos[0], i.pos[1]
            half_w = 80.0 * 0.5
            half_h = 20.0 * 0.5
            left = x - half_w
            right = x + half_w
            bottom = y - half_h
            top = y + half_h

            if player.pos[1] > y and player_left <= right and player_right >= left and player_bottom <= top and player_top >= bottom:
                player.pos = player.pos[0], y + 30.0
                player.jump = False
                player.speed_y = 0.0
                break


def draw():
    gfw.world.draw()
    score_pos = 30, get_canvas_height() - 30
    font.draw(*score_pos, 'Score : %.1f' % score, (255,255,255))
    if state == STATE_GAME_OVER:
        center = get_canvas_width() // 2, get_canvas_height()  * 2 // 3
        game_over_image.draw(*center)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_RETURN:
            start_game()

    player.handle_event(e)

if __name__ == '__main__':
    gfw.run_main()