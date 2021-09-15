import pygame
from .BaseMenuState import BaseMenuState
from display.Text import Text

class InitState(BaseMenuState):
    def __init__(self):
        super(InitState, self).__init__()
        self.active_index = 0

        self.__title = Text("prototipo/assets/fonts/title.ttf", 200, pygame.Color(255, 30, 30), "Masmorra")
        self.__title.rect = self.__title.surface.get_rect(center=(self.screen_rect.width/2, self.screen_rect.height/2 - 90))

        self.options = [Text(
            "prototipo/assets/fonts/menu_option.ttf",
            50,
            pygame.Color(255, 255, 255),
            option
        ) for option in ["New", "Load", "Options", "Exit"]]

        menu_height = 0
        for option in self.options:
            option.rect = option.surface.get_rect(center=(self.screen_rect.center[0], self.screen_rect.center[1] + menu_height + 50))
            menu_height += (option.surface.get_height() + 10)

    def handle_action(self):
        if self.active_index == 0:
            return "START_COMBAT"
        elif self.active_index == 1:
            # load
            pass
        elif self.active_index == 2:
            return "OPTIONS"
        elif self.active_index == 3:
            return "QUIT"

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        self.__title.draw(surface)
        for index, option in enumerate(self.options):
            option.color = pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255)
            option.draw(surface)
