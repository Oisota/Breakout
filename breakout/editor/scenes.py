import pygame
from pygame.locals import *

from breakout.util.scene import Scene
from breakout.util.constants import *
from breakout.util.resource import load_image
from breakout.editor.cell import Cell


class Editor(Scene):
    """Level Editor scene class"""
    def __init__(self):
        self.next_scene = self 
        self.mouse_pos = (0,0)
        self.pressed = ''
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
        #pygame.display.update(self.menu.rects)
        pygame.display.update()
 
 
    def handle_events(self):
        """Hande user input events."""
        for event in pygame.event.get(): 
            if event.type == QUIT:
                self.goto(None)
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = event.pos
                self.pressed = 'mouse ' + str(event.button)
            elif event.type == MOUSEBUTTONUP:
                self.mouse_pos = event.pos
                self.pressed = ''
            elif event.type == MOUSEMOTION:
                self.mouse_pos = event.pos
