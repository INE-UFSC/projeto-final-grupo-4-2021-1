from display.Text import Text
import pygame

class Button:
    def __init__(self, path: str, text: Text):
        self.__surface: pygame.Surface = pygame.image.load(path).convert_alpha()

        height = self.__surface.get_height()
        width = self.__surface.get_width()

        self.__rect = pygame.Surface(size=(width, height)).get_rect(center=(400, 300))
        self.__surface.blit(text.surface(), center=(text.surface().get_width()/2, text.surface().get_height()/2))

    def draw(self, surface: pygame.Surface):
        surface.blit(self.__surface, self.__rect)
        