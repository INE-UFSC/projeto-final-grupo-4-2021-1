import pygame
from copy import copy

from .Animation import Animation

class LinearAnimation(Animation):
    def __init__(self, surface, start_rect: pygame.Rect, end_rect: pygame.Rect, duration):
        super().__init__(surface, start_rect, end_rect, duration)
        self.__speed = ((end_rect[0] - start_rect[0])/duration, (end_rect[1] - start_rect[1])/duration)

        self.__x = start_rect.x
        self.__y = start_rect.y

    def update(self):
        if not self._finished:
            self.__x += self.__speed[0]
            self.__y += self.__speed[1]
            
            self._rect.topleft = (int(round(self.__x)), int(round(self.__y)))

            if self._rect == self.end_rect:
                self._finished = True

    def draw(self, surface: pygame.Surface):
        surface.blit(self.surface, self._rect)

    def reset(self):
        self._rect = copy(self.start_rect)
        self.__x = self.start_rect.x
        self.__y = self.start_rect.y
        self._finished = False
