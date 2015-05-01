class Scene(object):
    """Base class for game scenes"""
    def __init__(self):
        """Initialize the scene"""
        self.next_scene = self

    def render(self):
        """Render the Scene"""
        raise NotImplementedError

    def update(self):
        """Update the Scene"""
        raise NotImplementedError

    def handle_events(self):
        """Handle Events"""
        raise NotImplementedError

    def goto(self, scene):
        """switch scenes"""
        self.next_scene = scene

    def terminate(self):
        """End the scene"""
        self.goto(None)
