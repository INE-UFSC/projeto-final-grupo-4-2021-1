import pygame

from states.SplashState import SplashState
from states.InitState import InitState
from states.OptionsState import OptionsState
from states.TreasureRoomState import TreasureRoomState
from states.HealRoomState import HealRoomState
from states.StartCombatState import StartCombatState
from states.EndCombatState import EndCombatState
from states.MainCharacterPlayingState import MainCharacterPlayingState
from states.OpponentPlayingState import OpponentPlayingState
from states.EndState import EndState
from Game import Game
from fighter.main_character.MainCharacter import MainCharacter
from fighter.opponent.Opponent import Opponent
from Singleton import Singleton

pygame.init()
screen = pygame.display.set_mode((800, 600))
states = {
    "SPLASH": SplashState(),
    "INIT": InitState(),
    "OPTIONS": OptionsState(),
    "START_COMBAT": StartCombatState(),
    "MAIN_CHARACTER_PLAYING": MainCharacterPlayingState(),
    "OPPONENT_PLAYING": OpponentPlayingState(),
    "END_COMBAT": EndCombatState(),
    "HEAL_ROOM": HealRoomState(),
    "TREASURE_ROOM": TreasureRoomState(),
    "END": EndState(),
}

Singleton.main_character = MainCharacter.generate_test_character()
Singleton.background = pygame.image.load("prototipo/Images/Background.png")

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
