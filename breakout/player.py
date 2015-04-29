"""
Player Module

This module defines the player class. It keeps track of the players
name, score, and whether they have won. It also displays their score.
"""

import pygame
from pygame.locals import *

class Player(object):
    """Player Class""" 
    def __init__(self, RES, name, score=0):
        """Initialize player."""
        self.name = ''
        self.score = Score(RES, score)
        self.alive = True
        self.won = False
        

    def update(self):
        """Update the player's score."""
        self.score.update()


    def reset(self):
        """Reset player attributes."""
        self.score.score = 0
        self.alive = True
        self.won = False


class Score(pygame.sprite.Sprite):
    """Score Class"""
    def __init__(self, RES, score=0):
        """Initialize player score."""
        pygame.sprite.Sprite.__init__(self)
        self.RES = RES
        self.score = score
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


    def incr(self, incr=5):
        """Increment score"""
        self.score += incr
