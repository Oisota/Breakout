from abc import ABCMeta, abstractmethod

class Scene(metaclass=ABCMeta):
    """Base class for game scenes"""
    @abstractmethod
    def __init__(self):
        """Initialize the scene"""
        pass

    @abstractmethod
    def render(self):
        """Render the Scene"""
        pass

    @abstractmethod
    def update(self):
        """Update the Scene"""
        pass

    @abstractmethod
    def handle_events(self):
        """Handle Events"""
        pass

    def goto(self, scene):
        """switch scenes"""
        self.scene = scene

    def terminate(self):
        """End the scene"""
        self.goto(None) 
        


class SceneManager(object):
    """Manage the game scenes"""
    def __init__(self):
       pass 
