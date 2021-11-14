from os.path import join

from pygame.mixer import Sound

from models.base import Entity


class Bullet(Entity):
    def __init__(self, pos_x, pos_y):
        super(Bullet, self).__init__('bullets')
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self) -> None:
        self.rect.y -= self.speed

    def set_sound(self, name):
        super(Bullet, self).set_sound(name)
        self.sound.play()


class PlaneBullet(Bullet):
    def __init__(self, pos_x, pos_y):
        super(PlaneBullet, self).__init__(pos_x, pos_y)
        self.set_images('plane_bullet')
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.set_sound('plane_bullet.wav')


class SpaceShipBullet(Bullet):
    def __init__(self, pos_x, pos_y):
        super(SpaceShipBullet, self).__init__(pos_x, pos_y)
        self.set_images('plane_bullet')
        self.set_sound('spaceship_bullet.wav')


class PassBullet(Bullet):
    pass
