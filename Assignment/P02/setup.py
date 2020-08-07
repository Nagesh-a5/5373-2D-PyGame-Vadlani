import os
import pygame as pg
import constants as c
import tools


###Game Setup
###Load Images, Allow events
pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

GFX = tools.load_all_gfx(os.path.join("resources","graphics"))