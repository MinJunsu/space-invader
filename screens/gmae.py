from models.managers import PlayerManager, EnemyManager
from .base import Screen


class GameScreen(Screen):
    def __init__(self, size, set_screen):
        super(GameScreen, self).__init__(size)
        self.set_screen = set_screen
        self.player = PlayerManager()
        self.enemies = EnemyManager()

    def run(self):
        self.play()

        if len(self.enemies.enemy) == 0:
            self.enemies.upgrade()

        if self.enemies.level % 5 == 0:
            self.player.upgrade()

    def play(self):
        self.move()
        self.collide()
        self.update()
        self.draw()

    def collide(self):
        self.player.collide(self.enemies.enemy)
        self.enemies.collide(self.player.character)

    def draw(self):
        # TODO: 게임 백그라운드 배경 이미지 그리기
        self.fill((0, 0, 0))
        self.player.draw(self)
        self.enemies.draw(self)

    def update(self):
        self.player.update()
        self.enemies.update()

    def move(self):
        self.player.move()
        self.enemies.move()



