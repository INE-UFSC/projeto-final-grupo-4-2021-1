import pygame
from .BaseState import BaseState
from abc import ABC, abstractmethod


class BaseMenuState(BaseState, ABC):
    def __init__(self):
        super(BaseMenuState, self).__init__()
        self.active_index = int()
        self.options = list()

    @abstractmethod
    def handle_action(self):
        pass

    def handle_menu(self, key: int):
        if key == pygame.K_UP or key == pygame.K_LEFT:
            if self.active_index == 0:
                self.active_index = len(self.options) - 1
            else:
                self.active_index -= 1
        elif key == pygame.K_DOWN or key == pygame.K_RIGHT:
            if self.active_index == (len(self.options) - 1):
                self.active_index = 0
            else:
                self.active_index += 1
        elif key == pygame.K_RETURN:
            return self.handle_action()
