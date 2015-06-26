"""
Resource Module

This module defines functions for loading resource files for use
with pygame. It uses the built in pygame functions to accomplish
this but also handles exceptions if files are not found.
"""

import pygame, os, sys
import xml.etree.ElementTree as ET

def load_image(path):
    """Load an image and return the image object and the image rect."""
    img_path = 'breakout/resources/images/'
    path = os.path.join(img_path, path)
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


def load_sound(path):
    """Load a sound and return the sound object."""
    snd_path = 'breakout/resources/sounds/'
    path = os.path.join(snd_path, path)
    path = os.path.abspath(path)

    try:
        sound = pygame.mixer.Sound(path)
    except pygame.error as e:
        print('Could not load sound: ', path)
        print(e)
        raise SystemExit 

    return sound


def load_level(path):
    """Load the given level file into a dict and return the dict."""
    level = dict()
    tree = ET.parse(path)
    root = tree.getroot()
    
    for child in root:
        print(child.tag, child.attrib, child.text)
    
