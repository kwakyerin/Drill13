from pico2d import load_image
from sdl2 import (SDL_KEYDOWN, SDL_KEYUP, SDLK_0, SDLK_i, SDLK_KP_0)


item_select_image = None
is_open = False
key_down = False
shooting_enabled = True


def init():
    global item_select_image, is_open, key_down, shooting_enabled
    item_select_image = load_image('item_select.png')
    is_open = False
    key_down = False
    shooting_enabled = True


def handle_event(event):
    global is_open, key_down, shooting_enabled

    if event.type == SDL_KEYDOWN and event.key == SDLK_i:
        if not key_down:
            is_open = not is_open
            key_down = True
        return True

    if event.type == SDL_KEYUP and event.key == SDLK_i:
        key_down = False
        return True

    if event.type == SDL_KEYDOWN and event.key in (SDLK_0, SDLK_KP_0):
        if is_open:
            is_open = False
        shooting_enabled = False
        return True

    return False


def can_shoot():
    return shooting_enabled


def draw():
    if is_open:
        item_select_image.draw(400, 300)


def finish():
    global item_select_image, is_open, key_down, shooting_enabled
    item_select_image = None
    is_open = False
    key_down = False
    shooting_enabled = True
