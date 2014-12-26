#!/usr/bin/python3

import pygame

#paddle class definition
class Paddle(pygame.sprite.Sprite):

    def __init__(self, RES, player):
        pygame.sprite.Sprite.__init__(self)
        self.RES = RES
        self.player = player
        self.image = pygame.image.load('images/paddle.png').convert()
        self.rect = self.image.get_rect()
        self.draw_rect = self.rect.inflate(120, 40)
        self.rect.center = (self.RES[0]/2, self.RES[1] - 75)
        self.vel = 16
   

    def update(self):
        if self.player.pressed == 'right':
            self.rect = self.rect.move(self.vel, 0)
            self.draw_rect.center = self.rect.center
            if self.rect.x > self.RES[0] - 100:
                self.rect.x = self.RES[0] - 100
        elif self.player.pressed == 'left':
            self.rect = self.rect.move(-self.vel, 0)
            self.draw_rect.center = self.rect.center
            if self.rect.x < 0:
                self.rect.x = 0
