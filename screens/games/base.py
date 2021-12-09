from pygame.constants import KEYDOWN, K_BACKSPACE, K_ESCAPE
from pygame.key import get_pressed

from models.managers import PlayerManager, EnemyManager, BackGroundManager
from screens.base import Screen


class GameScreen(Screen):
    def __init__(self, size, set_screen, return_screen):
        super(GameScreen, self).__init__(size, set_screen, return_screen)
        self.level = 0
        self.image = dict()
        self.load_image()

        self.player = PlayerManager()
        self.enemies = EnemyManager()
        self.background = BackGroundManager()

    def load_image(self):
        self.image['heart'] = self.get_image('heart.png')
        self.image['trophy'] = self.get_image('trophy.png')

    def run(self):
        # Initialize
        if self.level == 0 and len(self.enemies.enemy) == 0:
            self.player.upgrade()
            self.background.upgrade()
            self.enemies.upgrade()

        self.play()

        # Explosion 이 다 나온 경우
        if len(self.enemies.collision) == 0:
            if self.player.health_point < 0:
                self.set_screen('ending_fail')

            if self.level > 15:
                self.set_screen('ending_clear')

            if len(self.enemies.enemy) == 0 and self.enemies.level % 5 == 0:
                self.player.upgrade()
                self.background.upgrade()
                self.set_screen('explain')

            if len(self.enemies.enemy) == 0:
                self.enemies.upgrade()
                self.level += 1



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
        self.background.draw(self)
        self.enemies.draw(self)
        self.setting()
        self.player.draw(self)

    def setting(self):
        for i in range(self.player.health_point):
            self.blit(self.image['heart'], (10 + 30 * i, 10))
        self.blit(self.image['trophy'], (530, 10))
        level = self.font.render(f'Level: {self.level}', 1, (255, 255, 255))
        self.blit(level, (640 // 2 - level.get_width() // 2, 10))
        score = self.small_font.render(f'{self.player.score}', 1, (255, 0, 0))
        self.blit(score, (580, 10))

    def update(self):
        self.background.update()
        self.player.update()
        self.enemies.update()

    def move(self):
        self.player.move()
        self.enemies.move()

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()

            if key[K_BACKSPACE]:
                self.player.health_point -= 1

            elif key[K_ESCAPE]:
                self.set_screen('pause')

