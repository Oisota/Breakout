"""
Resource Module

This module defines functions for loading resource files for use
with pygame. It uses the built in pygame functions to accomplish
this but also handles exceptions if files are not found.
"""

import pygame, os, sys
import lxml.etree as ET

from breakout.utils.constants import *

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
    """Load the given xml level file into a dict and return the dict."""
    path = os.path.join(LEVEL_PATH, file_name)
    path = os.path.abspath(path)
    level = dict()
    bricks = list()
    brick_colors = list()

    try:
        tree = ET.parse(path)
    except FileNotFoundError as e:
        print('Could not load level: ', path)
        print(e)
        raise SystemExit

    root = tree.getroot()

    level.update({root[0].tag : root[0].text}) # name
    level.update({root[1].tag : root[1].text}) # difficulty
    level.update({root[2].tag : root[2].text}) # ball speed
    level.update({root[3].tag : root[3].text}) # filename of next level

    for row in root[4]: # load brick data into list of lists
        tmp = list()
        color_tmp = list()
        for column in row:
            tmp.append(column.text)
            color_tmp.append(column.attrib['color'])

        bricks.append(tmp)
        brick_colors.append(color_tmp)

    level.update({root[4].tag : bricks}) # brick data
    level.update({'brick_colors' : brick_colors}) # brick data

    return level


def save_level(level, file_name):
    """Write the given level to an xml file."""
    pass 
