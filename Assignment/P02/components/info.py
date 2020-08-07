import pygame as pg
import setup, tools
import constants as c
from . import coin

class Character(pg.sprite.Sprite):
    def __init__(self, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        

### Info  Handle labels and images to display
class Info():
    def __init__(self, game_info, state):
        self.coin_total = game_info[c.COIN_TOTAL]
        self.total_lives = game_info[c.LIVES]
        self.state = state
        self.game_info = game_info
        
        self.create_font_image_dict()
        self.create_info_labels()
        self.create_state_labels()
        self.flashing_coin = coin.FlashCoin(280, 53)
        
    ###Get Characters from images
    def create_font_image_dict(self):
        self.image_dict = {}
        image_list = []
        
        image_rect_list = [# 0 - 9
                           (3, 230, 7, 7), (12, 230, 7, 7), (19, 230, 7, 7),
                           (27, 230, 7, 7), (35, 230, 7, 7), (43, 230, 7, 7),
                           (51, 230, 7, 7), (59, 230, 7, 7), (67, 230, 7, 7),
                           (75, 230, 7, 7), 
                           # A - Z
                           (83, 230, 7, 7), (91, 230, 7, 7), (99, 230, 7, 7),
                           (107, 230, 7, 7), (115, 230, 7, 7), (123, 230, 7, 7),
                           (3, 238, 7, 7), (11, 238, 7, 7), (20, 238, 7, 7),
                           (27, 238, 7, 7), (35, 238, 7, 7), (44, 238, 7, 7),
                           (51, 238, 7, 7), (59, 238, 7, 7), (67, 238, 7, 7),
                           (75, 238, 7, 7), (83, 238, 7, 7), (91, 238, 7, 7),
                           (99, 238, 7, 7), (108, 238, 7, 7), (115, 238, 7, 7),
                           (123, 238, 7, 7), (3, 246, 7, 7), (11, 246, 7, 7),
                           (20, 246, 7, 7), (27, 246, 7, 7), (48, 246, 7, 7),
                           # -*
                           (68, 249, 6, 2), (75, 247, 6, 6)]
                           
        character_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*'
        
        for character, image_rect in zip(character_string, image_rect_list):
            self.image_dict[character] = tools.get_image(setup.GFX['text_images'], 
                                            *image_rect, (92, 148, 252), 2.9)
    ###  Info Labels
    def create_info_labels(self):
        self.score_text = []
        self.coin_count_text = []
        self.mario_label = []
        self.world_label = []
        self.time_label = []
        self.stage_label = []

        self.create_label(self.score_text, '000000', 75, 55)
        self.create_label(self.coin_count_text, '*00', 320, 55)
        self.create_label(self.mario_label, 'PLAYER', 75, 30)
        self.create_label(self.world_label, 'LEVEL', 450, 30)
        self.create_label(self.time_label, 'TIME', 625, 30)
        self.create_label(self.stage_label, '1', 472, 55)

        self.info_labels = [self.score_text, self.coin_count_text, self.mario_label,
                    self.world_label, self.time_label, self.stage_label]

    def create_state_labels(self):
        if self.state == c.MAIN_MENU:
            self.create_main_menu_labels()
        elif self.state == c.LOAD_SCREEN:
            self.create_player_image()
            self.create_load_screen_labels()
        elif self.state == c.LEVEL:
            self.create_level_labels()
        elif self.state == c.GAME_OVER:
            self.create_game_over_labels()
        elif self.state == c.TIME_OUT:
            self.create_time_out_labels()

    def create_player_image(self):
        
        
        if self.game_info[c.PLAYER_NAME] == c.PLAYER_MARIO:
            rect = (178, 32, 12, 16)
        else:
            rect = (178, 128, 12, 16)
        self.player_image = tools.get_image(setup.GFX['icon'], 
                                *rect, (0, 0, 32), 2.9)
        self.player_rect = self.player_image.get_rect(center=(320, 290))

    def create_main_menu_labels(self):
        self.state_labels = [*self.info_labels]
    
    def create_load_screen_labels(self):
        world_label = []
        self.stage_label2 = []

        self.create_label(world_label, 'LEVEL', 280, 200)
        self.create_label(self.stage_label2, '1', 430, 200)
        self.state_labels = [world_label, self.stage_label2,
                *self.info_labels]

    def create_level_labels(self):
        self.time = c.GAME_TIME_OUT
        self.current_time = 0

        self.clock_time_label = []
        self.create_label(self.clock_time_label, str(self.time), 645, 55)
        self.state_labels = [*self.info_labels, self.clock_time_label]

    def create_game_over_labels(self):
        game_label = []
        over_label = []
        
        self.create_label(game_label, 'GAME', 280, 300)
        self.create_label(over_label, 'OVER', 400, 300)
        
        self.state_labels = [game_label, over_label, *self.info_labels]

    def create_time_out_labels(self):
        timeout_label = []
        self.create_label(timeout_label, 'TIME OUT', 290, 310)
        self.state_labels = [timeout_label, *self.info_labels]

    def create_label(self, label_list, string, x, y):
        for letter in string:
            label_list.append(Character(self.image_dict[letter]))
        self.set_label_rects(label_list, x, y)
    
    def set_label_rects(self, label_list, x, y):
        for i, letter in enumerate(label_list):
            letter.rect.x = x + ((letter.rect.width + 3) * i)
            letter.rect.y = y
            if letter.image == self.image_dict['-']:
                letter.rect.y += 7
                letter.rect.x += 2
    
    def update(self, level_info, level=None):
        self.level = level
        self.handle_level_state(level_info)
    
    def handle_level_state(self, level_info):
        self.score = level_info[c.SCORE]
        self.update_text(self.score_text, self.score)
        self.update_text(self.coin_count_text, level_info[c.COIN_TOTAL])
        self.update_text(self.stage_label, level_info[c.LEVEL_NUM])
        self.flashing_coin.update(level_info[c.CURRENT_TIME])
        if self.state == c.LOAD_SCREEN:
            self.update_text(self.stage_label2, level_info[c.LEVEL_NUM])
        if self.state == c.LEVEL:
            if (level_info[c.CURRENT_TIME] - self.current_time) > 1000:
                self.current_time = level_info[c.CURRENT_TIME]
                self.time -= 1
                self.update_text(self.clock_time_label, self.time, True)
    
    def update_text(self, text, score, reset=False):
        if reset and len(text) > len(str(score)):
            text.remove(text[0])
        index = len(text) - 1
        for digit in reversed(str(score)):
            rect = text[index].rect
            text[index] = Character(self.image_dict[digit])
            text[index].rect = rect
            index -= 1

    ### Draw 
    def draw(self, surface):
        self.draw_info(surface, self.state_labels)
        

        if self.state == c.TIME_OUT:
            ###set Timeout Image
            loadimg = pg.image.load('resources/graphics/timeout.png')
            surface.blit(loadimg, (0,0))
        elif self.state == c.GAME_OVER:
            ###set Gameover Image
            loadimg = pg.image.load('resources/graphics/gameover.png')
            surface.blit(loadimg, (0,0))
        elif self.state == c.MAIN_MENU:
            ###set Start Image
            loadimg = pg.image.load('resources/graphics/start.png')
            surface.blit(loadimg, (320,260))
        if self.state == c.LOAD_SCREEN:
            surface.blit(self.player_image, self.player_rect)
        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)
    
    def draw_info(self, surface, label_list):
        for label in label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)