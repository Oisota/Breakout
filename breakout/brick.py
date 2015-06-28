"""
Brick and BrickManager Classes

This module contains the Brick and BrickManager classes. The Brick
class displays a brick on the screen that gets destroyed once it
is hit with a ball. The Brick Manager class is a container class 
that allows easy manipulation of many bricks.
"""

import pygame
from breakout.resource import load_image

class Brick(pygame.sprite.Sprite):
    """Brick Class"""
    def __init__(self, x, y):
        """Initialize the brick."""
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('brick.png')
        self.rect.center = (x,y)
        
        
    def update(self, *args, **kwargs): 
        """Check for ball collision and delete brick if there is a collision."""
        group = args[0]
        ball = args[1]
        on_collision = args[2]

        if self.rect.colliderect(ball.rect):
            #self.ball.sound.play()
            self.remove(group)
            on_collision()
            #bounce ball
            if ball.rect.x < self.rect.x or (ball.rect.x + ball.rect.width) > (self.rect.x + self.rect.width):
                ball.x_vel = -ball.x_vel 
            elif ball.rect.x < (self.rect.x + self.rect.width):
                ball.y_vel = -ball.y_vel 

        

def addBrick(group, x, y):
    """Add a brick with the given x,y position to the given group"""
    brick = Brick(x, y)
    group.add(brick)
    
        
def fillDisplay(group, RES, bricks):
    """Place bricks onto the screen, adding them to the given group"""
    for y, row in zip(range(50, RES[1]-150, 30), bricks):
        for x, brick in zip(range(40, RES[0], 80), row):
            if brick == '1':
                addBrick(group, x, y)
