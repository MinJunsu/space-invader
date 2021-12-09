from pathlib import Path
import os

from pygame import Surface, image
from pygame.font import Font
from pygame.mixer import Sound


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

