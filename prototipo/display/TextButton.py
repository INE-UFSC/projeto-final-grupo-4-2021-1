from display.Text import Text
from .Button import Button
import pygame

class TextButton(Button):
    def __init__(self, path: str, text: Text, rect = None):
        self.__text = text
        super().__init__(pygame.image.load(path).convert_alpha(), rect)
        self.__blit_text()

    def __blit_text(self):
        self.__text.rect = self.__text.surface.get_rect(center = self._surface.get_rect().center)
        self._surface.blit(self.__text.surface, self.__text.rect)

    def change_text_color(self, color: pygame.Color):
        self.__text.color = color
        self.__blit_text()