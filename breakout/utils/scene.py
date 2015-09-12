"""
Scene Module
"""

from abc import ABCMeta, abstractmethod

class Scene(metaclass=ABCMeta):
    """Base class for game scenes."""
    def __init__(self):
        """Initialize the scene."""
        self.next_scene = self

    @abstractmethod
    def render(self):
        """Render the scene."""
        pass

    @abstractmethod
    def update(self):
        """Update the scene."""
        pass

    @abstractmethod
    def handle_events(self):
        """Handle user input events."""
        pass

    def goto(self, scene):
        """Switch scenes."""
        self.next_scene = scene
