import unittest

from breakout.utils.constants import BRICK_IMAGES, START_LEVEL
from breakout.utils.resource import load_level

class TestLoadLevel(unittest.TestCase):

    def test_level_contains_correct_keys(self):
        self.assertIn('name', self.level.keys())
        self.assertIn('ball_speed', self.level.keys())
        self.assertIn('next', self.level.keys())
        self.assertIn('bricks', self.level.keys())


    def test_brick_array_length(self):
        self.assertEqual(10, len(self.level['bricks']))
        for row in self.level['bricks']:
            self.assertEqual(10, len(row))


    def test_brick_colors(self):
        for row in self.level['bricks']:
            for color in row:
                self.assertIn(color, BRICK_IMAGES.keys())


    def setUp(self):
        self.level = load_level(START_LEVEL)


    def tearDown(self):
        self.level = None



class TestLoadImage(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
