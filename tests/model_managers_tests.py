from unittest import TestCase

from pygame import mixer

from models.managers import PlayerManager, EnemyManager, BackGroundManager
from pygame.sprite import Group, GroupSingle
from models.player.players import PlanePlayer, SpaceShipPlayer

mixer.pre_init(44100, -16, 2, 512)


class ManagerTest(TestCase):
    def setUp(self) -> None:
        self.playerManager = PlayerManager()
        self.enemyManager = EnemyManager()
        self.backgroundManager = BackGroundManager()

    def test_playerManager_attribute(self):
        self.assertEqual(self.playerManager.level, 0)
        self.assertIsInstance(self.playerManager.character, GroupSingle)
        self.assertEqual(self.playerManager.health_point, 5)
        self.assertEqual(self.playerManager.score, 0)

    def test_enemymanager_attribute(self):
        self.assertEqual(self.enemyManager.level, 0)
        self.assertIsInstance(self.enemyManager.enemy, Group)
        self.assertIsInstance(self.enemyManager.collision, Group)

    def test_backgroundmanager_attribute(self):
        self.assertIsInstance(self.backgroundManager.background, GroupSingle)
        self.assertEqual(self.backgroundManager.level, 0)

    def test_playermanager_upgrade(self):
        before_level = self.playerManager.level
        self.playerManager.upgrade()
        after_level = self.playerManager.level
        self.assertEqual(1, after_level - before_level)

        if self.playerManager.level == 1:
            self.assertEqual(type(self.playerManager.character.sprite), type(PlanePlayer(0,0)))

        elif self.playerManager.level == 2:
            self.assertEqual(type(self.playerManager.character.sprite), type(SpaceShipPlayer(0,0)))

        '''
        # 3 스테이지 플레이어가 결정되면 추가
        elif self.playerManager.level == 3:
            self.assertEqual(type(self.playerManager.character.sprite), type(Other(0, 0)))
        '''

    def test_enemymanager_upgrade(self):
        before_level = self.enemyManager.level
        self.enemyManager.upgrade()
        after_level = self.enemyManager.level
        self.assertEqual(1, after_level - before_level)

    def test_enemymanager_is_empty(self):
        for enemy in self.enemyManager.enemy.sprites():
            enemy.kill()
        self.assertTrue(self.enemyManager.is_empty())

    def test_backgroundmanager_upgrade(self):
        before_level = self.backgroundManager.level
        before_background = self.backgroundManager.background.sprite
        self.backgroundManager.upgrade()
        after_level = self.backgroundManager.level

        self.assertEqual(1, after_level - before_level)

        after_background = self.backgroundManager.background.sprite
        self.assertNotEqual(before_background, after_background)