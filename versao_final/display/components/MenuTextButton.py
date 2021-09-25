from .Text import Text
from .Button import Button
from .Pressable import Pressable
import pygame


class MenuTextButton(Button, Pressable):
    def __init__(self, path: str, text: Text, next_state: str, rect=None):
        self.__text = text
        self.__next_state = next_state
        super().__init__(pygame.image.load(path).convert_alpha(), rect)
        self.__blit_text()

    def __blit_text(self):
        self.__text.rect = self.__text.surface.get_rect(center=self._surface.get_rect().center)
        self._surface.blit(self.__text.surface, self.__text.rect)

    def _blit_selected(self):
        self.__text.color = pygame.Color(255, 0, 0)
        self.__blit_text()

    def _blit_unselected(self):
        self.__text.color = pygame.Color(255, 255, 255)
        self.__blit_text()

    def on_pressed(self):
        return self.__next_state
