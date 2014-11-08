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
       
        #load images
        self.background = pygame.image.load('Images/brickwall.png')
        self.background.convert()

        #initialize game objects
        self.player = Player(self.DISPLAY_SIZE, self.display, 'Derek', 0)
        self.paddle = Paddle(self.DISPLAY_SIZE, self.display, self.player)
        self.ball = Ball(self.DISPLAY_SIZE, self.display, self.paddle, self.player)
        self.bricks = BrickManager(self.DISPLAY_SIZE, self.display, self.ball, self.player)


    def run(self): 

        pygame.mouse.set_visible(False) #make mouse invisible while playing the game
  
        self.player.reset()
        self.paddle.reset()
        self.ball.reset()
        self.bricks.reset()
        self.bricks.fillDisplay() #place bricks
        
        self.display.blit(self.background, (0,0)) #blit background to the screen
        self.paddle.draw()   #draw the ball, paddle, bricks
        self.ball.draw()
        self.bricks.draw()
        pygame.display.update()

        #main game loop
        while self.player.alive:
            
            self.player.getInput() #get input from player

            if self.player.paused:
                continue

            self.display.blit(self.background, (0,0)) #blit background to the screen
                        
            self.paddle.draw()   #draw the ball, paddle, bricks
            self.ball.draw()
            self.bricks.draw()
            self.player.draw_score()
            
            self.paddle.update()  #update ball, paddle, bricks
            self.ball.update() 
            self.bricks.update()
            
            pygame.display.update((self.ball.draw_rect, self.paddle.draw_rect, self.player.score_rect))
            self.clock.tick(self.FPS)

        #check if player has won/lost 
        if self.player.won:
            self.win()
        elif not self.player.won:
            self.lose()


    def start(self):

        pygame.mouse.set_visible(True)

        #construct menu
        menu = Menu(self.DISPLAY_SIZE, self.display, self.player) 
        menu.addTitle(self.DISPLAY_SIZE[0]/2, 100, 'Breakout!')
        start = menu.addButton(self.DISPLAY_SIZE[0]/2, 200, 'Start')
        quit = menu.addButton(self.DISPLAY_SIZE[0]/2, 300, 'Quit')
        
        self.display.blit(self.background, (0,0))
        menu.draw()
        pygame.display.update()

        while self.player.alive:
            
            self.player.getInput() 
            self.display.blit(self.background, (0,0))
            menu.draw()
            menu.update()

            if start.pressed:
                self.run()
            elif quit.pressed:
                pygame.quit()
                sys.exit()

            
            #fix so that only buttons and title get updated
            pygame.display.update((menu.title.img_rect, start.img_rect, quit.img_rect))
            self.clock.tick(self.FPS)


    def win(self):
    
        pygame.mouse.set_visible(True)

        #construct menu
        menu = Menu(self.DISPLAY_SIZE, self.display, self.player) 
        menu.addTitle(self.DISPLAY_SIZE[0]/2, 100, 'You Won!')
        again = menu.addButton(self.DISPLAY_SIZE[0]/2, 200, 'Retry')
        quit = menu.addButton(self.DISPLAY_SIZE[0]/2, 300, 'Quit')
        
        self.display.blit(self.background, (0,0))
        menu.draw()
        pygame.display.update()

        while True:
            self.player.getInput()
            self.display.blit(self.background, (0,0))
            self.player.draw_score()
            menu.draw()
            menu.update()

            if again.pressed:
                self.run()
            elif quit.pressed:
                pygame.quit()
                sys.exit()

            pygame.display.update((menu.title.img_rect, again.img_rect, quit.img_rect, self.player.score_rect))
            self.clock.tick(self.FPS)


    def lose(self):
       
        pygame.mouse.set_visible(True)

        #construct menu
        menu = Menu(self.DISPLAY_SIZE, self.display, self.player) 
        menu.addTitle(self.DISPLAY_SIZE[0]/2, 100, 'You Lost')
        again = menu.addButton(self.DISPLAY_SIZE[0]/2, 200, 'Retry')
        quit = menu.addButton(self.DISPLAY_SIZE[0]/2, 300, 'Quit')
        
        self.display.blit(self.background, (0,0))
        menu.draw()
        pygame.display.update()

        while True:
            self.player.getInput()
            self.display.blit(self.background, (0,0))
            self.player.draw_score()
            menu.draw()
            menu.update()

            if again.pressed:
                self.run()
            elif quit.pressed:
                pygame.quit()
                sys.exit()

            pygame.display.update((menu.title.img_rect, again.img_rect, quit.img_rect, self.player.score_rect))
            self.clock.tick(self.FPS)
