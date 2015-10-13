import tkinter as tk

class EntryFrame(tk.Frame):
    """Frame containing level attribute entry boxes"""
    def __init__(self, parent, level):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.level = level

        self.level_name = tk.StringVar()
        self.ball_speed = tk.StringVar()
        self.next_level = tk.StringVar() #should be dropdown of available level files

        self.level_name.set(self.level['name'])
        self.ball_speed.set(self.level['ball_speed'])
        self.next_level.set(self.level['next'])

        self.create_widgets()
        self.grid_widgets()


    def create_widgets(self):
        """Create frame widgets"""
        self.level_name_label = tk.Label(self, text='Level Name: ')
        self.ball_speed_label = tk.Label(self, text='Ball Speed: ')
        self.next_level_label = tk.Label(self, text='Next Level: ')

        self.level_name_entry = tk.Entry(self, textvariable=self.level_name)
        self.ball_speed_entry = tk.Entry(self, textvariable=self.ball_speed)
        self.next_level_entry = tk.Entry(self, textvariable=self.next_level)


    def grid_widgets(self):
        """Postition frame widgets"""
        self.level_name_label.grid(row=0, column=0, sticky='E')
        self.ball_speed_label.grid(row=1, column=0, sticky='E')
        self.next_level_label.grid(row=2, column=0, sticky='E')
        
        self.level_name_entry.grid(row=0, column=1, sticky='W')
        self.ball_speed_entry.grid(row=1, column=1, sticky='W')
        self.next_level_entry.grid(row=2, column=1, sticky='W')
