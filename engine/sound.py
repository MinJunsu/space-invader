from pathlib import Path
import os

from pygame.mixer import Sound

from utils import Singleton


class SoundManager(Singleton):
    BASE_DIR = Path(__file__).resolve().parent.parent
    SOUND_ROOT = os.path.join(BASE_DIR, 'assets', 'sounds')

    def __init__(self):
        super().__init__()
        try:
            self.sounds = self.instance.sounds
            self.volume = self.instance.volume
        except AttributeError:
            self.instance.sounds = dict()
            self.instance.volume = 1
        finally:
            self.sounds = self.instance.sounds
            self.volume = self.instance.volume

    def get(self, key):
        if self.sounds.get(key):
            return self.sounds.get(key)
        else:
            return self.set(key)

    def set(self, key):
        self.sounds[key] = self.set_sound(key)
        return self.sounds.get(key)

    def set_sound(self, key):
        print(self.volume)
        sound = Sound(os.path.join(self.SOUND_ROOT, key))
        sound.set_volume(self.volume)
        return sound

    def volume_up(self):
        self.volume += 0.05
        if self.volume > 1:
            self.volume = 1
        self.set_volume()

    def volume_down(self):
        self.volume -= 0.05
        if self.volume < 0:
            self.volume = 0
        self.set_volume()

    def set_volume(self):
        for sound in self.sounds.keys():
            self.sounds.get(sound).set_volume(self.volume)

    def mute(self):
        self.volume = 0
        for sound in self.sounds.keys():
            self.sounds.get(sound).set_volume(self.volume)
