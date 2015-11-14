"""
Game Module

This module defines a run function. The run function
initializes pygame, sets some game variables and runs 
the game.
"""

import sys

import pygame

from breakout.game.scenes import MenuScene
from breakout.utils.constants import GAME_NAME, RESOLUTION, FRAMES_PER_SECOND


def run():
    """Run the game.""" 
    pygame.init() 
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()

    scene = MenuScene.start()

    while scene != None:
        scene.handle_events()
        scene.update()
        scene.render(screen)
        scene = scene.next_scene

        clock.tick(FRAMES_PER_SECOND)
        pygame.time.wait(5)


    pygame.quit()
    sys.exit()
