"""
Menu, Button, and Title Classes

This module contains the Menu, Button, and Title classes.
These are used to create and display the menus for the start
and quit screens. Button is a clickable button that changes
color when the user mouses over it. Title is a a simple sprite.
Menu is a container for the buttons and a title.
"""

import pygame

from breakout.utils.asset import load_image


class Button(pygame.sprite.Sprite):
    """Button Class"""    
    def __init__(self, kwargs):
        """Initialize button."""
        pygame.sprite.Sprite.__init__(self)
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.text = kwargs['text']
        self.on_click = kwargs['on_click']
        #self.sound = pygame.mixer.Sound('sounds/blip.wav')
        self.font = pygame.font.Font(None, 60)
        self.color1 = (255,255,255)
        self.color2 = (255,50,50) 

        #render text and set position
        self.image_not_pressed = self.font.render(str(self.text), True, self.color1)
        self.image_pressed = self.font.render(str(self.text), True, self.color2)
        self.image = self.image_not_pressed
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        
    def update(self, mouse_pos, pressed):
        """Check to see if user has moused over or clicked the button."""
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_pressed
            if pressed == 'mouse 1':
                #self.sound.play() 
                self.on_click()
        else:
            self.image = self.image_not_pressed



class Title(pygame.sprite.Sprite):
    """Title Class"""
    def __init__(self, kwargs):
        """Initialzie title."""
        pygame.sprite.Sprite.__init__(self)
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.text = kwargs['text']
        self.font = pygame.font.Font(None, 80)
        self.color = (255,255,255) #black

        #render text and set position
        self.image = self.font.render(str(self.text), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)



class Menu(pygame.sprite.Group):
    """Menu Class"""
    def __init__(self):
        """Initialize menu."""
        pygame.sprite.Group.__init__(self)
        self.rects = []


    def add_button(self, *args, **kwargs):
        """Create new button and add it to the menu."""
        button = Button(kwargs)
        self.add(button) 
        self.rects.append(button.rect)
   
    
    def add_title(self, *args, **kwargs):
        """Create new title and add it to the menu."""
        title = Title(kwargs)
        self.add(title)
        self.rects.append(title.rect)
