from .Text import Text
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
    
    def _blit_selected(self):
        self.__text.color = pygame.Color("red")
        self.__blit_text()

    def _blit_unselected(self):
        self.__text.color = pygame.Color("white")
        self.__blit_text()
