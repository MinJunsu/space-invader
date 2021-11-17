from pygame.event import get
from pygame import QUIT, KEYUP, K_UP, K_DOWN, K_SPACE

from .base import Screen


class LoadingScreen(Screen):
    CONTEXT = [
        {
            'text': 'PLAY',
            'action': 'P'
        },
        {
            'text': 'SCORES',
            'action': 'S'
        },
        {
            'text': 'SUMMARY',
            'action': 'L'
        },
        {
            'text': 'SETTING [C]',
            'action': 'C'
        }
    ]
    CHOICE_COLOR = (249, 166, 2)
    UN_CHOICE_COLOR = (255, 255, 255)

    def __init__(self, size, set_screen):
        super(LoadingScreen, self).__init__(size)
        self.index = 0
        self.set_screen = set_screen

    def run(self):
        self.draw()

    def draw(self):
        # 기본 배경 이미지 그리기
        for idx, element in enumerate(self.CONTEXT):
            if idx == self.index:
                label = self.font.render(element['text'], 1, self.CHOICE_COLOR)
            else:
                label = self.font.render(element['text'], 1, self.UN_CHOICE_COLOR)
            # FIXME: height 와 width 변수로 받기
            position = (640 // 2 - label.get_width() // 2, 210 + idx * 40)
            self.blit(label, position)

    def get_event(self, event):
        if event.type == QUIT:
            quit()
        if event.type == KEYUP:
            if event.key == K_UP:
                self.index = self.index - 1 if self.index < len(self.CONTEXT) else len(self.CONTEXT)
            if event.key == K_DOWN:
                self.index = self.index + 1 if self.index < len(self.CONTEXT) else 0
            if event.key == K_SPACE:
                self.set_screen(self.index)
        else:
            return None
