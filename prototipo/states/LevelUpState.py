import pygame
from typing import List
from .BaseMenuState import BaseMenuState
from display.components.Text import Text
from display.components.TextPressable import TextPressable
from display.components.ItemTextPressable import ItemTextPressable
from display.components.MenuTextPressable import MenuTextPressable
from fighter.main_character.MainCharacter import MainCharacter
from Singleton import Singleton

class LevelUpState(BaseMenuState):
    def __init__(self):
        super(LevelUpState, self).__init__()
        self.active_index = 0
        self.__title = Text("prototipo/assets/fonts/menu_option.ttf", 40, pygame.Color(255, 255, 255), "LEVEL UP!")
        self.__title.rect = self.__title.surface.get_rect(topleft=(10, 10))
        self.options: List["TextPressable"] = [TextPressable("prototipo/assets/fonts/menu_option.ttf", 50, text, (100 + 300*index, self.screen_rect.height/2 )) for index, text in enumerate(MainCharacter().stats.stats)]

    def run(self):
        MainCharacter().leveled_up = False
        if MainCharacter().stats.availablePoints:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "QUIT"
                elif event.type == pygame.KEYUP:
                    return self.handle_menu(event.key)
        else:
            return "END_COMBAT"

    def handle_action(self):
        return MainCharacter().stats.upgrade_stat(self.options[self.active_index].text)

    def draw(self, surface: pygame.Surface):
        surface.fill(pygame.Color(0,0,0))
        self.__title.draw(surface)

        for index, option in enumerate(self.options):
            option.select() if index == self.active_index else option.unselect()
            option.draw(surface)
    
