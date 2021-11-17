from random import choice, randint

from pygame.sprite import Group

from .base import Enemy
from .explosions import BirdExplosion


class Bird(Enemy):
    DEFAULT_COUNT = 0

    def __init__(self, pos_x, pos_y):
        super(Bird, self).__init__('birds')
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health_point = 1
        self.explosion = BirdExplosion
        self.is_reverse = True


class SmileBird(Bird):
    DEFAULT_COUNT = 5

    def __init__(self, pos_x, pos_y):
        super(SmileBird, self).__init__(pos_x, pos_y)
        self.speed = 4
        self.set_images('smile_bird')
        self.score = 10


class PoisonedBird(Bird):
    DEFAULT_COUNT = 8

    def __init__(self, pos_x, pos_y):
        super(PoisonedBird, self).__init__(pos_x, pos_y)
        self.speed = 6
        self.set_images('poisoned_bird')
        self.score = 30


class CircledBird(Bird):
    DEFAULT_COUNT = 10

    def __init__(self, pos_x, pos_y):
        super(CircledBird, self).__init__(pos_x, pos_y)
        self.speed = 6
        self.set_images('circled_bird')
        self.score = 50


class OldBird(Bird):
    DEFAULT_COUNT = 15

    def __init__(self, pos_x, pos_y):
        super(OldBird, self).__init__(pos_x, pos_y)
        self.speed = 2
        self.set_images('old_bird')
        self.score = 60


class CrazyBird(Bird):
    DEFAULT_COUNT = 1
    COOLDOWN = 500

    def __init__(self, pos_x, pos_y):
        super(CrazyBird, self).__init__(pos_x, pos_y)
        self.speed = 8
        self.health_point = 15
        self.set_images('crazy_bird')
        self.birds = [SmileBird, PoisonedBird, CircledBird, OldBird]
        self.children = Group()
        self.is_boss = True
        self.coll_down_count = 0
        self.score = 500

    def create_birds(self) -> None:
        base_pos_x = randint(0, 640)
        base_pos_y = self.rect.y + self.image.get_height() + randint(30, 50)
        self.children.add(choice(self.birds)(base_pos_x, base_pos_y))

    def update(self, *args, **kwargs) -> None:
        self.coll_down_count += 1
        super(CrazyBird, self).update()
        self.children.update()

    def move(self) -> None:
        if 0 > self.rect.x or 640 - self.image.get_width() < self.rect.x:
            self.speed *= -1
        self.rect.x += self.speed
