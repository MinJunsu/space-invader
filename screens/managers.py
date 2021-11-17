from .loading import LoadingScreen
from .gmae import GameScreen

WIDTH = 640
HEIGHT = 480


class ScreenManager:
    def __init__(self):
        self.screen = None
        self.initialize()

    def run(self):
        self.screen.run()

    def push(self, key):
        self.screen.get_event(key)

    def initialize(self):
        self.screen = LoadingScreen((WIDTH, HEIGHT), self.set_screen)

    def set_screen(self, num):
        if num == 0:
            self.screen = LoadingScreen((WIDTH, HEIGHT), self.set_screen)

        elif num == 1:
            self.screen = GameScreen((WIDTH, HEIGHT), self.set_screen)
