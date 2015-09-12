import pygame
from pygame.locals import *

from breakout.util.scene import Scene
from breakout.util.constants import *


class LevelEditor(Scene):
    """Level Editor scene class"""
    def __init__(self):
        self.next_scene = self 
        self.mouse_pos = (0,0)
        self.pressed = ''
        self.background, self.bg_rect = load_image(BACKGROUND_IMAGE)
 
        pygame.event.set_allowed([QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
        pygame.mouse.set_visible(True)
 
 
    def render(self, screen):
        """Render the scene."""
        screen.blit(self.background, (0,0))
        self.grid.draw(screen)
 
 
    def update(self):
        """Update the scene."""
        self.grid.update(self.mouse_pos, self.pressed)
        #pygame.display.update(self.menu.rects)
        pygame.display.update()
 
 
    def hand_events(self):
        """Hande user input events."""
        for event in pygame.events.get(): 
            if event.type == QUIT:
                self.goto(None)
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = event.pos
                self.pressed = 'mouse ' + str(event.button)
            elif event.type == MOUSEBUTTONUP:
                self.mouse_pos = event.pos
                self.pressed = ''
            elif event.type == MOUSEMOTION:
