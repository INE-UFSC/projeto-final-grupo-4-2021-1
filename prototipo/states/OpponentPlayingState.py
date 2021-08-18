import pygame
from .BaseState import BaseState


class OpponentPlaying(BaseState):
    def __init__(self):
        super(OpponentPlaying, self).__init__()

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
