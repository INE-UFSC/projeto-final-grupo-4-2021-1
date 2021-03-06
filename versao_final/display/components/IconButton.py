from abc import ABC, abstractmethod
from .Button import Button
from .Pressable import Pressable
import pygame


class IconButton(Button, Pressable, ABC):
    def __init__(self, icon_path: str, rect=None):
        self.__icon: pygame.Surface = pygame.transform.scale(pygame.image.load(icon_path).convert_alpha(), (80, 80))
        super().__init__(self.__icon.copy(), rect)

    def _blit_icon(self):
        self._surface.blit(self.__icon, self.__icon.get_rect(center=self._surface.get_rect().center))

    def _blit_selected(self):
        self._blit_icon()
        pygame.draw.rect(self._surface, pygame.Color(255, 0, 0), pygame.Rect((0, 0), self._surface.get_size()), 8)
        pygame.draw.rect(self._surface, pygame.Color(0, 0, 0), pygame.Rect((0, 0), self._surface.get_size()), 4)

    def _blit_unselected(self):
        self._blit_icon()
        pygame.draw.rect(self._surface, pygame.Color(255, 255, 255), pygame.Rect((0, 0), self._surface.get_size()), 8)
        pygame.draw.rect(self._surface, pygame.Color(0, 0, 0), pygame.Rect((0, 0), self._surface.get_size()), 4)

    @abstractmethod
    def on_pressed(self):
        pass
