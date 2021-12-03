from pygame.key import get_pressed
from pygame.constants import K_SPACE, K_UP, K_DOWN, QUIT, KEYDOWN
from pygame.sprite import GroupSingle

from screens.base import Screen
from screens import LOADING_CONTEXT


class LoadingScreen(Screen):
    CONTEXT = LOADING_CONTEXT

    CHOICE_COLOR = (249, 166, 2)
    UN_CHOICE_COLOR = (255, 255, 255)

    def __init__(self, size, set_screen, return_screen):
        super(LoadingScreen, self).__init__(size, set_screen, return_screen)
        self.index = 0

    def draw(self):
        # 기본 배경 이미지 그리기
        for idx, element in enumerate(self.CONTEXT):
            if idx == self.index:
                label = self.big_font.render(element['text'], 1, self.CHOICE_COLOR)
            else:
                label = self.big_font.render(element['text'], 1, self.UN_CHOICE_COLOR)
            # FIXME: height 와 width 변수로 받기
            position = (640 // 2 - label.get_width() // 2, 210 + idx * 40)
            self.blit(label, position)

    def get_event(self, event):
        key = get_pressed()
        if event.type == KEYDOWN:
            if key[QUIT]:
                quit()

            if key[K_UP]:
                self.index = self.index - 1 if self.index > 0 else len(self.CONTEXT) - 1

            if key[K_DOWN]:
                self.index = self.index + 1 if self.index < len(self.CONTEXT) - 1 else 0

            if key[K_SPACE]:
                self.set_screen(self.CONTEXT[self.index]['action'])
