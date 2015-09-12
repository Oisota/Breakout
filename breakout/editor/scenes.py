"""
Editor Module

This module defines the editor scene which is the
main scene for running the level editor.
"""

import pygame
from pygame.locals import *

from breakout.utils.scene import Scene
from breakout.utils.constants import *
from breakout.utils.resource import load_image
from breakout.editor.cell import Cell


class Editor(Scene):
    """Level Editor scene class"""
    def __init__(self):
        self.next_scene = self 
        self.mouse_pos = (0,0)
        self.pressed = False
        self.background, self.bg_rect = load_image(BACKGROUND_IMAGE)
        
        self.sprites = pygame.sprite.Group()
        Cell.fill_display(self.sprites)
 
        pygame.event.set_allowed([QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
        pygame.mouse.set_visible(True)
 
 
    def render(self, screen):
        """Render the scene."""
        screen.blit(self.background, (0,0))
        self.sprites.draw(screen)
 
 
    def update(self):
        """Update the scene."""
        self.sprites.update(self.mouse_pos, self.pressed)
        pygame.display.update()
 
 
    def handle_events(self):
        """Hande user input events."""
        for event in pygame.event.get(): 
            if event.type == QUIT:
                self.goto(None)
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = event.pos
                if event.button == 1 and not self.pressed:
                    self.pressed = True
            elif event.type == MOUSEBUTTONUP:
                self.mouse_pos = event.pos
                self.pressed = False
            elif event.type == MOUSEMOTION:
                self.mouse_pos = event.pos
