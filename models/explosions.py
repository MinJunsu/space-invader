from models.base import Entity


class Explosion(Entity):
    def __init__(self):
        super(Explosion, self).__init__('explosion')

    def set_sound(self, name):
        super(Explosion, self).set_sound(name)
        self.sound.play()

    def update(self, *args, **kwargs) -> None:
        self.image_index += 1
        if self.image_index > len(self.images) - 1:
            self.image_index = 0
            self.kill()
        self.image = self.images[self.image_index]


class BirdExplosion(Explosion):
    def __init__(self, pos_x, pos_y):
        super(BirdExplosion, self).__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.set_images('birds')
        self.set_sound('explosion09.wav')

