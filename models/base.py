from pathlib import Path
import os

from pygame import image
from pygame.sprite import Sprite, Group, spritecollide
from pygame.mixer import Sound

from engine.sound import SoundManager

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

        self.weapon = None
        self.weapons = None
        self.is_reverse = False
        self.sound_manager = SoundManager()

    def set_sound(self, name):
        self.sound = self.sound_manager.get(name)

    def set_images(self, image_path) -> None:
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


class BackGround(Entity):
    def __init__(self):
        super().__init__('background')

    def set_sound(self, name):
        super().set_sound(name)
        self.sound.play(-1)


class Bullet(Entity):
    def __init__(self, pos_x, pos_y):
        super().__init__('bullets')
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sounds = SoundManager()

    def set_sound(self, name):
        super().set_sound(name)
        self.sound.play()


class Explosion(Entity):
    def __init__(self):
        super().__init__('explosion')
        self.sounds = SoundManager()

    def set_sound(self, name):
        super().set_sound(name)
        self.sound.play()

    def update(self, *args, **kwargs) -> None:
        self.image_index += 1
        if self.image_index > len(self.images) - 1:
            self.image_index = 0
            self.kill()
        self.image = self.images[self.image_index]
