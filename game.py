#!/usr/bin/python3

import sys
import time
import pygame
from pygame.locals import *

#import game modules
from ball import Ball
from paddle import Paddle
from player import Player
from brick import BrickManager
from menu import Menu
from colors import *

#initialize pygame
pygame.init()

class Game(object):

    def __init__(self):
    
        self.GAME_NAME    = "Breakout"  #name of the game 
        self.FPS          = 40          #frames per second limit
        self.DISPLAY_SIZE = (800,600)   #size of the display

        self.display = pygame.display.set_mode(self.DISPLAY_SIZE)
        pygame.display.set_caption(self.GAME_NAME)
        self.clock = pygame.time.Clock()
       
        self.background = pygame.image.load('Images/brickwall.png')
        self.background.convert()

        #initialize game objects
        self.player = Player(self.DISPLAY_SIZE, self.display, 'Derek', 0)
        self.paddle = Paddle(self.DISPLAY_SIZE, self.display, self.player)
        self.ball = Ball(self.DISPLAY_SIZE, self.display, self.paddle, self.player)
        self.bricks = BrickManager(self.DISPLAY_SIZE, self.ball, self.player)
        self.sprites = pygame.sprite.Group(self.paddle, self.ball)


    def run(self): #function that runs the game

        pygame.mouse.set_visible(False) #make mouse invisible while playing the game
  
        self.player.reset()
        self.paddle.reset()
        self.ball.reset()
        self.bricks.reset()
        self.bricks.fillDisplay() #place bricks
        
        self.display.blit(self.background, (0,0)) #blit background to the screen
        self.bricks.draw(self.display)
        self.sprites.draw(self.display)
        pygame.display.update()
        pygame.time.wait(500)
        
        #main game loop
        while self.player.alive:
            
            self.player.getInput() #get input from player

            if self.player.paused:
                continue

            self.display.blit(self.background, (0,0)) #blit background to the screen
                        
            self.bricks.draw(self.display)
            self.sprites.draw(self.display)
            self.player.draw_score()
            
            self.bricks.update(self.bricks)
            self.sprites.update()
        
            if not self.bricks.sprites(): #check if all bricks are destroyed
                self.player.won = True
                self.player.alive = False 
            
            pygame.display.update((self.ball.draw_rect, self.paddle.draw_rect, self.player.score_rect))
            self.clock.tick(self.FPS)
            pygame.time.wait(5)

        #check if player has won/lost 
        if self.player.won:
            self.end('Images/win.png')
        elif not self.player.won:
            self.end('Images/lose.png')


    def start(self): #function displays the start screen

        pygame.mouse.set_visible(True)

        #construct menu
        menu = Menu(self.DISPLAY_SIZE, self.player) 
        title = menu.addTitle(self.DISPLAY_SIZE[0]/2, 100, 'Images/breakout.png') 
        start = menu.addButton(self.DISPLAY_SIZE[0]/2, 200, 'Images/start.png', 'Images/start_pressed.png')
        quit = menu.addButton(self.DISPLAY_SIZE[0]/2, 300, 'Images/quit.png', 'Images/quit_pressed.png')
        
        self.display.blit(self.background, (0,0))
        menu.draw(self.display)
        pygame.display.update()

        while self.player.alive:
            
            self.player.getInput() 
            self.display.blit(self.background, (0,0))
            menu.draw(self.display)
            menu.update()

            if start.pressed:
                self.run()
            elif quit.pressed:
                pygame.quit()
                sys.exit()

            pygame.display.update(menu.rects)
            self.clock.tick(self.FPS)
            pygame.time.wait(5)


    def end(self, image): #function displays the win/lose screens
    
        pygame.mouse.set_visible(True)

        #construct menu
        menu = Menu(self.DISPLAY_SIZE, self.player)       
        title = menu.addTitle(self.DISPLAY_SIZE[0]/2, 100, image) 
        again = menu.addButton(self.DISPLAY_SIZE[0]/2, 200, 'Images/retry.png', 'Images/retry_pressed.png')
        quit = menu.addButton(self.DISPLAY_SIZE[0]/2, 300, 'Images/quit.png', 'Images/quit_pressed.png')
        
        self.display.blit(self.background, (0,0))
        menu.draw(self.display)
        pygame.display.update()

        while True:
            self.player.getInput()
            self.display.blit(self.background, (0,0))
            self.player.draw_score()
            menu.draw(self.display)
            menu.update()

            if again.pressed:
                self.run()
            elif quit.pressed:
                pygame.quit()
                sys.exit()

            pygame.display.update(menu.rects)
            self.clock.tick(self.FPS)
            pygame.time.wait(5)
