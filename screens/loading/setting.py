from pygame.constants import KEYDOWN, K_h, K_UP, K_DOWN, K_m, K_BACKSPACE, K_LEFT, K_RIGHT
from pygame.key import get_pressed

from engine.sound import SoundManager
from utils.constants import game_tick
from screens import Screen, SETTING_CONTEXT


class SettingScreen(Screen):
    CONTEXT = SETTING_CONTEXT

    def __init__(self, size, set_screen, return_screen):
        super(SettingScreen, self).__init__(size, set_screen, return_screen)
        self.sound_manager = SoundManager()
        self.set_sound('menu.wav')
        self.tick = game_tick()

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

            elif key[K_DOWN]:
                self.tick.down()

            elif key[K_UP]:
                print("123")
                self.tick.up()

            # TODO: Mute Audio
            elif key[K_m]:
                self.sound_manager.mute()

            # TODO: Change Audio Volume
            elif key[K_RIGHT]:
                self.sound_manager.volume_up()

            elif key[K_LEFT]:
                self.sound_manager.volume_down()

            elif key[K_BACKSPACE]:
                self.set_screen('main')

        print(self.sound_manager.volume)
