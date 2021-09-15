from abc import ABC
import pygame

class Button(ABC):
    def __init__(self, surface, rect):
        self._surface: pygame.Surface = surface
        self.__rect: pygame.Rect = rect
    
    @property
    def surface(self):
        return self._surface

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value: pygame.Rect):
        self.__rect = value
        
    def draw(self, surface: pygame.Surface):
        surface.blit(self._surface, self.__rect)