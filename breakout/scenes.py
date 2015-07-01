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
from breakout.brick import Brick
from breakout.menu import Menu
from breakout.resource import *
from breakout.constants import *

class GamePlay(Scene):
    """Main gameplay scene."""
    def __init__(self, level):
        """Initialize the scene."""
        self.level = level
        self.next_level = load_level(level['next'])
        self.next_scene = self
        self.background, self.bg_rect = load_image('brickwall.png')
        self.score = Score(0) 
        self.paddle = Paddle()
        self.ball = Ball(paddle=self.paddle, speed=self.level['ball_speed'], 
                on_lose=lambda: self.goto(MenuScene.lose()))
        self.sprites = pygame.sprite.Group(self.ball, self.paddle, self.score)

        Brick.fill_display(self.sprites, level['bricks']) #place bricks
        self.draw_rects = (self.ball.draw_rect, self.paddle.draw_rect, self.score.draw_rect) #list of rects to update

        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
        pygame.mouse.set_visible(False) #make mouse invisible while playing the game


    def render(self, screen):
        """Render the Scene."""
        screen.blit(self.background, (0,0))
        self.sprites.draw(screen) 


    def update(self):
        """Update the Scene."""
        self.sprites.update(self.sprites, self.ball, lambda: self.score.incr()) #update sprites
            
        if len(self.sprites.sprites()) == 3: #check if all bricks are destroyed
            self.goto(GamePlay(self.next_level))
            pygame.time.wait(300)

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
                    self.goto(Pause(self))
                elif event.key == K_ESCAPE:
                    self.goto(MenuScene.lose())


# consider using *args, **kwargs for constructor
class MenuScene(Scene):
    """Menu scene class"""
    def __init__(self, title, btn1, btn1_pressed, btn2, btn2_pressed, scene1, scene2):
        """Initialize the scene."""
        self.next_scene = self
        self.mouse_pos = (0,0)
        self.pressed = ''
        self.background, self.bg_rect = load_image('brickwall.png')

        self.menu = Menu() #construct menu
        self.menu.addTitle(RESOLUTION[0]/2, 100, title) 
        self.menu.addButton(RESOLUTION[0]/2, 200, btn1, btn1_pressed, lambda: self.goto(scene1))
        self.menu.addButton(RESOLUTION[0]/2, 300, btn2, btn2_pressed, lambda: self.goto(scene2))
        
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
    def start(cls):
        """Return a menu scene object for the start screen."""
        level = load_level('level_1.xml')
        return cls('breakout.png','start.png','start_pressed.png',
                'quit.png','quit_pressed.png', GamePlay(level), None)
    
    
    @classmethod
    def win(cls):
        """Return a menu scene object for the win screen."""
        level = load_level('level_1.xml')
        return cls('win.png','retry.png','retry_pressed.png',
                'quit.png','quit_pressed.png', GamePlay(level), None)
    
    
    @classmethod
    def lose(cls):
        """Return a menu scene object for the lose screen."""
        level = load_level('level_1.xml')
        return cls('lose.png','retry.png','retry_pressed.png',
                'quit.png','quit_pressed.png', GamePlay(level), None)



class Pause(Scene):
    """Pause scene class."""
    def __init__(self, return_scene):
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

