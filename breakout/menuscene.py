import pygame, sys
from pygame.locals import *
from breakout.scene import Scene
from breakout.menu import Menu
import breakout.resource as resource

class MenuScene(Scene):
    """Base menu scene class"""
    def __init__(self, RES, title, btn1, btn1_pressed, btn2, btn2_pressed, func1, func2):
        self.next_scene = self
        self.mouse_pos = (0,0)
        self.pressed = ''
        self.background, self.bg_rect = resource.load_image('brickwall.png')

        self.menu = Menu(RES) #construct menu
        self.menu.addTitle(RES[0]/2, 100, title) 
        self.menu.addButton(RES[0]/2, 200, btn1, btn1_pressed, func1)
        self.menu.addButton(RES[0]/2, 300, btn2, btn2_pressed, func2)
        
        pygame.event.set_allowed([QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
        pygame.mouse.set_visible(True)
        

    def render(self, screen):
        """Render the scene"""
        screen.blit(self.background, (0,0))
        self.menu.draw(screen)

        
    def update(self):
        """Update the scene"""
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
