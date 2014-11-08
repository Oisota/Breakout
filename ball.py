#!/usr/bin/python3

import sys
import random
import pygame

#ball class definition
class Ball(pygame.sprite.Sprite):

    def __init__(self, DISPLAY_SIZE, display, paddle, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/ball.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(1,DISPLAY_SIZE[0]-35), 450)
        self.draw_rect = self.rect.inflate(150, 150)
        self.x_speed = random.randint(6,9)
        self.y_speed = -random.randint(6,9)
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.display = display
        self.paddle = paddle 
        self.player = player
        self.left_wall = pygame.Rect(0,0,1,DISPLAY_SIZE[1]) 
        self.right_wall = pygame.Rect(799,0,1,DISPLAY_SIZE[1])
        self.top_wall = pygame.Rect(0,0,DISPLAY_SIZE[0],1)
        self.bottom_wall = pygame.Rect(0,DISPLAY_SIZE[1]-50,DISPLAY_SIZE[0],1)       
        
        
    def draw(self): 
        self.display.blit(self.image, self.rect)
  
       
    def update(self):
        self.rect = self.rect.move(self.x_speed, self.y_speed)
        self.draw_rect.center = self.rect.center
        
        if self.rect.colliderect(self.left_wall) or self.rect.colliderect(self.right_wall): #ball has hit side of screen
            self.x_speed = -self.x_speed 
        elif self.rect.colliderect(self.top_wall):     #ball has hit top of screen
            self.y_speed = -self.y_speed 
        elif self.rect.colliderect(self.paddle.rect):  #ball has hit paddle
            self.y_speed = -self.y_speed               #bounce ball up
        elif self.rect.colliderect(self.bottom_wall):  #ball has missed paddle
            self.player.won = False
            self.player.alive = False 


    def reset(self):
        self.rect.center = (random.randint(1, self.DISPLAY_SIZE[0]-35), 450)
        self.x_speed = random.randint(4,7)
        self.y_speed = -random.randint(4,7)

