from pygame.constants import KEYDOWN, K_LESS, K_GREATER, K_LEFTBRACKET, K_RIGHTBRACKET, K_m, K_BACKSPACE, K_PLUS, K_MINUS, K_UP, K_DOWN, K_z, K_x
from pygame.key import get_pressed

from screens import Screen, SETTING_CONTEXT

class SettingScreen(Screen):
    CONTEXT = SETTING_CONTEXT

    CHOICE_COLOR = (249, 166, 2)
    UN_CHOICE_COLOR = (255, 255, 255)

    def __init__(self, size, set_screen, return_screen):
        super(SettingScreen, self).__init__(size, set_screen, return_screen)
        self.index = 0
        self.speed_val = 100
        self.volume_val = 100

    def draw(self):
        # Draw Title
        title = self.big_font.render('SETTINGS', 1, (255, 255, 0))
        self.blit(title, (640 // 2 - title.get_width() // 2, 100))

        # Draw Return Home
        home = self.small_font.render('Return [BACKSPACE]', 1, (255, 255, 255))
        self.blit(home, (10, 10))

        # Draw Settings
        for idx, element in enumerate(self.CONTEXT):
            if idx == self.index:
                name = self.small_font.render(element['name'], 1, self.CHOICE_COLOR)
            else:
                name = self.small_font.render(element['name'], 1, self.UN_CHOICE_COLOR)

            name_position = (70, 200 + idx * 40)
            key_position = (430, 200 + idx * 40)

            if element['key'] == '|':
                if idx == 2:
                    key = self.small_font.render(str(self.speed_val) + " " + element['key'] * (self.speed_val/5), 1, (0, 255, 0))
                elif idx == 3:
                    key = self.small_font.render(str(self.volume_val) + " " + element['key'] * (self.volume_val/5), 1, (0, 255, 0))
            else:
                key = self.small_font.render(element['key'], 1, (0, 255, 0))

            self.blit(name, name_position)
            self.blit(key, key_position)

    def get_event(self, event):
        key = get_pressed()
        if event.type == KEYDOWN:
            if key[K_UP]:
                self.index = self.index - 1 if self.index > 0 else len(self.CONTEXT) - 1

            if key[K_DOWN]:
                self.index = self.index + 1 if self.index < len(self.CONTEXT) - 1 else 0

            # TODO: Change Game Ticks
            if key[K_LEFTBRACKET]:
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

            elif key[K_z]:
                key_position = (430, 200 + self.index * 40)
                if self.index == 2:
                    if self.speed_val > 30:
                        key = self.small_font.render(str(self.speed_val) + " " + "|" * 20, True, (0, 0, 0))
                        self.speed_val -= 5
                        self.blit(key, key_position)
                elif self.index == 3:
                    if self.volume_val > 30:
                        key = self.small_font.render(str(self.volume_val) + " " + "|" * 20, True, (0, 0, 0))
                        self.volume_val -= 5
                        self.blit(key, key_position)

            elif key[K_x]:
                key_position = (430, 200 + self.index * 40)
                if self.index == 2:
                    if self.speed_val < 100:
                        key = self.small_font.render(str(self.speed_val) + " " + "|" * 20, True, (0, 0, 0))
                        self.speed_val += 5
                        self.blit(key, key_position)
                elif self.index == 3:
                    if self.volume_val < 100:
                        key = self.small_font.render(str(self.volume_val) + " " + "|" * 20, True, (0, 0, 0))
                        self.volume_val += 5
                        self.blit(key, key_position)

            elif key[K_BACKSPACE]:
                self.return_screen()
