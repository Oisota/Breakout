from unittest import TestCase

import pygame

from ..config import BRICK_IMAGES, START_LEVEL, BLIP
from .. import asset

class TestAsset(TestCase):

    def setUp(self):
        pygame.init()

    def test_load_image(self):
        img = asset.load_image(BRICK_IMAGES['red'])
        self.assertTrue(False)

    def test_load_sound(self):
        snd = asset.load(BLIP)
        self.assertTrue(False)

    def test_load_level(self):
        level = asset.load_level(START_LEVEL)
        self.assertIn('name', level)
        self.assertIn('ball_speed', level)
        self.assertIn('next', level)
        self.assertIn('bricks', level)

        self.assertEqual(10, len(level['bricks']))
        for row in level['bricks']:
            self.assertEqual(10, len(row))

        for row in level['bricks']:
            for color in row:
                self.assertIn(color, BRICK_IMAGES)

    def test_save_level(self):
        self.assertTrue(False)

    def tearDown(self):
        pygame.quit()
