#!/usr/bin/python3

import pygame, resource

class Paddle(pygame.sprite.Sprite):
    """Paddle Class"""
    def __init__(self, RES, player):
        """Initialize paddle"""
        pygame.sprite.Sprite.__init__(self)
        self.RES = RES
        self.player = player
        self.image, self.rect = resource.load_image('resources/images/paddle.png')
        self.draw_rect = self.rect.inflate(120, 40)
        self.rect.center = (self.RES[0]/2, self.RES[1] - 75)
        self.vel = 16
   

    def move(self, direction):
        """Move paddle in specified direction."""
        if direction == 'right':
            self.rect = self.rect.move(self.vel, 0)
            self.draw_rect.center = self.rect.center
            if self.rect.x > self.RES[0] - 100:
                self.rect.x = self.RES[0] - 100
        elif direction == 'left':
            self.rect = self.rect.move(-self.vel, 0)
            self.draw_rect.center = self.rect.center
            if self.rect.x < 0:
                self.rect.x = 0


    def update(self):
        """Update method needed for sprite group."""
        pass
