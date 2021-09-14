from Singleton import Singleton
from display.Text import Text
import pygame
from .BaseState import BaseState


class Splash(BaseState):
    def __init__(self):
        super(Splash, self).__init__()
        self.__title = Text("prototipo/assets/fonts/title.ttf", 200, pygame.Color(255, 30, 30), "Masmorra")
        self.__title_rect = self.__title.surface().get_rect(center=tuple(size/2 for size in Singleton.screen_size))
        self.time_active = 0

    def run(self):
        self.time_active += 1
        self.__title_rect.move_ip(0, -1)
        if self.time_active > 119:
            return "INIT"

    def draw(self, surface: pygame.Surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.__title.surface(),
            self.__title_rect)
