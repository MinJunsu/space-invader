from models import Explosion


class BirdExplosion(Explosion):
    def __init__(self, pos_x, pos_y):
        super(BirdExplosion, self).__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.set_images('birds')
        self.set_sound('explosion09.wav')
