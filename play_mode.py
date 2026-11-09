from pico2d import *
import game_framework
import game_world
import item_mode
import title_mode
from boy import Boy
from grass import Grass

paused = False
pause_started_at = 0.0
pause_key_down = False
pause_image = None


def handle_events():
    global paused, pause_started_at, pause_key_down

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            if not pause_key_down:
                if paused:
                    boy.idle_started_at += get_time() - pause_started_at
                    paused = False
                else:
                    pause_started_at = get_time()
                    paused = True
            pause_key_down = True
        elif event.type == SDL_KEYUP and event.key == SDLK_p:
            pause_key_down = False
        elif item_mode.handle_event(event):
            continue
        elif not paused or event.type == SDL_KEYUP:
            boy.handle_event(event)


def init():
    global boy, paused, pause_started_at, pause_key_down, pause_image
    paused = False
    pause_started_at = 0.0
    pause_key_down = False
    pause_image = load_image('pause_icon.png')
    item_mode.init()
    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    if not paused:
        game_world.update()


def render():
    clear_canvas()
    game_world.render()
    item_mode.draw()
    if paused:
        pause_image.draw(400, 300)
    update_canvas()


def finish():
    global pause_image
    game_world.clear()
    pause_image = None
    item_mode.finish()
