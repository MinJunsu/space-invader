from random import randint

from .base import EnemyBullet


class BlueSpaceShipBullet(EnemyBullet):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 3
        self.set_images('blue_spaceship_bullet')
        self.set_sound('blue_spaceship_bullet.wav')


class RedSpaceShipBullet(EnemyBullet):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 5
        self.set_images('red_spaceship_bullet')
        self.set_sound('red_spaceship_bullet.wav')


class GreenSpaceShipBullet(EnemyBullet):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 7
        self.set_images('green_spaceship_bullet')
        self.set_sound('green_spaceship_bullet.wav')


class CircledSpaceShipBullet(EnemyBullet):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 7
        self.set_images('circled_spaceship_bullet')
        self.set_sound('boss_spaceship_bullet.wav')
