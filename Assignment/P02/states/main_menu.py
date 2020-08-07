import pygame as pg
import tools
import setup
import constants as c
from components import info

class Menu(tools.State):
    def __init__(self):
        tools.State.__init__(self)
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
        self.setup_cursor()
        
    def setup_background(self):
        self.background = setup.GFX['level']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                    (int(self.background_rect.width*c.BACKGROUND_MULTIPLER),
                                    int(self.background_rect.height*c.BACKGROUND_MULTIPLER)))

        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

    def setup_player(self):
        self.player_list = []
        self.player_index = 0

    def setup_cursor(self):
        self.cursor = pg.sprite.Sprite()
        self.cursor.image = tools.get_image(setup.GFX[c.ITEM_SHEET], 24, 160, 8, 8, c.BLACK, 3)
        rect = self.cursor.image.get_rect()
        rect.x, rect.y = (220, 358)
        self.cursor.rect = rect
        self.cursor.state = c.PLAYER1

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = self.current_time
        self.update_cursor(keys)
        self.overhead_info.update(self.game_info)
        surface.blit(self.background, self.viewport, self.viewport)
        self.overhead_info.draw(surface)
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if 320+150 > mouse[0] > 320 and 260+70 > mouse[1] > 260:
            loadimg = pg.image.load('resources/graphics/start_hover.png')
            surface.blit(loadimg, (320,260))
            if click[0]:
                self.done = True

    def update_cursor(self, keys):
        if self.cursor.state == c.PLAYER1:
            self.cursor.rect.y = 358
            if keys[pg.K_DOWN]:
                self.cursor.state = c.PLAYER2
                self.player_index = 1
                self.game_info[c.PLAYER_NAME] = c.PLAYER_LUIGI
        elif self.cursor.state == c.PLAYER2:
            self.cursor.rect.y = 403
            if keys[pg.K_UP]:
                self.cursor.state = c.PLAYER1
                self.player_index = 0
                self.game_info[c.PLAYER_NAME] = c.PLAYER_MARIO
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
