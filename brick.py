#!/usr/bin/python3

import pygame
import random
import sys

class Brick(pygame.sprite.Sprite):

    def __init__(self, DISPLAY_SIZE, display, x, y, ball):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/brick.png').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit = False
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.display = display
        self.ball = ball
        
        
    def draw(self):
        self.display.blit(self.image, self.rect)
        
     
    def update(self):
        if self.rect.colliderect(self.ball.rect):
                if self.ball.rect.x < self.rect.x:
                    self.ball.x_speed = -self.ball.x_speed
                    self.hit = True
                elif self.ball.rect.x < self.rect.x + self.rect.width:
                    self.ball.y_speed = -self.ball.y_speed
                    self.hit = True
                elif self.ball.rect.x + self.ball.rect.width > self.rect.x + self.rect.width:
                    self.ball.x_speed = -self.ball.x_speed
                    self.hit = True

        
#figure out how to inherit Group class
class BrickManager(object):

    def __init__(self, DISPLAY_SIZE, display, ball, player):
        #pygame.sprite.Group.__init__(self)
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.display = display
        self.ball = ball
        self.player = player
        self.bricks = []
        
        
    def addBrick(self, x_pos, y_pos):
        brick = Brick(self.DISPLAY_SIZE, self.display, x_pos, y_pos, self.ball)
        #pygame.sprite.Group.add(brick)
        self.bricks.append(brick)
        
    def addBricks(self, num_bricks):
        for i in range(0,num_bricks):
            self.addBrick()
            
            
    def fillDisplay(self):
        #fix so bricks are placed based on screen resolution
        for x_pos in range(85,785,70):
            for y_pos in range(100,281,30):
                self.addBrick(x_pos, y_pos)
        
       
    def delBrick(self, brick):
        #pygame.sprite.remove(brick)
        self.bricks.remove(brick)
       
    def draw(self):
        #pygame.sprite.Group.draw(self, display)
        for brick in self.bricks:
            brick.draw()

    def update(self):
        #pygame.sprite.Group.draw(self, display)
        for brick in self.bricks:
            brick.update()
            if brick.hit:
                self.delBrick(brick)
    
        if not self.bricks:
            self.player.won = True
            self.player.alive = False 
            

    def reset(self):
        self.bricks = []
