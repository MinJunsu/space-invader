from pygame.constants import KEYDOWN, K_SPACE
from pygame.key import get_pressed

from screens import TextBaseScreen, EXPLAIN_CONTEXT


class DyingScreen(TextBaseScreen):
    CONTEXT = EXPLAIN_CONTEXT

    def __init__(self, size, set_screen, return_screen):
        super().__init__(size, set_screen, return_screen, 'dying')

    def draw(self):
        # TODO: 적절한 이미지 넣기
        # solider = self.get_image('solider.png')

        start = self.small_font.render("Press [SPACE] to return Main!!", 1, (255, 255, 255))
        self.blit(start, (640 // 2 - start.get_width() // 2, 450))

        super().draw()

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()

            if key[K_SPACE]:
                self.set_screen('main')

