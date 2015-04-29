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
        


class SceneManager(object):
    """Manage the game scenes"""
    def __init__(self):
       pass 
