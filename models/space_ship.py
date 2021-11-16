from random import randint
from pygame.sprite import Group

from .base import Enemy
from .explosions import BirdExplosion
from .bullets import BlueSpaceShipBullet, RedSpaceShipBullet, GreenSpaceShipBullet


class SpaceShip(Enemy):
    COOLDOWN = 100

    def __init__(self, pos_x, pos_y):
        super(SpaceShip, self).__init__('spaceships')
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health_point = 1
        self.explosion = BirdExplosion
        self.weapon = None
        self.weapons = Group()
        self.cool_down_counter = 0

    def update(self, *args, **kwargs) -> None:
        self.cool_down_counter += randint(0, 1)
        self.attack()
        super(SpaceShip, self).update()

    def attack(self) -> None:
        if self.cool_down_counter > self.COOLDOWN:
            self.weapons.add(self.weapon(self.rect.x, self.rect.y))
            self.cool_down_counter = 0


class BlueSpaceShip(SpaceShip):
    DEFAULT_COUNT = 10
    COOLDOWN = 70

    def __init__(self, pos_x, pos_y):
        super(BlueSpaceShip, self).__init__(pos_x, pos_y)
        self.speed = 5
        self.set_images('blue_ship')
        self.weapon = BlueSpaceShipBullet


class RedSpaceShip(SpaceShip):
    DEFAULT_COUNT = 10
    COOLDOWN = 60

    def __init__(self, pos_x, pos_y):
        super(RedSpaceShip, self).__init__(pos_x, pos_y)
        self.speed = 7
        self.set_images('red_ship')
        self.weapon = RedSpaceShipBullet


class GreenSpaceShip(SpaceShip):
    DEFAULT_COUNT = 15
    COOLDOWN = 50

    def __init__(self, pos_x, pos_y):
        super(GreenSpaceShip, self).__init__(pos_x, pos_y)
        self.speed = 8
        self.set_images('green_ship')
        self.weapon = GreenSpaceShipBullet
