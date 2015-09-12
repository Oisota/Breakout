import pygame, sys

from breakout.utils.resource import load_image
from breakout.utils.constants import *

class Cell(pygame.sprite.Sprite):
    """Grid Cell Class"""
    def __init__(self, x, y):
        """Initialize the Cell"""
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(BRICK_IMAGES['cell'])
        self.rect.center = (x,y)
        self.index = 0
        self.colors = ['red','orange','yellow','green','blue',
                'purple','tan','white','grey','black','cell']


    def update(self, mouse_pos, pressed):
        """Place a brick if user has click on the cell."""
        if self.rect.collidepoint(mouse_pos) and pressed:
            pressed = False
            self.advance()
    
    
    def advance(self):
        """Advance image to next color brick."""
        if self.index == 10:
            self.index = 0
        else:
            self.index += 1
        
        x, y = self.rect.center
        self.image, self.rect = load_image(BRICK_IMAGES[self.colors[self.index]])
        self.rect.center = (x,y)


    @classmethod
    def fill_display(cls, group):
        """Place bricks onto the screen, adding them to the given group"""
        for y in range(50, RESOLUTION[1]-150, 30):
            for x in range(40, RESOLUTION[0], 80):
                cell = cls(x, y)
                group.add(cell) 
