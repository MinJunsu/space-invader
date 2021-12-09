<<<<<<< HEAD
from pygame.key import get_pressed
from pygame.constants import K_LEFT, K_RIGHT, K_SPACE
from pygame.sprite import Group

from .base import Player
from .bullets import PlaneBullet
=======
from .base import Player
from .bullets import PlaneBullet, SpaceShipBullet
>>>>>>> 7de83ecefb57547b9e44c2e11a6d87651059fb1d

WEIGHT = 640
HEIGHT = 480


class PlanePlayer(Player):
<<<<<<< HEAD
    COOLDOWN = 20

    def __init__(self, health_point, score):
        super(PlanePlayer, self).__init__(health_point, score)
=======
    COOLDOWN = 50

    def __init__(self, health_point, score):
        super().__init__(health_point, score)
>>>>>>> 7de83ecefb57547b9e44c2e11a6d87651059fb1d
        self.speed = 10
        self.weapon = PlaneBullet
        self.is_horizontal_move = True
        self.set_images('plane')


class SpaceShipPlayer(Player):
<<<<<<< HEAD
    COOLDOWN = 15

    def __init__(self, health_point, score):
        super(SpaceShipPlayer, self).__init__(health_point, score)
        self.speed = 15
        self.weapon = PlaneBullet
=======
    COOLDOWN = 45

    def __init__(self, health_point, score):
        super().__init__(health_point, score)
        self.speed = 15
        self.weapon = SpaceShipBullet
>>>>>>> 7de83ecefb57547b9e44c2e11a6d87651059fb1d
        self.is_horizontal_move = True
        self.set_images('spaceship')
