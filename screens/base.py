from pathlib import Path
import os

from pygame import Surface
from pygame.font import Font


class Screen(Surface):
    BASE_PATH = Path(__file__).resolve().parent.parent

    def __init__(self, size):
        super(Screen, self).__init__(size)
        self.font = Font(os.path.join(self.BASE_PATH, "assets", "fonts", "edit_undo.ttf"), 50)
        self.sound = None

    def draw(self):
        pass

    def get_event(self, event):
        """
        Implement When you get event in Surface
        """

# class ScreenManager:
#     def __init__(self):
#         self.screen = LoadingScreen()
#         self.player = PlayerManager()
#         self.enemy = EnemyuManager()
#
#     def upgrade(self):
#         self.screen = DescriptScreen(1)
#         if 1 % 5:
#             self.player.upgrade()
#         self.enemy.upgrade()
