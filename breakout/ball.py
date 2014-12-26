#!/usr/bin/python3

import sys
import random
import pygame

#ball class definition
class Ball(pygame.sprite.Sprite):

    def __init__(self, RES, paddle, player):
        pygame.sprite.Sprite.__init__(self)
        self.RES = RES
        self.paddle = paddle 
        self.player = player
        self.image = pygame.image.load('images/ball.png').convert_alpha()
        #self.sound = pygame.mixer.Sound('sounds/blip.wav')
        self.rect = self.image.get_rect()
        self.draw_rect = self.rect.inflate(170, 170)
        self.rect.center = (random.randint(1, self.RES[0]-35), 450)
        self.x_vel = random.randint(6,9)
        self.y_vel = -random.randint(6,9)
        self.left_wall = pygame.Rect(0,0,1,RES[1]) 
        self.right_wall = pygame.Rect(799,0,1,RES[1])
        self.top_wall = pygame.Rect(0,0,RES[0],1)
        self.bottom_wall = pygame.Rect(0,RES[1]-40,RES[0],1)       
        
        
    def update(self):
        #edit so the method takes a list of rects as a parameter and
        #have the ball bounce off the rects.
        self.rect = self.rect.move(self.x_vel, self.y_vel)
        self.draw_rect.center = self.rect.center
        
        if self.rect.colliderect(self.left_wall) or self.rect.colliderect(self.right_wall): #ball has hit side of screen
            self.x_vel = -self.x_vel 
            #self.sound.play()
        elif self.rect.colliderect(self.top_wall):     #ball has hit top of screen
            self.y_vel = -self.y_vel 
            #self.sound.play()
        elif self.rect.colliderect(self.paddle.rect):  #ball has hit paddle
            self.y_vel = -self.y_vel               #bounce ball up
            #self.sound.play()
        elif self.rect.colliderect(self.bottom_wall):  #ball has missed paddle
            self.player.won = False
            self.player.alive = False 
            #self.sound.play()


    #def update(self, rects):
    #    self.rect = self.rect.move(self.x_vel, self.y_vel)
    #    self.draw_rect.center = self.rect.center

    #    for rect in rects:
    #        if self.rect.colliderect(rect):
    #            if self.x_vel > 0:
    #    
