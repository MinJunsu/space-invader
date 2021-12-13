from pygame.constants import KEYDOWN, K_s, K_ESCAPE
from pygame.key import get_pressed

from screens import Screen, PAUSE_CONTEXT
from utils.file import File


class ScoreScreen(Screen):
    CONTEXT = PAUSE_CONTEXT

    def __init__(self, size, set_screen, return_screen):
        super().__init__(size, set_screen, return_screen)
        self.score = str(1000)
        print(File.load_data())

    def draw(self):
        # Draw Title
        title = self.big_font.render('SCORE', 1, (0, 255, 0))
        self.blit(title, (640 // 2 - title.get_width() // 2, 100))

        # Draw Score
        for idx, element in enumerate(self.CONTEXT):
            name = self.font.render(element['text'], 1, (255, 255, 255))

            name_position = (100 + idx * 80, 200 + idx * 80)
            self.blit(name, name_position)

        score = self.big_font.render(self.score.zfill(5), 1, (0, 255, 0))
        self.blit(score, (640 // 2 - title.get_width() // 2, 350))

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()
            if key[K_ESCAPE]:
                self.return_screen()

            if key[K_s]:
                self.set_screen('main')
