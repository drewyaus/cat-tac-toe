#!/usr/bin/env python
""" Cat-tac-toe
"""

import os

# import basic pygame modules
import pygame as pg

SCREENRECT = pg.Rect(0, 0, 335 * 3, 186 * 3)

main_dir = os.path.split(os.path.abspath(__file__))[0]

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 600:
            self.pos.left = 0

def load_image(file):
    """ loads an image, prepares it for play
    """
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()


def main(winstyle=0):
    # Initialize pygame
    if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 1024)
    pg.init()

    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    bgdtile = load_image("shelter.jpg")
    background = pg.Surface(SCREENRECT.size)
    for y in range(0, SCREENRECT.height, bgdtile.get_height()):
        for x in range(0, SCREENRECT.width, bgdtile.get_width()):
            background.blit(bgdtile, (x, y))
    screen.blit(background, (0, 0))
    pg.display.flip()

    black = load_image("black.png")
    white = load_image("white.png")

    try:
        going = True
        while going:

            # wait for events before doing anything.
            # events = [pg.event.wait()] + pg.event.get()
            events = pg.event.get()

            for e in events:
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_ESCAPE:
                        going = False
                    # elif e.key == pg.K_DOWN:
                    #     scroll_view(screen, image, DIR_DOWN, view_rect)
                    # elif e.key == pg.K_UP:
                    #     scroll_view(screen, image, DIR_UP, view_rect)
                    # elif e.key == pg.K_LEFT:
                    #     scroll_view(screen, image, DIR_LEFT, view_rect)
                    # elif e.key == pg.K_RIGHT:
                    #     scroll_view(screen, image, DIR_RIGHT, view_rect)
                elif e.type == pg.QUIT:
                    going = False
                elif e.type == pg.MOUSEBUTTONDOWN:

                # elif e.type == pg.MOUSEBUTTONDOWN:
                #     direction = regions.get_at(e.pos)[0]
                # elif e.type == pg.MOUSEBUTTONUP:
                #     direction = None

            # if direction:
            #     scroll_view(screen, image, direction, view_rect)
            # clock.tick(30)

    finally:
        # pg.key.set_repeat(old_k_delay, old_k_interval)
        pg.quit()


# call the "main" function if running this script
if __name__ == "__main__":
    main()
