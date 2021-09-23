import pygame
from typing import List
from .BaseMenuState import BaseMenuState
from display.components.Text import Text
from display.components.TextPressable import TextPressable
from display.components.ItemTextPressable import ItemTextPressable
from display.components.MenuTextPressable import MenuTextPressable
from fighter.main_character.MainCharacter import MainCharacter

class InventoryState(BaseMenuState):
    def __init__(self):
        self.active_index = 0
        self.options: List["TextPressable"] = []
        self.__item_descriptions: List["Text"] = []
        self.__item_weights: List["Text"] = []
        self.__should_update = True

    def run(self):
        if self.__should_update:
            self.__should_update = False
            self.__update_item_list()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def handle_action(self):
        self.__should_update = True
        return self.options[self.active_index].on_pressed()

    def __update_item_list(self):
        self.options.clear()
        self.__item_descriptions.clear()
        self.__item_weights.clear()
        for item in MainCharacter().inventory.items:
            self.options.append(ItemTextPressable("prototipo/assets/fonts/description.ttf", 30, item.name, item))
            self.__item_descriptions.append(Text("prototipo/assets/fonts/description.ttf", 30, pygame.Color(255, 255, 255), f"{item.description} ({item.type.value})"))
            self.__item_weights.append(Text("prototipo/assets/fonts/description.ttf", 30, pygame.Color(255, 255, 255), str(item.weight)))
        
        self.options.append(MenuTextPressable("prototipo/assets/fonts/description.ttf", 30, "Return", "PREVIOUS"))
        
        adder = 20
        for option, desc, weight in zip(self.options, self.__item_descriptions, self.__item_weights):
            option.rect = option.surface.get_rect(topleft = (20, adder))
            desc.rect = desc.surface.get_rect(topleft= (400, adder))
            weight.rect = weight.surface.get_rect(topleft= (1240, adder))

            adder += (option.surface.get_height() + 5)

        self.options[-1].rect = self.options[-1].surface.get_rect(topleft = (10, adder))

    def draw(self, surface: pygame.Surface):
        surface.fill(pygame.Color(0,0,0))
        for index, option in enumerate(self.options):
            option.select() if index == self.active_index else option.unselect()
            surface.blit(option.surface, option.rect)

        for desc, weight in zip(self.__item_descriptions, self.__item_weights):
            surface.blit(desc.surface, desc.rect)
            surface.blit(weight.surface, weight.rect)
    
