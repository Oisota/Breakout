"""
Brick and BrickManager Classes

This module contains the Brick and BrickManager classes. The Brick
class displays a brick on the screen that gets destroyed once it
is hit with a ball. The Brick Manager class is a container class 
that allows easy manipulation of many bricks.
"""

import pygame
import breakout.resource as resource

class Brick(pygame.sprite.Sprite):
    """Brick Class"""
    def __init__(self, x, y):
        """Initialize the brick."""
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resource.load_image('brick.png')
        self.rect.center = (x,y)
        
        
    def update(self, group, ball, on_collision): 
        """Check for ball collision and delete brick if there is a collision."""
        if self.rect.colliderect(ball.rect):
            #self.ball.sound.play()
            self.remove(group)
            on_collision()
            #bounce ball
            if ball.rect.x < self.rect.x or (ball.rect.x + ball.rect.width) > (self.rect.x + self.rect.width):
                ball.x_vel = -ball.x_vel 
            elif ball.rect.x < (self.rect.x + self.rect.width):
                ball.y_vel = -ball.y_vel 

        

class BrickManager(pygame.sprite.Group):
    """BrickManager Class"""
    def __init__(self, RES):
        """Initialze brick manager."""
        pygame.sprite.Group.__init__(self)
        self.RES = RES
        
        
    def addBrick(self, x, y):
        """Add a brick with the given x,y position to the group"""
        brick = Brick(x, y)
        self.add(brick)
        
            
    def fillDisplay(self):
        """Place bricks onto the screen."""
        for x in range(85,self.RES[0]-15,70):
            for y in range(100,self.RES[1]-319,30):
                self.addBrick(x, y)
