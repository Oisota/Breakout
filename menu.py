#!/usr/bin/python3

import pygame
from colors import *

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, img1, img2, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.pressed = False 

        #load image
        self.img_not_pressed = pygame.image.load(img1)
        self.img_pressed = pygame.image.load(img2)
        self.img_not_pressed  = pygame.transform.scale(self.img_not_pressed, (130,70))
        self.img_pressed  = pygame.transform.scale(self.img_pressed, (130,70))
        self.image = self.img_not_pressed
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        
    def update(self):
        if self.rect.collidepoint(self.player.mouse_pos):
            self.image = self.img_pressed
            
            if self.player.pressed == 'mouse 1':
                self.pressed = True
            else:
                self.pressed = False
        else:
            self.image = self.img_not_pressed


class Title(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        #load image
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (200,80))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


    def update(self):
        pass



class Menu(pygame.sprite.Group):

    def __init__(self, DISPLAY_SIZE, player):
        pygame.sprite.Group.__init__(self)
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.player = player
        self.rects = []


    def addButton(self, x, y, img1, img2):
        button = Button(x, y, img1, img2, self.player)
        self.add(button) 
        self.rects.append(button.rect)
        return button
   
    
    def addTitle(self, x, y, image):
        title = Title(x, y, image)
        self.add(title)
        self.rects.append(title.rect)
        return title
