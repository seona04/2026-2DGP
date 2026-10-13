from pico2d import *
import random

# Game object class here

GROUND_Y = 60


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self, x):
        self.x, self.y = x, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Zombie:
    def __init__(self):
        self.x, self.y = 0, GROUND_Y
        self.frame = 0
        self.speed = 8
        self.follow_distance = 90
        self.image = load_image('zombie_run_animation.png')

    def update(self, target):
        self.frame = (self.frame + 1) % 10
        distance = target.x - self.x
        if distance > self.follow_distance:
            self.x += min(self.speed, distance - self.follow_distance)
        else:
            self.x += min(5, max(0, distance))

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        draw_width = frame_width / 2
        draw_height = frame_height / 2
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
                            self.x, self.y + draw_height / 2,
                            draw_width, draw_height)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global world

    running = True
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy(x) for x in random.sample(range(100, 701), 11)]
    world += team


def update_world():
    for o in world:
        if isinstance(o, Zombie):
            target = min(
                (boy for boy in world if isinstance(boy, Boy)),
                key=lambda boy: abs(boy.x - o.x),
            )
            o.update(target)
        else:
            o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


def main():
    open_canvas()
    reset_world()
    world.append(Zombie())

    while running:
        handle_events()
        update_world()
        render_world()
        delay(0.05)

    close_canvas()


if __name__ == '__main__':
    main()
