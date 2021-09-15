from display.Text import Text
from .Button import Button
import pygame

class IconButton(Button):
    def __init__(self, backgroundPath: str, iconPath: str, rect = None):
        self.__background: pygame.Surface = pygame.image.load(backgroundPath).convert_alpha()
        self.__icon: pygame.Surface = pygame.image.load(iconPath).convert_alpha()
        super().__init__(None, rect)
        self.__blit_icon()

    def __blit_icon(self):
        self._surface = self.__background
        self._surface.blit(self.__icon, self.__icon.get_rect(center = self.__background.get_rect().center))

    def change_background(self, path):
        self.__background: pygame.Surface = pygame.image.load(path).convert_alpha()
        self.__blit_icon()

    def change_icon(self, path):
        self.__icon: pygame.Surface = pygame.image.load(path).convert_alpha()
        self.__blit_icon()

    @property
    def background(self):
        return self.__background

    @property
    def icon(self):
        return self.__icon