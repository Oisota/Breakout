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

#initialize pygame
pygame.init()

class Game(object):

    def __init__(self):
    
        self.GAME_NAME  = "Breakout"  #name of the game 
        self.FPS = 40 #frames per second limit
        self.RES = (800,600)  #size of the display

        self.display = pygame.display.set_mode(self.RES)
        pygame.display.set_caption(self.GAME_NAME)
        self.clock = pygame.time.Clock()
       
        self.background = pygame.image.load('images/brickwall.png')
        self.background.convert()


    def run(self): #function that runs the game

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

        pygame.mouse.set_visible(True)

        player = Player(self.RES, 'player1', 0)
        #construct menu
        menu = Menu(self.RES, player) 
        title = menu.addTitle(self.RES[0]/2, 100, 'images/breakout.png') 
        start = menu.addButton(self.RES[0]/2, 200, 'images/start.png', 'images/start_pressed.png')
        quit = menu.addButton(self.RES[0]/2, 300, 'images/quit.png', 'images/quit_pressed.png')
        
        self.display.blit(self.background, (0,0))
        menu.draw(self.display)
        pygame.display.update()

        while True:
            
            player.getInput() 
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

        player = Player(self.RES, 'player1', 0)
        #construct menu
        menu = Menu(self.RES, player)       
        title = menu.addTitle(self.RES[0]/2, 100, image) 
        again = menu.addButton(self.RES[0]/2, 200, 'images/retry.png', 'images/retry_pressed.png')
        quit = menu.addButton(self.RES[0]/2, 300, 'images/quit.png', 'images/quit_pressed.png')
        
        self.display.blit(self.background, (0,0))
        menu.draw(self.display)
        pygame.display.update()

        while True:
            player.getInput()
            self.display.blit(self.background, (0,0))
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
