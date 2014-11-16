#!/usr/bin/python

import sys
from colors import *
import pygame
from pygame.locals import *


class Player(object):
    
    def __init__(self,DISPLAY_SIZE, display, name, score):
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.display = display
        self.name = ''
        self.reset()
        self.paused = False
        self.score_rect = None
        self.font = pygame.font.Font(None, 40)

    
    def getInput(self):
        #event handling loop
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


    def draw_score(self):
        text = self.font.render(str(self.score), True, BLACK)
        self.score_rect = text.get_rect()
        self.score_rect.center = (self.DISPLAY_SIZE[0]-100, self.DISPLAY_SIZE[1]-25)
        self.display.blit(text, self.score_rect)


    def reset(self):
        self.score = 0
        self.alive = True
        self.won = False
        self.pressed = ''
        self.mouse_pos = (0,0)
