from pathlib import Path
import os

from pygame import Surface, image
from pygame.font import Font
from pygame.mixer import Sound
from pygame.sprite import GroupSingle

from models import BackGround


class Screen(Surface):
    BASE_PATH = Path(__file__).resolve().parent.parent
    IMAGE_PATH = os.path.join(BASE_PATH, 'assets', 'graphics')
    FONT_PATH = os.path.join(BASE_PATH, 'assets', 'fonts')
    SOUND_PATH = os.path.join(BASE_PATH, 'assets', 'sounds')

    def __init__(self, size, set_screen, return_screen):
        super(Screen, self).__init__(size)
        self.font = self.get_font("edit_undo.ttf", 30)
        self.big_font = self.get_font("edit_undo.ttf", 40)
        self.middle_font = self.get_font('edit_undo.ttf',25)
        self.small_font = self.get_font("edit_undo.ttf", 20)
        self.set_screen = set_screen
        self.return_screen = return_screen
        self.sound = None

    def set_sound(self, name):
        return Sound(os.path.join(self.SOUND_PATH, name))

    def get_image(self, name):
        return image.load(os.path.join(self.IMAGE_PATH, name))

    def get_font(self, name, size):
        return Font(os.path.join(self.FONT_PATH, name), size)

    def run(self):
        self.draw()

    def draw(self):
        pass

    def get_event(self, event):
        """
        Implement When you get event in Surface
        """


class TextBaseScreen(Screen):
    CONTEXT = None

    def __init__(self, size, set_screen, return_screen, category):
        super().__init__(size, set_screen, return_screen)
        self.count = 0
        self.index = 0
        self.big_font = self.get_font('elice.ttf', 50)
        self.middle_font = self.get_font('elice.ttf', 20)
        self.font = self.get_font('elice.ttf', 15)
        self.context = self.CONTEXT.get(category)
        self.sound = self.set_sound('explain.wav')
        self.sound.play(-1)
        self.background = GroupSingle()
        self.category = category

    def draw(self):
        # Draw Title
        title = self.big_font.render(f"STAGE {self.context['stage']}", 1, (255, 255, 255))
        self.blit(title, (640 // 2 - title.get_width() // 2, 50))

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

        self.update()

    def set_background(self, name):
        background = BackGround()
        background.set_images(name)
        self.background.add(background)

    def update(self):
        self.background.update()
