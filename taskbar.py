import pygame as pg
from settings import update_settings
from funcs import inbetween, end
from time import perf_counter, sleep

pg.font.init()

class Taskbar:
    def __init__(self, window):
        self.window = window

        self.hover = None
        self.mouse_last_pressed = pg.mouse.get_pressed()
        self.mouse_last_pos = pg.mouse.get_pos()

        self.update()

    def define(self):
        self.settings = update_settings()

        top = left = 0
        width = self.settings["screen.width"]
        height = self.settings["taskbar.height"]

        self.top = top
        self.left = left
        self.topleft = (left, top)
        self.bottom = top + height
        self.right = left + width
        self.bottomright = (self.right, self.bottom)
        self.topright = (self.right, top)
        self.bottomleft = (left, self.bottom)
        self.width = width
        self.height = height

        self.hover = None

        self.font = pg.font.match_font(self.settings["taskbar.title.font.name"])
        if self.font is None:
            raise Exception(f"Invalid font name: \'{self.settings['taskbar.title.font.name']}\'")

        self.font = pg.font.Font(self.font, self.settings["taskbar.title.font.size"])

    def check(self):
        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()

        self.hover = None

        tcbt = self.settings["taskbar.close.button-topleft"]
        tcbt = [self.settings["screen.width"] + tcbt[0], tcbt[1]]

        tmbt = self.settings["taskbar.minimize.button-topleft"]
        tmbt = [self.settings["screen.width"] + tmbt[0], tmbt[1]]

        if inbetween(pos, topleft=tcbt, bottomright=self.bottomright):
            self.hover = "close"
            if pressed[0] and pressed[0] != self.mouse_last_pressed[0]:
                end(f"Manual exit by pressing the exit button after '{perf_counter()}s'")
        if inbetween(pos, topleft=tmbt, bottomright=[tcbt[0] - 1, tcbt[1] + self.settings["taskbar.height"]]):
            self.hover = "minimize"
            if pressed[0] and pressed[0] != self.mouse_last_pressed[0]:
                pg.display.iconify()


        self.mouse_last_pressed = pressed
        self.mouse_last_pos = pos

    def draw(self):
        # background
        pg.draw.rect(self.window.screen, self.settings["taskbar.background-color"] if pg.key.get_focused() else self.settings["taskbar.off-background-color"], (self.top, self.left, self.width, self.height))

        # hover
        if self.hover:
            tabt = self.settings[f"taskbar.{self.hover}.button-topleft"]
            tabt = [self.settings["screen.width"] + tabt[0], tabt[1]]
            w = 40
            h = 30
            pg.draw.rect(self.window.screen, self.settings["taskbar.hover-background-color"], (tabt[0], tabt[1], w, h))

        # close img
        surf = pg.transform.scale(pg.image.load(self.settings["taskbar.close.img-path"]), self.settings["taskbar.close.size"])
        tcit = self.settings["taskbar.close.img-topleft"]
        tcit = [self.settings["screen.width"] + tcit[0], tcit[1]]
        self.window.screen.blit(surf, tcit)

        # minimize img
        surf = pg.transform.scale(pg.image.load(self.settings["taskbar.minimize.img-path"]), self.settings["taskbar.minimize.size"])
        tmit = self.settings["taskbar.minimize.img-topleft"]
        tmit = [self.settings["screen.width"] + tmit[0], tmit[1]]
        self.window.screen.blit(surf, tmit)

        # title
        text = self.font.render(self.settings["taskbar.title.name"], True, self.settings["taskbar.title.font.color"])
        rect = text.get_rect()
        topleft = (self.settings["taskbar.title.x-pad"], self.settings["taskbar.height"] / 2 - rect.height / 2)
        self.window.screen.blit(text, topleft)

    def update(self):
        self.define()
        self.check()
        self.draw()
