import pygame

from states.SplashState import Splash
from states.InitState import Init
from states.OptionsState import Options
from states.TreasureRoomState import TreasureRoom
from states.HealRoomState import HealRoom
from states.StartCombatState import StartCombat
from states.EndCombatState import EndCombat
from states.MainCharacterPlayingState import MainCharacterPlaying
from states.OpponentPlayingState import OpponentPlaying
from states.EndState import End
from Game import Game
from fighter.main_character.MainCharacter import MainCharacter
from fighter.opponent.Opponent import Opponent
from Singleton import Singleton

pygame.init()
screen = pygame.display.set_mode(Singleton.screen_size)
states = {
    "SPLASH": Splash(),
    "INIT": Init(),
    "OPTIONS": Options(),
    "START_COMBAT": StartCombat(),
    "MAIN_CHARACTER_PLAYING": MainCharacterPlaying(),
    "OPPONENT_PLAYING": OpponentPlaying(),
    "END_COMBAT": EndCombat(),
    "HEAL_ROOM": HealRoom(),
    "TREASURE_ROOM": TreasureRoom(),
    "END": End(),
}

Singleton.main_character = MainCharacter.generate_test_character()
Singleton.background = pygame.image.load("prototipo/assets/Background.png")

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
