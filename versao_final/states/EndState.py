import pygame
from .BaseState import BaseState
from display.components.Text import Text


class EndState(BaseState):
    def __init__(self):
        super(EndState, self).__init__()
        self.__title = Text("versao_final/assets/fonts/title.ttf", 400, pygame.Color(255, 20, 20), "End")
        self.__title.rect = self.__title.surface.get_rect(center=(self.screen_rect.center[0], self.screen_rect.center[1]))
        self.time_active = 0

    def run(self):
        self.time_active += 1
        if self.time_active >= 119:
            return "QUIT"

    def draw(self, surface):
        surface.fill(pygame.Color(0, 0, 0))
        self.__title.draw(surface)