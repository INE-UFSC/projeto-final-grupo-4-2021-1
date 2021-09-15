from Singleton import Singleton
from display.Text import Text
import pygame
from .BaseState import BaseState


class SplashState(BaseState):
    def __init__(self):
        super(SplashState, self).__init__()
        self.__title = Text("prototipo/assets/fonts/title.ttf", 200, pygame.Color(255, 30, 30), "Masmorra")
        self.__title.rect = self.__title.surface.get_rect(center=(self.screen_rect.width/2, self.screen_rect.height/2))
        self.__time_active = 0

    def run(self):
        self.__time_active += 1
        if self.__time_active % 2 and self.__time_active > 60:
            self.__title.rect.move_ip(0, -1)
        if self.__time_active > 239:
            return "INIT"

    def draw(self, surface: pygame.Surface):
        surface.fill(pygame.Color("black"))
        self.__title.draw(surface)
