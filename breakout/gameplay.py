from scene import Scene

class GamePlay(Scene):
    """Main gameplay scene"""
    def __init__(self, RES):
        """Initialize the scene"""
        self.RES = RES
        self.player.reset()
        
        self.paddle = Paddle(self.RES)
        self.ball = Ball(self.RES, paddle, self.player)
        self.bricks = BrickManager(self.RES, self.player)
        self.sprites = pygame.sprite.Group(paddle, ball, self.player.score)
  
        self.bricks.fillDisplay() #place bricks
        self.draw_rects = (ball.draw_rect, paddle.draw_rect, self.player.score.draw_rect) #list of rects to update
        self.display.blit(self.background, (0,0)) #blit background to the screen

        bricks.draw(self.display)
        sprites.draw(self.display)
        
        pygame.display.update()
        pygame.time.wait(500)
            
        self.allowed_events = [QUIT, KEYDOWN, KEYUP]
        pygame.event.set_allowed(allowed_events)
        pygame.mouse.set_visible(False) #make mouse invisible while playing the game


    def render(self):
        """Render the Scene"""
        self.bricks.draw(self.display) #draw sprites
        self.sprites.draw(self.display) 


    def update(self):
        """Update the Scene"""
        self.bricks.update(self.bricks, self.ball) #update sprites
        self.sprites.update()
            
        if not bricks.sprites(): #check if all bricks are destroyed
            self.goto(Win(self.RES))
            self.player.alive = False 

        pygame.display.update(draw_rects)


    def handle_events(self):
        """Handle Events"""
        pass
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                paddle.direction = 'left'
            elif event.key == K_RIGHT:
                paddle.direction = 'right'
            elif event.key == K_p:
                self.goto(Pause(self.RES))
            elif event.key == K_ESCAPE:
                self.player.won = False
                self.player.alive = False
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    paddle.direction = ''
                elif event.key == K_RIGHT:
                    paddle.direction = ''
                elif event.key == K_p:
                    paused = False

