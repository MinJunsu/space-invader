from models.enemy.base import Entity


class Alien(Entity):
    DEFAULT_COUNT = 0

    def __init__(self, image_path):
        super().__init__()
        
        
class SmallFlyAlien(Alien):
    DEFAULT_COUNT = 5

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.speed = 5
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_vertical_move = False
        self.is_horizontal_move = True
        self.health_point = 1
        # FIXME: Weapon 구현 후 넣기
        self.weapon = None


class BigFlyAlien(Alien):
    DEFAULT_COUNT = 10

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.speed = 10
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_vertical_move = True
        self.is_horizontal_move = True
        self.health_point = 1
        # FIXME: Weapon 구현 후 넣기
        self.weapon = None
