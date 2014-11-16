
#This file is used to make a distribution of the game using distutils. 

from distutils.core import setup

setup(name='Breakout',
      version='1.0',
      description='A remake of the classic aracade game',
      author='Derek Morey',
      author_email='dman6505@gmail.com',
      url='none',
      license='GPL',
      long_description="""This is a remake of the classic game Breakout. I made 
                          this game for the sole purpose of educating myself about
                          python, pygame, and game development in general. Feel free 
                          to use or modify my code in any way.""",
      download_url='https://github.com/Oisota/Breakout',
      py_modules=['breakout/run',
                  'breakout/game',
                  'breakout/menu',
                  'breakout/brick',
                  'breakout/ball',
                  'breakout/paddle',
                  'breakout/player',
                  'breakout/colors'
                 ],
      data_files=['breakout/Images/ball.png',
                  'breakout/Images/brick.png',
                  'breakout/Images/paddle.png',
                  'breakout/Images/brickwall.png',
                  'breakout/Images/breakout.png',
                  'breakout/Images/lose.png',
                  'breakout/Images/win.png',
                  'breakout/Images/start.png',
                  'breakout/Images/start_pressed.png',
                  'breakout/Images/quit.png',
                  'breakout/Images/quit_pressed.png',
                  'breakout/Images/retry.png',
                  'breakout/Images/retry_pressed.png',
                  'breakout/files/breakout.desktop'
                 ],
     classifiers=[]
     )
