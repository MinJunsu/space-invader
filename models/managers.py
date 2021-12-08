from pygame.sprite import Group, GroupSingle

from models import BackGround
from models.player.players import PlanePlayer, SpaceShipPlayer
from models.enemy import (
    SmileBird, PoisonedBird, CircledBird, OldBird, CrazyBird,
    BlueSpaceShip, RedSpaceShip, GreenSpaceShip, CircledSpaceShip
)


class PlayerManager:
    def __init__(self):
        self.level = 0
        self.character = GroupSingle()
        self.health_point = 5
        self.score = 0

    def clear(self):
        if self.character.sprite.rect.y > 0:
            self.character.sprite.rect.y -= 15
            return False
        return True

    def upgrade(self):
        if self.level == 0:
            self.character.empty()
            self.character.add(PlanePlayer(self.health_point, self.score))

        elif self.level == 1:
            self.character.empty()
            self.character.add(SpaceShipPlayer(self.health_point, self.score))

        # # FIXME: Replace other Player
        # elif self.level == 2:
        #     self.character.empty()
        #     self.character.add(PlanePlayer(self.health_point))
        self.level += 1

    def collide(self, enemies) -> None:
        for enemy in enemies:
            if enemy.weapon:
                if self.character.sprite.collide(enemy.weapons):
                    self.health_point -= 1

    def move(self):
        self.character.sprite.move()

    def draw(self, surface):
        self.character.draw(surface)
        self.character.sprite.weapons.draw(surface)

    def update(self):
        self.character.update()
        self.score = self.character.sprite.score


class EnemyManager:
    ENEMIES = [
        SmileBird, PoisonedBird, CircledBird, OldBird, CrazyBird,
        BlueSpaceShip, RedSpaceShip, GreenSpaceShip,
        CircledSpaceShip
    ]

    def __init__(self):
        self.level = 0
        self.enemy = Group()
        self.collision = Group()

    def move(self):
        for element in self.enemy:
            element.move()

    def upgrade(self):
        self.ENEMIES[self.level].create(self.enemy.add)
        self.level += 1

    # 플레이어의 총알과 충돌할 경우
    def collide(self, player) -> None:
        for enemy in self.enemy:
            explosion = enemy.collide(player.sprite.weapons)
            if explosion:
                player.sprite.score += enemy.score
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


class BackGroundManager:
    def __init__(self):
        self.background = GroupSingle()
        self.level = 0

    def upgrade(self):
        background = BackGround()
        if self.level == 0:
            self.background.empty()
            background.set_images('stage3')
            self.background.add(background)

        elif self.level == 1:
            self.background.empty()
            background.set_images('stage2')
            self.background.add(background)

        # elif self.level == 2:
        #     self.background.empty()
        #     background.set_images('stage3')
        #     self.background.add(background)

        self.level += 1

    def draw(self, surface):
        self.background.draw(surface)

    def update(self):
        self.background.update()
