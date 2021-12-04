from pygame.constants import KEYDOWN, K_SPACE
from pygame.key import get_pressed

from screens import TextBaseScreen, EXPLAIN_CONTEXT


class _BeginBaseScreen(TextBaseScreen):
    CONTEXT = EXPLAIN_CONTEXT

    def __init__(self, size, set_screen, return_screen, num):
        super().__init__(size, set_screen, return_screen, 'begin')
        self.context = self.context[num]

    def draw(self):
        solider = self.get_image('solider.png')
        self.blit(solider, (30, 100))

        start = self.small_font.render("Press [SPACE] to Next Level!!", 1, (255, 255, 255))
        self.blit(start, (640 // 2 - start.get_width() // 2, 450))

        super().draw()

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()

            if key[K_SPACE]:
                self.return_screen()
                self.sound.stop()


class BeginFirstScreen(_BeginBaseScreen):
    def __init__(self, size, set_screen, return_screen):
        super().__init__(size, set_screen, return_screen, 0)


class BeginSecondScreen(_BeginBaseScreen):
    def __init__(self, size, set_screen, return_screen):
        super().__init__(size, set_screen, return_screen, 1)


class BeginThirdScreen(_BeginBaseScreen):
    def __init__(self, size, set_screen, return_screen):
        super().__init__(size, set_screen, return_screen, 2)
