from abc import abstractmethod
from .Text import Text
from .Pressable import Pressable
import pygame

class TextPressable(Text, Pressable):
    def __init__(self, font_path: str, size: int, text: str):
        super().__init__(font_path, size, pygame.Color(255, 255, 255), text)

    @property
    def selected(self):
        return self.__selected

    def select(self):
        self.color = pygame.Color(255, 0, 0)

    def unselect(self):
        self.color = pygame.Color(255, 255, 255)

    @abstractmethod
    def on_pressed(self):
        pass