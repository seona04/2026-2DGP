# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.1)

def draw_circle():
    print ("CIRCLE")
    for deg in range(0, 360, 5):
        rad = math.radians(deg)
        x = 400 + 200 * math.cos(rad)
        y = 300 + 200 * math.sin(rad)
       draw_character(x, y)
    pass

def draw_top():
    print ('TOP')
    y = 500
    for x in range(200, 601, 5):
        draw_character(x, y)
    pass

def draw_right():
    print ('RIGHT')
    x = 600
    for y in range(500, 99, -5):
        draw_character(x, y)
    pass

def draw_bottom():
    print ('BOTTOM')
    y = 100
    for x in range(600, 199, -5):
        draw_character(x, y)
    pass

def draw_left():
    print ('LEFT')
    x = 200
    for y in range(100, 501, 5):
        draw_character(x, y)
    pass

def draw_rectangle():
    print ("RECTANGLE")
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass

# 삼각형 꼭짓점: 왼쪽아래(200,100), 오른쪽아래(600,100), 꼭대기(400,500)

def draw_triangle_bottom():
    print ('TRIANGLE_BOTTOM')
    y = 100
    for x in range(200, 601, 5):
        draw_character(x, y)
    pass

def draw_triangle_right():
    print ('TRIANGLE_RIGHT')
    for y in range(100, 501, 5):
        x = 600 - 0.5 * (y - 100)
        draw_character(x, y)
    pass

def draw_triangle_left():
    print ('TRIANGLE_LEFT')
    for y in range(500, 99, -5):
        x = 400 - 0.5 * (500 - y)
        draw_character(x, y)
    pass

def draw_triangle():
    print ("TRIANGLE")
    draw_triangle_bottom()
    draw_triangle_right()
    draw_triangle_left()
    pass

while True:
    draw_circle ()
    draw_rectangle ()
    draw_triangle ()

close_canvas()