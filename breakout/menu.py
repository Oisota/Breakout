#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Menu, Button, and Title Classes

This module contains the Menu, Button, and Title classes.
These are used to create and display the menus for the start
and quit screens. Button is a clickable button that changes
color when the user mouses over it. Title is a a simple sprite.
Menu is a container for the buttons and a title.
"""

import pygame

class Button(pygame.sprite.Sprite):
    
    def __init__(self, x, y, img1, img2, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.pressed = False 
        #self.sound = pygame.mixer.Sound('sounds/blip.wav')

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
                #self.sound.play() 
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

    def __init__(self, RES, player):
        pygame.sprite.Group.__init__(self)
        self.RES = RES
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
