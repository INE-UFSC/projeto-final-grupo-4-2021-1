import pygame

from states.EquipmentState import EquipmentState
from states.SplashState import SplashState
from states.InitState import InitState
from states.OptionsState import OptionsState
from states.TreasureRoomState import TreasureRoomState
from states.HealRoomState import HealRoomState
from states.InventoryState import InventoryState
from states.StartCombatState import StartCombatState
from states.EndCombatState import EndCombatState
from states.MainCharacterPlayingState import MainCharacterPlayingState
from states.OpponentPlayingState import OpponentPlayingState
from states.EndState import EndState
from states.LevelUpState import LevelUpState
from creators.MainCharacterCreator import MainCharacterCreator
from Game import Game


pygame.init()
screen = pygame.display.set_mode((1280, 720))

MainCharacterCreator.generate_test_character()

states = {
    "SPLASH": SplashState(),
    "INIT": InitState(),
    "OPTIONS": OptionsState(),
    "EQUIPMENT": EquipmentState(),
    "START_COMBAT": StartCombatState(),
    "OPPONENT_PLAYING": OpponentPlayingState(),
    "END_COMBAT": EndCombatState(),
    "HEAL_ROOM": HealRoomState(),
    "TREASURE_ROOM": TreasureRoomState(),
    "INVENTORY": InventoryState(),
    "END": EndState(),
    "MAIN_CHARACTER_PLAYING": MainCharacterPlayingState(),
    "LEVEL_UP": LevelUpState()
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
