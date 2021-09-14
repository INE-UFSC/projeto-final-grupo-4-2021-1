import pygame

class Text:
    def __init__(self, font_path: str, size: int, color: pygame.Color, text: str):
        self.__font = pygame.font.Font(font_path, size)
        self.__text = text
        self.__color = color

    def surface(self) -> pygame.Surface:
        return self.__font.render(self.__text, True, self.__color)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: pygame.Color):
        self.__color = color
