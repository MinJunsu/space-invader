from pygame.constants import KEYDOWN, K_h, K_ESCAPE
from pygame.key import get_pressed

from engine.sound import SoundManager
from screens import Screen, PAUSE_CONTEXT
from utils.constants import game_tick


class PauseScreen(Screen):
    CONTEXT = PAUSE_CONTEXT

    def __init__(self, size, set_screen, return_screen, score):
        super(PauseScreen, self).__init__(size, set_screen, return_screen)
        self.sound_manager = SoundManager()
        self.tick = game_tick()
        self.score = str(score)

    def draw(self):
        # Draw Title
        title = self.big_font.render('PAUSE', 1, (0, 255, 0))
        self.blit(title, (640 // 2 - title.get_width() // 2, 100))

        # Draw Return Home
        home = self.small_font.render('Return [ESC]', 1, (255, 255, 255))
        self.blit(home, (10, 10))

        # Draw Setting
        setting = self.small_font.render('Home [H]', 1, (255, 255, 255))
        self.blit(setting, (640 - setting.get_width() - 20, 10))

        speed_option = self.small_font.render('Speed : ', 1, (255, 255, 255))
        self.blit(speed_option, (640 - speed_option.get_width() - 60, 55))

        speed_val = self.small_font.render(str(int(round(self.sound_manager.get_volume(), 2) * 100)), 1, (0, 255, 0))
        self.blit(speed_val, (640 - speed_val.get_width() - 30, 55))

        volume_option = self.small_font.render('volume : ', 1, (255, 255, 255))
        self.blit(volume_option, (640 - volume_option.get_width() - 60, 75))

        volume_val = self.small_font.render(str(self.tick.get()), 1, (0, 255, 0))
        self.blit(volume_val, (640 - volume_val.get_width() - 30, 75))

        # Draw Score
        for idx, element in enumerate(self.CONTEXT):
            name = self.font.render(element['text'], 1, (255, 255, 255))

            name_position = (100 + idx * 80, 200 + idx * 80)
            self.blit(name, name_position)

        score = self.big_font.render(self.score.zfill(5), 1, (0, 255, 0))
        self.blit(score, (640 // 2 - title.get_width() // 2, 350))

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()
            if key[K_ESCAPE]:
                self.return_screen()

            if key[K_h]:
                self.set_screen('main')
