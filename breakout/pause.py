import pygame
from pygame.locals import *
from breakout.scene import Scene

class Pause(Scene):
    """Title scene class"""
    def __init__(self, RES, game_scene):
        self.next_scene = self
        self.game_scene = game_scene
        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
        

    def render(self, screen):
        """Render the Title scene"""
        pass

        
    def update(self):
        """Update the Title scene"""
        pass


    def handle_events(self):
        """handle user input events"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    self.goto(self.game_scene)


    def goto(self, scene):
        """change the scene"""
        self.next_scene = scene


    def terminate(self):
        """End the scene"""
        self.goto(None)
