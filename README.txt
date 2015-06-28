Breakout 
========

Author: Derek Morey 

Description: A simple breakout clone that I made for myself in order to
teach myself about python, pygame, and game development.

Controls: 
- use mouse to click on menu buttons
- left arrow: moves paddle left
- right arrow: moves paddle right
- hold p: pauses the game
- esc: quits to main menu

Installation
------------
Download the zip file and extract the contents. From the game
directory, execute breakout.py on the command line to run the
game. Note that this game requires pyhon 3 and pygame to be
installed.

Level Customization
-------------------
Custom levels can be added to the game by adding properly formatted
xml files to the breakout/resources/levels/ directory. The levels files
must be formatted like the provided level files. The level progression
relies on each level file having the name of the next level inside
the 'next' tags. Note that the 'name' and 'difficulty' tags currently
do not have an affect on gameplay.
