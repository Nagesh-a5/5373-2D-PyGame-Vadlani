import pygame
import setup, tools
import constants
from states import menu, load_screen, level

###Display Splash Screen
def start():
    ###Start sound play
    startSound = pygame.mixer.Sound('resources/sound/start.wav')
    startSound.play()
    ######

    ###Set Display Mode
    win = pygame.display.set_mode((800,600))
    pygame.event.pump()

    ##Set Icon
    icon = pygame.image.load('resources/graphics/icon.png')
    pygame.display.set_icon(icon)

    ##Set Caption
    pygame.display.set_caption("My Game")

    ##Load Background Image of Splash Screen
    loadimg = pygame.image.load('resources/graphics/loading.png')

    ##Display
    win.blit(loadimg, (0,0))
    pygame.display.flip()
    pygame.event.pump()

    ##Delay Screen
    clock = pygame.time.Clock()
    please_work = True
    count0r = 0
    while please_work:
        pygame.event.pump()
        count0r += 1
        clock.tick(30)
        if count0r == 60:
            please_work = False

    ##Start Game 
    game = tools.Control()

    ##Initialize States
    state_dict = {constants.MAIN_MENU: menu.Menu(),
                  constants.LOAD_SCREEN: load_screen.LoadScreen(),
                  constants.LEVEL: level.Level(),
                  constants.GAME_OVER: load_screen.GameOver(),
                  constants.TIME_OUT: load_screen.TimeOut()}

    ##Show Menu Screen
    game.setup_states(state_dict, constants.MAIN_MENU)
    game.main()

