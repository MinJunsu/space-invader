from pygame.constants import KEYDOWN, K_SPACE
from pygame.key import get_pressed

from pygame.sprite import GroupSingle

from models import BackGround
from screens import Screen, EXPLAIN_CONTEXT


class ExplainScreen(Screen):
    def __init__(self, size, set_screen, return_screen, category, num):
        super(ExplainScreen, self).__init__(size, set_screen, return_screen)
        self.count = 0
        self.index = 0
        self.big_font = self.get_font('elice.ttf', 50)
        self.font = self.get_font('elice.ttf', 15)
        self.context = EXPLAIN_CONTEXT.get(category)[num]
        self.sound = self.set_sound('explain.wav')
        self.sound.play(-1)
        self.background = GroupSingle()

    def draw(self):
        # Draw Title
        title = self.big_font.render(f"STAGE {self.context['stage']}", 1, (255, 255, 255))
        self.blit(title, (640 // 2 - title.get_width() // 2, 50))

        # Draw Solider Icon
        solider = self.get_image('solider.png')
        self.blit(solider, (30, 100))

        for idx, element in enumerate(self.context['text']):
            self.count += 1
            if self.index > idx:
                text = self.font.render(element, 1, (255, 255, 255))
                position = (280, 130 + 35 * idx)
                self.blit(text, position)

            elif self.index == idx:
                text = self.font.render(element[0:self.count], 1, (255, 255, 255))
                position = (280, 130 + 35 * idx)
                self.blit(text, position)
                if element[0:self.count] == element:
                    self.index += 1
                    self.count = 0

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

