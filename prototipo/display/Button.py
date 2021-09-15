from display.Text import Text
import pygame

class Button:
    def __init__(self, path: str, text: Text):
        self.__surface: pygame.Surface = pygame.image.load(path).convert_alpha()
        self.__rect: pygame.Rect = None
        self.__text = text
        self.__blit_text()

    def __blit_text(self):
        height = self.__surface.get_height()
        width = self.__surface.get_width()
        self.__text.rect = self.__text.surface.get_rect(center=(width/2, height/2))
        self.__surface.blit(self.__text.surface, self.__text.rect)

    def change_text_color(self, color: pygame.Color):
        self.__text.color = color
        self.__blit_text()
    
    @property
    def surface(self):
        return self.__surface

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value: pygame.Rect):
        self.__rect = value
        
    def draw(self, surface: pygame.Surface):
        surface.blit(self.__surface, self.__rect)