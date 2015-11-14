"""
Scene Module

This module defines the Scene class. It  is an abstract 
base class used as a base class for all other game scenes. 
It can not be instantiated itself. It must be subclassed 
instead. The subclasses must then provide implementations 
for every abstract method. This ensures that each scene
will function properly in the main game loop.
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
