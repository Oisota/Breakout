"""
Game Module

This module defines a run function. The run function
initializes pygame, sets some game variables and runs 
the game.
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import sys

class Editor(tk.Frame):
    """Main level editor frame."""
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.level_filename = ''
        self.level_name = tk.StringVar()
        self.ball_speed = tk.StringVar()
        self.next_level = tk.StringVar()
        self.parent.geometry('800x600')
        self.parent.title('Breakout Level Editor')
        self.grid()
        self.create_widgets()
        self.pack_widgets()


    def create_widgets(self):
        """Create editor frame widgets."""
        #create file menu
        self.menu = tk.Menu(self.parent)
        self.parent.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.file_menu.add_command(label='Save', command=self.save_level)
        self.file_menu.add_command(label='Open', command=self.open_level)
        self.file_menu.add_command(label='Exit', command=self.quit)
        self.menu.add_cascade(label='File', menu=self.file_menu)

        self.lvl_nm_lbl = tk.Label(self, text='Level Name: ')
        self.ball_spd_lbl = tk.Label(self, text='Ball Speed: ')
        self.nxt_lvl_lbl = tk.Label(self, text='Next Level: ')


        self.lvl_nm_tb = tk.Entry(self, textvariable=self.level_name)
        self.ball_spd_tb = tk.Entry(self, textvariable=self.ball_speed)
        self.nxt_lvl_tb = tk.Entry(self, textvariable=self.next_level)


    def pack_widgets(self):
        """Pack widgets into the frame."""
        self.lvl_nm_lbl.grid(row=0, column=0, sticky='E')
        self.ball_spd_lbl.grid(row=1, column=0, sticky='E')
        self.nxt_lvl_lbl.grid(row=2, column=0, sticky='E')
        
        self.lvl_nm_tb.grid(row=0, column=1, sticky='W')
        self.ball_spd_tb.grid(row=1, column=1, sticky='W')
        self.nxt_lvl_tb.grid(row=2, column=1, sticky='W')


    def save_level(self):
        """Save the level file."""
        self.level_filename = asksaveasfilename()
        
        
    def open_level(self):
        """Open the level file."""
        self.level_filename = askopenfilename()


    def quit(self):
        """Exit the editor."""
        sys.exit()




def run():
    """Run the Editor.""" 
    root = tk.Tk()
    editor = Editor(root)
    editor.mainloop()
