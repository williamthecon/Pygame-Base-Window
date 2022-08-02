import pygame as pg
from settings import update_settings, save_settings
from taskbar import Taskbar
import os

class Window:
    def __init__(self):
        self.settings = update_settings()

        self.screen = pg.display.set_mode((self.settings["screen.width"], self.settings["screen.height"]), pg.NOFRAME)
        pg.display.set_caption(self.settings["title"])

        self.taskbar = Taskbar(self)

    def update(self):
        self.taskbar.update()
