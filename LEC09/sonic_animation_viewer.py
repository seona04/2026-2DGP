import pico2d

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
SPRITE_PATH = "sonic-sprite.png"
FIRST_FRAME_CLIP = (0, 445, 30, 40)

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