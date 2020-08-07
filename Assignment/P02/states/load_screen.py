import setup, tools
import constants as c
from components import info

### LoadScreen (When level up, timeout, gameover)
class LoadScreen(tools.State):
    def __init__(self):
        tools.State.__init__(self)
        self.time_list = [2400, 2600, 2635]
        
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()
        info_state = self.set_info_state()
        self.overhead_info = info.Info(self.game_info, info_state)
    
    def set_next_state(self):
        return c.LEVEL
    
    def set_info_state(self):
        return c.LOAD_SCREEN

    ### update(delay display)
    def update(self, surface, keys, current_time):
        if (current_time - self.start_time) < self.time_list[0]:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        elif (current_time - self.start_time) < self.time_list[1]:
            surface.fill(c.BLACK)
        elif (current_time - self.start_time) < self.time_list[2]:
            surface.fill((106, 150, 252))
        else:
            self.done = True
            
### Handle GameOver Screen
class GameOver(LoadScreen):
    def __init__(self):
        LoadScreen.__init__(self)
        self.time_list = [3000, 3200, 3235]

    def set_next_state(self):
        return c.MAIN_MENU
    
    def set_info_state(self):
        return c.GAME_OVER

### Handle Timeout Screen
class TimeOut(LoadScreen):
    def __init__(self):
        LoadScreen.__init__(self)
        self.time_list = [2400, 2600, 2635]

    def set_next_state(self):
        return c.GAME_OVER

    def set_info_state(self):
        return c.TIME_OUT
