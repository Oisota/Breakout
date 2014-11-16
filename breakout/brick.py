#!/usr/bin/python3

import sys
import pygame

class Brick(pygame.sprite.Sprite):

    def __init__(self, x, y, ball, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/brick.png').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.ball = ball
        self.player = player
        
        
    def update(self, group):
        if self.rect.colliderect(self.ball.rect):
                #tweak this
                if self.ball.rect.x < self.rect.x:
                    self.ball.x_speed = -self.ball.x_speed
                    self.player.score += 5
                    self.remove(group)
                elif self.ball.rect.x < self.rect.x + self.rect.width:
                    self.ball.y_speed = -self.ball.y_speed
                    self.player.score += 5
                    self.remove(group)
                elif self.ball.rect.x + self.ball.rect.width > self.rect.x + self.rect.width:
                    self.ball.x_speed = -self.ball.x_speed
                    self.player.score += 5
                    self.remove(group)

        

class BrickManager(pygame.sprite.Group):

    def __init__(self, DISPLAY_SIZE, ball, player):
        pygame.sprite.Group.__init__(self)
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.ball = ball
        self.player = player
        
        
    def addBrick(self, x_pos, y_pos):
        brick = Brick(x_pos, y_pos, self.ball, self.player)
        self.add(brick)
        
            
    def fillDisplay(self):
        #fix so bricks are placed based on screen resolution
        for x_pos in range(85,785,70):
            for y_pos in range(100,281,30):
                self.addBrick(x_pos, y_pos)
        

    def reset(self):
        self.empty()
