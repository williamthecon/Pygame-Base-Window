import pygame as pg
from settings import update_settings, save_settings
from funcs import end
from window import Window
from time import perf_counter, sleep

pg.init()

settings = update_settings()

desktop_size = list(pg.display.get_desktop_sizes()[0])
settings["screen.width"] = desktop_size[0]
settings["screen.height"] = desktop_size[1]
settings = save_settings(settings)

window = Window()

clock = pg.time.Clock()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end(f"Manual exit by pressing the close button after {perf_counter()}s")

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                end(f"Manual exit by pressing 'esc' after {perf_counter()}s")

        if event.type == pg.VIDEORESIZE:
            window.resize(event.w, event.h)

    window.screen.fill(settings["screen.background-color"])

    window.update()

    pg.display.update()

    clock.tick(settings["fps"])
