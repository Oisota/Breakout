"""
Scenes Module

This module contains all the game scenes. The scenes
included are MenuScene, GamePlay, and Pause scenes.
"""

import pygame, sys
from pygame.locals import *
from breakout.scene import Scene
from breakout.ball import Ball
from breakout.paddle import Paddle
from breakout.score import Score
from breakout.brick import BrickManager
from breakout.menu import Menu
import breakout.resource as resource

class GamePlay(Scene):
    """Main gameplay scene."""
    def __init__(self, RES):
        """Initialize the scene."""
        self.RES = RES
        self.next_scene = self
        self.background, self.bg_rect = resource.load_image('brickwall.png')
        self.score = Score(self.RES, 0) 
        self.paddle = Paddle(self.RES)
        self.ball = Ball(self.RES, self.paddle, lambda: self.goto(MenuScene.lose(self.RES)))
        self.bricks = BrickManager(self.RES)
        self.sprites = pygame.sprite.Group(self.ball, self.paddle, self.score)
  
        self.bricks.fillDisplay() #place bricks
        self.draw_rects = (self.ball.draw_rect, self.paddle.draw_rect, self.score.draw_rect) #list of rects to update

        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
        pygame.mouse.set_visible(False) #make mouse invisible while playing the game


    def render(self, screen):
        """Render the Scene."""
        screen.blit(self.background, (0,0))
        self.bricks.draw(screen)
        self.sprites.draw(screen) 


    def update(self):
        """Update the Scene."""
        self.bricks.update(self.bricks, self.ball, lambda: self.score.incr()) #update sprites
        self.sprites.update()
            
        if not self.bricks.sprites(): #check if all bricks are destroyed
            self.goto(MenuScene.win(self.RES))

        #pygame.display.update(self.draw_rects)
        pygame.display.update()


    def handle_events(self):
        """Handle user input events."""
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.paddle.move_left()
        elif keys[K_RIGHT]:
            self.paddle.move_right()

        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    self.goto(Pause(self.RES, self))
                elif event.key == K_ESCAPE:
                    self.goto(MenuScene.lose(self.RES))



class MenuScene(Scene):
    """Menu scene class"""
    def __init__(self, RES, title, btn1, btn1_pressed, btn2, btn2_pressed, scene1, scene2):
        """Initialize the scene."""
        self.next_scene = self
        self.mouse_pos = (0,0)
        self.pressed = ''
        self.background, self.bg_rect = resource.load_image('brickwall.png')

        self.menu = Menu() #construct menu
        self.menu.addTitle(RES[0]/2, 100, title) 
        self.menu.addButton(RES[0]/2, 200, btn1, btn1_pressed, lambda: self.goto(scene1))
        self.menu.addButton(RES[0]/2, 300, btn2, btn2_pressed, lambda: self.goto(scene2))
        
        pygame.event.set_allowed([QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
        pygame.mouse.set_visible(True)
        

    def render(self, screen):
        """Render the scene."""
        screen.blit(self.background, (0,0))
        self.menu.draw(screen)

        
    def update(self):
        """Update the scene."""
        self.menu.update(self.mouse_pos, self.pressed)
        #pygame.display.update(self.menu.rects)
        pygame.display.update()


    def handle_events(self):
        """Handle user input events."""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = event.pos
                self.pressed = 'mouse ' + str(event.button)
            elif event.type == MOUSEMOTION:
                self.mouse_pos = event.pos


    @classmethod
    def start(cls, RES):
        """Return a menu scene object for the start screen."""
        return cls(RES, 'breakout.png','start.png','start_pressed.png',
                'quit.png','quit_pressed.png', GamePlay(RES), None)
    
    
    @classmethod
    def win(cls, RES):
        """Return a menu scene object for the win screen."""
        return cls(RES, 'win.png','retry.png','retry_pressed.png',
                'quit.png','quit_pressed.png', GamePlay(RES), None)
    
    
    @classmethod
    def lose(cls, RES):
        """Return a menu scene object for the lose screen."""
        return cls(RES, 'lose.png','retry.png','retry_pressed.png',
                'quit.png','quit_pressed.png', GamePlay(RES), None)



class Pause(Scene):
    """Pause scene class."""
    def __init__(self, RES, return_scene):
        """Initialize the scene."""
        self.next_scene = self
        self.return_scene = return_scene
        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
        

    def render(self, screen):
        """Render the scene."""
        pass

        
    def update(self):
        """Update the scene."""
        pass


    def handle_events(self):
        """Handle user input events."""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    self.goto(self.return_scene)

