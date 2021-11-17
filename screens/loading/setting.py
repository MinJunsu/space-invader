from pygame.constants import KEYDOWN, K_h, K_LEFTBRACKET, K_RIGHTBRACKET, K_m, K_BACKSPACE, K_PLUS, K_MINUS
from pygame.key import get_pressed

from screens import Screen, SETTING_CONTEXT


class SettingScreen(Screen):
    CONTEXT = SETTING_CONTEXT

    def __init__(self, size, set_screen, return_screen):
        super(SettingScreen, self).__init__(size, set_screen, return_screen)

    def draw(self):
        # Draw Title
        title = self.big_font.render('SETTINGS', 1, (0, 0, 255))
        self.blit(title, (640 // 2 - title.get_width() // 2, 100))

        # Draw Return Home
        home = self.small_font.render('Home [BACKSPACE]', 1, (255, 255, 255))
        self.blit(home, (10, 10))

        # Draw Settings
        for idx, element in enumerate(self.CONTEXT):
            name = self.small_font.render(element['name'], 1, (255, 255, 255))
            key = self.small_font.render(element['key'], 1, (255, 0, 0))

            name_position = (100, 200 + idx * 40)
            key_position = (400, 200 + idx * 40)
            self.blit(name, name_position)
            self.blit(key, key_position)

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()

            if key[K_h]:
                self.set_screen('help')

            # TODO: Change Game Ticks
            elif key[K_LEFTBRACKET]:
                pass

            elif key[K_RIGHTBRACKET]:
                pass

            # TODO: Mute Audio
            elif key[K_m]:
                pass

            # TODO: Change Audio Volume
            elif key[K_PLUS]:
                pass

            elif key[K_MINUS]:
                pass

            elif key[K_BACKSPACE]:
                self.set_screen('main')
