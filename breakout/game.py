#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Game Class

This module defines the game class. The class is used to
create a game object that is able to run and control the game
"""

import pygame, resource, sys
from pygame.locals import *

#import game modules
from ball import Ball
from paddle import Paddle
from player import Player
from brick import BrickManager
from menu import Menu

pygame.init() #initialize pygame

class Game(object):
    """Main Game Class"""
    def __init__(self):
        """Initialize Game object""" 
        self.GAME_NAME  = "Breakout"  #name of the game 
        self.FPS = 40 #frames per second limit
        self.RES = (800,600)  #size of the display

        self.display = pygame.display.set_mode(self.RES)
        pygame.display.set_caption(self.GAME_NAME)
        self.clock = pygame.time.Clock()
        
        self.player = Player(self.RES, 'player1', 0) 
       
        self.background, self.bg_rect = resource.load_image('resources/images/brickwall.png')
        self.background.convert()


    def run(self): 
        """Run the main game loop."""
        pygame.mouse.set_visible(False) #make mouse invisible while playing the game
        paused = False

        self.player.reset()
        
        paddle = Paddle(self.RES)
        ball = Ball(self.RES, paddle, self.player)
        bricks = BrickManager(self.RES, ball, self.player)
        sprites = pygame.sprite.Group(paddle, ball, self.player)
  
        bricks.fillDisplay() #place bricks
        draw_rects = (ball.draw_rect, paddle.draw_rect, self.player.draw_rect) #list of rects to update
        self.display.blit(self.background, (0,0)) #blit background to the screen

        bricks.draw(self.display)
        sprites.draw(self.display)
        
        pygame.display.update()
        pygame.time.wait(500)
            
        allowed_events = [QUIT, KEYDOWN, KEYUP]
        pygame.event.set_allowed(allowed_events)
        
        while self.player.alive: #main game loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        paddle.direction = 'left'
                    elif event.key == K_RIGHT:
                        paddle.direction = 'right'
                    elif event.key == K_p:
                        paused = True
                    elif event.key == K_ESCAPE:
                        self.player.won = False
                        self.player.alive = False
                elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        paddle.direction = ''
                    elif event.key == K_RIGHT:
                        paddle.direction = ''
                    elif event.key == K_p:
                        paused = False
   

            if paused:
                continue

            self.display.blit(self.background, (0,0)) #blit background to the screen
                        
            bricks.draw(self.display) #draw sprites
            sprites.draw(self.display) 
            bricks.update(bricks) #update sprites
            sprites.update()
        
            if not bricks.sprites(): #check if all bricks are destroyed
                self.player.won = True
                self.player.alive = False 
            
            pygame.display.update(draw_rects)
            self.clock.tick(self.FPS)
            pygame.time.wait(5)

        pygame.time.wait(300)
        self.end()

    def start(self): #function displays the start screen
        """Display the start screen."""
        pygame.mouse.set_visible(True)
        mouse_pos = (0,0)
        pressed = ''

        menu = Menu(self.RES) #construct menu
        menu.addTitle(self.RES[0]/2, 100, 'resources/images/breakout.png') 
        menu.addButton(self.RES[0]/2, 200, 'resources/images/start.png', 'resources/images/start_pressed.png', self.run)
        menu.addButton(self.RES[0]/2, 300, 'resources/images/quit.png', 'resources/images/quit_pressed.png', self.quit)
        
        self.display.blit(self.background, (0,0))
        menu.draw(self.display)
        pygame.display.update()
        
        allowed_events = [QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN]
        pygame.event.set_allowed(allowed_events)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    pressed = 'mouse ' + str(event.button)
                elif event.type == MOUSEMOTION:
                    mouse_pos = event.pos
            
            self.display.blit(self.background, (0,0))
            menu.draw(self.display)
            menu.update(mouse_pos, pressed)

            pygame.display.update(menu.rects)
            self.clock.tick(self.FPS)
            pygame.time.wait(5)


    def end(self): #function displays the win/lose screens
        """Display the quit screen.""" 
        pygame.mouse.set_visible(True)
        mouse_pos = (0,0)
        pressed = ''

        menu = Menu(self.RES) #construct menu
        if self.player.won:
            menu.addTitle(self.RES[0]/2, 100, 'resources/images/win.png') 
        else:
            menu.addTitle(self.RES[0]/2, 100, 'resources/images/lose.png') 
        menu.addButton(self.RES[0]/2, 200, 'resources/images/retry.png', 'resources/images/retry_pressed.png', self.run)
        menu.addButton(self.RES[0]/2, 300, 'resources/images/quit.png', 'resources/images/quit_pressed.png', self.quit)
        
        self.display.blit(self.background, (0,0))
        menu.draw(self.display)
        pygame.display.update()
        
        allowed_events = [QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN]
        pygame.event.set_allowed(allowed_events)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    pressed = 'mouse ' + str(event.button)
                elif event.type == MOUSEBUTTONUP:
                    mouse_pos = event.pos
                    pressed = ''
                elif event.type == MOUSEMOTION:
                    mouse_pos = event.pos

            self.display.blit(self.background, (0,0))
            menu.draw(self.display)
            menu.update(mouse_pos, pressed)

            pygame.display.update(menu.rects)
            self.clock.tick(self.FPS)
            pygame.time.wait(5)

    
    def quit(self):
        """Quit the game."""
        pygame.quit()
        sys.exit()
