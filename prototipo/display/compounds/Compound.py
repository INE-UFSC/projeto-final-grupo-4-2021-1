import pygame
from abc import ABC, abstractstaticmethod

class Compound(ABC):
    @abstractstaticmethod
    def draw(surface: pygame.Surface):
        pass
