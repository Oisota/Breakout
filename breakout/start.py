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
                lambda: self.goto(GamePlay(RES), lambda: self.terminate())
        self.next_scene = self
        self.mouse_pos = (0,0)
        self.pressed = ''
        self.background, self.bg_rect = resource.load_image('brickwall.png')

        self.menu = Menu(RES) #construct menu
        self.menu.addTitle(RES[0]/2, 100, 'breakout.png') 
        self.menu.addButton(RES[0]/2, 200, 'start.png', 'start_pressed.png', lambda: self.goto(GamePlay(RES)))
        self.menu.addButton(RES[0]/2, 300, 'quit.png', 'quit_pressed.png', lambda: self.terminate())
        
        pygame.event.set_allowed([QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
        pygame.mouse.set_visible(True)
        

    def render(self, screen):
        """Render the Start scene"""
        screen.blit(self.background, (0,0))
        self.menu.draw(screen)

        
    def update(self):
        """Update the Start scene"""
        self.menu.update(self.mouse_pos, self.pressed)
        #pygame.display.update(self.menu.rects)
        pygame.display.update()


    def handle_events(self):
        """handle user input events"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = event.pos
                self.pressed = 'mouse ' + str(event.button)
            elif event.type == MOUSEMOTION:
                self.mouse_pos = event.pos
         
        
    def goto(self, scene):
        """change the scene"""
        self.next_scene = scene


    def terminate(self):
        """End the scene"""
        self.goto(None)
