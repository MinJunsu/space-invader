from pathlib import Path
import os

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
        self.speed = 5
        self.pos_x = 0
        self.pos_y = 0
        self.health_point = 1
        self.is_boss = False

    def set_sound(self, name):
        self.sound = Sound(os.path.join(self.SOUND_ROOT, name))

    def set_images(self, image_path) -> None:
        os.chdir(os.path.join(Entity.IMAGE_ROOT, os.path.join(self.name, image_path)))
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

    def collide(self, sprite: Sprite) -> None:
        return spritecollide(self, sprite, True)


class Enemy(Entity):
    def __init__(self, name):
        super(Enemy, self).__init__(os.path.join('enemy', name))
        self.explosion = None

    def move(self) -> None:
        if 0 > self.rect.x or WIDTH - self.image.get_width() < self.rect.x:
            self.speed *= -1
            self.rect.y += abs(self.speed)
        self.rect.x += self.speed

    def collide(self, sprite: Sprite):
        if super(Enemy, self).collide(sprite):
            self.health_point -= 1
            if self.health_point == 0:
                self.kill()
                return self.explosion(self.rect.x + (self.image.get_width() / 2), self.rect.y + self.image.get_height() / 2)

        if self.is_boss:
            for child in self.children:
                child.collide(sprite)


class PlayerGroup(GroupSingle):
    pass


class EnemyGroup(Group):
    def __init__(self):
        super(EnemyGroup, self).__init__()
        self.collision = Group()

    # 플레이어의 총알과 충돌할 경우
    def collide(self, player: PlayerGroup) -> None:
        for enemy in self:
            explosion = enemy.collide(player.sprite.weapons)
            if explosion:
                self.collision.add(explosion)

    def draw(self, surface) -> None:
        super(EnemyGroup, self).draw(surface)
        for enemy in self:
            if enemy.is_boss:
                enemy.children.draw(surface)
