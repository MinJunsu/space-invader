from pygame.constants import KEYDOWN, K_BACKSPACE
from pygame.key import get_pressed

from screens import Screen, HELP_CONTEXT
from utils.file import File


class ScoreScreen(Screen):
    CONTEXT = HELP_CONTEXT

    def __init__(self, size, set_screen, return_screen):
        super().__init__(size, set_screen, return_screen)
        self.scores = File.load_data().items()

    def draw(self):
        title = self.big_font.render('Score', 1, (0, 0, 255))
        self.blit(title, (640 // 2 - title.get_width() // 2, 100))

        # Draw Return Home
        home = self.small_font.render('Home [BACKSPACE]', 1, (255, 255, 255))
        self.blit(home, (10, 10))

        # Draw Summary
        for idx, element in enumerate(self.scores):
            text = self.middle_font.render(f"{idx + 1}.  {element[0]} - {element[1]}", 1, (255, 255, 255))
            text_position = ((640 - text.get_width())//2, 180 + idx * 40)
            self.blit(text, text_position)

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()

            if key[K_BACKSPACE]:
                self.set_screen('main')
