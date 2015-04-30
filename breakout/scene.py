from abc import ABCMeta, abstractmethod

class Scene(object, metaclass=ABCMeta):
    """Abstract Base class for game scenes"""
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

    @abstractmethod
    def goto(self, scene):
        """switch scenes"""
        pass

    @abstractmethod
    def terminate(self):
        """End the scene"""
        pass
