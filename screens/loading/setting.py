from pygame.constants import KEYDOWN, K_LESS, K_GREATER, K_LEFTBRACKET, K_RIGHTBRACKET, K_m, K_BACKSPACE, K_z, K_x, K_MINUS, K_UP, K_DOWN, K_z, K_x
from pygame.key import get_pressed

from screens import Screen, SETTING_CONTEXT
from engine.sound import SoundManager
from utils.constants import game_tick


class SettingScreen(Screen):
    CONTEXT = SETTING_CONTEXT

    CHOICE_COLOR = (249, 166, 2)
    UN_CHOICE_COLOR = (255, 255, 255)

    def __init__(self, size, set_screen, return_screen):
        super(SettingScreen, self).__init__(size, set_screen, return_screen)
        self.index = 0
        self.sound_manager = SoundManager()
        self.tick = game_tick()

    def draw(self):
        self.fill((0, 0, 0))
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

            name_position = (70, 180 + idx * 40)
            key_position = (430, 180 + idx * 40)

            key = self.small_font.render(element['key'], 1, (0, 255, 0))

            speed_label = self.small_font.render('SOUND', 1, (0, 255, 255))
            sound_label = self.small_font.render('SPEED', 1, (0, 255, 255))

            self.blit(speed_label, (100, 380))
            self.blit(sound_label, (450, 380))
            self.blit(self.small_font.render('|' * int(self.sound_manager.get_volume() / 0.05), 1, (0, 255, 0)), (85, 405))
            self.blit(self.small_font.render('|' * int(self.tick.get() / 5), 1, (0, 255, 0)), (435, 405))

            self.blit(name, name_position)
            self.blit(key, key_position)

    def get_event(self, event):
        key = get_pressed()
        if event.type == KEYDOWN:
            if key[K_UP]:
                self.index = self.index - 1 if self.index > 0 else len(self.CONTEXT) - 1

            if key[K_DOWN]:
                self.index = self.index + 1 if self.index < len(self.CONTEXT) - 1 else 0

            if key[K_LEFTBRACKET]:
                self.tick.down()

            elif key[K_RIGHTBRACKET]:
                self.tick.up()

            elif key[K_m]:
                self.sound_manager.mute()

            elif key[K_x]:
                self.sound_manager.volume_up()

            elif key[K_z]:
                self.sound_manager.volume_down()

            elif key[K_BACKSPACE]:
                self.return_screen()
