"""
Paddle class definition.

This module defines the paddle class. It is used to display
and animate the paddle controlled by the user.
"""

import pygame 
from breakout.resource import load_image

class Paddle(pygame.sprite.Sprite):
    """Paddle Class"""
    def __init__(self, RES):
        """Initialize paddle"""
        pygame.sprite.Sprite.__init__(self)
        self.RES = RES
        self.image, self.rect = load_image('paddle.png')
        self.draw_rect = self.rect.inflate(120, 40)
        self.rect.center = (self.RES[0]/2, self.RES[1] - 75)
        self.vel = 16
   

    def move_left(self):
        """Move the paddle left."""
        self.rect = self.rect.move(-self.vel, 0)
        self.draw_rect.center = self.rect.center
        if self.rect.x < 0: #keep paddle within the display
            self.rect.x = 0


    def move_right(self):
        """Move the paddle right."""
        self.rect = self.rect.move(self.vel, 0)
        self.draw_rect.center = self.rect.center
        if self.rect.x > self.RES[0] - 100: #keep paddle within the display
            self.rect.x = self.RES[0] - 100
