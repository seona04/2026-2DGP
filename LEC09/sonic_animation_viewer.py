import pico2d

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
SPRITE_PATH = "sonic-sprite.png"
ACTION_FRAMES = {
    "walk": [
        (0, 447, 30, 39),
        (30, 447, 27, 39),
        (58, 447, 29, 39),
        (87, 447, 31, 39),
        (118, 447, 32, 39),
        (150, 447, 32, 39),
        (182, 447, 30, 39),
        (212, 447, 28, 39),
        (240, 447, 30, 39),
        (270, 447, 32, 39),
        (302, 447, 29, 39),
    ],
    "run": [
        (8, 407, 26, 39),
        (37, 407, 27, 39),
        (65, 407, 31, 39),
        (97, 407, 37, 39),
        (135, 407, 32, 39),
        (170, 407, 32, 39),
        (206, 407, 26, 39),
        (238, 407, 24, 39),
        (263, 407, 30, 39),
        (295, 407, 36, 39),
        (334, 407, 32, 39),
        (370, 407, 29, 39),
    ],
    "spin": [
        (1, 325, 29, 33),
        (35, 325, 29, 33),
        (67, 325, 30, 33),
        (98, 325, 31, 33),
        (131, 325, 29, 33),
        (162, 325, 29, 33),
        (193, 325, 30, 33),
        (230, 325, 31, 33),
        (268, 325, 30, 33),
    ],
}
ACTION_ORDER = tuple(ACTION_FRAMES)
current_action_index = 0
current_frame_index = 0
FIRST_FRAME_CLIP = ACTION_FRAMES["walk"][0]

sprite_sheet = None


def load_resources():
    global sprite_sheet
    sprite_sheet = pico2d.load_image(SPRITE_PATH)
    print(f"Sprite sheet size: {sprite_sheet.w} x {sprite_sheet.h}")


def handle_events():
    events = pico2d.get_events()
    for event in events:
        if event.type == "QUIT":
            return False
        elif event.type == "KEYDOWN" and event.key == "ESC":
            return False
    return True


def update():
    pass


def draw():
    pico2d.clear_canvas()
    if sprite_sheet is not None:
        sprite_sheet.clip_draw(
            *FIRST_FRAME_CLIP,
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2,
        )
    pico2d.update_canvas()


def main():
    pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    load_resources()

    while True:
        if not handle_events():
            break
        update()
        draw()

    pico2d.close_canvas()


if __name__ == "__main__":
    main()