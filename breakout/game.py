"""
Game Module

This module defines a run function. The run function
initializes pygame, sets some game variabls and runs 
the game.
"""

import pygame, sys
from breakout.start import Start

pygame.init() #initialize pygame

def run():
    """Run the game""" 
    GAME_NAME  = "Breakout"  #name of the game 
    FPS = 40 #frames per second limit
    RES = (800,600)  #size of the display

    screen = pygame.display.set_mode(RES)
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()
    

    scene = Start(RES)

    while scene != None:
        scene.handle_events()
        scene.update()
        scene.render(screen)
        scene = scene.next_scene

        clock.tick(FPS)
        pygame.time.wait(5)


    pygame.quit()
    sys.exit()
