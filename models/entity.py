from pygame.sprite import Group, GroupSingle

from .players import PlanePlayer, SpaceShipPlayer
from .birds import SmileBird, PoisonedBird, CircledBird, OldBird, CrazyBird
from .space_ship import BlueSpaceShip, RedSpaceShip, GreenSpaceShip


class PlayerGroup:

    def __init__(self):
        self.level = 0
        self.character = GroupSingle()
        self.health_point = 5
        self.upgrade()

    def upgrade(self):
        if self.level == 0:
            self.character.empty()
            self.character.add(PlanePlayer(self.health_point))

        elif self.level == 1:
            self.character.empty()
            self.character.add(SpaceShipPlayer(self.health_point))

        # FIXME: Replace other Player
        elif self.level == 2:
            self.character.empty()
            self.character.add(PlanePlayer(self.health_point))
            self.level += 1

    def move(self):
        self.character.sprite.move()

    def draw(self, surface):
        self.character.draw(surface)
        self.character.sprite.weapons.draw(surface)

    def update(self):
        self.character.update()


class EnemyGroup:
    ENEMIES = [
        SmileBird, PoisonedBird, CircledBird, OldBird, CrazyBird,
        BlueSpaceShip, RedSpaceShip, GreenSpaceShip,
    ]

    def __init__(self):
        self.level = 0
        self.enemy = Group()
        self.collision = Group()
        self.upgrade()

    def move(self):
        for element in self.enemy:
            element.move()

    def upgrade(self):
        self.ENEMIES[self.level].create(self.enemy.add)
        self.level += 1

    # 플레이어의 총알과 충돌할 경우
    def collide(self, player: PlayerGroup) -> None:
        for enemy in self.enemy:
            explosion = enemy.collide(player.sprite.weapons)
            if explosion:
                self.collision.add(explosion)

    def update(self):
        self.enemy.update()
        self.collision.update()

    def draw(self, surface) -> None:
        self.enemy.draw(surface)
        self.collision.draw(surface)
        for enemy in self.enemy:
            if enemy.weapon:
                enemy.weapons.draw(surface)

    def is_empty(self):
        return len(self.enemy.sprites()) == 0
