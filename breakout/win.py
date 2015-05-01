import pygame, sys
from pygame.locals import *
from breakout.menuscene import MenuScene
from breakout.menu import Menu
import breakout.resource as resource

class Win(MenuScene):
    """Win scene"""
    def __init__(self, RES):
        """Initialize the scene"""
        MenuScene.__init__(self, RES, 
                'win.png','retry.png','retry_pressed.png','quit.png','quit_pressed.png', 
                lambda: self.goto(GamePlay(RES)), lambda: self.terminate())
