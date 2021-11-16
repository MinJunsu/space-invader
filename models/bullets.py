from os.path import join
from random import randint

from pygame.mixer import Sound

from models.base import Entity


class Bullet(Entity):
    def __init__(self, pos_x, pos_y):
        super(Bullet, self).__init__('bullets')
        self.pos_x = pos_x
        self.pos_y = pos_y

    def set_sound(self, name):
        super(Bullet, self).set_sound(name)
        self.sound.play()


class PlayerBullet(Bullet):
    def __init__(self, pos_x, pos_y):
        super(PlayerBullet, self).__init__(pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self) -> None:
        self.rect.y -= self.speed


class EnemyBullet(Bullet):
    def __init__(self, pos_x, pos_y):
        super(EnemyBullet, self).__init__(pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self) -> None:
        self.rect.y += randint(1, self.speed)


class PlaneBullet(PlayerBullet):
    def __init__(self, pos_x, pos_y):
        super(PlaneBullet, self).__init__(pos_x, pos_y)
        self.set_images('plane_bullet')
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.set_sound('plane_bullet.wav')


class BlueSpaceShipBullet(EnemyBullet):
    def __init__(self, pos_x, pos_y):
        super(BlueSpaceShipBullet, self).__init__(pos_x, pos_y)
        self.speed = 3
        self.set_images('blue_spaceship_bullet')
        self.set_sound('blue_spaceship.wav')


class RedSpaceShipBullet(EnemyBullet):
    def __init__(self, pos_x, pos_y):
        super(RedSpaceShipBullet, self).__init__(pos_x, pos_y)
        self.speed = 5
        self.set_images('red_spaceship_bullet')
        self.set_sound('red_spaceship.wav')


class GreenSpaceShipBullet(EnemyBullet):
    def __init__(self, pos_x, pos_y):
        super(GreenSpaceShipBullet, self).__init__(pos_x, pos_y)
        self.speed = 7
        self.set_images('green_spaceship_bullet')
        self.set_sound('green_spaceship.wav')
