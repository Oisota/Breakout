"""
Game Module

This module defines a run function. The run function
initializes pygame, sets some game variabls and runs 
the game.
"""

import pygame, sys
from breakout.title import Title

pygame.init() #initialize pygame

def run():
    """Run the game""" 
    GAME_NAME  = "Breakout"  #name of the game 
    FPS = 40 #frames per second limit
    RES = (800,600)  #size of the display

    screen = pygame.display.set_mode(RES)
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()
    

    current_scene = Title(RES)

    while current_scene != None:
        current_scene.handle_events()
        current_scene.update()
        current_scene.render(screen)
        current_scene = current_scene.next_scene

        clock.tick(FPS)


    pygame.quit()
    sys.exit()
