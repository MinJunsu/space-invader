from pygame.key import get_pressed
from pygame.constants import K_LEFT, K_RIGHT, K_SPACE
from pygame.sprite import Group

from .base import Player
from .bullets import PlaneBullet

WEIGHT = 640
HEIGHT = 480


class PlanePlayer(Player):
    COOLDOWN = 20

    def __init__(self, health_point):
        super(PlanePlayer, self).__init__(health_point)
        self.speed = 10
        self.weapon = PlaneBullet
        self.is_horizontal_move = True
        self.set_images('plane')


class SpaceShipPlayer(Player):
    COOLDOWN = 15

    def __init__(self, health_point):
        super(SpaceShipPlayer, self).__init__(health_point)
        self.speed = 15
        self.weapon = PlaneBullet
        self.is_horizontal_move = True
        self.set_images('spaceship')
