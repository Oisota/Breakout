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
    def __init__(self, x, y, ball, player):
        """Initialize brick"""
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resource.load_image('brick.png')
        self.rect.center = (x,y)
        self.ball = ball
        self.player = player
        
        
    def update(self, group):
        """Check for ball collision and delete brick if there is a collision."""
        if self.rect.colliderect(self.ball.rect):
            #self.ball.sound.play()
            #tweak this
            if self.ball.rect.x < self.rect.x:
                self.ball.x_vel = -self.ball.x_vel
                self.player.score += 5
                self.remove(group)
            elif self.ball.rect.x < self.rect.x + self.rect.width:
                self.ball.y_vel = -self.ball.y_vel
                self.player.score += 5
                self.remove(group)
            elif self.ball.rect.x + self.ball.rect.width > self.rect.x + self.rect.width:
                self.ball.x_vel = -self.ball.x_vel
                self.player.score += 5
                self.remove(group)

        

class BrickManager(pygame.sprite.Group):
    """BrickManager Class"""
    def __init__(self, RES, ball, player):
        """Initialze brick manager."""
        pygame.sprite.Group.__init__(self)
        self.RES = RES
        self.ball = ball
        self.player = player
        
        
    def addBrick(self, x, y):
        """Add a brick with the given x,y position to the group"""
        brick = Brick(x, y, self.ball, self.player)
        self.add(brick)
        
            
    def fillDisplay(self):
        """Place bricks onto the screen."""
        for x in range(85,self.RES[0]-15,70):
            for y in range(100,self.RES[1]-319,30):
                self.addBrick(x, y)
