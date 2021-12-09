from screens.loading.base import LoadingScreen
from screens.loading.help import HelpScreen
from screens.games.base import GameScreen
from screens.loading.setting import SettingScreen
from screens.loading.summary import SummaryScreen
from screens.games.explain import ExplainScreen
from screens.loading.score import ScoreScreen

SCREEN = {
    'main': LoadingScreen,
    'game': GameScreen,
    'help': HelpScreen,
    'setting': SettingScreen,
    'explain': ExplainScreen,
    'summary': SummaryScreen,
    'score': ScoreScreen
}


WIDTH = 640
HEIGHT = 480


class ScreenManager:
    def __init__(self):
        self.screen = None
        self.initialize()
        self.before_screen = None

    def run(self):
        self.screen.run()

    def push(self, event):
        self.screen.get_event(event)

    def initialize(self):
        self.screen = LoadingScreen((WIDTH, HEIGHT), self.set_screen, self.return_screen)

    def set_screen(self, action):
        self.before_screen = self.screen
        if action != 'explain':
            self.screen = SCREEN.get(action)((WIDTH, HEIGHT), self.set_screen, self.return_screen)
        else:
            category = 'begin' if self.screen.player.health_point != 0 else 'ending'
            num = self.screen.level % 5 + self.screen.level // 5
            self.screen = SCREEN.get(action)((WIDTH, HEIGHT), self.set_screen, self.return_screen, category, num)

    def return_screen(self):
        self.screen = self.before_screen
