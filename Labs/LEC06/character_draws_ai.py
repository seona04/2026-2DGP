# 실습 과제 진행(AI로 개발)
from pico2d import *
import math

# -----------------------------------
# 화면 설정
# -----------------------------------
open_canvas(800, 600)

# 캐릭터 이미지
character = load_image('character.png')


# -----------------------------------
# 캐릭터 위치
# -----------------------------------
x = 400
y = 300

# 현재 운동
# 0 = 원운동
# 1 = 사각운동
# 2 = 삼각운동
motion = 0

# 각 운동이 시작된 시간
motion_start_time = get_time()

# 운동 속도
speed = 150


# -----------------------------------
# 사각형 / 삼각형의 꼭짓점
# -----------------------------------

# 사각운동
square_points = [
    (500, 200),
    (500, 400),
    (300, 400),
    (300, 200)
]

# 삼각운동
triangle_points = [
    (500, 200),
    (300, 200),
    (400, 373)
]


# -----------------------------------
# 두 점 사이의 거리
# -----------------------------------
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# -----------------------------------
# 선분 위를 이동
# -----------------------------------
def move_on_line(points, elapsed, total_length):
    current_distance = (elapsed * speed) % total_length

    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]

        line_length = distance(x1, y1, x2, y2)

        if current_distance <= line_length:
            ratio = current_distance / line_length

            x = x1 + (x2 - x1) * ratio
            y = y1 + (y2 - y1) * ratio

            return x, y

        current_distance -= line_length

    return points[0]


# -----------------------------------
# 사각형 전체 길이
# -----------------------------------
square_length = 0

for i in range(len(square_points)):
    x1, y1 = square_points[i]
    x2, y2 = square_points[(i + 1) % len(square_points)]
    square_length += distance(x1, y1, x2, y2)


# -----------------------------------
# 삼각형 전체 길이
# -----------------------------------
triangle_length = 0

for i in range(len(triangle_points)):
    x1, y1 = triangle_points[i]
    x2, y2 = triangle_points[(i + 1) % len(triangle_points)]
    triangle_length += distance(x1, y1, x2, y2)


# -----------------------------------
# 게임 루프
# -----------------------------------
running = True

while running:

    # 이벤트 처리
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

    # 현재 시간
    current_time = get_time()

    # 현재 운동이 시작된 후 지난 시간
    elapsed = current_time - motion_start_time


    # -----------------------------------
    # 1. 원운동
    # -----------------------------------
    if motion == 0:

        center_x = 400
        center_y = 300
        radius = 150

        # 원운동
        angle = elapsed * 2

        x = center_x + math.cos(angle) * radius
        y = center_y + math.sin(angle) * radius

        # 원운동을 1바퀴 완료하면 사각운동
        if angle >= 2 * math.pi:

            motion = 1
            motion_start_time = current_time

            x, y = square_points[0]


    # -----------------------------------
    # 2. 사각운동
    # -----------------------------------
    elif motion == 1:

        x, y = move_on_line(
            square_points,
            elapsed,
            square_length
        )

        # 사각형 한 바퀴 완료
        if elapsed >= square_length / speed:

            motion = 2
            motion_start_time = current_time

            x, y = triangle_points[0]


    # -----------------------------------
    # 3. 삼각운동
    # -----------------------------------
    elif motion == 2:

        x, y = move_on_line(
            triangle_points,
            elapsed,
            triangle_length
        )

        # 삼각형 한 바퀴 완료
        if elapsed >= triangle_length / speed:

            motion = 0
            motion_start_time = current_time

            x = 550
            y = 300


    # -----------------------------------
    # 화면 출력
    # -----------------------------------
    clear_canvas()

    # 캐릭터 출력
    character.draw(x, y)

    update_canvas()

    delay(0.01)


# -----------------------------------
# 종료
# -----------------------------------
close_canvas()