#!/usr/bin/python3

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
      py_modules=['run',
                  'game',
                  'menu',
                  'brick',
                  'ball',
                  'paddle',
                  'player',
                  'colors'
                 ],
      data_files=['Images/ball.png',
                  'Images/brick.png',
                  'Images/paddle.png',
                  'Images/brickwall.png'
                 ]
     )
