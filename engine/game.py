import sys

import pygame
from pygame import display
from pygame.time import Clock
from pygame.constants import QUIT

from .screen import ScreenManager
from utils.constants import game_tick


class GameManager:
    SCREEN_SIZE = (640, 480)

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.frame = display.set_mode(self.SCREEN_SIZE)
        self.screen_manager = ScreenManager()
        self.clock = Clock()
        self.run = True
        self.tick = game_tick()

    def update(self):
        self.screen_manager.run()
        display.update()

    def play(self):
        while self.run:
            self.clock.tick(self.tick.get())
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                self.screen_manager.push(event)

            self.frame.fill((0, 0, 0))

            self.frame.blit(self.screen_manager.screen, (0, 0))

            self.update()
