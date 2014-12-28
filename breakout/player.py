#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from colors import *
import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    """Player Class""" 
    def __init__(self,RES, name, score):
        """Initialize player."""
        pygame.sprite.Sprite.__init__(self)
        self.RES = RES
        self.name = ''
        self.score = score
        self.paused = False
        self.alive = True
        self.won = False
        self.pressed = ''
        self.mouse_pos = (0,0)
        
        #set which events will be allowed in the queue
        allowed_events = [QUIT, KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN]
        pygame.event.set_allowed(allowed_events)
       
        self.font = pygame.font.Font(None, 40)
        self.image = self.font.render(str(self.score), True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (self.RES[0]-100, self.RES[1]-25)
        self.draw_rect = self.rect.inflate(40,10)

    
    def getInput(self):
        """Get input from the keyboard and mouse"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.pressed = 'left'
                elif event.key == K_RIGHT:
                    self.pressed = 'right'
                elif event.key == K_p:
                    self.paused = True
                elif event.key == K_ESCAPE:
                    self.won = False
                    self.alive = False
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    self.pressed = ''
                elif event.key == K_RIGHT:
                    self.pressed = ''
                elif event.key == K_p:
                    self.paused = False
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = event.pos
                self.pressed = 'mouse ' + str(event.button)
            elif event.type == MOUSEBUTTONUP:
                self.mouse_pos = event.pos
                self.pressed = ''
            elif event.type == MOUSEMOTION:
                self.mouse_pos = event.pos


    def update(self):
        """Update the player's score."""
        self.image = self.font.render(str(self.score), True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (self.RES[0]-100, self.RES[1]-25)
