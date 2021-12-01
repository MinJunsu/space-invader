from unittest import TestCase

from pygame.constants import K_SPACE, K_UP, K_DOWN, QUIT, KEYDOWN
from screens import LOADING_CONTEXT
from screens.managers import ScreenManager
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
        self.assertEqual(self.loading_screen.index, 0)

    # def test_loading_screen_index_get_event_K_UP(self):
    #     before_loading_screen_index = self.loading_screen.index
    #     up_event = pygame.event.Event(KEYDOWN, key=1073741906)
    #     print(up_event)
    #     # key_test =
    #
    #     # if before_loading_screen_index > 0:
    #     self.loading_screen.get_event(up_event)
    #     after_loading_screen_index = self.loading_screen.index
    #     self.assertEqual(before_loading_screen_index - 1, after_loading_screen_index)
    #
    #     # else:
    #     self.loading_screen.get_event(up_event)
    #     after_loading_screen_index = self.loading_screen.index
    #     self.assertEqual(len(self.context)-1, after_loading_screen_index)
    #
    # def test_loading_screen_index_get_event_K_DOWN(self):
    #     before_loading_screen_index = self.loading_screen.index
    #     down_event = pygame.event.Event(KEYDOWN, key=K_DOWN)
    #     # print(down_event)
    #     # print(self.loading_screen.index)
    #     # test = pygame.key.ScancodeWrapper
    #     # print(test[K_DOWN])
    #     # test[K_DOWN] = 'true'
    #     # if before_loading_screen_index < len(self.context)-1:
    #     # self.loading_screen.get_event.key = down_event
    #     self.loading_screen.get_event(down_event)
    #
    #     # print(self.loading_screen.index)
    #     after_loading_screen_index = self.loading_screen.index
    #     self.assertEqual(before_loading_screen_index + 1, after_loading_screen_index)
    #
    #     # else
    #     self.loading_screen.index = 4
    #     self.loading_screen.get_event(down_event)
    #     after_loading_screen_index = self.loading_screen.index
    #     self.assertEqual(0, after_loading_screen_index)

