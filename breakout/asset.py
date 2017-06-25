"""
Asset Module

This module defines functions for loading resource files for use
with the game and the level editor.
"""

import os
import sys
import json

import pygame

from .config import IMAGE_PATH, SOUND_PATH, LEVEL_PATH


def load_image(path):
    """Load an image and return the image object and the image rect."""
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


def load_sound(path):
    """Load a sound and return the sound object."""
    try:
        sound = pygame.mixer.Sound(path)
    except pygame.error as e:
        print('Could not load sound: ', path)
        print(e)
        raise SystemExit 

    return sound


def load_level(path):
    """Load the given json level file into a dict and return the dict."""
    with open(path, 'r') as f:
        level = json.load(f)

    return level


def save_level(level, path):
    """Write the given level to the given json file."""
    with open(path, 'w') as f:
        json.dump(level, f, indent=4)
