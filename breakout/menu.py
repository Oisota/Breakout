"""
Menu, Button, and Title Classes

This module contains the Menu, Button, and Title classes.
These are used to create and display the menus for the start
and quit screens. Button is a clickable button that changes
color when the user mouses over it. Title is a a simple sprite.
Menu is a container for the buttons and a title.
"""

import pygame
from breakout.resource import load_image
from breakout.constants import *

class Button(pygame.sprite.Sprite):
    """Button Class"""    
    def __init__(self, x, y, img1, img2, on_click):
        """Initialize button."""
        pygame.sprite.Sprite.__init__(self)
        self.on_click = on_click
        #self.sound = pygame.mixer.Sound('sounds/blip.wav')

        #load image and set position
        self.img_not_pressed, self.rect = load_image(img1)
        self.img_pressed, self.rect = load_image(img2)
        self.img_not_pressed  = pygame.transform.scale(self.img_not_pressed, (130,70))
        self.img_pressed  = pygame.transform.scale(self.img_pressed, (130,70))
        self.image = self.img_not_pressed
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        
    def update(self, mouse_pos, pressed):
        """Check to see if user has moused over or clicked the button."""
        if self.rect.collidepoint(mouse_pos):
            self.image = self.img_pressed
            if pressed == 'mouse 1':
                #self.sound.play() 
                self.on_click()
        else:
            self.image = self.img_not_pressed


class Title(pygame.sprite.Sprite):
    """Title Class"""
    def __init__(self, x, y, image):
        """Initialzie title."""
        pygame.sprite.Sprite.__init__(self)

        #load image and set position
        self.image, self.rect = load_image(image)
        self.image = pygame.transform.scale(self.image, (200,80))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


class Menu(pygame.sprite.Group):
    """Menu Class"""
    def __init__(self):
        """Initialize menu."""
        pygame.sprite.Group.__init__(self)
        self.rects = []


    def addButton(self, x, y, img1, img2, on_click):
        """Create new button and add it to the menu."""
        button = Button(x, y, img1, img2, on_click)
        self.add(button) 
        self.rects.append(button.rect)
   
    
    def addTitle(self, x, y, image):
        """Create new title and add it to the menu."""
        title = Title(x, y, image)
        self.add(title)
        self.rects.append(title.rect)
