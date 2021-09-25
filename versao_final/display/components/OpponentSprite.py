import pygame

class OpponentSprite:
    def __init__(self, sprite_path: str):
        self.__sprite = pygame.image.load(sprite_path).convert_alpha()
        sprite_height = self.__sprite.get_height()
        sprite_width = self.__sprite.get_width()

        self.__rect = pygame.Surface(size=(sprite_width, sprite_height)).get_rect(center=(640, 360))

    @property
    def rect(self):
        return self.__rect

    def draw(self, surface: pygame.Surface):
        surface.blit(self.__sprite, self.__rect)
