from .base import PlayerBullet


class PlaneBullet(PlayerBullet):
    def __init__(self, pos_x, pos_y):
        super(PlaneBullet, self).__init__(pos_x, pos_y)
        self.set_images('plane_bullet')
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.set_sound('plane_bullet.wav')