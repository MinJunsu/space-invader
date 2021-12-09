from pygame.constants import KEYDOWN, K_s, K_ESCAPE
from pygame.key import get_pressed

from screens import Screen, PAUSE_CONTEXT


class PauseScreen(Screen):
    CONTEXT = PAUSE_CONTEXT

    def __init__(self, size, set_screen, return_screen):
        super(PauseScreen, self).__init__(size, set_screen, return_screen)
        self.speed_val = 0
        self.volume_val = 0

    def draw(self):
        # Draw Title
        title = self.big_font.render('PAUSE', 1, (0, 255, 0))
        self.blit(title, (640 // 2 - title.get_width() // 2, 100))

        # Draw Return Home
        home = self.small_font.render('Return [ESC]', 1, (255, 255, 255))
        self.blit(home, (10, 10))

        # Draw Setting
        setting = self.small_font.render('Setting [S]', 1, (255, 255, 255))
        self.blit(setting, (640 - setting.get_width() - 20, 10))

        setting_img = self.get_image('setting.png')
        self.blit(setting_img, (640 - setting_img.get_width() - 120, 10))

        speed_option = self.small_font.render('Speed : ', 1, (255, 255, 255))
        self.blit(speed_option, (640 - speed_option.get_width() - 40, 55))

        speed_val = self.small_font.render(str(self.speed_val), 1, (0, 255, 0))
        self.blit(speed_val, (640 - speed_val.get_width() - 30, 55))

        volume_option = self.small_font.render('volume : ', 1, (255, 255, 255))
        self.blit(volume_option, (640 - volume_option.get_width() - 40, 75))

        volume_val = self.small_font.render(str(self.volume_val), 1, (0, 255, 0))
        self.blit(volume_val, (640 - volume_val.get_width() - 30, 75))

        # Draw Score
        for idx, element in enumerate(self.CONTEXT):
            name = self.font.render(element['text'], 1, (255, 255, 255))

            name_position = (100 + idx * 80, 200 + idx * 80)
            self.blit(name, name_position)

        score = self.big_font.render('000', 1, (0, 255, 0))
        self.blit(score, (640 // 2 - title.get_width() // 2 + 20, 360))

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()
            if key[K_ESCAPE]:
                self.return_screen()

            if key[K_s]:
                self.set_screen('setting')
