from pygame.key import get_pressed
from pygame.constants import K_LEFT, K_RIGHT, K_SPACE
from pygame.sprite import Group

from .base import Player
from .bullets import PlaneBullet, SpaceShipBullet

WEIGHT = 640
HEIGHT = 480


class PlanePlayer(Player):
    COOLDOWN = 50

    def __init__(self, health_point, score):
        super().__init__(health_point, score)
        self.speed = 10
        self.weapon = PlaneBullet
        self.is_horizontal_move = True
        self.set_images('plane')


class SpaceShipPlayer(Player):
    COOLDOWN = 45

    def __init__(self, health_point, score):
        super().__init__(health_point, score)
        self.speed = 15
        self.weapon = SpaceShipBullet
        self.is_horizontal_move = True
        self.set_images('spaceship')


class AlienPlayer(Player):
    COOLDOWN = 40

    def __init__(self, health_point, score):
        super().__init__(health_point, score)
        self.speed = 18
        self.weapon = SpaceShipBullet
        self.is_horizontal_move = True
        self.set_images('alien')
