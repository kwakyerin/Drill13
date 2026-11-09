from pico2d import load_image
from sdl2 import SDL_KEYDOWN, SDL_KEYUP, SDLK_i


item_select_image = None
is_open = False
key_down = False


def init():
    global item_select_image, is_open, key_down
    item_select_image = load_image('item_select.png')
    is_open = False
    key_down = False


def handle_event(event):
    global is_open, key_down

    if event.type == SDL_KEYDOWN and event.key == SDLK_i:
        if not key_down:
            is_open = not is_open
            key_down = True
        return True

    if event.type == SDL_KEYUP and event.key == SDLK_i:
        key_down = False
        return True

    return False


def draw():
    if is_open:
        item_select_image.draw(400, 300)


def finish():
    global item_select_image, is_open, key_down
    item_select_image = None
    is_open = False
    key_down = False
