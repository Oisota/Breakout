"""
Editor Module

This module defines the Editor class. This module runs
the game's level editor.
"""

import sys, os
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

import breakout.utils.resource as resource
from breakout.utils.constants import START_LEVEL
from breakout.editor.brick import BrickFrame
from breakout.editor.entry import EntryFrame


class Editor(tk.Frame):
    """Main level editor frame."""
    def __init__(self, parent):
        """Initialize the editor."""
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.level_filename = START_LEVEL
        self.level = resource.load_level(self.level_filename)

        self.grid()
        self.create_widgets()
        self.grid_widgets()


    def create_widgets(self):
        """Create editor frame widgets."""
        #create file menu
        self.menu = tk.Menu(self.parent)
        self.parent.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.file_menu.add_command(label='New', command=self.new_level)
        self.file_menu.add_command(label='Save', command=self.save_level)
        self.file_menu.add_command(label='Open', command=self.open_level)
        self.file_menu.add_command(label='Exit', command=self.quit)
        self.menu.add_cascade(label='File', menu=self.file_menu)

        #create input boxes
        #move to separate class/file
        self.entry_frame = EntryFrame(self, self.level)

        #create brick button grid
        self.brick_frame = BrickFrame(self, self.level['bricks'], self.entry_frame.color_option)


    def grid_widgets(self):
        """position widgets in the frame."""
        self.brick_frame.grid(row=0, column=0)
        self.brick_frame['pady'] = 35
        self.brick_frame['padx'] = 10
        self.entry_frame.grid(row=1, column=0)


    def save_level(self):
        """Save the level file."""
        self.level_filename = asksaveasfilename()

        level = {}
        level.update({'name': self.entry_frame.level_name.get()})
        level.update({'ball_speed': self.entry_frame.ball_speed.get()})
        level.update({'next': self.entry_frame.next_level.get()})
        level.update({'bricks': self.brick_frame.get_layout()})

        resource.save_level(level, self.level_filename)
        
        
    def open_level(self):
        """Open the level file."""
        self.level_filename = askopenfilename()
        self.level = resource.load_level(os.path.basename(self.level_filename))
        self.brick_frame.update(self.level['bricks'])
        self.entry_frame.update(self.level)


    def new_level(self):
        """Create a blank level."""
        pass


    def quit(self):
        """Exit the editor."""
        sys.exit()



def run():
    """Run the Editor.""" 
    root = tk.Tk()
    root.geometry('800x600')
    root.title('Breakout Level Editor')
    editor = Editor(root)
    editor.mainloop()
