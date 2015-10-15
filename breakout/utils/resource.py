"""
Resource Module

This module defines functions for loading resource files for use
with pygame. It uses the built in pygame functions to accomplish
this but also handles exceptions if files are not found.
"""

import pygame, os, sys
import lxml.etree as etree

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
    level = {}
    bricks = []

    try:
        tree = etree.parse(path)
    except FileNotFoundError as e:
        print('Could not load level: ', path)
        print(e)
        raise SystemExit

    root = tree.getroot()

    level.update({root[0].tag : root[0].text}) # name
    level.update({root[1].tag : root[1].text}) # ball speed
    level.update({root[2].tag : root[2].text}) # filename of next level

    for row in root[3]: # load brick data into list of lists
        temp = list()
        for column in row:
            temp.append(column.text)

        bricks.append(temp)

    level.update({root[3].tag : bricks}) # brick data

    return level


def save_level(level, file_name):
    """Write the given level to an xml file."""
    root = etree.Element('level')
    etree.SubElement(root, 'name')
    etree.SubElement(root, 'ball_speed')
    etree.SubElement(root, 'next')
    bricks = etree.SubElement(root, 'bricks')

    root[0].text = level['name']
    root[1].text = level['ball_speed']
    root[2].text = level['next']

    for row in level['bricks']:
        r = etree.SubElement(bricks, 'row')
        for color in row:
            c = etree.SubElement(r, 'column')
            c.text = color

    tree = etree.ElementTree(root)
    tree.write(file_name, pretty_print=True, encoding='UTF-8', xml_declaration=True)
