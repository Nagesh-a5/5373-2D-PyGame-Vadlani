import pygame as pg
import tools
import setup
import constants as c
from components import info


### Handle Menu
class Menu(tools.State):
    def __init__(self):
        tools.State.__init__(self)

        ### Initialize Game state
        persist = {c.COIN_TOTAL: 0,
                   c.SCORE: 0,
                   c.LIVES: 1,
                   c.TOP_SCORE: 0,
                   c.CURRENT_TIME: 0.0,
                   c.LEVEL_NUM: 1,
                   c.PLAYER_NAME: c.PLAYER_MARIO}
        self.startup(0.0, persist)
    
    def startup(self, current_time, persist):
        self.next = c.LEVEL
        self.persist = persist
        self.game_info = persist
        self.overhead_info = info.Info(self.game_info, c.MAIN_MENU)
        self.setup_background()
        self.setup_player()
        
    def setup_background(self):
        ### Setup Background pictures and lables
        self.background = setup.GFX['level']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                    (int(self.background_rect.width*c.BACKGROUND_MULTIPLER),
                                    int(self.background_rect.height*c.BACKGROUND_MULTIPLER)))

        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

    def setup_player(self):
        self.player_list = []
        self.player_index = 0

    ### Handle Updating
    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = self.current_time

        ### Handle Return pressed (Start when press return key)
        self.update_keys(keys)
        self.overhead_info.update(self.game_info)
        surface.blit(self.background, self.viewport, self.viewport)
        self.overhead_info.draw(surface)

        ### Handle mouse hover event
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if 320+150 > mouse[0] > 320 and 260+70 > mouse[1] > 260:
            loadimg = pg.image.load('resources/graphics/start_hover.png')
            surface.blit(loadimg, (320,260))
            if click[0]:
                self.done = True

    ### Handle return key
    def update_keys(self, keys):
        if keys[pg.K_RETURN]:
            self.reset_game_info()
            self.done = True
    
    def reset_game_info(self):
        self.game_info[c.COIN_TOTAL] = 0
        self.game_info[c.SCORE] = 0
        self.game_info[c.LIVES] = 1
        self.game_info[c.CURRENT_TIME] = 0.0
        self.game_info[c.LEVEL_NUM] = 1
        
        self.persist = self.game_info
