import pygame, sys
from pygame.locals import *

# scenes
from breakout.menuscene import MenuScene
#from breakout.gameplay import GamePlay

# game objects
from breakout.menu import Menu
import breakout.resource as resource

class Lose(MenuScene):
    """Win scene"""
    def __init__(self, RES):
        """Initialize the scene"""
        MenuScene.__init__(self, RES, 
                'lose.png','retry.png','retry_pressed.png','quit.png','quit_pressed.png', 
                lambda: self.goto(GamePlay(RES), lambda: self.terminate())
        self.mouse_pos = (0,0)
        self.pressed = ''
        self.next_scene = self
        self.background, self.bg_rect = resource.load_image('brickwall.png')

        self.menu = Menu(RES) #construct menu
        self.menu.addTitle(RES[0]/2, 100, 'lose.png') 
        self.menu.addButton(RES[0]/2, 200, 'retry.png', 'retry_pressed.png', lambda: self.goto(Gameplay(RES)))
        self.menu.addButton(RES[0]/2, 300, 'quit.png', 'quit_pressed.png', lambda: self.terminate())

        pygame.event.set_allowed([QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
        pygame.mouse.set_visible(True)


    def render(self, screen):
        """Render the Scene"""
        screen.blit(self.background, (0,0))
        self.menu.draw(screen)


    def update(self):
        """Update the Scene"""
        self.menu.update(self.mouse_pos, self.pressed)
        #pygame.display.update(self.menu.rects)
        pygame.display.update()


    def handle_events(self):
        """Handle Events"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = event.pos
                pressed = 'mouse ' + str(event.button)
            elif event.type == MOUSEMOTION:
                self.mouse_pos = event.pos


    def goto(self, scene):
        """change the scene"""
        self.next_scene = scene


    def terminate(self):
        """End the scene"""
        self.goto(None)
