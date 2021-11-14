from pygame.sprite import Sprite
from .entity import Entity


class SpaceShip(Entity):
    DEFAULT_COUNT = 0
    IMAGE_PATH = 'spaceships'

    def __init__(self):
        super(SpaceShip, self).__init__()

    def is_collision(self, sprites: Sprite):
        if super().is_collision(sprites):
            pass


class BlueSpaceShip(SpaceShip):
    pass


class RedSpaceShip(SpaceShip):
    pass


class GreenSpaceShip(SpaceShip):
    pass
