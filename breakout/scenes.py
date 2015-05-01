import pygame, sys
from pygame.locals import *
from breakout.BaseScenes import Scene
from breakout.BaseScenes import MenuScene
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
        self.ball = Ball(self.RES, self.paddle, self.player, lambda: self.goto(Lose(self.RES)))
        self.bricks = BrickManager(self.RES, self.player)
        self.sprites = pygame.sprite.Group(self.ball, self.paddle, self.player.score)
  
        self.bricks.fillDisplay() #place bricks
        self.draw_rects = (self.ball.draw_rect, self.paddle.draw_rect, self.player.score.draw_rect) #list of rects to update

        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
        pygame.mouse.set_visible(False) #make mouse invisible while playing the game


    def render(self, screen):
        """Render the Scene"""
        screen.blit(self.background, (0,0))
        self.bricks.draw(screen)
        self.sprites.draw(screen) 


    def update(self):
        """Update the Scene"""
        self.bricks.update(self.bricks, self.ball) #update sprites
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
    


class Start(MenuScene):
    """Start scene class"""
    def __init__(self, RES):
        MenuScene.__init__(self, RES, 
                'breakout.png','start.png','start_pressed.png','quit.png','quit_pressed.png', 
                lambda: self.goto(GamePlay(RES)), lambda: self.terminate())



class Win(MenuScene):
    """Win scene"""
    def __init__(self, RES):
        """Initialize the scene"""
        MenuScene.__init__(self, RES, 
                'win.png','retry.png','retry_pressed.png','quit.png','quit_pressed.png', 
                lambda: self.goto(GamePlay(RES)), lambda: self.terminate())



class Lose(MenuScene):
    """Win scene"""
    def __init__(self, RES):
        """Initialize the scene"""
        MenuScene.__init__(self, RES, 
                'lose.png','retry.png','retry_pressed.png','quit.png','quit_pressed.png', 
                lambda: self.goto(GamePlay(RES)), lambda: self.terminate())



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
