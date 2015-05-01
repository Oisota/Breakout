"""
Scene class definition

This module defines the scene class. It is an abstract 
base class used as a base class for all other game 
scenes. It can not be instantiated itself. It must be
subclassed instead. The subclasses must then provide
implementations for every abstract method.
"""

from abc import ABCMeta, abstractmethod

class Scene(object, metaclass=ABCMeta):
    """Base class for game scenes"""
    def __init__(self):
        """Initialize the scene"""
        self.next_scene = self

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
        """Switch scenes"""
        self.next_scene = scene

    def terminate(self):
        """End the scene"""
        self.goto(None)
