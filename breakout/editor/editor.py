"""
Game Module

This module defines the Editor class. This module runs
the game's level editor.
"""

import sys, os
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

from breakout.utils.resource import load_level, save_level


class Editor(tk.Frame):
    """Main level editor frame."""
    def __init__(self, parent=None):
        """Initialize the editor."""
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.level_filename = ''
        self.brick_img = tk.PhotoImage(file='breakout/resources/images/brick_red.gif')
        self.level_name = tk.StringVar()
        self.ball_speed = tk.StringVar()
        self.next_level = tk.StringVar()
        self.grid()
        self.create_widgets()
        self.grid_widgets()


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

        #create input boxes
        self.input_frm = tk.Frame(self)
        self.lvl_nm_lbl = tk.Label(self.input_frm, text='Level Name: ')
        self.ball_spd_lbl = tk.Label(self.input_frm, text='Ball Speed: ')
        self.nxt_lvl_lbl = tk.Label(self.input_frm, text='Next Level: ')

        self.lvl_nm_tb = tk.Entry(self.input_frm, textvariable=self.level_name)
        self.ball_spd_tb = tk.Entry(self.input_frm, textvariable=self.ball_speed)
        self.nxt_lvl_tb = tk.Entry(self.input_frm, textvariable=self.next_level)

        #create button grid
        #TODO put button frame in separate class
        self.button_frm = tk.Frame(self)
        self.buttons = []
        for i in range(10):
            btn_row = []
            for j in range(10):
                button = tk.Button(self.button_frm, image=self.brick_img, width=72, height=27)
                btn_row.append(button)

            self.buttons.append(btn_row)



    def grid_widgets(self):
        """position widgets in the frame."""
        #place buttons
        self.button_frm.grid(row=0, column=0)
        self.button_frm['pady'] = 35
        self.button_frm['padx'] = 10
        for i, row in enumerate(self.buttons):
            for j, btn in enumerate(row):
                btn.grid(row=i, column=j)

        self.input_frm.grid(row=1, column=0)
        self.lvl_nm_lbl.grid(row=0, column=0, sticky='E')
        self.ball_spd_lbl.grid(row=1, column=0, sticky='E')
        self.nxt_lvl_lbl.grid(row=2, column=0, sticky='E')
        
        self.lvl_nm_tb.grid(row=0, column=1, sticky='W')
        self.ball_spd_tb.grid(row=1, column=1, sticky='W')
        self.nxt_lvl_tb.grid(row=2, column=1, sticky='W')


    def save_level(self):
        """Save the level file."""
        self.level_filename = asksaveasfilename()
        resource.save_level(self.level_filename)
        
        
    def open_level(self):
        """Open the level file."""
        self.level_filename = askopenfilename()
        if self.level_filename != '':
            self.level = load_level(os.path.basename(self.level_filename))


    def quit(self):
        """Exit the editor."""
        sys.exit()



class ButtonGrid(tk.Frame):
    """Frame that contains grid of brick buttons"""
    def __init__(self, parent=None):
        """Initialze the button grid"""
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.create_widgets()
        self.grid_widgets()


    def create_widgets(self):
        """create grid of buttons"""
        pass


    def grid_widgets(self):
        """Position buttons."""
        pass
        



def run():
    """Run the Editor.""" 
    root = tk.Tk()
    root.geometry('800x600')
    root.title('Breakout Level Editor')
    editor = Editor(root)
    editor.mainloop()
