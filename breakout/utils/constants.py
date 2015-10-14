"""
Constants Module

This module defines game constants in a central location
so that they can be easily accessed in other modules and
easily modified if need be.
"""

# General 
GAME_NAME = 'Breakout' 
FRAMES_PER_SECOND = 40 
RESOLUTION = (800,600) 

# Images
IMAGE_PATH = 'breakout/resources/images/'
BACKGROUND_IMAGE = 'background.png'
BALL_IMAGE = 'ball.png'
PADDLE_IMAGE = 'paddle.png'
BRICK_IMAGES = {'red' : 'brick_red.gif',
                'orange' : 'brick_orange.gif',
                'yellow' : 'brick_yellow.gif',
                'green' : 'brick_green.gif',
                'blue' : 'brick_blue.gif',
                'purple' : 'brick_purple.gif',
                'tan' : 'brick_tan.gif',
                'white' : 'brick_white.gif',
                'grey' : 'brick_gray.gif',
                'black' : 'brick_black.gif',
                'none' : 'brick_cell.gif'}

# Menu Images
BREAKOUT_IMAGE = 'breakout.png'
WIN_IMAGE = 'win.png'
LOSE_IMAGE = 'lose.png'

START_IMAGE = 'start.png'
START_PRESSED_IMAGE = 'start_pressed.png'

QUIT_IMAGE = 'quit.png'
QUIT_PRESSED_IMAGE = 'quit_pressed.png' 

RETRY_IMAGE = 'retry.png'
RETRY_PRESSED_IMAGE = 'retry_pressed.png' 

# Sounds
SOUND_PATH = 'breakout/resources/sounds/'
BLIP = 'blip.wav'

# Levels
LEVEL_PATH = 'breakout/resources/levels/'
START_LEVEL = 'level_1.xml'
