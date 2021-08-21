import pygame
from .BaseState import BaseState
import Singleton


class OpponentPlaying(BaseState):
    def __init__(self):
        super(OpponentPlaying, self).__init__()
        self.time_active = 0

    def draw(self, surface):
        surface.fill(pygame.Color("black"))

    def handle_action(self):
        Singleton.main_character.get_attacked(Singleton.opponent.use_skill(0))

        if Singleton.main_character.hp.is_zero():
            return "END_COMBAT"
        return "MAIN_CHARACTER_PLAYING"

    def run(self):
        self.time_active += 1
        if self.time_active > 119:
            self.time_active = 0
            return self.handle_action()
        
    

