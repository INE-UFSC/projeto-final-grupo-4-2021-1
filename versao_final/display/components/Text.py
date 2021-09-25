import pygame


class Text:
    def __init__(self, font_path: str, size: int, color: pygame.Color, text: str, topleft: tuple = None):
        self.__font = pygame.font.Font(font_path, size)
        self.__text = text
        self.__color = color

        if topleft:
            self.__rect = pygame.Rect(self.surface.get_rect(topleft=topleft))
        else:
            self.__rect = None

    @property
    def surface(self) -> pygame.Surface:
        return self.__font.render(self.__text, True, self.__color)

    @property
    def color(self):
        return self.__color

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

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
