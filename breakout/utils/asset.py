"""
Resource Module

This module defines functions for loading resource files for use
with the game and the level editor.
"""

import os, sys, json

import pygame

from breakout.utils.constants import IMAGE_PATH, SOUND_PATH, LEVEL_PATH


def load_image(file_name):
    """Load an image and return the image object and the image rect."""
    path = os.path.join(IMAGE_PATH, file_name)
    path = os.path.abspath(path)

    try:
        image = pygame.image.load(path)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as e:
        print('Could not load image: ', path)
        print(e)
        raise SystemExit 

    return image, image.get_rect()


def load_sound(file_name):
    """Load a sound and return the sound object."""
    path = os.path.join(SOUND_PATH, file_name)
    path = os.path.abspath(path)

    try:
        sound = pygame.mixer.Sound(path)
    except pygame.error as e:
        print('Could not load sound: ', path)
        print(e)
        raise SystemExit 

    return sound


def load_level(file_name):
    """Load the given json level file into a dict and return the dict."""
    path = os.path.join(LEVEL_PATH, file_name)
    path = os.path.abspath(path)

    with open(path, 'r') as f:
        level = json.load(f)

    return level


def save_level(level, file_name):
    """Write the given level to the given json file."""
    with open(file_name, 'w') as f:
        json.dump(level, f, indent=4)
