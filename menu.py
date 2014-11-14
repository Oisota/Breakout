#!/usr/bin/python3

import os
import pygame
from colors import *

class Button(pygame.sprite.Sprite):

    def __init__(self, DISPLAY_SIZE, x, y, text, player):
        pygame.sprite.Sprite.__init__(self)
        self.DISPLAY_SIZE = DISPLAY_SIZE 
        self.player = player
        self.pressed = False 

        #load font
        self.font_norm = pygame.font.Font(None, 60)
        self.font_bold = pygame.font.Font(None, 60)
        self.font_bold.set_bold(True)
        #render text
        self.text_norm = self.font_norm.render(text, True, BLACK)
        self.text_bold = self.font_bold.render(text, True, BLACK)
         
        self.rect = self.text_norm.get_rect()
        self.rect.center = (x,y)
        self.image = self.text_norm


    def update(self):
        if self.rect.collidepoint(self.player.mouse_pos):
            self.image = self.text_bold
            
            if self.player.pressed == 'mouse 1':
                self.pressed = True
            else:
                self.pressed = False
        else:
            self.image = self.text_norm


class Title(pygame.sprite.Sprite):

    def __init__(self, DISPLAY_SIZE, x, y, text):
        pygame.sprite.Sprite.__init__(self)
        self.DISPLAY_SIZE = DISPLAY_SIZE

        #load font/render text
        self.font = pygame.font.Font(None, 80)
        self.image = self.font.render(text, True, ORANGE)

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


    def update(self):
        pass


class Block(pygame.sprite.Sprite):

    def __init__(self, image, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        #load image
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        
#TO DO: make new menu buttons using GIMP instead of rendering
#       text. 

class Menu(pygame.sprite.Group):

    def __init__(self, DISPLAY_SIZE, player):
        pygame.sprite.Group.__init__(self)
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.player = player
        self.rects = []


    def addButton(self, x, y, text):
        button_block = Block('Images/brick.png', x, y, (140,60))
        button = Button(self.DISPLAY_SIZE, x, y, text, self.player)
        self.add(button_block)
        self.add(button) 
        self.rects.append(button_block.rect)
        return button
   
    
    def addTitle(self, x, y, text):
        title_block = Block('Images/paddle.png', x, y, (300,80))
        title = Title(self.DISPLAY_SIZE, x, y, text)
        self.add(title_block)
        self.add(title)
        self.rects.append(title_block.rect)
        return title
