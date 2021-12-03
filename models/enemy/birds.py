from random import choice, randint
import os

from pygame.sprite import Group
from pygame import image

from .base import Enemy
from .explosions import BirdExplosion


class Bird(Enemy):
    DEFAULT_COUNT = 0

    def __init__(self, pos_x, pos_y):
        super().__init__('birds')
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health_point = 1
        self.explosion = BirdExplosion
        self.is_reverse = True

    def set_images(self, image_path) -> None:
        if self.is_reverse:
            os.chdir(os.path.join(self.IMAGE_ROOT, os.path.join(self.name, f'{image_path}_left')))
            self.lefts = [image.load(element) for element in sorted(os.listdir())]
            os.chdir(os.path.join(self.IMAGE_ROOT, os.path.join(self.name, f'{image_path}_right')))
            self.rights = [image.load(element) for element in sorted(os.listdir())]
            self.images = self.rights
        else:
            os.chdir(os.path.join(self.IMAGE_ROOT, os.path.join(self.name, f'{image_path}')))
            self.images = [image.load(element) for element in sorted(os.listdir())]
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        if self.pos_x or self.pos_y:
            self.rect.x, self.rect.y = self.pos_x, self.pos_y


class SmileBird(Bird):
    DEFAULT_COUNT = 5
    # DEFAULT_COUNT = 1

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 4
        self.set_images('smile_bird')
        self.score = 10


class PoisonedBird(Bird):
    DEFAULT_COUNT = 8
    # DEFAULT_COUNT = 1

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 6
        self.set_images('poisoned_bird')
        self.score = 30


class CircledBird(Bird):
    DEFAULT_COUNT = 10
    # DEFAULT_COUNT = 1

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 6
        self.set_images('circled_bird')
        self.score = 50


class OldBird(Bird):
    DEFAULT_COUNT = 15
    # DEFAULT_COUNT = 1

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 2
        self.set_images('old_bird')
        self.score = 60


class CrazyBird(Bird):
    DEFAULT_COUNT = 1

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 8
        self.health_point = 10
        self.set_images('crazy_bird')
        self.children = Group()
        self.score = 500

    def update(self, *args, **kwargs) -> None:
        super().update()
        self.children.update()

    def move(self) -> None:
        if 0 > self.rect.x or 640 - self.image.get_width() < self.rect.x:
            self.speed *= -1
        self.rect.x += self.speed
