import pygame
from states.SplashState import Splash
from states.InitState import Init
from states.MenuState import Menu
from states.TreasureRoomState import TreasureRoom
from states.HealRoomState import HealRoom
from states.MainCharacterPlayingState import MainCharacterPlaying
from states.OpponentPlayingState import OpponentPlaying
from states.EndState import End
from Game import Game


pygame.init()
screen = pygame.display.set_mode((800, 600))
states = {
    "SPLASH": Splash(),
    "INIT": Init(),
    "MENU": Menu(),
    "MAIN_CHARACTER_PLAYING": MainCharacterPlaying(),
    "OPPONENT_PLAYING": OpponentPlaying(),
    "HEAL_ROOM": HealRoom(),
    "TREASURE_ROOM": TreasureRoom(),
    "END": End(),
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
