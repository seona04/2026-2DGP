# Drill #8. 애니메이션 뷰어 - AI 이용한 개발
# 사용 스프라이트 시트: spritesheet.png (배경 투명 처리 완료)
#
# [보너스 기능 구현 안내]
# 1) 애니메이션(ATTACK/DEATH/HURT/IDLE/WALK)마다 프레임 개수가 서로 다름
#    (ATTACK 6, DEATH 6, HURT 2, IDLE 4, WALK 6장)
# 2) 같은 시트 안에서도 프레임마다 캐릭터의 가로/세로 크기가 전부 다름
#    (예: DEATH 애니메이션은 쓰러지면서 세로 158px -> 44px로 점점 줄어듦)
#    -> clip_composite_draw로 프레임별 원본 크기를 그대로 읽어 스케일링
 
from pico2d import *
 
open_canvas(800, 600)
 
character_sheet = load_image('spritesheet.png')
 
# 화면(800x600)의 절반 이상을 차지하도록 긴 변 기준 목표 크기를 지정
TARGET_SIZE = 400
FRAME_DELAY = 0.08
REPEAT_COUNT = 5
PAUSE_SEC = 1.0
CENTER_X, CENTER_Y = 400, 300
 
# 각 프레임은 (left, bottom, width, height) 튜플
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
 
WALK_FRAMES = [
    (427, 109, 94, 150),
    (640, 110, 67, 157),
    (838, 111, 101, 156),
    (1039, 110, 116, 149),
    (1259, 109, 88, 158),
    (1483, 111, 88, 156),
]
 
animations = {
    'ATTACK': ATTACK_FRAMES,
    'DEATH': DEATH_FRAMES,
    'HURT': HURT_FRAMES,
    'IDLE': IDLE_FRAMES,
    'WALK': WALK_FRAMES,
}
 
# 재생 순서 (스프라이트 시트에 적힌 순서 그대로)
ANIMATION_ORDER = ['ATTACK', 'DEATH', 'HURT', 'IDLE', 'WALK']
 
 
def get_scale(width, height):
    longer_side = max(width, height)
    return TARGET_SIZE / longer_side
 
 
def draw_frame(frame, x, y):
    left, bottom, width, height = frame
    scale = get_scale(width, height)
    draw_w, draw_h = width * scale, height * scale
    clear_canvas()
    character_sheet.clip_composite_draw(
        left, bottom, width, height,
        0, '', x, y, draw_w, draw_h
    )
    update_canvas()
    delay(FRAME_DELAY)
 
 
def play_animation_once(frames, x, y):
    for frame in frames:
        draw_frame(frame, x, y)
 
 
def play_animation_repeat(name, x, y):
    frames = animations[name]
    print(name)
    for _ in range(REPEAT_COUNT):
        play_animation_once(frames, x, y)
    delay(PAUSE_SEC)  # 마지막 프레임을 유지한 채 1초 정지
 
 
def play_all_animations_once():
    for name in ANIMATION_ORDER:
        play_animation_repeat(name, CENTER_X, CENTER_Y)
 
 
def main():
    while True:
        play_all_animations_once()
 
 
main()
close_canvas()