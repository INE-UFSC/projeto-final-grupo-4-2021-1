from fighter.main_character.MainCharacter import MainCharacter
from creators.OpponentCreator import OpponentCreator
from .BaseState import BaseState
from display.components.Background import Background
from room.CombatRoom import CombatRoom


class StartCombatState(BaseState):
    def __init__(self):
        super(StartCombatState, self).__init__()
        self.time_active = 0

    def run(self):
        CombatRoom()
        self.time_active += 1
        if self.time_active > 50:
            self.time_active = 0

            MainCharacter().ap.increase_current(2)
            OpponentCreator().generate_enemy()

            return "MAIN_CHARACTER_PLAYING"

    def draw(self, surface):
        surface.blit(Background().image, (0,0))

        if self.time_active > 50:
            OpponentCreator.current.draw(surface)
