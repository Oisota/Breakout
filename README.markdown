Breakout 
========
A breakout clone that I made in order to teach
myself about python, pygame, and game development.

**Controls:** 
- Use mouse to click on menu buttons
- left arrow: moves paddle left
- right arrow: moves paddle right
- P: pauses the game
- ESC: quits to main menu

### Installation
Download the zip file and extract the contents. From the game
directory, execute breakout.py on the command line to run the
game. Note that this game requires python 3 and pygame to be
installed.

### Level Customization
Custom levels can be added to the game by adding properly formatted
xml files to the breakout/resources/levels/ directory. The levels files
must be formatted like the provided level files. The level progression
relies on each level file having the name of the next level inside
the 'next' tags. Note that the 'name' and 'difficulty' tags currently
do not have an affect on gameplay.

### Screenshots
#### Start Screen
![Start](screenshots/start_scrot.png "Start")
#### Gameplay
![Breakout](screenshots/breakout_scrot.png "Breakout")
