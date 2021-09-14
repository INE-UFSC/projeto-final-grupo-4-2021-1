import pygame

class OpponentSprite:
    def __init__(self, spritePath: str):
        self.__sprite = pygame.image.load(spritePath).convert_alpha()
        sprite_height = self.__sprite.get_height()
        sprite_width = self.__sprite.get_width()

        self.__rect = pygame.Surface(size=(sprite_width, sprite_height)).get_rect(center=(400, 300))

    def draw(self, surface: pygame.Surface):
        surface.blit(self.__sprite, self.__rect)
