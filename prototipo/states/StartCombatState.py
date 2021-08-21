from fighter.opponent.Opponent import Opponent
import pygame
import Singleton
from .BaseState import BaseState


class StartCombat(BaseState):
    def __init__(self):
        super(StartCombat, self).__init__()
        self.time_active = 0

    def run(self):
        self.time_active += 1
        if self.time_active > 50:
            self.time_active = 0
            Singleton.opponent = Opponent.generate_test_opponent()
            return "MAIN_CHARACTER_PLAYING"

    def draw(self, surface):
        surface.fill(pygame.Color("red"))
        # desenhar quadrado como oponente
