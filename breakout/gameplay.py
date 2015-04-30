import pygame, sys
from pygame.locals import *

# scenes
from breakout.scene import Scene
from breakout.pause import Pause
from breakout.lose import Lose
from breakout.win import Win

# game objects
from breakout.ball import Ball
from breakout.paddle import Paddle
from breakout.player import Player
from breakout.brick import BrickManager
import breakout.resource as resource

class GamePlay(Scene):
    """Main gameplay scene"""
    def __init__(self, RES):
        """Initialize the scene"""
        self.RES = RES
        self.next_scene = self
        self.background, self.bg_rect = resource.load_image('brickwall.png')
        self.player = Player(self.RES, 'player1', 0) 
        self.paddle = Paddle(self.RES)
        self.ball = Ball(self.RES, self.paddle, self.player)
        self.bricks = BrickManager(self.RES, self.player)
        self.sprites = pygame.sprite.Group(self.paddle, self.player.score)
  
        self.bricks.fillDisplay() #place bricks
        self.draw_rects = (self.ball.draw_rect, self.paddle.draw_rect, self.player.score.draw_rect) #list of rects to update

        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
        pygame.mouse.set_visible(False) #make mouse invisible while playing the game


    def render(self, screen):
        """Render the Scene"""
        self.bricks.draw(screen) #draw sprites
        self.sprites.draw(screen) 


    def update(self):
        """Update the Scene"""
        self.bricks.update(self.bricks, self.ball) #update sprites
        self.ball.update(lambda: self.goto(Lose(self.RES)))
        self.sprites.update()
            
        if not self.bricks.sprites(): #check if all bricks are destroyed
            self.goto(Win(self.RES))

        #pygame.display.update(self.draw_rects)
        pygame.display.update()


    def handle_events(self):
        """Handle Events"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.paddle.direction = 'left'
                elif event.key == K_RIGHT:
                    self.paddle.direction = 'right'
                elif event.key == K_p:
                    self.goto(Pause(self.RES, self))
                elif event.key == K_ESCAPE:
                    self.goto(Lose(self.RES))
                elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.paddle.direction = ''
                    elif event.key == K_RIGHT:
                        self.paddle.direction = ''
                    elif event.key == K_p:
                        paused = False
    

    def goto(self, scene):
        """change the scene"""
        self.next_scene = scene


    def terminate(self):
        """End the scene"""
        self.goto(None)
