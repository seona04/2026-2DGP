from pico2d import *
 
open_canvas(800, 600)

character_sheet = load_image('character_sheet.png')

TARGET_SIZE = 400
FRAME_DELAY = 0.08
REPEAT_COUNT = 5
PAUSE_SEC = 1.0
CENTER_X, CENTER_Y = 400, 300

# 각 프레임은 (left, bottom, width, height) 튜플로 저장
# (pico2d clip 계열 함수 좌표계: 이미지의 왼쪽 아래가 기준점)

ATTACK_FRAMES = [
    (418, 949, 96, 158),
    (632, 950, 91, 157),
    (847, 949, 84, 158),
    (1061, 949, 90, 158),
    (1256, 949, 139, 158),
    (1464, 951, 112, 156),
]

DEATH_FRAMES = [
    (416, 741, 96, 158),
    (629, 741, 94, 158),
    (853, 741, 115, 126),
    (1061, 741, 150, 70),
    (1271, 741, 153, 46),
    (1481, 741, 154, 44),
]

HURT_FRAMES = [
    (416, 533, 96, 156),
    (623, 533, 100, 156),
]

IDLE_FRAMES = [
    (416, 317, 96, 158),
    (629, 318, 92, 157),
    (832, 318, 99, 157),
    (1045, 318, 94, 157),
]