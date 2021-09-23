from abc import abstractmethod
from .Text import Text
from .Pressable import Pressable
import pygame

class TextPressable(Text, Pressable):
    def __init__(self, font_path: str, size: int, text: str):
        super().__init__(font_path, size, pygame.Color("white"), text)

    @property
    def selected(self):
        return self.__selected

    def select(self):
        self.color = pygame.Color("red")

    def unselect(self):
        self.color = pygame.Color("white")

    @abstractmethod
    def on_pressed(self):
        pass