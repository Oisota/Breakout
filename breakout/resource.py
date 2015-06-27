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
    """Load the given xml level file into a dict and return the dict."""
    level_path = 'breakout/resources/levels/'
    path = os.path.join(level_path, path)
    path = os.path.abspath(path)
    level = dict()
    bricks = list()
    tree = ET.parse(path)
    root = tree.getroot()

    level.update({root[0].tag : root[0].text}) # name
    level.update({root[1].tag : root[1].text}) # difficulty
    level.update({root[2].tag : root[2].text}) # ball speed
    level.update({root[3].tag : root[3].text}) # filename of next level

    for row in root[4]: # load brick data into list of lists
        tmp = list()
        for column in row:
            tmp.append(column.text)

        bricks.append(tmp)

    level.update({root[4].tag : bricks}) # brick data

    return level
