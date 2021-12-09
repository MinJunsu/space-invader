from utils import Singleton


class GameTick(Singleton):
    def __init__(self):
        super().__init__()
        try:
            self.tick = self.instance.tick
        except AttributeError:
            self.instance.tick = 60
        finally:
            self.tick = self.instance.tick

    def up(self):
        self.tick += 5
        if self.tick > 100:
            self.tick = 100
        self.instance.tick = self.tick

    def down(self):
        self.tick -= 5
        if self.tick < 30:
            self.tick = 30
        self.instance.tick = self.tick

    def get(self):
        return self.tick
