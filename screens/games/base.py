from pygame.constants import KEYDOWN, K_BACKSPACE, K_ESCAPE, K_p
from pygame.key import get_pressed
from pygame.time import wait

from models.managers import PlayerManager, EnemyManager, BackGroundManager
from screens.base import Screen
from .pause import PauseScreen


class GameScreen(Screen):
    def __init__(self, size, set_screen, return_screen):
        super(GameScreen, self).__init__(size, set_screen, return_screen)
        self.level = 0
        self.image = dict()
        self.load_image()
        self.is_pause = False
        self.pause = PauseScreen((size[0] // 2, size[1] // 2), set_screen, return_screen)
        self.player = PlayerManager()
        self.enemies = EnemyManager()
        self.background = BackGroundManager()

    def load_image(self):
        self.image['heart'] = self.get_image('heart.png')
        self.image['trophy'] = self.get_image('trophy.png')

    def run(self):

        if self.player.health_point == 0:
            self.set_screen('dying')
            # self.set_screen('dying')

        if len(self.enemies.enemy) == 0 and self.enemies.level % 5 == 0:
            self.player.upgrade()
            self.background.upgrade()

            if self.level // 5 == 0:
                self.set_screen('begin_first')
            elif self.level // 5 == 1:
                self.set_screen('begin_second')
            elif self.level // 5 == 2:
                self.set_screen('begin_third')
            else:
                # TODO: stage3까지 완성되면 clear effect로 변경
                self.set_screen('dying')

        if len(self.enemies.enemy) == 0:
            # if self.player.dying() or self.level == 0:
            self.enemies.upgrade()
            self.level += 1
        self.play()

    def play(self):
        self.draw()
        if self.is_pause:
            self.pause.draw()
            # self.blit(self.pause, (300, 100))
        else:
            self.move()
            self.collide()
            self.update()

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
                self.enemies.enemy.empty()

            if key[K_ESCAPE] or key[K_p]:
                self.is_pause = not self.is_pause

        if self.is_pause:
            self.pause.get_event(event)






