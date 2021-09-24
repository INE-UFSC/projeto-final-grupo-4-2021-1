import pygame
from .BaseMenuState import BaseMenuState
from display.components.Text import Text
from display.components.MenuTextPressable import MenuTextPressable


class InitState(BaseMenuState):
    def __init__(self):
        super(InitState, self).__init__()
        self.active_index = 0

        self.__title = Text("prototipo/assets/fonts/title.ttf", 200, pygame.Color(255, 30, 30), "Masmorra")
        self.__title.rect = self.__title.surface.get_rect(center=(self.screen_rect.width/2, self.screen_rect.height/2 - 90))

        self.options = [MenuTextPressable(
            "prototipo/assets/fonts/menu_option.ttf",
            50,
            option[0],
            option[1]
        ) for option in [("New", "START_COMBAT"), ("Options", "OPTIONS"), ("Exit", "QUIT")]]

        adder = self.screen_rect.center[1] + 100
        for option in self.options:
            option.rect = option.surface.get_rect(center=(self.screen_rect.center[0], adder))
            adder += (option.surface.get_height() + 10)

    def handle_action(self):
        return self.options[self.active_index].on_pressed()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def draw(self, surface):
        surface.fill(pygame.Color(0, 0, 0))
        self.__title.draw(surface)
        for index, option in enumerate(self.options):
            option.color = pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255)
            option.draw(surface)
