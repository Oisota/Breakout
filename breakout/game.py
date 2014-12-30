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

#initialize pygame
pygame.init()

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
       
        self.background, self.bg_rect = resource.load_image('images/brickwall.png')
        self.background.convert()


    def run(self): 
        """Run the main game loop."""
        pygame.mouse.set_visible(False) #make mouse invisible while playing the game
        
        #initialize game objects 
        player = Player(self.RES, 'player1', 0)
        paddle = Paddle(self.RES, player)
        ball = Ball(self.RES, paddle, player)
        bricks = BrickManager(self.RES, ball, player)
        sprites = pygame.sprite.Group(paddle, ball, player)
  
        bricks.fillDisplay() #place bricks
        draw_rects = (ball.draw_rect, paddle.draw_rect, player.draw_rect) #list of rects to update
        self.display.blit(self.background, (0,0)) #blit background to the screen

        bricks.draw(self.display)
        sprites.draw(self.display)
        
        pygame.display.update()
        pygame.time.wait(500)
        
        #main game loop
        while player.alive:
            
            player.getInput() #get input from player

            if player.paused:
                continue

            self.display.blit(self.background, (0,0)) #blit background to the screen
                        
            #draw sprites
            bricks.draw(self.display)
            sprites.draw(self.display)
            
            #update sprites
            bricks.update(bricks)
            sprites.update()
        
            if not bricks.sprites(): #check if all bricks are destroyed
                player.won = True
                player.alive = False 
            
            pygame.display.update(draw_rects)
            self.clock.tick(self.FPS)
            pygame.time.wait(5)

        #check if player has won/lost 
        pygame.time.wait(300)
        if player.won:
            self.end('images/win.png')
        elif not player.won:
            self.end('images/lose.png')


    def start(self): #function displays the start screen
        """Display the start screen."""
        pygame.mouse.set_visible(True)

        player = Player(self.RES, 'player1', 0)
        #construct menu
        menu = Menu(self.RES, player) 
        menu.addTitle(self.RES[0]/2, 100, 'images/breakout.png') 
        menu.addButton(self.RES[0]/2, 200, 'images/start.png', 'images/start_pressed.png', self.run)
        menu.addButton(self.RES[0]/2, 300, 'images/quit.png', 'images/quit_pressed.png', self.quit)
        
        self.display.blit(self.background, (0,0))
        menu.draw(self.display)
        pygame.display.update()

        while True:
            
            player.getInput() 
            self.display.blit(self.background, (0,0))
            menu.draw(self.display)
            menu.update()

            pygame.display.update(menu.rects)
            self.clock.tick(self.FPS)
            pygame.time.wait(5)


    def end(self, image): #function displays the win/lose screens
        """Display the quit screen.""" 
        pygame.mouse.set_visible(True)

        player = Player(self.RES, 'player1', 0)
        #construct menu
        menu = Menu(self.RES, player)       
        menu.addTitle(self.RES[0]/2, 100, image) 
        menu.addButton(self.RES[0]/2, 200, 'images/retry.png', 'images/retry_pressed.png', self.run)
        menu.addButton(self.RES[0]/2, 300, 'images/quit.png', 'images/quit_pressed.png', self.quit)
        
        self.display.blit(self.background, (0,0))
        menu.draw(self.display)
        pygame.display.update()

        while True:
            player.getInput()
            self.display.blit(self.background, (0,0))
            menu.draw(self.display)
            menu.update()

            pygame.display.update(menu.rects)
            self.clock.tick(self.FPS)
            pygame.time.wait(5)


    def quit(self):
        """Quit the game."""
        pygame.quit()
        sys.exit()
