"""
Brick Module
"""

import os
import tkinter as tk

from breakout.utils.constants import BRICK_IMAGES_GIF, IMAGE_PATH


class BrickFrame(tk.Frame):
    """Frame that contains grid of brick buttons"""
    def __init__(self, parent, level):
        """Initialze the button grid"""
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.level = level
        self.buttons = []
        self.create_widgets()
        self.grid_widgets()


    def create_widgets(self):
        """create grid of buttons"""
        bricks = self.level['bricks']
        brick_colors = self.level['brick_colors']

        for row, colors in zip(bricks, brick_colors):
            btn_row = []
            for col, color in zip(row, colors):
                if col == '1':
                    img_path = os.path.join(IMAGE_PATH, BRICK_IMAGES_GIF[color])
                else:
                    img_path = os.path.join(IMAGE_PATH, BRICK_IMAGES_GIF['cell'])

                brick_img = tk.PhotoImage(file=img_path)
                button = tk.Button(self, image=brick_img, width=72, height=27)
                btn_row.append(button)

            self.buttons.append(btn_row)


    def grid_widgets(self):
        """Position buttons."""
        for y, button_row in enumerate(self.buttons):
            for x, button in enumerate(button_row):
                button.grid(row=y, column=x)
