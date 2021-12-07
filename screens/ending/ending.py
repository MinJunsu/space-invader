from pygame.constants import KEYDOWN, K_SPACE
from pygame.key import get_pressed

from screens import Screen, ENDING_CONTEXT

from pygame.sprite import Group, GroupSingle
from models import BackGround

class ClearScreen(Screen):
    CONTEXT = ENDING_CONTEXT

    def __init__(self, size, set_screen, return_screen):
        super(ClearScreen, self).__init__(size, set_screen, return_screen)
        self.background = Group()
        self.sound = self.set_sound('clear.mp3')
        self.sound.play()
        self.frame = 0

        background = BackGround()
        background.set_images('clear')

        self.background.empty()
        self.background.add(background)

    def draw(self):
        self.background.draw(self)
        self.background.update()

        for idx, element in enumerate(self.CONTEXT):
            name = self.font.render(element['text'], 1, (255, 255, 255))

            name_position = (100 + idx * 80, 360 + idx * 80)
            self.blit(name, name_position)

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()

            if key[K_SPACE]:
                self.set_screen('main')