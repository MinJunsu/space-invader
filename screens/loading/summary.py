from pygame.constants import KEYDOWN, K_BACKSPACE
from pygame.key import get_pressed

from screens import Screen, SUMMARY_CONTEXT


class SummaryScreen(Screen):
    CONTEXT = SUMMARY_CONTEXT

    def __init__(self, size, set_screen, return_screen):
        super().__init__(size, set_screen, return_screen)
        self.big_font = self.get_font('elice.ttf', 30)
        self.middle_font = self.get_font('elice.ttf', 30)
        self.small_font = self.get_font('elice.ttf', 20)

    def draw(self):
        # Draw Title
        title = self.big_font.render('Summary', 1, (0, 0, 255))
        self.blit(title, (640 // 2 - title.get_width() // 2, 100))

        # Draw Return Home
        home = self.small_font.render('Home [BACKSPACE]', 1, (255, 255, 255))
        self.blit(home, (10, 10))

        # Draw Summary
        for idx, element in enumerate(self.CONTEXT):
            text = self.middle_font.render(element['text'], 1, (255, 255, 255))
            text_position = ((640 - text.get_width())//2, 180 + idx * 60)
            self.blit(text, text_position)

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()

            if key[K_BACKSPACE]:
                self.set_screen('main')
