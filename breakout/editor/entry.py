import tkinter as tk

from breakout.utils.constants import BRICK_IMAGES

class EntryFrame(tk.Frame):
    """Frame containing level attribute entry boxes"""
    def __init__(self, parent, level):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.level = level
        self.colors = sorted(BRICK_IMAGES.keys())

        self.level_name = tk.StringVar()
        self.ball_speed = tk.StringVar()
        self.next_level = tk.StringVar()
        self.color_option = tk.StringVar()

        self.level_name.set(self.level['name'])
        self.ball_speed.set(self.level['ball_speed'])
        self.next_level.set(self.level['next'])
        self.color_option.set(self.colors[0])

        self.create_widgets()
        self.grid_widgets()


    def create_widgets(self):
        """Create frame widgets"""
        self.level_name_label = tk.Label(self, text='Level Name: ')
        self.ball_speed_label = tk.Label(self, text='Ball Speed: ')
        self.next_level_label = tk.Label(self, text='Next Level: ')
        self.color_label = tk.Label(self, text='Brick Color:')

        self.level_name_entry = tk.Entry(self, textvariable=self.level_name)
        self.ball_speed_entry = tk.Entry(self, textvariable=self.ball_speed)
        self.next_level_entry = tk.Entry(self, textvariable=self.next_level)

        self.color_dropdown = tk.OptionMenu(self, self.color_option, *self.colors)


    def grid_widgets(self):
        """Postition frame widgets"""
        self.color_label.grid(row=0, column=0, stick='W', padx=50)
        self.color_dropdown.grid(row=1, column=0, sticky='W', padx=50)

        self.level_name_label.grid(row=0, column=1, sticky='E')
        self.ball_speed_label.grid(row=1, column=1, sticky='E')
        self.next_level_label.grid(row=2, column=1, sticky='E')
        
        self.level_name_entry.grid(row=0, column=2, sticky='W')
        self.ball_speed_entry.grid(row=1, column=2, sticky='W')
        self.next_level_entry.grid(row=2, column=2, sticky='W')


    def update(self, level):
        """Update the frame with new level info."""
        self.level = level
        self.level_name.set(self.level['name'])
        self.ball_speed.set(self.level['ball_speed'])
        self.next_level.set(self.level['next'])
