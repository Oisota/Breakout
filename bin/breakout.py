#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Run Module

This module imports the game package and runs the game.
"""

if __name__ == '__main__':
    from breakout.game import Game
    game = Game()
    game.start()
