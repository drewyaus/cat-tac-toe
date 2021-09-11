#!/usr/bin/env python
""" Cat-tac-toe
"""

import os

# import basic pygame modules
import pygame as pg

SCREENRECT = pg.Rect(0, 0, 335 * 3, 186 * 3)

main_dir = os.path.split(os.path.abspath(__file__))[0]

# sam's comment

class GameObject:
    def __init__(self, image, position):
        self.image = image
        self.pos = position
        print("created {0} at {1}".format(image, position))

    def move(self, position):
        self.pos = position


def load_image(file):
    """ loads an image, prepares it for play
    """
    path = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(path)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()


def scale_image(file, scale):
    """ scales an image, prepares it for play
    """
    path = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(path)
        surface = pg.transform.rotozoom(surface, 0, scale)
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

    black = scale_image("black.png", 0.1)
    white = load_image("white.png")

    try:
        going = True
        while going:

            # wait for events before doing anything.
            events = pg.event.get()

            for e in events:
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_ESCAPE:
                        going = False
                elif e.type == pg.QUIT:
                    going = False
                elif e.type == pg.MOUSEBUTTONDOWN:
                    player = GameObject(black, e.pos)
                    screen.blit(player.image, e.pos)

            pg.display.update()

    finally:
        pg.quit()


# call the "main" function if running this script
if __name__ == "__main__":
    main()
