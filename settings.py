import os

BASE_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(BASE_DIR, "assets", "images")
SOUND_DIR = os.path.join(BASE_DIR, "assets", "sounds")
RECORD_FILE = os.path.join(BASE_DIR, "record.txt")

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
FPS = 60
GROUND_Y = SCREEN_HEIGHT - 80
GRAVITY = 0.8
JUMP_SPEED = -15
START_SPEED = 6
