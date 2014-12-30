#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Image Module

This module defines a function for loading images for use
with pygame. It uses the built in pygame functions to accomplish
this but also handles exceptions if images are not found.
"""

import pygame

def load(path):
    """Load an image and return the image object."""
    try:
        image = pygame.image.load(path)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as e:
        print('Cannot load image: ', path)
        raise SystemExit, e

    return image, image.get_rect()

