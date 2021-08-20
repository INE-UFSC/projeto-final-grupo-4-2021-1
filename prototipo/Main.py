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

from fighter.main_character.MainCharacter import MainCharacter
from fighter.opponent.Opponent import Opponent

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

main_character = MainCharacter.test_character()
opponent = Opponent.test_opponent()

opponent.get_attacked(main_character.basicattack())
main_character.get_attacked(opponent.basicattack())

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()