from abc import ABC, abstractmethod
import pygame

class Button(ABC):
    def __init__(self, surface, rect):
        self._surface: pygame.Surface = surface
        self.__rect: pygame.Rect = rect
        self.__selected = False
    
    @property
    def surface(self):
        return self._surface

    @property
    def rect(self):
        return self.__rect

    @property
    def selected(self):
        return self.__selected

    @rect.setter
    def rect(self, value: pygame.Rect):
        self.__rect = value

    def select(self):
        self.__selected = True

    def unselect(self):
        self.__selected = False

    def draw(self, surface: pygame.Surface):
        self._blit_selected() if self.selected else self._blit_unselected()
        surface.blit(self._surface, self.__rect)

    @abstractmethod
    def _blit_selected(self):
        pass

    @abstractmethod
    def _blit_unselected(self):
        pass