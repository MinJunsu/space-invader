from unittest import TestCase

from pygame.constants import K_SPACE, K_UP, K_DOWN, QUIT, KEYDOWN
from screens import LOADING_CONTEXT
from engine.screen import ScreenManager
from screens import LOADING_CONTEXT
import pygame


class LoadingScreenTest(TestCase):
    # context = LOADING_CONTEXT;
    def setUp(self) -> None:
        pygame.init()
        pygame.font.init()
        self.screen_manager = ScreenManager()
        self.screen_manager.set_screen('main')
        self.loading_screen = self.screen_manager.screen

    def test_loading_screen_attribute(self):
        self.assertEqual(self.loading_screen.get_width(), 640)
        self.assertEqual(self.loading_screen.get_height(), 480)
        self.assertEqual(self.loading_screen.index, 1)
