import pygame
from typing import List
from .BaseMenuState import BaseMenuState
from display.components.Text import Text
from display.components.TextPressable import TextPressable
from fighter.main_character.MainCharacter import MainCharacter

class LevelUpState(BaseMenuState):
    def __init__(self):
        super(LevelUpState, self).__init__()
        self.active_index = 0
        self.__title = Text("prototipo/assets/fonts/menu_option.ttf", 80, pygame.Color(255, 255, 255), "LEVEL UP!")
        self.__availablePoints = Text("prototipo/assets/fonts/menu_option.ttf", 50, pygame.Color(255, 255, 255), "Available Points: " + str(MainCharacter().stats.availablePoints))
        self.__availablePoints.rect = self.__availablePoints.surface.get_rect(midtop = (self.screen_rect.width/2, 150))
        self.__title.rect = self.__title.surface.get_rect(midtop = (self.screen_rect.width/2, 50))
        self.options: List["TextPressable"] = [TextPressable("prototipo/assets/fonts/menu_option.ttf", 50, text, (100 + 300*index, self.screen_rect.height/2 )) for index, text in enumerate(MainCharacter().stats.stats)]
        self.stats = [Text("prototipo/assets/fonts/menu_option.ttf", 50, pygame.Color(255, 255, 255), str(MainCharacter().stats.stats[option.text])) for option in self.options]
        for index, stat in enumerate(self.stats):
            stat.rect = stat.surface.get_rect(midtop = self.options[index].rect.midbottom)

    def run(self):
        MainCharacter().leveled_up = False
        self.__availablePoints.text = "Available Points: " + str(MainCharacter().stats.availablePoints)
        for index, option in enumerate(self.options):
            self.stats[index].text = str(MainCharacter().stats.stats[option.text])
        if MainCharacter().stats.availablePoints:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "QUIT"

                elif event.type == pygame.KEYUP:
                    return self.handle_menu(event.key)
        else:
            return "END_COMBAT"

    def handle_action(self):
        MainCharacter().stats.upgrade_stat(self.options[self.active_index].text)


    def draw(self, surface: pygame.Surface):
        surface.fill(pygame.Color(0,0,0))
        self.__title.draw(surface)
        self.__availablePoints.draw(surface)


        for index, option in enumerate(self.options):
            option.select() if index == self.active_index else option.unselect()
            option.draw(surface)

        for stat in self.stats:
            stat.draw(surface)
    
