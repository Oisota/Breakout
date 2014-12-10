#!/usr/bin/python3

import pygame

#paddle class definition
class Paddle(pygame.sprite.Sprite):

    def __init__(self, DISPLAY_SIZE, player):
        pygame.sprite.Sprite.__init__(self)
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.player = player
        self.image = pygame.image.load('images/paddle.png').convert()
        self.rect = self.image.get_rect()
        self.draw_rect = self.rect.inflate(120, 40)
        self.rect.center = (self.DISPLAY_SIZE[0]/2, self.DISPLAY_SIZE[1] - 75)
        self.speed = 16
   

    def update(self):
        if self.player.pressed == 'right':
            self.rect = self.rect.move(self.speed, 0)
            self.draw_rect.center = self.rect.center
            if self.rect.x > self.DISPLAY_SIZE[0] - 100:
                self.rect.x = self.DISPLAY_SIZE[0] - 100
        elif self.player.pressed == 'left':
            self.rect = self.rect.move(-self.speed, 0)
            self.draw_rect.center = self.rect.center
            if self.rect.x < 0:
                self.rect.x = 0
