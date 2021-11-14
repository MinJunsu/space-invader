from os.path import join
from random import choice
from .entity import Entity


class Bird(Entity):
    DEFAULT_COUNT = 0

    def __init__(self):
        super(Bird, self).__init__('birds')
        self.is_horizontal_move = True
        self.health_point = 1


class SmileBird(Bird):
    DEFAULT_COUNT = 5

    def __init__(self, pos_x, pos_y):
        super(SmileBird, self).__init__()
        self.speed = 5
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_vertical_move = False
        self.set_images('smile_bird')
        self.rect = self.image.get_rect()

    def move(self) -> None:
        # 이동 추가
        super(SmileBird, self).move()


class PoisonedBird(Bird):
    DEFAULT_COUNT = 8

    def __init__(self, pos_x, pos_y):
        super(PoisonedBird, self).__init__()
        self.speed = 15
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_vertical_move = False
        self.set_images('poisoned_bird')
        self.rect = self.image.get_rect()
        
    def move(self) -> None:
        # 이동 추가
        super(PoisonedBird, self).move()


class CircledBird(Bird):
    DEFAULT_COUNT = 10

    def __init__(self, pos_x, pos_y):
        super(CircledBird, self).__init__()
        self.speed = 10
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_vertical_move = True
        self.set_images('circled_bird')
        self.rect = self.image.get_rect()

    def move(self) -> None:
        # 이동 추가
        super(PoisonedBird, self).move()


class OldBird(Bird):
    DEFAULT_COUNT = 15

    def __init__(self, pos_x, pos_y):
        super(OldBird, self).__init__()
        self.speed = 3
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_vertical_move = False
        self.set_images('old_bird')
        self.rect = self.image.get_rect()


class CrazyBird(Bird):
    DEFAULT_COUNT = 1

    def __init__(self, pos_x, pos_y):
        super(CrazyBird, self).__init__()
        self.speed = 15
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_vertical_move = True
        self.health_point = 15
        self.set_images('crazy_bird')
        self.rect = self.image.get_rect()
        # self.birds = [SmileBird(), PoisonedBird(), CircledBird(), OldBird()]

    def create_birds(self) -> Bird:
        return choice(self.birds)

    def move(self) -> None:
        # 이동 추가
        super(PoisonedBird, self).move()
