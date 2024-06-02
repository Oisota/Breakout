from argparse import ArgumentParser

from breakout.game import run as run_game
from breakout.editor import run as run_editor

if __name__ == '__main__':
    parser = ArgumentParser(
        prog='Breakout',
        description='Clone of breakout game in python using pygame'
    )
    parser.add_argument('-e', '--editor', action='store_true', help='launch the level editor')
    args = parser.parse_args()

    if args.editor:
        run_editor()
    else:
        run_game()