import pygame
from .BaseState import BaseState


class StartCombatState(BaseState):
    def __init__(self):
        super(StartCombatState, self).__init__()
        self.time_active = 0

    def run(self):
        self.time_active += 1
        if self.time_active > 50:
            return "MAIN_CHARACTER_PLAYING"

    def draw(self, surface):
        surface.fill(pygame.Color("red"))
        # desenhar quadrado como oponente

