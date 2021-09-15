import pygame

class Text:
    def __init__(self, font_path: str, size: int, color: pygame.Color, text: str):
        self.__font = pygame.font.Font(font_path, size)
        self.__text = text
        self.__color = color
        self.__rect: pygame.Rect = None

    @property
    def surface(self) -> pygame.Surface:
        return self.__font.render(self.__text, True, self.__color)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: pygame.Color):
        self.__color = color

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value: tuple):
        self.__rect = value

    def draw(self, surface: pygame.Surface):
        surface.blit(self.surface, self.__rect)
