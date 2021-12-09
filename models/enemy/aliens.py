from random import randint
from pygame.sprite import Group

from .base import Enemy
from .explosions import BirdExplosion, AlienExplosion
from .bullets import AlienBullet


class Alien(Enemy):
    COOLDOWN = 100

    def __init__(self, pos_x, pos_y):
        super().__init__('aliens')
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health_point = 1
        self.explosion = AlienExplosion
        self.weapon = None
        self.weapons = Group()
        self.cool_down_counter = 0

    def update(self, *args, **kwargs) -> None:
        self.cool_down_counter += randint(0, 1)
        self.attack()
        super().update()

    def attack(self) -> None:
        if self.cool_down_counter > self.COOLDOWN:
            self.weapons.add(self.weapon(self.rect.x, self.rect.y))
            self.cool_down_counter = 0


class RedEyeAlien(Alien):
    # DEFAULT_COUNT = 8
    DEFAULT_COUNT = 1
    COOLDOWN = 120

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 8
        self.set_images('red_eye')
        self.weapon = AlienBullet
        self.score = 250


class GreenSomAlien(Alien):
    # DEFAULT_COUNT = 10
    DEFAULT_COUNT = 1
    COOLDOWN = 90

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 5
        self.set_images('green_som')
        self.weapon = AlienBullet
        self.score = 300


class GreenEyeAlien(Alien):
    # DEFAULT_COUNT = 10
    DEFAULT_COUNT = 1
    COOLDOWN = 90

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 10
        self.set_images('green_eye')
        self.weapon = AlienBullet
        self.score = 400


class GreenOctorAlien(Alien):
    # DEFAULT_COUNT = 5
    DEFAULT_COUNT = 1
    COOLDOWN = 60

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 8
        self.set_images('green_octor')
        self.weapon = AlienBullet
        self.score = 500


class BossAlien(Alien):
    DEFAULT_COUNT = 1
    COOLDOWN = 70
    HEALTH_POINT = 30

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.health_point = 30
        self.speed = 5
        self.set_images('green_boss')
        self.weapon = AlienBullet
        self.score = 2000
        self.is_boss = True

    def move(self) -> None:
        if self.rect.x < 0 or 640 - self.image.get_width() < self.rect.x:
            self.speed *= -1
        self.rect.x += self.speed
