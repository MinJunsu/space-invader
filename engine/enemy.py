from pygame.sprite import Group

from models.enemy import (
    SmileBird, PoisonedBird, CircledBird, OldBird, CrazyBird,
    BlueSpaceShip, RedSpaceShip, GreenSpaceShip, GreenSpaceShip, CircledSpaceShip,
    RedEyeAlien, GreenSomAlien, GreenEyeAlien, GreenOctorAlien, BossAlien
)


class EnemyManager:
    ENEMIES = [
        SmileBird, PoisonedBird, CircledBird, OldBird, CrazyBird,
        BlueSpaceShip, RedSpaceShip, GreenSpaceShip, GreenSpaceShip, CircledSpaceShip,
        RedEyeAlien, GreenSomAlien, GreenEyeAlien, GreenOctorAlien, BossAlien
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
