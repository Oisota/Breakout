#!/usr/bin/python3

import pygame

#paddle class definition
class Paddle(pygame.sprite.Sprite):

    def __init__(self, DISPLAY_SIZE, display, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/paddle.png').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (DISPLAY_SIZE[0] - 500, DISPLAY_SIZE[1] - 95)
        self.draw_rect = self.rect.inflate(120, 40)
        self.speed = 14
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.display = display
        self.player = player
   

    def draw(self):
        self.display.blit(self.image, self.rect)
        

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


    def reset(self):
        self.rect.center = (self.DISPLAY_SIZE[0] - 500, self.DISPLAY_SIZE[1] - 95)
