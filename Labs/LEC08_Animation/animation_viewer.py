from pico2d import *
 
open_canvas(800, 600)

character_sheet = load_image('character_sheet.png')

TARGET_SIZE = 400
FRAME_DELAY = 0.08
REPEAT_COUNT = 5
PAUSE_SEC = 1.0
CENTER_X, CENTER_Y = 400, 300