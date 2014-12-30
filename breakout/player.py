#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Player Module

This module handles user events from the keyboard and mouse. It
is also responsible for displaying the users score.
"""

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
        self.alive = True
        self.won = False
        
        self.color = (0,0,0) #black
        self.font = pygame.font.Font(None, 40)
        self.image = self.font.render(str(self.score), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.RES[0]-100, self.RES[1]-25)
        self.draw_rect = self.rect.inflate(40,10)


    def update(self):
        """Update the player's score."""
        self.image = self.font.render(str(self.score), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.RES[0]-100, self.RES[1]-25)
