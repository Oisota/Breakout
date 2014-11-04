#!/usr/bin/python3

import pygame
from colors import *

class Button(pygame.sprite.Sprite):

    def __init__(self, DISPLAY_SIZE, display, x, y, text, player):
        pygame.sprite.Sprite.__init__(self)
        #load image
        self.image = pygame.image.load('Images/brick.png')
        self.image = pygame.transform.scale(self.image, (140,60))
        self.img_rect = self.image.get_rect()
        self.img_rect.center = (x,y)
        #load font
        self.font_norm = pygame.font.Font(None, 60)
        self.font_bold = pygame.font.Font(None, 60)
        self.font_bold.set_bold(True)
        #render text
        self.text_norm = self.font_norm.render(text, True, BLACK)
        self.text_bold = self.font_bold.render(text, True, BLACK)
         
        self.text_rect = self.text_norm.get_rect()
        self.text_rect.center = (x,y)
        self.text = self.text_norm

        self.DISPLAY_SIZE = DISPLAY_SIZE 
        self.display = display
        self.player = player
        self.pressed = False 


    def draw(self):
        self.display.blit(self.image, self.img_rect)
        self.display.blit(self.text, self.text_rect)


    def update(self):
        if self.img_rect.collidepoint(self.player.mouse_pos):
            self.text = self.text_bold
            
            if self.player.pressed == 'mouse 1':
                self.pressed = True
            else:
                self.pressed = False
        else:
            self.text = self.text_norm


class Title(pygame.sprite.Sprite):

    def __init__(self, DISPLAY_SIZE, display, x, y, text):
        pygame.sprite.Sprite.__init__(self)
        #load image
        self.image = pygame.image.load('Images/paddle.png')
        self.image = pygame.transform.scale(self.image, (300,80))
        self.img_rect = self.image.get_rect()
        self.img_rect.center = (x,y)
        #load font/render text
        self.font = pygame.font.Font(None, 80)
        self.text = self.font.render(text, True, ORANGE)

        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x,y)

        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.display = display


    def draw(self):
        self.display.blit(self.image, self.img_rect) 
        self.display.blit(self.text, self.text_rect)


    def update(self):
        pass


class Menu(object):

    def __init__(self, DISPLAY_SIZE, display, player):
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.display = display
        self.player = player
        self.title = None 
        self.buttons = []


    def addButton(self, x, y, text):
        button = Button(self.DISPLAY_SIZE, self.display, x, y, text, self.player)
        self.buttons.append(button) 
        return button
   
    
    def addTitle(self, x, y, text):
        self.title = Title(self.DISPLAY_SIZE, self.display, x, y, text)
        
    def draw(self):
        self.title.draw()
        for button in self.buttons:
            button.draw()
        
        
    def update(self):
        self.title.update()
        for button in self.buttons:
            button.update()
            
