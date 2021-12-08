from pygame.constants import KEYDOWN, K_BACKSPACE
from pygame.key import get_pressed

from screens import Screen, SCORE_CONTEXT


class ScoreScreen(Screen):
    CONTEXT = SCORE_CONTEXT

    def __init__(self, size, set_screen, return_screen):
        super(ScoreScreen, self).__init__(size, set_screen, return_screen)

    def draw(self):
        # Draw Title
        title = self.big_font.render('SCORES', 1, (0, 0, 255))

        self.blit(title, (640 // 2 - title.get_width() // 2, 100))

        # Draw Return Home
        home = self.small_font.render('Home [BACKSPACE]', 1, (255, 255, 255))
        self.blit(home, (10, 10))

        # Draw Score
        for idx, element in enumerate(self.CONTEXT):
            name = self.font.render(element['name'], 1, (255, 255, 255))
            key = self.font.render(element['key'], 1, (255, 0, 0))

            name_position = (100, 200 + idx * 40)
            key_position = (400, 200 + idx * 40)
            self.blit(name, name_position)
            self.blit(key, key_position)

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()

            if key[K_BACKSPACE]:
                self.set_screen('main')