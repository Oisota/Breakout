from scene import Scene
from gameplay import GamePlay

class Pause(Scene):
    """Title scene class"""
    def __init__(self, RES, game_scene):
        self.game_scene = game_scene
        self.allowed_events = [QUIT, KEYDOWN, KEYUP]
        pygame.event.set_allowed(self.allowed_events)
        

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
