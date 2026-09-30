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