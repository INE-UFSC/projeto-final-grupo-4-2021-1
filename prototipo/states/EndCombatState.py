import pygame
from Singleton import Singleton
from .BaseState import BaseState


class EndCombat(BaseState):
    def __init__(self):
        super(EndCombat, self).__init__()
        self.time_active = 0

    def run(self):
        self.time_active += 1
        if self.time_active > 50:
            self.time_active = 0
            Singleton.opponent = None
            if Singleton.main_character.hp.is_zero():
                return "END"
            else:
                return "START_COMBAT"

    def draw(self, surface):
        surface.fill(pygame.Color("blue"))
