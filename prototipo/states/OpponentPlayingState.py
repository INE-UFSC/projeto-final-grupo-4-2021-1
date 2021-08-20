import pygame
from .BaseState import BaseState


class OpponentPlaying(BaseState):
    def __init__(self):
        super(OpponentPlaying, self).__init__()
        self.time_active = 0

    def run(self):
        pass

    def draw(self, surface):
        surface.fill(pygame.Color("white"))
