from pygame.constants import KEYDOWN, K_SPACE
from pygame.key import get_pressed
from pygame.sprite import GroupSingle

from models import BackGround
from screens import Screen, EXPLAIN_CONTEXT


class _TextBaseScreen(Screen):
    def __init__(self, size, set_screen, return_screen, category):
        super().__init__(size, set_screen, return_screen)
        self.count = 0
        self.index = 0
        self.big_font = self.get_font('elice.ttf', 50)
        self.font = self.get_font('elice.ttf', 15)
        self.sound = self.set_sound('explain.wav')
        self.background = GroupSingle()
        background = BackGround()
        background.set_images('clear')
        self.background.add(background)
        self.context = EXPLAIN_CONTEXT.get(category)

    def draw(self):
        self.background.draw(self)

        # Draw Title
        title = self.big_font.render(f"STAGE {self.context['stage']}", 1, (255, 255, 255))
        self.blit(title, (640 // 2 - title.get_width() // 2, 50))

        start = self.small_font.render("Press [SPACE] to play Game!!", 1, (255, 255, 255))
        self.blit(start, (640 // 2 - start.get_width() // 2, 450))
        self.update()

    def update(self):
        self.background.update()

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()

            if key[K_SPACE]:
                self.return_screen()
                self.sound.stop()


class DyingScreen(_BaseScreen):
    def __init__(self, size, set_screen, return_screen):
        super().__init__(size, set_screen, return_screen, 'dying')


class ClearScreen(_BaseScreen):
    def __init__(self, size, set_screen, return_screen):
        super().__init__(size, set_screen, return_screen, 'clear')
