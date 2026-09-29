# 실습 과제 진행
from pico2d import *
open_canvas(800, 600)

character = load_image('character.png')

def move_circle():
    print ("CIRCLE")
    for deg in range(0, 360, 5):
        rad = math.radians(deg)
        x = 400 + 200 * math.cos(rad)
        y = 300 + 200 * math.sin(rad)
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.1)
    pass

def draw_top():
    pass

def draw_right():
    pass

def draw_bottom():
    pass

def draw_left():
    pass


def move_rectangle():
    print ("RECTANGLE")
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass

def move_triangle():
    print ("TRIANGLE")
    pass

while True:
    move_circle ()
    move_rectangle ()
    move_triangle ()
    pass

close_canvas()