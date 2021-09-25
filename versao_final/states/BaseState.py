import pygame
from abc import ABC, abstractmethod


class BaseState(ABC):
    def __init__(self):
        # self.done = False
        # self.quit = False
        # self.next_state = None
        self.screen_rect: pygame.Rect = pygame.display.get_surface().get_rect()
        # self.persist = {}
        self.font = pygame.font.Font(None, 24)

    # def startup(self, persistent):
    #     self.persist = persistent

    @abstractmethod
    def run(self):
        pass

    # Colocar dentro do run? Ou pelo menos ser executado dentro dele.
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self, surface):
        pass
