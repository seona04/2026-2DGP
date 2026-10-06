import pico2d

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800


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
    pico2d.update_canvas()


def main():
    pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)

    while True:
        if not handle_events():
            break
        update()
        draw()

    pico2d.close_canvas()


if __name__ == "__main__":
    main()