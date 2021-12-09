from pygame.constants import KEYDOWN, K_SPACE
from pygame.key import get_pressed

from screens import TextBaseScreen, EXPLAIN_CONTEXT


class DyingScreen(TextBaseScreen):
    CONTEXT = EXPLAIN_CONTEXT['dying']

    def __init__(self, size, set_screen, return_screen):
        super().__init__(size, set_screen, return_screen, 'dying')
        self.set_background('dying')

    def draw(self):
        self.background.draw(self)

        title = self.big_font.render("GAME OVER", 1, (255, 255, 255))
        self.blit(title, (640 // 2 - title.get_width() // 2, 30))

        for idx, element in enumerate(self.CONTEXT['text']):
            # print(element)
            text = self.middle_font.render(element, 1, (200, 30, 30))
            text_position = ((640 - text.get_width())//2, 160 + idx * 40)
            self.blit(text, text_position)

        start = self.small_font.render("Press [SPACE] to return Score", 1, (255, 255, 255))
        self.blit(start, (640 // 2 - start.get_width() // 2, 450))
        self.update()

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()

            if key[K_SPACE]:
                self.set_screen('main')

