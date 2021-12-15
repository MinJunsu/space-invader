from pygame.constants import KEYDOWN, K_BACKSPACE, K_ESCAPE, K_p
from pygame.key import get_pressed
from pygame.draw import rect

from engine.player import PlayerManager
from engine.enemy import EnemyManager
from engine.background import BackGroundManager
from screens.base import Screen
from utils.file import File


class GameScreen(Screen):
    def __init__(self, size, set_screen, return_screen):
        super(GameScreen, self).__init__(size, set_screen, return_screen)
        self.level = 0
        self.image = dict()
        self.load_image()
        self.is_pause = False
        self.player = PlayerManager()
        self.enemies = EnemyManager()
        self.background = BackGroundManager()

    def load_image(self):
        self.image['heart'] = self.get_image('heart.png')
        self.image['trophy'] = self.get_image('trophy.png')

    def run(self):
        if len(self.enemies.enemy) == 0 and self.enemies.level % 5 == 0:
            self.player.upgrade()
            self.background.upgrade()

            if self.level // 5 == 0:
                self.set_screen('begin_first')
            if self.level // 5 == 1:
                self.set_screen('begin_second')
            elif self.level // 5 == 2:
                self.set_screen('begin_third')

        self.play()
        self.is_enemy_out()

        if self.player.health_point == 0:
            self.set_screen('dying')

        if self.level > 15:
            scores = File.load_data()
            scores['TEMP'] = self.player.score
            if self.player.score in sorted(scores.values(), reverse=True)[:5]:
                self.set_screen('score')
            else:
                self.set_screen('ending_clear')

        if len(self.enemies.enemy) == 0:
            self.level += 1
            if self.level < 16:
                self.enemies.upgrade()

    def is_enemy_out(self):
        for enemy in self.enemies.enemy:
            if enemy.rect.y + enemy.image.get_height() > 480:
                self.player.health_point -= 1
                enemy.kill()

    def play(self):
        self.draw()
        self.move()
        self.collide()
        self.update()

    def collide(self):
        self.player.collide(self.enemies.enemy)
        self.enemies.collide(self.player.character)

    def draw(self):
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
        for element in self.enemies.enemy.sprites():
            if not element.is_boss:
                break
            rect(self, (255, 255, 255), [self.get_width() // 2 - 75, 40, 150, 20], 2)
            rect(self, (255, 0, 0),
                 [self.get_width() // 2 - 75, 40, int(151 * (element.health_point / element.HEALTH_POINT)), 21])

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
                self.set_screen('pause')
