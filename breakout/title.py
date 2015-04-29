from scene import Scene

class Title(scene.Scene):
    """Title scene class"""
    def __init__(self):
        self.pygame.mouse.set_visible(True)
        self.mouse_pos = (0,0)
        self.pressed = ''

        self.allowed_events = [QUIT, MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN]
        pygame.event.set_allowed(allowed_events)

        self.menu = Menu(self.RES) #construct menu
        self.menu.addTitle(self.RES[0]/2, 100, 'breakout.png') 
        self.menu.addButton(self.RES[0]/2, 200, 'start.png', 'start_pressed.png', self.run)
        self.menu.addButton(self.RES[0]/2, 300, 'quit.png', 'quit_pressed.png', self.quit)
        

    def render(self, screen):
        """Render the Title scene"""
        screen.blit(self.background, (0,0))
        self.menu.draw(screen)
        pygame.display.update()

        
    def update(self):
        """Update the Title scene"""
        self.display.blit(self.background, (0,0))
        self.menu.draw(self.display)
        self.menu.update(mouse_pos, pressed)
        pygame.display.update(self.menu.rects)


    def handle_events(self):
        """handle user input events"""
        for event in pygame.event.get():
            if event.type == QUIT:
                game.quit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                pressed = 'mouse ' + str(event.button)
            elif event.type == MOUSEMOTION:
                mouse_pos = event.pos
         
        
