import pygame
from abc import ABC, abstractmethod
from copy import copy

class Animation(ABC):
    def __init__(self, surface, start_rect: pygame.Rect, end_rect: pygame.Rect, duration):
        self.__surface = surface
        self.__start_rect = start_rect
        self._rect: pygame.Rect = copy(start_rect)
        self.__end_rect = end_rect
        self.__duration = duration
        self._finished = False
        

    @property
    def start_rect(self):
        return self.__start_rect

    @property
    def end_rect(self):
        return self.__end_rect

    @property
    def duration(self):
        return self.__duration

    @property
    def finished(self):
        return self._finished

    @property
    def surface(self):
        return self.__surface

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def reset(self):
        pass