from models import Explosion
from engine.sound import SoundManager


class BirdExplosion(Explosion):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.set_images('birds')
        self.set_sound('birds_death.wav')


class SpaceShipExplosion(Explosion):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.set_images('birds')
        self.set_sound('spaceships_death.wav')


class AlienExplosion(Explosion):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.set_images('aliens')
        self.set_sound('aliens_death.wav')
