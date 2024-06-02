"""
Constants Module

This module defines game constants in a central location
so that they can be easily accessed in other modules and
easily modified if need be.
"""

import os.path

# General 
GAME_NAME = 'Breakout' 
FRAMES_PER_SECOND = 40 
RESOLUTION = (800,600) 

# Images
IMAGE_PATH = os.path.join('breakout', 'assets', 'images') 
BACKGROUND_IMAGE = os.path.join(IMAGE_PATH, 'background.png')
BALL_IMAGE = os.path.join(IMAGE_PATH, 'ball.png')
PADDLE_IMAGE = os.path.join(IMAGE_PATH, 'paddle.png')

BRICK_IMAGES = {}
BRICK_IMAGES['red'] = os.path.join(IMAGE_PATH, 'brick_red.gif')
BRICK_IMAGES['orange'] = os.path.join(IMAGE_PATH, 'brick_orange.gif')
BRICK_IMAGES['yellow'] = os.path.join(IMAGE_PATH, 'brick_yellow.gif')
BRICK_IMAGES['green'] = os.path.join(IMAGE_PATH, 'brick_green.gif')
BRICK_IMAGES['blue'] = os.path.join(IMAGE_PATH, 'brick_blue.gif')
BRICK_IMAGES['purple'] = os.path.join(IMAGE_PATH, 'brick_purple.gif')
BRICK_IMAGES['tan'] = os.path.join(IMAGE_PATH, 'brick_tan.gif')
BRICK_IMAGES['white'] = os.path.join(IMAGE_PATH, 'brick_white.gif')
BRICK_IMAGES['grey'] = os.path.join(IMAGE_PATH, 'brick_gray.gif')
BRICK_IMAGES['black'] = os.path.join(IMAGE_PATH, 'brick_black.gif')
BRICK_IMAGES['none'] = os.path.join(IMAGE_PATH, 'brick_cell.gif')

# Menu Images
BREAKOUT_IMAGE = os.path.join(IMAGE_PATH, 'breakout.png')
WIN_IMAGE = os.path.join(IMAGE_PATH, 'win.png')
LOSE_IMAGE = os.path.join(IMAGE_PATH, 'lose.png')

START_IMAGE = os.path.join(IMAGE_PATH, 'start.png')
START_PRESSED_IMAGE = os.path.join(IMAGE_PATH, 'start_pressed.png')

QUIT_IMAGE = os.path.join(IMAGE_PATH, 'quit.png')
QUIT_PRESSED_IMAGE = os.path.join(IMAGE_PATH, 'quit_pressed.png' )

RETRY_IMAGE = os.path.join(IMAGE_PATH, 'retry.png')
RETRY_PRESSED_IMAGE = os.path.join(IMAGE_PATH, 'retry_pressed.png' )

# Sounds
SOUND_PATH = os.path.join('breakout', 'assets', 'sounds')
BLIP = os.path.join(IMAGE_PATH, 'blip.wav')

# Levels
LEVEL_PATH = os.path.join('breakout', 'assets', 'levels')
START_LEVEL = os.path.join(LEVEL_PATH, 'level_1.json')
