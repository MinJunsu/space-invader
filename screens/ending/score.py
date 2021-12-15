from pygame.constants import KEYDOWN, K_q, K_SPACE, K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.key import get_pressed

from screens import Screen, PAUSE_CONTEXT
from utils.file import File


class ScoreScreen(Screen):
    CONTEXT = PAUSE_CONTEXT
    CHOICE_COLOR = (249, 166, 2)
    UN_CHOICE_COLOR = (255, 255, 255)

    def __init__(self, size, set_screen, return_screen, score):
        super().__init__(size, set_screen, return_screen)
        self.score = str(score)
        self.alphabets = [chr(i) for i in range(65, 91)]
        self.name_index = [0, 0, 0]
        self.index = 0

    def draw(self):
        # Draw Title
        self.fill((0, 0, 0))
        title = self.big_font.render('NEW RECODE!', 1, (0, 255, 0))
        self.blit(title, (640 // 2 - title.get_width() // 2, 100))

        home = self.small_font.render('QUIT [Q]', 1, (255, 255, 255))
        self.blit(home, (10, 10))

        score_label = self.font.render('Your Score is', 1, (255, 255, 255))
        self.blit(score_label, (640 // 2 - score_label.get_width() // 2, 180))

        score = self.big_font.render(self.score.zfill(5), 1, (0, 255, 0))
        self.blit(score, (640 // 2 - score.get_width() // 2, 250))

        name_label = self.font.render('Save Your Name', 1, (255, 255, 255))
        self.blit(name_label, (640 // 2 - name_label.get_width() // 2, 320))

        for idx, name in enumerate(range(3)):
            if idx == self.index:
                text = self.font.render(self.alphabets[self.name_index[idx]], 1, self.CHOICE_COLOR)
            else:
                text = self.font.render(self.alphabets[self.name_index[idx]], 1, self.UN_CHOICE_COLOR)
            self.blit(text, (270 + (idx * 40), 380))

        save_label = self.font.render('Press [Enter] to Save', 1, (255, 255, 255))
        self.blit(save_label, (640 // 2 - save_label.get_width() // 2, 450))

    def get_event(self, event):
        if event.type == KEYDOWN:
            key = get_pressed()

            if key[K_q]:
                self.set_screen('main')

            if key[K_UP]:
                self.name_index[self.index] += 1
                if self.name_index[self.index] > len(self.alphabets) - 1:
                    self.name_index[self.index] = 0

            if key[K_DOWN]:
                self.name_index[self.index] -= 1
                if self.name_index[self.index] < 0:
                    self.name_index[self.index] = 0

            if key[K_RIGHT]:
                self.index += 1
                if self.index > 2:
                    self.index = 0

            if key[K_LEFT]:
                self.index -= 1
                if self.index < 0:
                    self.index = 0

            if key[K_SPACE]:
                File.save_data(new_score={
                    'player': ''.join([self.alphabets[i] for i in self.name_index]),
                    'score': int(self.score)
                })
                self.set_screen('ending_clear')
