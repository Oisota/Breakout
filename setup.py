"""
Setup Module

This module is used to make a distribution of 
the game using distutils.
"""

from distutils.core import setup

setup( 
              name = 'Breakout',
           version = '1.0',
       description = 'A remake of the classic video game',
            author = 'Derek Morey',
      author_email = 'dman6505@gmail.com',
           license = 'GPL',
               url = 'https://github.com/Oisota/Breakout',
      download_url = 'https://github.com/Oisota/Breakout/archive/master.zip',
          keywords = ['breakout', 'arcade', 'game', 'pygame', 'python',],
         platforms = ['linux', 'windows'],
           scripts = ['breakout.py'],
          packages = ['breakout'],
      #package_data = {'breakout':['resources/images/*.png',
                                  #'resources/sounds/*.wav']},
        data_files = [('resources/images', ['resources/images/*.png']),
                      ('resources/sounds', ['resources/sounds/*.wav'])],
          requires = ['sys', 'os', 'random', 'pygame'],
       classifiers = ['Programming Language :: Python',
                      'Programming Language :: Python :: 3',
                      'Development Status :: 3 - Alpha',
                      'Environment :: Other Environment',
                      'Framework :: Pygame',
                      'Intended Audience :: End Users/Desktop',
                      'Intended Audience :: Developers',
                      'Intended Audience :: Education',
                      'License :: OSI Approved :: GNU General Public License (GPL)',
                      'Natural Language :: English',
                      'Operating System :: OS Independent',
                      'Topic :: Games/Entertainment',
                      'Topic :: Games/Entertainment :: Arcade'],
  long_description =
"""
Breakout
--------
This is a remake of the classic game Breakout. I made this game for the sole 
purpose of educating myself about python, pygame, and game development in general. 
Feel free use or modify my code in any way.
"""
)
