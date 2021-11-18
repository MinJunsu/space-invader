import os
from random import randint

from pygame.sprite import Sprite

from models import Entity, Bullet

WIDTH = 640
HEIGHT = 480


class Enemy(Entity):
    DEFAULT_COUNT = 1

    def __init__(self, name):
        super(Enemy, self).__init__(os.path.join('enemy', name))
        self.explosion = None
        self.score = 10

    def move(self) -> None:
        if 0 > self.rect.x or WIDTH - self.image.get_width() < self.rect.x:
            self.speed *= -1
            if self.is_reverse:
                if self.speed > 0:
                    self.images = self.rights
                else:
                    self.images = self.lefts
            self.rect.y += abs(self.speed)
        self.rect.x += self.speed

        if self.weapon:
            for weapon in self.weapons:
                weapon.move()

    def update(self, *args, **kwargs) -> None:
        super(Enemy, self).update()
        if self.weapon:
            self.weapons.update()

    def collide(self, sprite: Sprite):
        if super(Enemy, self).collide(sprite):
            self.health_point -= 1
            if self.health_point == 0:
                self.kill()
                return self.explosion(self.rect.x + (self.image.get_width() / 2), self.rect.y + self.image.get_height() / 2)

        # TODO: Remove this?
        if self.is_boss:
            for child in self.children:
                child.collide(sprite)

    @classmethod
    def create(cls, func):
        func(*[cls(randint(140, 500), randint(0, 100)) for _ in range(cls.DEFAULT_COUNT)])


class EnemyBullet(Bullet):
    def __init__(self, pos_x, pos_y):
        super(EnemyBullet, self).__init__(pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self) -> None:
        self.rect.y += randint(1, self.speed)
