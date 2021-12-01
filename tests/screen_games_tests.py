from unittest import TestCase

from models.managers import PlayerManager, EnemyManager, BackGroundManager
from screens.managers import ScreenManager

import pygame


class GameScreenTest(TestCase):
    def setUp(self) -> None:
        pygame.init()
        pygame.font.init()
        self.screen_manager = ScreenManager()
        self.screen_manager.set_screen('game')
        self.game_screen = self.screen_manager.screen

    def test_game_screen_attribute(self):
        self.assertEqual(self.game_screen.get_width(), 640)
        self.assertEqual(self.game_screen.get_height(), 480)
        self.assertEqual(self.game_screen.level, 0)
        self.assertIsInstance(self.game_screen.player, PlayerManager)
        self.assertIsInstance(self.game_screen.enemies, EnemyManager)
        self.assertIsInstance(self.game_screen.background, BackGroundManager)

    # def test_game_screen_level_update(self):
    #     before_game_screen_level = self.game_screen.level
    #     self.game_screen.enemies.enemy.empty()
    #     self.game_screen.run()
    #     after_game_screen_level = self.game_screen.level
    #     self.assertEqual(before_game_screen_level + 1, after_game_screen_level)


