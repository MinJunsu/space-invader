from .entity import Entity


class Alien(Entity):
    DEFAULT_COUNT = 0

    def __init__(self, image_path):
        super(Alien, self, image_path).__init__()
        
        
class SmallFlyAlien(Alien):
    DEFAULT_COUNT = 5

    def __init__(self, pos_x, pos_y):
        super(SmallFlyAlien, self, 'small_fly_alien').__init__()
        self.speed = 5
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_vertical_move = False
        self.is_horizontal_move = True
        self.health_point = 1
        # FIXME: Weapon 구현 후 넣기
        self.weapon = None
        
    def attack(self) -> None:
        # 추가 공격
        super(SmallFlyAlien, self).attack()


class BigFlyAlien(Alien):
    DEFAULT_COUNT = 10

    def __init__(self, pos_x, pos_y):
        super(BigFlyAlien, self, 'big_fly_alien').__init__()
        self.speed = 10
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_vertical_move = True
        self.is_horizontal_move = True
        self.health_point = 1
        # FIXME: Weapon 구현 후 넣기
        self.weapon = None
