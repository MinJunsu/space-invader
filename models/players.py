from pygame.key import get_pressed
from pygame.constants import K_LEFT, K_RIGHT, K_SPACE
from pygame.sprite import Group, Sprite

from models.base import Entity
from models.bullets import PlaneBullet

WEIGHT = 640
HEIGHT = 480


class Player(Entity):
    COOLDOWN = 20

    def __init__(self, health_point):
        super(Player, self).__init__('users')
        self.weapon = None
        self.weapons = Group()
        self.cool_down_counter = 0
        self.health_point = health_point

    def move(self) -> None:
        key = get_pressed()

        if key[K_LEFT]:
            self.rect.x -= self.speed

        if key[K_RIGHT]:
            self.rect.x += self.speed

        if key[K_SPACE]:
            self.attack()
        super(Player, self).move()
        for weapon in self.weapons:
            weapon.move()

    def attack(self) -> None:
        if self.cool_down_counter > self.COOLDOWN:
            self.weapons.add(self.weapon(self.rect.x, self.rect.y))
            self.cool_down_counter = 0

    def update(self, *args, **kwargs) -> None:
        self.cool_down_counter += 1
        super(Player, self).update()
        self.weapons.update()

    def set_images(self, image_path) -> None:
        super(Player, self).set_images(image_path)
        self.pos_y = HEIGHT - self.image.get_height() - 30
        self.pos_x = (WEIGHT - self.image.get_width()) / 2
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def collision(self, sprites: Group) -> None:
        for enemy_bullet in sprites:
            if self.is_collision(enemy_bullet):
                enemy_bullet.kill()
                self.health_point -= 1


class PlanePlayer(Player):
    COOLDOWN = 20

    def __init__(self, health_point):
        super(PlanePlayer, self).__init__(health_point)
        self.speed = 10
        self.weapon = PlaneBullet
        self.is_horizontal_move = True
        self.set_images('plane')


class SpaceShipPlayer(Player):
    COOLDOWN = 15

    def __init__(self, health_point):
        super(SpaceShipPlayer, self).__init__(health_point)
        self.weapon = None
        self.speed = 15
        self.set_images('spaceship')
