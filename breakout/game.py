"""
Game Class

This module defines the game class. The class is used to
create a game object that is able to run and control the game
"""

import pygame, sys
import breakout.resource as resource
from pygame.locals import *

from breakout.title import Title

pygame.init() #initialize pygame

class Game(object):
    """Main Game Class"""
    def __init__(self):
        """Initialize Game object""" 
        self.GAME_NAME  = "Breakout"  #name of the game 
        self.FPS = 40 #frames per second limit
        self.RES = (800,600)  #size of the display

        self.screen = pygame.display.set_mode(self.RES)
        pygame.display.set_caption(self.GAME_NAME)
        self.clock = pygame.time.Clock()
        

    def start(self): 
        """Run the game."""
        current_scene = Title(self.RES)

        while current_scene != None:
            current_scene.handle_events()
            current_scene.update()
            current_scene.render(self.screen)
            current_scene = current_scene.next_scene

            self.clock.tick(self.FPS)


        pygame.quit()
        sys.exit()
