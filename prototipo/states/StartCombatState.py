from fighter.main_character.MainCharacter import MainCharacter
from creators.OpponentCreator import OpponentCreator

from Singleton import Singleton
from .BaseState import BaseState
from room.CombatRoom import CombatRoom


class StartCombatState(BaseState):
    def __init__(self):
        super(StartCombatState, self).__init__()
        self.time_active = 0

    def run(self):
        self.time_active += 1
        if self.time_active > 50:
            self.time_active = 0
            Singleton.room = CombatRoom()

            MainCharacter().ap.increase_current(2)
            OpponentCreator.generate_test_opponent()

            return "MAIN_CHARACTER_PLAYING"

    def draw(self, surface):
        if self.time_active > 50:
            OpponentCreator.current.draw(surface)
        # desenhar quadrado como oponente
