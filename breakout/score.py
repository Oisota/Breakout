"""
Score Module

This module defines the score class. It keeps track of the players
score and displays it on the screen.
"""

import pygame

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
