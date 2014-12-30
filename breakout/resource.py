#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Resource Module

This module defines functions for loading resource files for use
with pygame. It uses the built in pygame functions to accomplish
this but also handles exceptions if files are not found.
"""

import pygame

def load_image(path):
    """Load an image and return the image object and a rect for the image."""
    try:
        image = pygame.image.load(path)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as e:
        print('Cannot load image: ', path)
        print(e)
        raise SystemExit 

    return image, image.get_rect()


def load_sound(path):
    """Load a sound and return the sound object."""
    try:
        sound = pygame.mixer.Sound(path)
    except pygame.error as e:
        print('Cannot load sound: ', path)
        print(e)
        raise SystemExit 

    return sound
