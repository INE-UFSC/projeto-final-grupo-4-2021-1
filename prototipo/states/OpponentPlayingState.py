import pygame
from .BaseState import BaseState
from prototipo.Singleton import Singleton


class OpponentPlaying(BaseState):
    def __init__(self):
        super(OpponentPlaying, self).__init__()
        self.time_active = 0

    def draw(self, surface):
        surface.fill(pygame.Color("black"))

    def is_zero(self):
        if Singleton.main_character.hp.current == 0:
            return "END"

    def handle_action(self):
        Singleton.main_character.get_attacked(Singleton.opponent.use_skill(0))
        self.is_zero()

        return "MAIN_CHARACTER_PLAYING"

    def run(self):
        self.time_active += 1
        if self.time_active > 119:
            self.time_active = 0
            self.handle_action()
        
    

