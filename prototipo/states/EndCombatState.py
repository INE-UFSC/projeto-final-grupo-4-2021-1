import pygame
from .BaseState import BaseState


class EndCombat(BaseState):
    def __init__(self):
        super(EndCombat, self).__init__()
        self.time_active = 0

    def run(self):
        pass

    def draw(self, surface):
        surface.fill(pygame.Color("red"))
