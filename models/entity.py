from pathlib import Path
import os

from pygame import image
from pygame.sprite import Sprite, spritecollide
from pygame.mixer import Sound


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
        self.speed = 5
        self.pos_x = 0
        self.pos_y = 0
        self.is_vertical_move = False
        self.is_horizontal_move = False
        self.health_point = 1

    def set_sound(self, name):
        self.sound = Sound(os.path.join(self.SOUND_ROOT, name))

    def set_images(self, image_path) -> None:
        os.chdir(os.path.join(Entity.IMAGE_ROOT, os.path.join(self.name, image_path)))
        self.images = [image.load(element) for element in sorted(os.listdir())]
        self.image = self.images[self.image_index]

    def update(self, *args, **kwargs) -> None:
        self.move()
        self.image_index += 1
        if self.image_index > len(self.images) - 1:
            self.image_index = 0
        self.image = self.images[self.image_index]

    def move(self) -> None:
        if self.is_vertical_move:
            self.pos_y += self.speed

        if self.is_horizontal_move:
            self.pos_X += self.speed

    def attack(self) -> None:
        if self.weapon:
            return self.weapon

    def is_collision(self, sprite: Sprite):
        return spritecollide(self, sprite)

