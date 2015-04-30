import pygame, sys
from pygame.locals import *
from breakout.scene import Scene
from breakout.menu import Menu
import breakout.resource as resource

class Win(Scene):
    """Win scene"""
    def __init__(self, RES):
        """Initialize the scene"""
        self.mouse_pos = (0,0)
        self.pressed = ''
        self.background, self.bg_rect = resource.load_image('brickwall.png')

        self.menu = Menu(self.RES) #construct menu
        self.menu.addTitle(self.RES[0]/2, 100, 'win.png') 
        self.menu.addButton(self.RES[0]/2, 200, 'retry.png', 'retry_pressed.png', lambda: self.goto(Gameplay()))
        self.menu.addButton(self.RES[0]/2, 300, 'quit.png', 'quit_pressed.png', lambda: self.terminate())

        self.allowed_events = [QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN]
        pygame.event.set_allowed(allowed_events)
        pygame.mouse.set_visible(True)


    def render(self):
        """Render the Scene"""
        screen.blit(self.background, (0,0))
        self.menu.draw(screen)

    def update(self):
        """Update the Scene"""
        self.menu.update(mouse_pos, pressed)
        #pygame.display.update(self.menu.rects)
        pygame.display.update()

    def handle_events(self):
        """Handle Events"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                pressed = 'mouse ' + str(event.button)
            elif event.type == MOUSEMOTION:
                mouse_pos = event.pos
    
    
    def goto(self, scene):
        """change the scene"""
        self.next_scene = scene


    def terminate(self):
        """End the scene"""
        self.goto(None)
