import pygame, sys
from pygame.locals import *
from breakout.menuscene import MenuScene
from breakout.menu import Menu
from breakout.gameplay import GamePlay
import breakout.resource as resource

class Start(MenuScene):
    """Start scene class"""
    def __init__(self, RES):
        MenuScene.__init__(self, RES, 
                'breakout.png','start.png','start_pressed.png','quit.png','quit_pressed.png', 
                lambda: self.goto(GamePlay(RES)), lambda: self.terminate())
