from abc import abstractmethod
import pygame
from Singleton import Singleton

class MainCharacterResources:
    def __init__(self):
        self.__surface: pygame.Surface = None
        self.__rect: pygame.Rect = None

    @abstractmethod
    def draw(surface):
        current_hp = Singleton.main_character.hp.current
        max_hp = Singleton.main_character.hp.max
        pygame.draw.rect(surface, (0, 0, 0), (10, 10, 500, 20))
        pygame.draw.rect(surface, (255, 0, 0), (11, 11, 498, 18))
        pygame.draw.rect(surface, (0, 255, 0), (11, 11, 498*current_hp/max_hp, 18))

        current_ap = Singleton.main_character.ap.current
        max_ap = Singleton.main_character.ap.max
        for index in range(max_ap):
            pygame.draw.circle(surface, (150, 150, 150), (20 * (index + 1) , 45), 8)
            if index < current_ap:
                pygame.draw.circle(surface, (0, 0, 255), (20 * (index + 1) , 45), 6)

