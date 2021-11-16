from pathlib import Path
import os
from random import randint

from pygame import image
from pygame.sprite import Sprite, Group, GroupSingle, spritecollide
from pygame.mixer import Sound

WIDTH = 640
HEIGHT = 480


class Entity(Sprite):
    BASE_DIR = Path(__file__).resolve().parent.parent
    IMAGE_ROOT = os.path.join(BASE_DIR, 'assets', 'images')
    SOUND_ROOT = os.path.join(BASE_DIR, 'assets', 'sounds')

    def __init__(self, name):
        Sprite.__init__(self)
        self.name = name
        self.sound = None
        self.image = None
        self.image_index = 0
        self.images = []
        self.lefts = []
        self.rights = []
        self.speed = 5
        self.pos_x = 0
        self.pos_y = 0
        self.health_point = 1
        self.is_boss = False
        self.weapon = None
        self.weapons = None
        self.is_reverse = False

    def set_sound(self, name):
        self.sound = Sound(os.path.join(self.SOUND_ROOT, name))

    def set_images(self, image_path) -> None:
        if self.is_reverse:
            os.chdir(os.path.join(Entity.IMAGE_ROOT, os.path.join(self.name, f'{image_path}_left')))
            self.lefts = [image.load(element) for element in sorted(os.listdir())]
            os.chdir(os.path.join(Entity.IMAGE_ROOT, os.path.join(self.name, f'{image_path}_right')))
            self.rights = [image.load(element) for element in sorted(os.listdir())]
            self.images = self.rights
        else:
            os.chdir(os.path.join(Entity.IMAGE_ROOT, os.path.join(self.name, f'{image_path}')))
            self.images = [image.load(element) for element in sorted(os.listdir())]
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        if self.pos_x or self.pos_y:
            self.rect.x, self.rect.y = self.pos_x, self.pos_y

    def update(self, *args, **kwargs) -> None:
        self.move()
        self.image_index += 1
        if self.image_index > len(self.images) - 1:
            self.image_index = 0
        self.image = self.images[self.image_index]

    def move(self) -> None:
        if 0 > self.rect.x:
            self.rect.x = 0

        if WIDTH - self.image.get_width() < self.rect.x:
            self.rect.x = WIDTH - self.image.get_width()

        if self.rect.y < 0:
            self.rect.y = 0

        if self.rect.y > HEIGHT - self.image.get_height():
            self.rect.y = HEIGHT - self.image.get_height()

    def attack(self) -> None:
        if self.weapon:
            return self.weapon

    def collide(self, sprites: Group) -> None:
        return spritecollide(self, sprites, True)


class Enemy(Entity):
    DEFAULT_COUNT = 1

    def __init__(self, name):
        super(Enemy, self).__init__(os.path.join('enemy', name))
        self.explosion = None

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
