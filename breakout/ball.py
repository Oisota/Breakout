"""
Ball class definition.

This module defines the ball class. It is used to
display and animate balls that bounce around the screen.
"""

import pygame, random
from breakout.resource import load_image

class Ball(pygame.sprite.Sprite):
    """Ball Class"""
    def __init__(self, RES, paddle, on_lose):
        """Initialize ball object."""
        pygame.sprite.Sprite.__init__(self)
        self.RES = RES
        self.paddle = paddle 
        self.on_lose = on_lose
        self.image, self.rect = load_image('ball.png')
        #self.sound = resource.load_sound('sounds/blip.wav')
        self.draw_rect = self.rect.inflate(170, 170)
        self.rect.center = (random.randint(1, self.RES[0]-35), 450)
        self.x_vel = random.randint(6,9)
        self.y_vel = -random.randint(6,9)
        self.left_wall = pygame.Rect(0,0,1,RES[1]) 
        self.right_wall = pygame.Rect(799,0,1,RES[1])
        self.top_wall = pygame.Rect(0,0,RES[0],1)
        self.bottom_wall = pygame.Rect(0,RES[1]-40,RES[0],1)       
        
        
    def update(self):
        """Update the ball position and check for rect collisions."""
        self.rect = self.rect.move(self.x_vel, self.y_vel)
        self.draw_rect.center = self.rect.center
        
        if self.rect.colliderect(self.left_wall) or self.rect.colliderect(self.right_wall): #ball has hit side of screen
            self.x_vel = -self.x_vel 
            #self.sound.play()
        elif self.rect.colliderect(self.top_wall):     #ball has hit top of screen
            self.y_vel = -self.y_vel 
            #self.sound.play()
        elif self.rect.colliderect(self.paddle.rect):  #ball has hit paddle
            self.y_vel = -self.y_vel
            #self.sound.play()
        elif self.rect.colliderect(self.bottom_wall):  #ball has missed paddle
            self.on_lose()
            #self.sound.play()
