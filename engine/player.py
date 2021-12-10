from pygame.sprite import Group, GroupSingle

from models.player.players import PlanePlayer, SpaceShipPlayer, AlienPlayer


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

        # FIXME: Replace other Player
        elif self.level == 2:
            self.character.empty()
            self.character.add(AlienPlayer(self.health_point, self.score))
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
