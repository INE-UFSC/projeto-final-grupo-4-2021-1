import pygame
from .BaseMenuState import BaseMenuState
from display.Text import Text

class Init(BaseMenuState):
    def __init__(self):
        super(Init, self).__init__()
        self.active_index = 0

        self.__title = Text("prototipo/assets/fonts/title.ttf", 200, pygame.Color(255, 30, 30), "Masmorra")
        self.__title_rect = self.__title.surface().get_rect(center=(self.screen_rect.width/2, self.screen_rect.height/2 - 90))

        self.options = [Text(
            "prototipo/assets/fonts/menu_option.ttf",
            50,
            pygame.Color(255, 255, 255),
            option
        ) for option in ["New", "Load", "Options", "Exit"]]

    def render_text(self, index):
        color = pygame.Color("red") if index == self.active_index else pygame.Color("white")
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text: Text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + 75 + (text.surface().get_height() + 20) * index)
        return text.surface().get_rect(center=center)

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
        surface.blit(self.__title.surface(), self.__title_rect)
        for index, option in enumerate(self.options):
            option.color = pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255)
            surface.blit(option.surface(), self.get_text_position(option, index))
